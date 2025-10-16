# Skeleton Retargeting Instructions

---

In the Unreal Project, I've created a blank IK Retargeter asset, and an IK Rig of the Skeleton model to use with it and retarget to.

Copy this IK Retargeter next to the source IK Rig - I'll put instructions for setting that up here too.

The following fields in the OP Stack are blank and require you to input the bones based on the source skeleton's bone names:

1. In the main IK Retargeter page, input your source IKRig asset.

<img width="686" height="276" alt="image" src="https://github.com/user-attachments/assets/5b53fb77-a989-4ece-838e-2cc94f0d334e" />

2. In the OP Stack - in "Copy Base Pose" - type out the name of the Root bone into the box - it must be exact, as it's not a selector tool.

<img width="437" height="93" alt="image" src="https://github.com/user-attachments/assets/c735ff32-5f0d-4bc4-a28a-fb581d164be6" />

3. In the OP Stack - in "Pelvis Motion" - select the source Pelvis bone.

<img width="497" height="96" alt="image" src="https://github.com/user-attachments/assets/4b1b6a1a-ee87-4e72-b494-48d96e8551e5" />

4. Finally in the OP Stack - in "Root Motion" - select the source Root bone.

<img width="475" height="91" alt="image" src="https://github.com/user-attachments/assets/19da515b-098d-4012-a782-b33a84e204dd" />


You're ready to go! The Skeleton Model should retarget correctly - use the normal retargeting method, but uncheck the "Auto Generate Retargeter" option, and select the one you've just set up. Select the animation and export.
 
<img width="1283" height="605" alt="image" src="https://github.com/user-attachments/assets/19df5c6a-2622-4b74-9479-affc1c08c03c" />

