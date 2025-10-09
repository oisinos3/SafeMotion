bl_info = {
    "name": "Motive FBX Retargeting Setup",
    "author": "Oisín O'Sullivan",
    "version": (1, 0, 0),
    "blender": (4, 1, 0),
    "location": "3D View > Sidebar (N Panel) > Motive Pipeline",
    "description": "Tools to prep your scene for retargeting your Motive FBX file onto another armature.",
    "warning": "",
    "doc_url": "",
    "category": "Animation",
}

import bpy
from bpy_extras.io_utils import ImportHelper, ExportHelper
import os

# --- Property Group and Operators ---
class PipelineProperties(bpy.types.PropertyGroup):
    source_fbx_name: bpy.props.StringProperty(default="")
class PIPELINE_OT_setup_scenes(bpy.types.Operator):
    bl_idname = "pipeline.setup_scenes"; bl_label = "Create Project Scenes"; bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        scenes_to_create = ["1. Motive Skeleton", "2. Unreal_Manny", "3. Retargeting"]
        template_scene = context.scene
        for scene_name in scenes_to_create:
            if scene_name in bpy.data.scenes: continue
            context.window.scene = template_scene; bpy.ops.scene.new(type='FULL_COPY')
            new_scene = context.scene; new_scene.name = scene_name
            if list(new_scene.objects): bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
            for coll in [c for c in new_scene.collection.children]: bpy.data.collections.remove(coll)
        bpy.ops.outliner.orphans_purge()
        context.window.scene = bpy.data.scenes[scenes_to_create[0]]; return {'FINISHED'}
class PIPELINE_OT_import_fbx(bpy.types.Operator, ImportHelper):
    bl_idname = "pipeline.import_fbx"; bl_label = "Import Motive FBX"; filename_ext = ".fbx"
    def execute(self, context):
        motive_scene_name = "1. Motive Skeleton"
        if context.scene.name != motive_scene_name: context.window.scene = bpy.data.scenes[motive_scene_name]
        collection_name = "Motive Import"
        if collection_name not in context.scene.collection.children:
            new_coll = bpy.data.collections.new(collection_name)
            context.scene.collection.children.link(new_coll)
        layer_collection = context.view_layer.layer_collection.children[collection_name]
        context.view_layer.active_layer_collection = layer_collection
        bpy.ops.import_scene.fbx(filepath=self.filepath, bake_space_transform=True, ignore_leaf_bones=True, automatic_bone_orientation=True)
        basename = os.path.basename(self.filepath); filename_no_ext, _ = os.path.splitext(basename)
        context.scene.pipeline_props.source_fbx_name = filename_no_ext
        armature = next((obj for obj in context.selected_objects if obj.type == 'ARMATURE'), None)
        if armature and armature.animation_data and armature.animation_data.action:
            frame_range = armature.animation_data.action.frame_range
            context.scene.frame_start = int(frame_range[0]); context.scene.frame_end = int(frame_range[1])
        return {'FINISHED'}
class PIPELINE_OT_save_with_prefix(bpy.types.Operator, ExportHelper):
    bl_idname = "pipeline.save_with_prefix"; bl_label = "Save & Continue"; filename_ext = ".blend"
    def invoke(self, context, event):
        fbx_basename = context.scene.pipeline_props.source_fbx_name
        if fbx_basename: self.filepath = f"{fbx_basename}{self.filename_ext}"
        context.window_manager.fileselect_add(self); return {'RUNNING_MODAL'}
    def execute(self, context):
        bpy.ops.wm.save_as_mainfile(filepath=self.filepath); return {'FINISHED'}
class PIPELINE_OT_append_packaged_manny(bpy.types.Operator):
    bl_idname = "pipeline.append_packaged_manny"; bl_label = "Append UE5 Mannequin"; bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        manny_scene_name = "2. Unreal_Manny"
        if context.scene.name != manny_scene_name: context.window.scene = bpy.data.scenes[manny_scene_name]
        addon_dir = os.path.dirname(__file__); blend_file_name = "UE5Rig_addonVer.blend"
        filepath = os.path.join(addon_dir, blend_file_name)
        if not os.path.exists(filepath): self.report({'ERROR'}, f"File not found: {blend_file_name}"); return {'CANCELLED'}
        collection_names = ["UE_Manny_Skeleton"]
        with bpy.data.libraries.load(filepath, link=False) as (data_from, data_to):
            data_to.collections = [c for c in data_from.collections if c in collection_names]
        if not data_to.collections: self.report({'ERROR'}, "Required collections not found"); return {'CANCELLED'}
        for coll in data_to.collections:
            if coll: context.scene.collection.children.link(coll)
        return {'FINISHED'}
class PIPELINE_OT_append_character(bpy.types.Operator):
    bl_idname = "pipeline.append_character"; bl_label = "Append Custom Rig"
    def execute(self, context):
        custom_scene_name = "2.a. User Character"
        if custom_scene_name not in bpy.data.scenes:
            bpy.ops.scene.new(type='FULL_COPY'); new_scene = context.scene; new_scene.name = custom_scene_name
            if list(new_scene.objects): bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
            for coll in [c for c in new_scene.collection.children]: bpy.data.collections.remove(coll)
        context.window.scene = bpy.data.scenes[custom_scene_name]
        return bpy.ops.wm.append('INVOKE_DEFAULT')

