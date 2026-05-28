# MedVirtuoso

MedVirtuoso is a customized medical imaging platform built on top of MRIcroGL, designed for MRI visualization, radiological workflows, and future clinical imaging integration.

This project focuses on creating a simplified and professional medical imaging application tailored for medical and research environments.

---

# Features

* MRI and NIfTI image visualization
* Multi-planar reconstruction (MPR)
* 2D slice navigation
* Volume rendering
* Overlay support
* Atlas support
* Simplified UI for clinical workflows
* Custom MedVirtuoso branding
* Lightweight native Windows desktop application

---

# Built With

* Lazarus IDE
* FreePascal
* OpenGL
* MRIcroGL base framework

---

# Current Customizations

* Removed unnecessary developer/research tools
* Simplified menu system
* Custom "About Us" dialog
* MedVirtuoso branding integration
* Streamlined clinical-style interface

---

# Project Structure

```text
MRIcroGL12/
├── MRIcroGL.exe
├── shader/
├── standard/
├── atlas/
├── Resources/
├── mainunit.pas
├── mainunit.lfm
└── MRIcroGL.lpi
```

---

# Building The Project

## Requirements

* Lazarus IDE
* FreePascal Compiler
* Windows environment
* OpenGL-supported GPU

---

## Build Instructions

1. Open:

```text
MRIcroGL.lpi
```

inside Lazarus.

2. Click:

```text
Run → Build
```

3. Output executable:

```text
MRIcroGL.exe
```

---

# Running The Application

Run:

```text
MRIcroGL.exe
```

Ensure required folders remain alongside the executable:

* shader/
* standard/
* atlas/
* Resources/

---

# Distribution

The application is distributed as a packaged Windows installer.

Installer workflow:

```text
Source Code
   ↓
Lazarus Build
   ↓
MRIcroGL.exe
   ↓
Release Folder
   ↓
Inno Setup Installer
   ↓
MedVirtuosoInstaller.exe
```

Users install the software using:

```text
MedVirtuosoInstaller.exe
```

---

# Future Roadmap

* DICOM workflow improvements
* PACS integration
* AI-assisted imaging tools
* Advanced 3D rendering
* Annotation system
* Reporting workflows
* Cloud synchronization
* Auto-update system

---

# License

This project is based on MRIcroGL and follows all applicable upstream licensing requirements.

Custom MedVirtuoso modifications © MedMarvel Software Solutions.

---

 - Rorden C (2025) MRIcroGL: voxel-based visualization for neuroimaging. Nature Methods. [doi: 10.1038/s41592-025-02763-7](https://doi.org/10.1038/s41592-025-02763-7)

