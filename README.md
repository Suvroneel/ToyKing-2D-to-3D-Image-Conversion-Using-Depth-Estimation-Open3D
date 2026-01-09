# ToyKing — Image-to-Pseudo-3D Processing API

ToyKing is an **API-first image processing service** that transforms 2D images into **pseudo-3D depth representations** using classical computer vision and 3D processing techniques.  
The project is designed as a **backend microservice**, prioritizing clean architecture, RESTful design, and deployability over UI polish.

---

## Problem Statement

Most 2D-to-3D or depth-estimation implementations exist as standalone scripts, Jupyter notebooks, or tightly coupled demo code.  
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

**Flow:**  

1. **Client**: Any HTTP client (curl, Postman, or other service) uploads an image.  
2. **Flask REST API**: Receives the image, validates it, and triggers the processing pipeline.  
3. **Processing Layer**: OpenCV / Open3D pipeline performs pseudo-3D depth transformation.  
4. **Output**: Processed image preview is stored in `outputs/` and a JSON response is returned with the file path and status.

**Design Principles:**

- API-only backend (no frontend coupling)  
- Clear separation of routing and processing logic  
- Stateless execution suitable for cloud deployment  
- Extensible processing pipeline

---

## Project Structure

```

toyking-backend/
├── app.py
├── processing/
│   └── pipeline.py
├── templates/
│   └── index.html
├── requirements.txt
└── README.md


````

---

## API Endpoints

### POST `/convert`

Uploads an image and triggers pseudo-3D processing.

**Request**  

- **Method:** `POST`  
- **Content-Type:** `multipart/form-data`  
- **Field:** `image` (file)

**Example using curl:**  
```bash
curl -X POST http://127.0.0.1:5000/convert \
     -F "image=@sample.jpg"
````

**Response:**

```json
{
  "status": "success",
  "output_path": "outputs/result.png"
}
```

---

### GET `/health`

Simple health check endpoint to verify the service is running.

**Request**

* **Method:** `GET`

**Example using curl:**

```bash
curl http://127.0.0.1:5000/health
```

**Response:**

```json
{
  "status": "ok"
}
```

---

## Running Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the backend

```bash
python app.py
```

### 3. Test using curl

```bash
curl -X POST http://127.0.0.1:5000/convert \
     -F "image=@sample.jpg"
```

---

## Deployment

ToyKing is designed to run as a **headless backend service** and can be deployed directly on platforms such as **Render**.

* No frontend build step
* No template rendering
* Minimal configuration required

---

## Technical Notes

* Focuses on **backend system design and integration**
* Pseudo-3D depth transformation is intentionally simplified
* Processing layer can be replaced with advanced depth models without changing the API contract

---

## Why ToyKing

ToyKing demonstrates:

* Backend-first engineering mindset
* REST API design for compute-heavy workloads
* Clean separation of concerns
* Deployment-ready architecture

Rather than presenting image processing as a script, ToyKing treats it as a **service**.

---

## Future Enhancements

* Multiple processing modes
* Asynchronous job handling
* Model-based depth estimation
* Client-side frontend integration

