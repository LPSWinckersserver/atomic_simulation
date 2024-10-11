
# Atomic Simulation Application

This project simulates and visualizes the electronic structure of chemical elements, incorporating their relationships with mathematical equations, neutrons, positrons, and light waves.

## Project Structure

- **backend/**: Python-based backend built with FastAPI and SQLAlchemy.
- **frontend/**: Rust-based frontend built with the Yew framework.
- **alembic/**: Database migration scripts using Alembic.
- **docker-compose.yml**: Docker configuration for containerizing services.
- **README.md**: Project documentation.

## Setup Instructions

### Prerequisites

- **Python 3.8+**
- **Rust and Cargo**
- **Trunk** (for building Yew frontend)
- **PostgreSQL**

### Steps

1. **Run the Setup Script:**
    ```bash
    python setup_project.py
    ```
    - This will create the entire project structure with necessary files.

2. **Backend Setup:**
    - Navigate to the backend directory:
        ```bash
        cd atomic_simulation/backend
        ```
    - Activate the virtual environment:
        - **On Unix or MacOS:**
            ```bash
            source ../env/bin/activate
            ```
        - **On Windows:**
            ```bash
            ..\env\Scripts\activate
            ```
    - Install dependencies:
        ```bash
        pip install -r requirements.txt
        ```
    - Run database migrations:
        ```bash
        alembic upgrade head
        ```
    - Start the backend server:
        ```bash
        uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
        ```
    - Access API documentation at [http://localhost:8000/docs](http://localhost:8000/docs)

3. **Frontend Setup:**
    - Navigate to the frontend directory:
        ```bash
        cd atomic_simulation/frontend
        ```
    - Build and serve the frontend:
        ```bash
        trunk serve
        ```
    - Access the frontend at [http://localhost:8080](http://localhost:8080)

4. **Docker Setup (Optional):**
    - If you prefer containerization, ensure Docker is installed and run:
        ```bash
        docker-compose up
        ```
    - This will set up the PostgreSQL database, backend server, and frontend simultaneously.

## Features

- **Backend:**
    - Manage chemical elements, groups, periods, equations, neutrons, positrons, and light waves.
    - Many-to-Many relationships between elements and equations, and between equations and light waves.
    - RESTful API built with FastAPI.

- **Frontend:**
    - Displays the periodic table organized by groups and periods.
    - Provides detailed information about each element.
    - Built with Yew for a fast and interactive user interface.

## Further Enhancements

- Implement dynamic simulations responding to changes in physical parameters.
- Enhance frontend interactivity with more detailed visualizations.
- Secure the application with authentication and authorization mechanisms.
- Containerize the application using Docker for easier deployment.

## License

MIT License
