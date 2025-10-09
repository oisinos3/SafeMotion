bl_info = {
    "name": "Quick Bone Renamer",
    "author": "Oisin O'Sullivan",
    "version": (1, 0, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > Quick Tools",
    "description": "Quickly rename bones by transferring names between two separate armatures.",
    "category": "Animation",
}

import bpy

# --- Helper function for PointerProperty ---
def poll_armatures(self, object):
    return object.type == 'ARMATURE'

# --- Main Operator ---
class BONE_OT_smart_renamer(bpy.types.Operator):
    """Copies name from source, removes prefix, then applies to target."""
    bl_idname = "pose.smart_renamer"
    bl_label = "Smart Rename"
    bl_options = {'REGISTER', 'UNDO'}

    # Helper function to get and validate source/target bones
    def _get_bones(self, context):
        source_armature = context.scene.smart_renamer_source_armature
        if not source_armature:
            self.report({'WARNING'}, "Please select a Source Armature in settings.")
            return None, None

        if len(context.selected_pose_bones) != 2:
            self.report({'WARNING'}, "Select one bone from Source and one from Target.")
            return None, None
            
        target_bone = context.active_pose_bone
        source_bone = next((b for b in context.selected_pose_bones if b != target_bone), None)

        if not target_bone or not source_bone:
            self.report({'WARNING'}, "Invalid selection. Select two bones.")
            return None, None
        
        if source_bone.id_data != source_armature:
            # Try swapping them if the user selected in reverse order
            source_bone, target_bone = target_bone, source_bone
            
        if source_bone.id_data != source_armature:
            self.report({'WARNING'}, f"No selected bone belongs to Source Armature '{source_armature.name}'.")
            return None, None
            
        if target_bone.id_data == source_armature:
            self.report({'WARNING'}, "Target bone cannot be on the Source Armature.")
            return None, None
            
        return source_bone, target_bone

    action: bpy.props.EnumProperty(
        items=[
            ('COPY', "Copy", "Copy name from source to the text box"),
            ('APPLY', "Apply", "Apply the name in the text box to the target"),
            ('QUICK_RENAME', "Quick Rename", "Copy, clean, and apply the name in a single step")
        ]
    )

    def execute(self, context):
        if context.mode != 'POSE':
            self.report({'WARNING'}, "Please switch to Pose Mode.")
            return {'CANCELLED'}

        if self.action == 'QUICK_RENAME':
            source_bone, target_bone = self._get_bones(context)
            if not source_bone:
                return {'CANCELLED'}
            
            copied_name = source_bone.bone.name
            prefix_to_remove = context.scene.smart_renamer_prefix
            cleaned_name = copied_name
            if prefix_to_remove and copied_name.startswith(prefix_to_remove):
                cleaned_name = copied_name[len(prefix_to_remove):]
            
            if not cleaned_name:
                self.report({'WARNING'}, "Resulting name cannot be empty.")
                return {'CANCELLED'}
            
            original_name = target_bone.bone.name
            try:
                target_bone.bone.name = cleaned_name
                self.report({'INFO'}, f"Quick Renamed '{original_name}' to '{cleaned_name}'")
            except Exception as e:
                self.report({'ERROR'}, f"Could not rename. Error: {e}")
                return {'CANCELLED'}

        elif self.action == 'COPY':
            source_bone, target_bone = self._get_bones(context)
            if not source_bone:
                return {'CANCELLED'}

            context.scene.smart_renamer_source_armature_name = source_bone.id_data.name

            copied_name = source_bone.bone.name
            prefix_to_remove = context.scene.smart_renamer_prefix
            cleaned_name = copied_name
            if prefix_to_remove and copied_name.startswith(prefix_to_remove):
                cleaned_name = copied_name[len(prefix_to_remove):]
            context.scene.smart_renamer_new_name = cleaned_name
            self.report({'INFO'}, f"Copied '{cleaned_name}' to text box.")

        elif self.action == 'APPLY':
            target_bone = context.active_pose_bone
            if not target_bone:
                self.report({'WARNING'}, "No active target bone selected.")
                return {'CANCELLED'}
            
            stored_source_name = context.scene.smart_renamer_source_armature_name
            if stored_source_name and target_bone.id_data.name == stored_source_name:
                self.report({'WARNING'}, "Cannot apply to a bone on the source armature.")
                return {'CANCELLED'}

            original_name = target_bone.bone.name
            new_name = context.scene.smart_renamer_new_name
            if not new_name:
                self.report({'WARNING'}, "New name cannot be empty.")
                return {'CANCELLED'}
            try:
                target_bone.bone.name = new_name
                self.report({'INFO'}, f"Renamed '{original_name}' to '{new_name}'")
            except Exception as e:
                self.report({'ERROR'}, f"Could not rename. Error: {e}")
                return {'CANCELLED'}

        return {'FINISHED'}

# --- Main Panel ---
class BONE_PT_smart_renamer_panel(bpy.types.Panel):
    bl_label = "Smart Renamer"
    bl_idname = "BONE_PT_smart_renamer"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Quick Tools'

    def draw(self, context):
        layout = self.layout
        
        if context.mode != 'POSE':
            layout.label(text="⚠️ Switch to Pose Mode to use this tool.", icon='ERROR')
            return

        box = layout.box()
        box.label(text="1. Set the Source Armature below.", icon='ARMATURE_DATA')
        box.label(text="2. Select a bone on Source & Target.", icon='BONE_DATA')
        box.label(text="3. Click Quick Rename.", icon='CHECKMARK')

        # --- THIS LINE IS NOW FIXED ---
        # Safely check if 'lock_object_modes' exists before checking its value
        if hasattr(context.workspace, 'lock_object_modes') and context.workspace.lock_object_modes:
            lock_box = layout.box()
            lock_box.label(text="'Lock Object Modes' is on.", icon='ERROR')
            lock_box.label(text="Disable it to select bones on two armatures.")

        box = layout.box()
        box.label(text="Settings:")
        box.prop(context.scene, "smart_renamer_source_armature", text="Source")
        box.prop(context.scene, "smart_renamer_prefix", text="Prefix to Remove")

        layout.label(text="One-Click Action:")
        row = layout.row()
        quick_op = row.operator(BONE_OT_smart_renamer.bl_idname, text="Quick Rename (Copy & Apply)", icon='SNAP_ON')
        quick_op.action = 'QUICK_RENAME'
        if len(context.selected_pose_bones) != 2:
            row.enabled = False

# --- Manual Renamer Panel ---
class BONE_PT_manual_renamer_panel(bpy.types.Panel):
    bl_label = "Manual Two-Step Process"
    bl_idname = "BONE_PT_manual_renamer"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Quick Tools'
    bl_parent_id = "BONE_PT_smart_renamer"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        if context.mode != 'POSE':
            layout.label(text="Requires Pose Mode.")
            return

        layout.label(text="1. Copy Name from Source Bone:")
        row = layout.row()
        copy_op = row.operator(BONE_OT_smart_renamer.bl_idname, text="Copy & Clean Name")
        copy_op.action = 'COPY'
        if len(context.selected_pose_bones) != 2:
            row.enabled = False
            
        layout.separator()
        layout.label(text="2. Apply to Target Bone:")
        layout.prop(context.scene, "smart_renamer_new_name", text="")
        row = layout.row()
        apply_op = row.operator(BONE_OT_smart_renamer.bl_idname, text="Apply Name")
        apply_op.action = 'APPLY'
        if not context.active_pose_bone or not context.scene.smart_renamer_new_name:
            row.enabled = False

# --- Registration ---
classes = [
    BONE_OT_smart_renamer,
    BONE_PT_smart_renamer_panel,
    BONE_PT_manual_renamer_panel,
]

def register():
    bpy.types.Scene.smart_renamer_new_name = bpy.props.StringProperty(name="New Bone Name")
    bpy.types.Scene.smart_renamer_source_armature_name = bpy.props.StringProperty(name="Source Armature Name")
    
    bpy.types.Scene.smart_renamer_prefix = bpy.props.StringProperty(name="Prefix to Remove", default="mixamorig:")
    bpy.types.Scene.smart_renamer_source_armature = bpy.props.PointerProperty(
        name="Source Armature",
        description="The armature to copy bone names FROM",
        type=bpy.types.Object,
        poll=poll_armatures
    )
    
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    del bpy.types.Scene.smart_renamer_new_name
    del bpy.types.Scene.smart_renamer_source_armature_name
    del bpy.types.Scene.smart_renamer_prefix
    del bpy.types.Scene.smart_renamer_source_armature
    
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    try:
        unregister()
    except Exception:
        pass
    register()
