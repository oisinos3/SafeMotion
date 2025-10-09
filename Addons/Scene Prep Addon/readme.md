
# Motive Scene Setup for Blender

A Blender addon that automates the setup process for retargeting motion capture data from Optitrack Motive FBX files onto custom character rigs or the Unreal Engine 5 Mannequin.

## Overview

This addon creates a structured, step-by-step workflow for preparing motion capture retargeting projects. It handles scene organization, a preset Motive FBX import configuration, rig setup, and retargeting preparation - eliminating the tedious manual setup typically required for mocap workflows.

---

## Features

- **Automated Scene Setup**: Creates three organized scenes for your retargeting workflow
- **Smart FBX Import**: Imports Motive FBX files with optimal settings and auto-configures timeline
- **Built-in UE5 Mannequin**: Includes pre-configured Unreal Engine 5 Mannequin rig
- **Custom Rig Support**: Easy workflow for using your own character rigs
- **One-Click Preparation**: Automatically duplicates and prepares all assets for retargeting
- **Clean Organization**: Keeps source data separate from working data

---

## Installation

1. **Download the addon** from this repository (the `.zip` file containing both `__init__.py` and `UE5Rig_addonVer.blend`)
2. In Blender, go to **Edit > Preferences > Add-ons**
3. Click **Install...** and select the downloaded `.zip` file
4. Enable the addon by checking the box next to "Motive Scene Setup"

**Important:** The addon requires the `UE5Rig_addonVer.blend` file to be in the same folder as `__init__.py`. Keep them together!

---

## The Workflow

The addon guides you through a 4-stage process, accessible from the **3D Viewport Sidebar** (press `N`) under the **"Motive Scene Setup"** tab.

### Stage 1: Project Setup
**What it does:** Creates three organized scenes in your Blender file:
- `1. Motive Skeleton` - Your source mocap data lives here
- `2. Unreal_Manny` - Target rig (UE5 Mannequin or your custom rig)
- `3. Retargeting` - Working scene where retargeting happens

**How to use:**
1. Click **"Create Project Scenes"**
2. The addon creates all three scenes and switches you to Scene 1

---

### Stage 2: Import Source Data
**What it does:** Imports your Motive FBX file with optimal settings and automatically:
- Applies correct transform baking
- Ignores leaf bones (cleaner hierarchy)
- Sets automatic bone orientation
- Configures timeline to match animation length

**How to use:**
1. Ensure you're viewing `1. Motive Skeleton` scene
2. Click **"Import Motive FBX"**
3. Navigate to your `.fbx` file exported from Motive
4. Select and import

The addon creates a "Motive Import" collection and sets your timeline to match the animation.

---

### Stage 3: Add Target Rig
**What it does:** Adds the character rig you want to retarget the motion onto.

**How to use:**

**Option A - Use UE5 Mannequin (Built-in):**
1. Save your project first (click **"Save & Continue"** if prompted)
2. Click **"Append UE5 Mannequin"**
3. The mannequin rig is automatically added to Scene 2

**Option B - Use Your Own Custom Rig:**
1. Save your project first
2. Click **"Append Custom Rig"**
3. Navigate to your character's `.blend` file
4. Select the collection(s) containing your rig
5. The addon creates a `2.a. User Character` scene for your custom rig

---

### Stage 4: Prepare Retargeting
**What it does:** Automatically duplicates and prepares everything for retargeting:
- Copies both source skeleton and target rig into the Retargeting scene
- Maintains all parent-child relationships
- Preserves armature modifiers and skinning
- Adds `_retargeting` suffix to keep data organized
- Syncs timeline with animation length

**How to use:**
1. Click **"Prepare Retargeting Scene"**
2. The addon switches you to `3. Retargeting` scene
3. Both rigs are ready - now use Blender's retargeting tools to transfer the animation!

---

## Usage Tips

### Best Practices
- **Always save your project** after importing the Motive FBX (Stage 2)
- **Don't modify Scene 1 or 2** after Stage 4 - they're your source data backups
- **Work only in Scene 3** (`3. Retargeting`) when setting up retargeting constraints
- **Keep the UE5Rig_addonVer.blend file** with the addon - don't delete it!


### Custom Rig Requirements
When using your own character rig (Option B in Stage 3):
- Ensure your rig is properly organized in collections
- All meshes should be parented/skinned to the armature
- Test your rig in a separate file first

---

## Scene Structure

After completing all stages, your project will have:

```
📁 Your Project.blend
├── 📋 1. Motive Skeleton (Source mocap - don't modify)
│   └── 📦 Motive Import
│       └── 🦴 Motive Armature + Animation
│
├── 📋 2. Unreal_Manny (Target rig - don't modify)
│   └── 📦 UE_Manny_Skeleton
│       └── 🦴 UE5 Mannequin
│
├── 📋 2.a. User Character (If using custom rig)
│   └── 📦 Your Character Collections
│
└── 📋 3. Retargeting (Working scene)
    ├── 📦 Motive Import_retargeting
    │   └── 🦴 Motive Armature_retargeting
    └── 📦 UE_Manny_Skeleton_retargeting
        └── 🦴 Target Rig_retargeting
```

---

## Troubleshooting

**"File not found: UE5Rig_addonVer.blend"**
- The addon can't find the packaged UE5 Mannequin file
- Reinstall the addon using the complete `.zip` file
- Ensure `UE5Rig_addonVer.blend` is in the addon folder

**"A required scene is missing"**
- You skipped a stage - stages must be completed in order
- Use the panel to see which stage needs completion

**Timeline doesn't update after import**
- Ensure your Motive FBX has animation data
- Check that the armature has an action assigned

**Custom rig doesn't appear**
- Make sure you selected collections (not objects) when appending
- Check that your source `.blend` file contains the rig

**Prepare Retargeting fails**
- Ensure Stages 1-3 are completed first
- Both Scene 1 and Scene 2 (or 2.a) must have content

---

## Requirements

- Blender 4.1 or higher
- FBX files exported from Optitrack Motive (or compatible mocap software)
- Basic understanding of animation retargeting concepts

---

## What This Addon Does NOT Do

This addon handles **project setup and organization**. You'll still need to:
- Manually set up retargeting constraints between bones
- Create bone mappings between source and target
- Bake and export the final animation
- Fine-tune the retargeted motion

Consider pairing this with the **SafeMotion Quicktools** addon for bone renaming and scale management!

---

## Credits

**Author:** Oisín O'Sullivan  
**Version:** 1.0.0  
**Category:** Animation
**UE5-Manny:** Epic Games and cjlima - https://github.com/cjmlima/UE5-Blender-Rig

Developed for the SafeMotion project to streamline Optitrack Motive to Unreal Engine mocap pipelines.

---

## License

Free to use, modify, and distribute. Attribution appreciated but not required.

---

## Support

Found a bug or have a feature request? Open an issue on this repository!
