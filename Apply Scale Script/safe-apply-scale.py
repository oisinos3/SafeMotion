import bpy

def main():
    """
    Main function to run the safe apply scale process.
    """
    context = bpy.context
    
    # Ensure we are in object mode
    if context.object and context.object.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')

    # Get the initial selection
    original_selection = context.selected_objects
    if not original_selection:
        print("Error: Please select an armature and its associated mesh parts.")
        return

    print("--- Starting Safe Apply Scale ---")

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
            children_to_unparent.append(obj)
            
    if not relationships:
        print("No parent-child relationships found in selection. Applying scale directly.")
    else:
        print(f"Memorized {len(relationships)} parent-child relationships.")

        # --- 2. Unparent All Children Safely ---
        bpy.ops.object.select_all(action='DESELECT')
        for child in children_to_unparent:
            child.select_set(True)
        
        if children_to_unparent:
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
                # Set the active bone in pose mode
                bpy.ops.object.mode_set(mode='POSE')
                active_bone = parent.data.bones.get(rel["bone_name"])
                if active_bone:
                    parent.data.bones.active = active_bone
                    bpy.ops.object.parent_set(type='BONE', keep_transform=True)
                else:
                    print(f"Warning: Could not find bone '{rel['bone_name']}' for child '{child.name}'.")
                bpy.ops.object.mode_set(mode='OBJECT')
            
            elif rel["type"] == 'OBJECT':
                bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)

        print(f"Successfully re-parented {len(relationships)} relationships.")

    # Restore original selection for user convenience
    bpy.ops.object.select_all(action='DESELECT')
    for obj in original_selection:
        obj.select_set(True)
        
    print("--- Safe Apply Scale Complete ---")

# Run the main function
if __name__ == "__main__":
    main()
