# OptiTrack Rigidbody Generator for Blender

A Blender addon for converting OptiTrack rigidbody animations into skeletal meshes suitable for game engines like Unreal Engine.

This tool streamlines the workflow of importing animated empties from an OptiTrack FBX, generating single-bone armatures for each, baking the animation, and exporting them as game-ready FBX files. It provides both a manual step-by-step process and a fully automated one-click pipeline.

## Features

* **Organized FBX Importer:** Imports OptiTrack FBX files and automatically organizes the contents into a clean collection hierarchy (Rigidbodies, Skeleton).
* **Rigidbody to Armature Creation:** Generates a single-bone armature for each selected empty that contains "_bone" in its name.
* **Live Animation Linking:** The created armatures are constrained to the original empties, allowing you to see the animation live before baking.
* **One-Click Baking:** Bakes the animation from the empties to the new armatures for all created rigs at once.
* **Game-Ready FBX Export:** Exports armatures with their mesh children to individual `.fbx` files with Unreal Engine-friendly settings.
* **Full Automation Pipeline:** A one-click operator that handles the entire process: importing an FBX, creating the rigs, baking the animations, and exporting the final files.
* **Post-Import Pipeline:** A second automation operator that can be run on an already imported scene.
* **Convenience Features:**
    * Automatically opens the export folder upon completion.
    * Automatically clears the internal "tracked armatures" list after each export for a clean workflow.
    * UI prompts and warnings to guide the user.

## Installation

1.  Download the `empties-to-rigidbodies.py` file.
2.  In Blender, go to `Edit` > `Preferences...`
3.  Navigate to the `Add-ons` tab and click `Install...`
4.  Select the `empties-to-rigidbodies.py` file and click `Install Add-on`.
5.  Find the "OptiTrack: Rigidbody Tools" addon in the list and enable it by checking the box.

The addon's panels will now be available in the 3D View's sidebar (press `N` to open).

## How to Use

The addon is organized into three panels in the Blender sidebar: **Importer**, **Rigidbody Tools**, and **Automation**.

### Workflow 1: Manual (Step-by-Step)

This workflow gives you the most control over each stage of the process.

#### Step 1: Import FBX
* In the **Importer** panel, click `Import OptiTrack FBX`.
* Select your `.fbx` file exported from Motive.
* The addon will import the file and create a new parent collection for its contents.

#### Step 2: Create Rigs
* Select the empties you wish to convert. You can select the parent empty or the `_bone` empty directly.
* In the **Rigidbody Tools** panel, under "Step 1: Empties to Armatures", choose how you want to select the source empties:
    * `From Selected`: Processes only the empties you have selected.
    * `From Active Collection`: Processes all `_bone` empties in the currently active collection.
    * `From All in Scene`: Processes every `_bone` empty in the entire scene.
* A pop-up will appear allowing you to confirm the names for the new armatures, set a size for the proxy mesh (`Cube Size`), and choose what to do with the original empties (`Cleanup Empties`).

#### Step 3: Bake Armatures
* Once you are happy with the generated rigs, go to "Step 2: Bake Created Armatures".
* Click `Bake Created Armatures`. This will bake the animation from the source empties onto the bones of the new armatures and remove the constraints.
* The trash can icon next to the title can be used to manually clear the addon's internal list of tracked armatures if needed.

#### Step 4: Export
* Go to "Step 3: Export Armatures".
* Set a name for your export sub-folder in the **Export Folder** text field.
* Choose your export method:
    * `Export Selected Armatures`: Only exports the armatures you currently have selected.
    * `Export All Created Armatures`: Exports all armatures that were generated and tracked by the addon in this session.
* After the export is complete, the addon will automatically **clear its internal tracked list** and **open the export folder** for you.

### Workflow 2: Automation

The **Automation** panel is designed for a fast, one-click workflow. All settings are controlled directly from this panel.

#### Settings
* **Export Folder**: The name of the sub-folder where the final FBX files will be saved.
* **Cube Size**: The size of the proxy mesh created for each rig.
* **Cleanup**: What to do with the original `_bone` empties after rig creation (Hide or Delete).

#### Running the Pipeline
There are two main automation operators:

1.  **Run Full Pipeline (from file)**:
    * This is a complete, hands-off process.
    * It will first ask you to select an `.fbx` file to import.
    * It will then automatically create rigs for all `_bone` empties found within that file, bake their animations, and export them as individual `.fbx` files.

2.  **Run on Entire Scene**:
    * This operator is for when you have already imported your FBX (or have the necessary empties in your scene).
    * It will scan the entire current scene for any `_bone` empties, create rigs, bake them, and export them.

Both automation pipelines will export the final files to a sub-folder located in the **same directory as your saved `.blend` file**. After the process is finished, the export folder will open automatically.
