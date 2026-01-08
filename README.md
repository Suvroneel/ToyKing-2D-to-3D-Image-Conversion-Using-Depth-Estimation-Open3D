# ToyKing — Image-to-Pseudo-3D Processing API

ToyKing is an **API-first image processing service** that transforms 2D images into **pseudo-3D depth representations** using classical computer vision and 3D processing techniques.  
The project is designed as a **backend microservice**, prioritizing clean architecture, RESTful design, and deployability over UI polish.

---

## Problem Statement

Most 2D-to-3D or depth-estimation implementations exist as:
- Standalone scripts
- Jupyter notebooks
- Tightly coupled demo code

These approaches are difficult to integrate, reuse, or deploy as part of real systems.

---

## Solution Overview

ToyKing exposes the image-to-depth transformation logic as a **Flask-based REST API**, enabling:

- Programmatic image upload
- Server-side pseudo-3D processing
- Stateless request–response handling
- Cloud-ready deployment (e.g., Render)

The system is intentionally **UI-agnostic**, allowing any HTTP client to consume the service.

---

## Architecture

