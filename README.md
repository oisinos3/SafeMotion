---

# SafeMotion Project

| Progress Bar | Percentage |
|:---|:---|
| ████████████░░░░░░░░ | **58.5%** |

This is the project repository for all documentation, assets, information, and tutorials on the **SafeMotion project**. The project utilizes **OptiTrack motion capture** to help visualize safety procedures and the effects of unsafe manual handling.

The repository is actively maintained and serves as a central hub for all project resources.

---

### ⚙️ Core Components & Documentation

* **Blender Addon & Documentation**: A custom Blender addon for converting Motive FBX rigidbodies into armatures for use in Unreal Engine.
  * [Find it here](https://github.com/oisinos3/SafeMotion/tree/main/Rigidbody%20Generator%20Addon)

* **Unreal Engine Setup**: Instructions for importing and setting up the rigid body armatures within Unreal Engine.
  * [Find it here](https://github.com/oisinos3/SafeMotion/blob/main/rigidbody_unreal_import.md)

* **FBX Files**: List of organised FBX Files, including documentation on the files contents.
  * [Find them here](https://github.com/oisinos3/SafeMotion/tree/main/Motion%20Capture%20Files)

---

### **🎬 Export & Workflow Best Practices**

### **For Better Exports - no Addons or Post-Processing required**

* **Skeletal Mesh Option:** When exporting your data, ensure the "Skeletal Mesh" option is enabled for both the **Rigidbodies** and the **Skeletons**. This is crucial for them to be recognized and imported correctly into Unreal Engine.

### **For Best Practice & Accurate Matching**

* **Mark Pivot Points:** In Motive, make a note of or physically mark the pivot point of each rigid body. This ensures we know its exact location, for accurate alignment when placing and parenting objects in Unreal.
* **Mark the Floor Point:** Mark and export the floor point from thr Motive capture. This provides a consistent reference for the ground plane, helping to align your entire scene correctly in Unreal Engine.
* **Collect Reference Footage:** As you record your motion capture data, simultaneously capture reference footage to be sure the captured data is accurate, and can help match rigidbodies etc.

---

### 💡 Upcoming Documentation

* Instructions for retargeting skeletons to Metahumans and iClone characters.
* Hosted Unreal Engine project files.

---

### ✅ Features Checklist

* [x] Blender Addon
* [x] Unreal Engine Rigidbodies Setup Guide
* [x] Hosted FBX Files
* [ ] Metahuman Retargeting Guide
* [ ] Required Settings List
* [x] Methodology Guide