# --- HELPER FUNCTIONS FOR THE PREPARE OPERATOR ---
def duplicate_collection_recursive(source_coll, target_parent_coll, suffix, mapping):
    new_coll = bpy.data.collections.new(name=source_coll.name + suffix)
    target_parent_coll.children.link(new_coll)
    for obj in source_coll.objects:
        new_obj = obj.copy()
        if obj.data: new_obj.data = obj.data.copy()
        new_coll.objects.link(new_obj)
        mapping[obj] = new_obj
    for child_coll in source_coll.children:
        duplicate_collection_recursive(child_coll, new_coll, suffix, mapping)
def relink_and_rename_data(mapping, suffix):
    for old_obj, new_obj in mapping.items():
        new_obj.name = old_obj.name + suffix
        if new_obj.data: new_obj.data.name = old_obj.data.name + suffix
        if old_obj.parent and old_obj.parent in mapping:
            new_obj.parent = mapping[old_obj.parent]
        for mod in new_obj.modifiers:
            if mod.type == 'ARMATURE' and mod.object and mod.object in mapping:
                mod.object = mapping[mod.object]

class PIPELINE_OT_prepare_retargeting(bpy.types.Operator):
    bl_idname = "pipeline.prepare_retargeting"; bl_label = "Prepare Retargeting Scene"; bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        scenes = bpy.data.scenes
        source_scene = scenes.get("1. Motive Skeleton")
        retarget_scene = scenes.get("3. Retargeting")
        target_scene = scenes.get("2. Unreal_Manny") if scenes.get("2. Unreal_Manny").objects else scenes.get("2.a. User Character")
        if not all([source_scene, target_scene, retarget_scene]): self.report({'ERROR'}, "A required scene is missing."); return {'CANCELLED'}
        mapping = {}; suffix = "_retargeting"
        for coll in source_scene.collection.children:
            duplicate_collection_recursive(coll, retarget_scene.collection, suffix, mapping)
        for coll in target_scene.collection.children:
            duplicate_collection_recursive(coll, retarget_scene.collection, suffix, mapping)
        relink_and_rename_data(mapping, suffix)
        source_armature = next((obj for obj in source_scene.objects if obj.type == 'ARMATURE'), None)
        if source_armature and source_armature.animation_data and source_armature.animation_data.action:
            frame_range = source_armature.animation_data.action.frame_range
            retarget_scene.frame_start = int(frame_range[0])
            retarget_scene.frame_end = int(frame_range[1])
        context.window.scene = retarget_scene
        self.report({'INFO'}, "Successfully prepared the Retargeting scene.")
        return {'FINISHED'}

# --- UI PANEL ---
class VIEW3D_PT_motive_pipeline(bpy.types.Panel):
    bl_label="Motive to Unreal"; bl_idname="VIEW3D_PT_motive_pipeline"
    bl_space_type='VIEW_3D'; bl_region_type='UI'; bl_category='Motive Pipeline'
    def draw(self, context):
        layout = self.layout; scenes = bpy.data.scenes
        required = {"1. Motive Skeleton", "2. Unreal_Manny", "3. Retargeting"}
        setup = required.issubset({s.name for s in scenes})
        imported = False; manny_appended = False; custom_appended = False; retarget_populated = False
        if setup:
            imported = len(scenes["1. Motive Skeleton"].objects) > 0
            manny_appended = len(scenes["2. Unreal_Manny"].objects) > 0
            custom_appended = ("2.a. User Character" in scenes and len(scenes["2.a. User Character"].objects) > 0)
            retarget_populated = len(scenes["3. Retargeting"].objects) > 0
        any_rig = manny_appended or custom_appended
        
        # UI Stages
        box = layout.box(); box.label(text="1. Project Setup", icon='CHECKMARK' if setup else 'SCENE_DATA')
        if not setup: box.operator(PIPELINE_OT_setup_scenes.bl_idname)
        if setup:
            box = layout.box(); box.label(text="2. Import Source Data", icon='CHECKMARK' if imported else 'IMPORT')
            if not imported: box.operator(PIPELINE_OT_import_fbx.bl_idname)
        if imported:
            box = layout.box(); box.label(text="3. Add Target Rig", icon='CHECKMARK' if any_rig else 'ARMATURE_DATA')
            if not any_rig:
                if not bpy.data.is_saved:
                    box.label(text="Please save project to continue:"); box.operator(PIPELINE_OT_save_with_prefix.bl_idname)
                else:
                    box.label(text="Choose Target Rig Type:")
                    box.operator(PIPELINE_OT_append_packaged_manny.bl_idname)
                    box.operator(PIPELINE_OT_append_character.bl_idname)
        if any_rig:
            box = layout.box(); box.label(text="4. Prepare Retargeting", icon='CHECKMARK' if retarget_populated else 'PLAY')
            if not retarget_populated: box.operator(PIPELINE_OT_prepare_retargeting.bl_idname)

# --- REGISTRATION ---
classes = (PipelineProperties, PIPELINE_OT_setup_scenes, PIPELINE_OT_import_fbx, PIPELINE_OT_save_with_prefix, PIPELINE_OT_append_packaged_manny, PIPELINE_OT_append_character, PIPELINE_OT_prepare_retargeting, VIEW3D_PT_motive_pipeline)
def register():
    for cls in classes: bpy.utils.register_class(cls)
    bpy.types.Scene.pipeline_props = bpy.props.PointerProperty(type=PipelineProperties)
def unregister():
    del bpy.types.Scene.pipeline_props
    for cls in reversed(classes): bpy.utils.unregister_class(cls)
if __name__ == "__main__": register()