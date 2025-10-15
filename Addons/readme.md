# Blender Addons for Motion Capture Workflows

A collection of Blender addons created to manage specific motion capture workflows. I originally created basic script versions to help manage the workflow - but later expanded to addons to be re-used by whoever needs them. Each addon + folder has its own specific readme included.

This package includes three addons:
- **Motive Scene Setup for Blender** - Automated scene organization and retargeting preparation
- **OptiTrack Rigidbody Generator** - Convert rigidbody animations to skeletal meshes
- **SafeMotion Quicktools** - Essential rigging and animation utilities

---

## Table of Contents

1. [Motive Scene Setup for Blender](#motive-scene-setup-for-blender)
2. [OptiTrack Rigidbody Generator](#optitrack-rigidbody-generator-for-blender)
3. [SafeMotion Quicktools](#safemotion-quicktools-for-blender)

---

# Motive Scene Setup for Blender

A Blender addon that automates the setup process for retargeting motion capture data from OptiTrack Motive FBX files onto custom character rigs or the Unreal Engine 5 Mannequin.

## Overview

This addon creates a structured, step-by-step workflow for preparing motion capture retargeting projects. It handles scene organization, preset Motive FBX import configuration, rig setup, and retargeting preparation - eliminating the tedious manual setup typically required for mocap workflows.

## Features

- **Automated Scene Setup**: Creates three organized scenes for your retargeting workflow
- **Smart FBX Import**: Imports Motive FBX files with optimal settings and auto-configures timeline
- **Built-in UE5 Mannequin**: Includes pre-configured Unreal Engine 5 Mannequin rig
- **Custom Rig Support**: Easy workflow for using your own character rigs
- **One-Click Preparation**: Automatically duplicates and prepares all assets for retargeting
- **Clean Organization**: Keeps source data separate from working data

## Installation

1. **Download the addon** from this repository (the `.zip` file containing both `__init__.py` and `UE5Rig_addonVer.blend`)
2. In Blender, go to **Edit > Preferences > Add-ons**
3. Click **Install...** and select the downloaded `.zip` file
4. Enable the addon by checking the box next to "Motive Scene Setup"

**Important:** The addon requires the `UE5Rig_addonVer.blend` file to be in the same folder as `__init__.py`. Keep them together!

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

## What This Addon Does NOT Do

This addon handles **project setup and organization**. You'll still need to:
- Manually set up retargeting constraints between bones
- Create bone mappings between source and target
- Bake and export the final animation
- Fine-tune the retargeted motion

Consider pairing this with the **SafeMotion Quicktools** addon for bone renaming and scale management!

---

# OptiTrack Rigidbody Generator for Blender

A Blender addon for converting OptiTrack rigidbody animations into skeletal meshes suitable for game engines like Unreal Engine.

This tool streamlines the workflow of importing animated empties from an OptiTrack FBX, generating single-bone armatures for each, baking the animation, and exporting them as FBX files. It provides both a manual step-by-step process and a fully automated one-click pipeline.

## Features

* **Organized FBX Importer:** Imports OptiTrack FBX files and automatically organizes the contents into a clean collection hierarchy (Rigidbodies, Skeleton)
* **Rigidbody to Armature Creation:** Generates a single-bone armature for each selected empty that contains "_bone" in its name
* **Live Animation Linking:** The created armatures are constrained to the original empties, allowing you to see the animation live before baking
* **One-Click Baking:** Bakes the animation from the empties to the new armatures for all created rigs at once
* **Game-Ready FBX Export:** Exports armatures with their mesh children to individual `.fbx` files with Unreal Engine-friendly settings
* **Full Automation Pipeline:** A one-click operator that handles the entire process: importing an FBX, creating the rigs, baking the animations, and exporting the final files
* **Post-Import Pipeline:** A second automation operator that can be run on an already imported scene
* **Convenience Features:**
    * Automatically opens the export folder upon completion
    * Automatically clears the internal "tracked armatures" list after each export for a clean workflow
    * UI prompts and warnings to guide the user

## Installation

1. Download the `empties-to-rigidbodies.py` file
2. In Blender, go to `Edit` > `Preferences...`
3. Navigate to the `Add-ons` tab and click `Install...`
4. Select the `empties-to-rigidbodies.py` file and click `Install Add-on`
5. Find the "Rigidbody Tools" addon in the list and enable it by checking the box

The addon's panels will now be available in the 3D View's sidebar (press `N` to open).

## How to Use

The addon is organized into three panels in the Blender sidebar: **Importer**, **Rigidbody Tools**, and **Automation**.

### Workflow 1: Manual (Step-by-Step)

This workflow gives you the most control over each stage of the process.

#### Step 1: Import FBX
* In the **Importer** panel, click `Import OptiTrack FBX`
* Select your `.fbx` file exported from Motive
* The addon will import the file and create a new parent collection for its contents

#### Step 2: Create Rigs
* Select the empties you wish to convert. You can select the parent empty or the `_bone` empty directly
* In the **Rigidbody Tools** panel, under "Step 1: Empties to Armatures", choose how you want to select the source empties:
    * `From Selected`: Processes only the empties you have selected
    * `From Active Collection`: Processes all `_bone` empties in the currently active collection
    * `From All in Scene`: Processes every `_bone` empty in the entire scene
* A pop-up will appear allowing you to confirm the names for the new armatures, set a size for the proxy mesh (`Cube Size`), and choose what to do with the original empties (`Cleanup Empties`)

#### Step 3: Bake Armatures
* Once you are happy with the generated rigs, go to "Step 2: Bake Created Armatures"
* Click `Bake Created Armatures`. This will bake the animation from the source empties onto the bones of the new armatures and remove the constraints
* The bin icon next to the title can be used to manually clear the addon's internal list of tracked armatures if needed

#### Step 4: Export
* Go to "Step 3: Export Armatures"
* Set a name for your export sub-folder in the **Export Folder** text field
* Choose your export method:
    * `Export Selected Armatures`: Only exports the armatures you currently have selected
    * `Export All Created Armatures`: Exports all armatures that were generated and tracked by the addon in this session
* After the export is complete, the addon will automatically **clear its internal tracked list** and **open the export folder** for you

### Workflow 2: Automation

The **Automation** panel is designed for a fast, one-click workflow. All settings are controlled directly from this panel.

#### Settings
* **Export Folder**: The name of the sub-folder where the final FBX files will be saved
* **Cube Size**: The size of the proxy mesh created for each rig
* **Cleanup**: What to do with the original `_bone` empties after rig creation (Hide or Delete)

#### Running the Pipeline
There are two main automation operators:

1. **Run Full Pipeline (from file)**:
    * This is a complete, hands-off process
    * It will first ask you to select an `.fbx` file to import
    * It will then automatically create rigs for all `_bone` empties found within that file, bake their animations, and export them as individual `.fbx` files

2. **Run on Imported Scene**:
    * This operator is for when you have already imported your FBX (or have the necessary empties in your scene)
    * It will scan the entire current scene for any `_bone` empties, create rigs, bake them, and export them

Both automation pipelines will export the final files to a sub-folder located in the **same directory as your saved `.blend` file**. After the process is finished, the export folder will open automatically.

---

# SafeMotion Quicktools for Blender

A comprehensive Blender addon providing basic rigging and animation utilities. Originally developed for working with anatomical skeletons and OptiTrack motion capture data, these scripts have been expanded into re-usable addons for future use.

## Features

### Quick Bone Renamer
Transfer bone names between armatures easily - perfect for animation retargeting, cleaning up Mixamo/Rigify imports, or matching naming conventions across different rigs.

- **One-Click Renaming**: Copy and apply bone names between armatures instantly
- **Designated Source Armature**: Set a specific armature as your source to avoid confusion
- **Smart Prefix Removal**: Automatically strip prefixes like `mixamorig:` during renaming
- **Safe Operations**: Enforces renaming between separate armatures only
- **Manual Override**: Optional two-step workflow for editing names before applying
- **Clear UI Guidance**: Contextual warnings and step-by-step instructions

### Safe Apply Scale
Apply scale transformations to armatures and their entire hierarchy without breaking skinning, parenting, or vertex weights. Final step for prepping a scaled rig for clean exports to game engines like Unreal Engine.

- **Automatic Hierarchy Detection**: Finds and processes all child objects recursively
- **Preserves Relationships**: Maintains all parent-child connections and bone parenting
- **One-Click Solution**: Select the armature and click - no manual selection needed
- **Export-Ready**: Achieves clean `(1, 1, 1)` scale values for proper retargeting

## Installation

1. Download `safemotion_quicktools.py` from this repository
2. In Blender, go to **Edit > Preferences > Add-ons**
3. Click **Install...** and select the downloaded `.py` file
4. Enable the addon by checking the box next to "SafeMotion Quicktools"

The tools will appear in the **3D Viewport Sidebar** (press `N` to toggle) under the **"SafeMotion Quicktools"** tab.

## Usage

### Quick Bone Renamer

**Setup:**
1. **Disable "Lock Object Modes"**: In the top-right of the 3D Viewport, ensure "Lock Object Modes" is disabled to allow selecting bones across multiple armatures
2. **Enter Pose Mode**: Select any armature and switch to Pose Mode (`Ctrl+Tab`)
3. **Set Source Armature**: In the panel, use the "Source" dropdown to select the armature you're copying names FROM

**Quick Rename (One-Click):**
1. Select a bone on your **source** armature
2. **Shift+Click** to select a bone on your **target** armature
3. Click **"Quick Rename (Copy & Apply)"**
4. The target bone is instantly renamed (with prefix removed if configured)

**Manual Mode (Two-Step):**
Expand the "Manual Two-Step Process" panel for more control:
1. Select source and target bones as above
2. Click **"Copy & Clean Name"** - the cleaned name appears in the text box
3. Edit the name if needed
4. Select your target bone and click **"Apply Name"**

**Settings:**
- **Source Armature**: The armature to copy bone names from
- **Prefix to Remove**: Automatically strips this text from copied names (default: `mixamorig:`)

### Safe Apply Scale

**Simple Workflow:**
1. **Switch to Object Mode** (`Tab`)
2. **Select your armature** (the root of the hierarchy you want to scale)
3. Click **"Safe Apply Scale to Hierarchy"**

That's it! The addon will:
- Automatically find all child objects (meshes, empties, nested armatures, etc.)
- Temporarily unparent everything
- Apply scale to the entire hierarchy
- Re-parent all objects back to their original parents/bones
- Preserve all skinning and vertex weights

**What This Fixes:**
- Prevents "exploded" meshes when applying scale to rigged characters
- Ensures proper scale values (`1, 1, 1`) for clean game engine/DCC exports
- Prevents the Unreal Engine "scaled root bone" import issue
- Makes retargeting actually work by having uniform scale

## Use Cases

- **Mixamo Retargeting**: Clean up Mixamo character bone names to match your custom rig
- **Anatomical Models**: Rename bones from scientific naming to animation-friendly names
- **Motion Capture**: Fix bone naming from OptiTrack Motive or other mocap systems
- **Game Export**: Apply scale properly before exporting to Unreal/Unity/Godot
- **Rig Standardization**: Match bone naming conventions across multiple characters

## Tips & Tricks

- **Batch Renaming**: Use Quick Rename repeatedly on different bone pairs to transfer an entire naming scheme
- **Undo Support**: All operations support Blender's undo system (`Ctrl+Z`)
- **Nested Hierarchies**: Safe Apply Scale handles complex parent chains automatically
- **Check Scale First**: Before exporting, verify all scale values are `(1, 1, 1)` in the object properties

## Troubleshooting

**"Lock Object Modes is on" warning:**
- Disable "Lock Object Modes" in the 3D Viewport header to select bones from multiple armatures

**Quick Rename button is greyed out:**
- Ensure you're in Pose Mode
- Make sure exactly 2 bones are selected (one from source, one from target)
- Verify the source armature is set in settings

**Safe Apply Scale not working:**
- Switch to Object Mode (the button only works in Object Mode)
- Make sure an armature is selected as the active object

---

## Requirements

- **Blender Version**: 4.1 or higher (SafeMotion Quicktools tested on 4.5+)
- FBX files exported from OptiTrack Motive (or compatible mocap software)
- Basic understanding of animation retargeting concepts

---

## Credits

**Author:** Oisín O'Sullivan  
**Version:** 1.0.0  
**Category:** Animation

**Special Thanks:**
- **Original Empties to Bones Script:** Artell - https://github.com/artellblender/empties_to_bones/tree/master
- **UE5-Manny:** Epic Games and cjlima - https://github.com/cjmlima/UE5-Blender-Rig

Developed for the SafeMotion project to streamline OptiTrack Motive to Unreal Engine mocap pipelines and anatomical skeleton workflows.

---

## License

Feel free to use, modify, and distribute these addons for your projects. Attribution appreciated but not required.

---

## Support

Found a bug or have a feature request? Open an issue on this repository!
