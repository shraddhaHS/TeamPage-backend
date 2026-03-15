
# Armatrix Team Page – Backend

This is the backend API for the Armatrix Team Page assignment.  
It provides REST endpoints for managing team member data used by the frontend application.

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/shraddhaHS/TeamPage-backend
````

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Mac/Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the server

```bash
uvicorn main:app --reload
```

The API will run at:

```
http://localhost:8000
```

---

## Design Decisions

### FastAPI for REST API

FastAPI was chosen for its simplicity, performance, and automatic API documentation.

### Simple Team Member Schema

Each team member includes fields such as **name, role, bio, photo, and social links**.

### Image Handling

Profile photos are uploaded and stored using **Cloudinary** to handle image storage efficiently.

### CRUD Endpoints

The API supports creating, updating, deleting, and fetching team members.

---

## Notes

* No authentication was added as per the assignment instructions.
* CORS is enabled to allow communication with the frontend application.

---

## Deployment

Backend deployed on **Render**:

```
https://teampage-backend.onrender.com
```

```

