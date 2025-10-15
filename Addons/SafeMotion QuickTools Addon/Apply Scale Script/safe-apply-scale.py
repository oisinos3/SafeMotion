import bpy

def main():
    """
    Main function to run the safe apply scale process.
    """
    context = bpy.context
    
    # Ensure we are in object mode
    if context.object and context.object.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')

    # Get the active object (should be an armature)
    armature = context.active_object
    if not armature:
        print("Error: No active object selected.")
        return
    
    if armature.type != 'ARMATURE':
        print("Error: Please select an armature as the active object.")
        return

    print("--- Starting Safe Apply Scale ---")

    # --- Helper function to find all children recursively ---
    def get_all_children_recursively(obj, children_list):
        """Helper function to find all descendants of a given object."""
        for child in obj.children:
            if child not in children_list:
                children_list.append(child)
                get_all_children_recursively(child, children_list)
        return children_list

    # Build the list of objects to process: the armature and all its descendants
    original_selection = [armature]
    get_all_children_recursively(armature, original_selection)
    
    print(f"Found armature and {len(original_selection) - 1} child object(s).")

    # --- 1. Store Parent-Child Relationships ---
    relationships = []
    children_to_unparent = []
    
    for obj in original_selection:
        if obj.parent:
            parent_info = {
                "child": obj,
                "parent": obj.parent,
                "type": obj.parent_type,
                "bone_name": obj.parent_bone if obj.parent_type == 'BONE' else None
            }
            relationships.append(parent_info)
            if obj != armature:  # Don't unparent the main armature from its potential parent
                children_to_unparent.append(obj)
            
    if not relationships:
        print("No parent-child relationships found in selection. Applying scale directly.")
    else:
        print(f"Memorized {len(relationships)} parent-child relationships.")

        # --- 2. Unparent All Children Safely ---
        if children_to_unparent:
            bpy.ops.object.select_all(action='DESELECT')
            for child in children_to_unparent:
                child.select_set(True)
            
            if context.selected_objects:
                bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
                print("Successfully unparented all children.")

    # --- 3. Apply Scale to All Original Objects ---
    bpy.ops.object.select_all(action='DESELECT')
    for obj in original_selection:
        obj.select_set(True)
    
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    print("Applied scale to all selected objects.")

    # --- 4. Re-parent Everything ---
    if relationships:
        for rel in relationships:
            child = rel["child"]
            parent = rel["parent"]
            
            # Deselect all and select the child, then the parent
            bpy.ops.object.select_all(action='DESELECT')
            child.select_set(True)
            parent.select_set(True)
            context.view_layer.objects.active = parent

            if rel["type"] == 'BONE':
                bone_name = rel["bone_name"]
                
                if bone_name and bone_name in parent.data.bones:
                    bpy.ops.object.mode_set(mode='POSE')
                    parent.data.bones.active = parent.data.bones[bone_name]
                    bpy.ops.object.parent_set(type='BONE', keep_transform=True)
                    bpy.ops.object.mode_set(mode='OBJECT')
                else:
                    print(f"Warning: Bone '{bone_name}' not found, skipping re-parent for {child.name}")
            
            elif rel["type"] == 'OBJECT':
                bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)

        print(f"Successfully re-parented {len(relationships)} relationships.")

    # Restore original active object selection
    bpy.ops.object.select_all(action='DESELECT')
    context.view_layer.objects.active = armature
    armature.select_set(True)
        
    print("--- Safe Apply Scale Complete ---")

# Run the main function
if __name__ == "__main__":
    main()