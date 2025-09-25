# Unreal Engine Level Setup for OptiTrack Rigid Bodies

This guide provides a step-by-step process for setting up an Unreal Engine level to import and use rigid body data from OptiTrack.

---

## 1. Import OptiTrack Rigid Body Assets

Drag and drop the **Rigidbody_Export** folder directly into your Unreal Engine project's Content Browser. This folder should contain the skeletal meshes, skeletons, and animation assets for your rigid bodies. If prompted during import, you may need to check the "Closest Frame Boundary" box in the Animation settings menu.

<div align="center">
  <img src="https://github.com/user-attachments/assets/94d4794e-5f4a-43a6-a789-5d0b3cbaf2e6" width="565" height="66" alt="image" />
</div>


---

## 2. Import Main Human Animations

Import the primary human animations. If there are any skeleton conflicts, you can clear the skeleton association; the skeleton itself will still import correctly.

| Image 1 | Image 2 | Image 3 |
|:---:|:---:|:---:|
| <img src="https://github.com/user-attachments/assets/a609fdf8-9ef3-4eae-a7b3-03882e3c3fa0" width="350" /> | <img src="https://github.com/user-attachments/assets/c3a790cf-e8cf-434e-9627-7ccbd52c3620" width="350" /> | <img src="https://github.com/user-attachments/assets/07e51669-db99-4b9b-bca3-698882e580c8" width="350" /> |

---

## 3. Configure Sockets on Skeletons

Open the **skeletons** (not the skeletal meshes) for your rigid bodies. Set up the necessary sockets on these skeletons. The sockets are crucial for attaching other meshes and aligning them with the OptiTrack data.

---

## 4. Set Up the Actor Blueprint

Create a new Actor Blueprint and follow these steps:

1.  Bring in the skeletal meshes for your rigid bodies.
2.  Set their animation mode to **Asset** and choose the corresponding animation asset you imported earlier.
3.  Bring in your 3D meshes (these should be designed to match your rigid bodies).
4.  For each 3D mesh, find the **Parent Socket** property and set it to the socket you created on the skeleton.

The pivot points of the 3D meshes will now match the rigid body locations, but you will likely need to adjust the scale, rotation, and final position of the meshes to perfectly suit your model.


---

## 5. Animate Using Sequencer

To set up the animation with proper scrubbing and playback controls, use the **Sequencer**.

1.  Pull your Actor Blueprint into the Sequencer timeline.
2.  Click the **+ Track** button on the Actor Blueprint and add a **Skeletal Mesh** track for one of your rigid bodies.
3.  Click the **+** button on the new Skeletal Mesh track and select **Animation**.
4.  Choose the correct animation asset from the drop-down menu.
5.  Repeat this process for all of your rigid bodies to create their respective animation tracks in the Sequencer.


---

## 6. Done!

Your rigid bodies are now correctly set up in Unreal Engine, ready to be driven by your OptiTrack data. You can now use the Sequencer to scrub through the animation, render out the sequence, or use it for real-time applications.
