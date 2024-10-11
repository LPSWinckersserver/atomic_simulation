
# Backend

This directory contains the Python-based backend built with FastAPI and SQLAlchemy.

## Setup

1. **Navigate to Backend Directory:**
    ```bash
    cd backend
    ```

2. **Activate Virtual Environment:**
    - **On Unix or MacOS:**
        ```bash
        source ../env/bin/activate
        ```
    - **On Windows:**
        ```bash
        ..\env\Scripts\activate
        ```

3. **Install Python Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run Database Migrations (Using Alembic):**
    ```bash
    alembic upgrade head
    ```

5. **Run the Backend Server:**
    ```bash
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
    ```

    - **Access API Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)

## Features

- Provides RESTful API endpoints for managing elements, groups, periods, equations, neutrons, positrons, and light waves.
- Implements Many-to-Many relationships between elements and equations, and between equations and light waves.
- Utilizes SQLAlchemy for ORM and Alembic for database migrations.
- Built with FastAPI for high performance and ease of development.
