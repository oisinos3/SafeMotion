***

# Blender - Safely Apply Scale Script

A basic Python script for Blender that allows you to safely apply scale to an armature and its associated objects without breaking parenting, skinning, or vertex weights. I had problems exporting to Unreal without scale applied - the root bone would always be scaled up in Unreal, meaning retargeting wouldn't work. This fixes that issue, and zeroes out all scale transforms.

## What It Does

When you scale an armature in Blender, using "Apply Scale" on it can cause broken, exploded models. This script automates the process to prevent these issues.

It safely applies the scale transformations to a selected armature and its meshes, ensuring that all parent-child relationships (including bone parenting), skinning, and vertex weights remain perfectly intact. The result is a properly scaled model with a clean `(1, 1, 1)` scale value, ready for animation or export.

## How to Use

1.  **Open the Scripting Workspace:** In Blender, navigate to the `Scripting` tab.
2.  **Create a New Script:** Click the `+ New` button to create a new text file.
3.  **Paste the Code:** Copy the entire `safe_apply_scale.py` script and paste it into the text editor.
4.  **Select Your Objects:** In the 3D Viewport, **select the armature and all of its child mesh objects** that you want to affect.
5.  **Run the Script:** Click the "Run Script" button (play icon) at the top of the text editor.

The script will then run. You can check the system console for progress messages.
