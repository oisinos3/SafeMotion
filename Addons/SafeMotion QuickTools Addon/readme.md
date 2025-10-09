# SafeMotion Quicktools for Blender

A comprehensive Blender addon providing basic rigging and animation utilities. Originally developed for working with anatomical skeletons and Optitrack motion capture data, I expanded the scripts I used into re-usable addons for anyone that needs them in future.

Since I built this from separate scripts for different uses - I have the original scripts and readme instructions in their folders, **Apply Scale Script** and **Quick Bone Renamer**.

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

---

## Installation

1. Download `safemotion_quicktools.py` from this repository
2. In Blender, go to **Edit > Preferences > Add-ons**
3. Click **Install...** and select the downloaded `.py` file
4. Enable the addon by checking the box next to "SafeMotion Quicktools"

The tools will appear in the **3D Viewport Sidebar** (press `N` to toggle) under the **"SafeMotion Quicktools"** tab.

---

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

---

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

---

## Use Cases

- **Mixamo Retargeting**: Clean up Mixamo character bone names to match your custom rig
- **Anatomical Models**: Rename bones from scientific naming to animation-friendly names
- **Motion Capture**: Fix bone naming from Optitrack Motive or other mocap systems
- **Game Export**: Apply scale properly before exporting to Unreal/Unity/Godot
- **Rig Standardization**: Match bone naming conventions across multiple characters

---

## Requirements

- Blender 4.5 or higher (Untested on previous versions, though I expect it would work)
- Works in both single and multiple armature workflows

---

## Tips & Tricks

- **Batch Renaming**: Use Quick Rename repeatedly on different bone pairs to transfer an entire naming scheme
- **Undo Support**: All operations support Blender's undo system (`Ctrl+Z`)
- **Nested Hierarchies**: Safe Apply Scale handles complex parent chains automatically
- **Check Scale First**: Before exporting, verify all scale values are `(1, 1, 1)` in the object properties

---

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

## Credits

**Author:** Oisín O'Sullivan  
**Version:** 1.0.0  
**Category:** Animation

Developed for the SafeMotion project to streamline rigging workflows with anatomical skeleton models and retargeted animations.

---

## License

Feel free to use, modify, and distribute this addon for your projects. Attribution appreciated but not required.

---

## Support

Found a bug or have a feature request? Open an issue on this repository!
