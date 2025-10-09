***

# Quick Bone Renamer for Blender

Originally made to set up the Anatomical Skeleton mesh for the project, but extended with some basic functionality.
A simple Blender addon for quickly renaming bones by transferring names between two separate armatures. This tool is ideal for animation retargeting, fixing models from Mixamo or Optitrack Motive, or matching naming conventions between different rigs.

---

 ## Features

* **One-Click Renaming**: Transfer a bone name from a source to a target with a single click.
* **Designated Source Armature**: Set a specific armature as the "source" to avoid ambiguity, regardless of selection order.
* **Custom Prefix Removal**: Automatically strip unwanted prefixes (e.g., `mixamorig:`) during the renaming process.
* **Safe & Strict**: Enforces renaming between two **separate** armatures to prevent accidentally renaming bones on the same rig.
* **Manual Workflow**: Includes an optional two-step process to copy, manually edit, and then apply a name.
* **Helpful UI**: Provides clear instructions and contextual warnings (e.g., if "Lock Object Modes" is enabled).

---

## Installation

1.  Download the `quick_bone_renamer.py` script from this repository.
2.  In Blender, go to **Edit > Preferences > Add-ons**.
3.  Click the **Install...** button and navigate to the downloaded `.py` file.
4.  Enable the addon by ticking the checkbox next to "Quick Bone Renamer".

---

## How to Use

The addon will appear in the **3D Viewport's Sidebar** (press the `N` key to show it) under the **"Quick Bone Renamer"** tab.


### Workflow

1.  **Disable "Lock Object Mode"**. In order to select bones from multiple skeletons, disable Lock Object Mode in the edit panel, then select each armature.
2.  **Enter Pose Mode on Each Armature**. The tool only works in this mode.
3.  **Set Source Armature**: In the "Smart Renamer" panel, click the "Source" dropdown and select the armature you want to copy bone names **FROM**.
4.  **Set Prefix (Optional)**: If your source bones have a common prefix you want to remove (e.g., `Skeleton001_`), type it into the **"Prefix to Remove"** field.
5.  **Select Bones**:
    * Select any bone on your **source** armature.
    * **Shift-select** any bone on your **target** armature (the one you want to rename).
6.  **Rename**: Click the **"Quick Rename (Copy & Apply)"** button. The target bone will be instantly renamed to match the source bone's name (minus the prefix).

### Manual Mode

If you need to edit a name before applying it, you can use the collapsed **"Manual Two-Step Process"** panel:
1.  Follow steps 1-4 above.
2.  Click **"Copy & Clean Name"**. The cleaned name will appear in the text box.
3.  Edit the name in the text box as needed.
4.  Click **"Apply Name"** to rename the active target bone.
