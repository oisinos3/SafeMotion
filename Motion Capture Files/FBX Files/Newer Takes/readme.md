### File Contents

The files in this folder are the most recent takes recorded, and are named to reflect their contents and required processing steps.

---

* **`RigidBodies_Only` files:** These files contain only rigid bodies with no human skeletons or skeletal meshes. They **must be processed through the Blender addon** to be read by Unreal, as they lack a skeletal mesh or armature.
* **`Box_Handoff` files:** These files contain no rigid bodies. They were recorded to test the interaction between two human subjects (Julian and myself) handing off boxes.
* **All other files:** These files contain both human skeletons and rigidbody empties. The rigidbody empties **must be processed through the Blender addon** before being imported into Unreal.
