# 🚀 Project Initialization: Backend Library System

Please complete the following foundational tasks to set up the library project. Ensure all code follows PEP 8 standards and includes necessary comments.

---

### 1. Modularize Project Configuration
* **Task:** Refactor the current configuration into a separate `settings.py` or a `settings/` package.
* **Description:** Move away from the default monolithic settings file. Ensure the configuration is structured to support different environments (Local, Dev, Production) to maintain a clean separation of concerns.

### 2. Environment Variable Management
* **Task:** Setup and access a `.env` file for sensitive configurations.
* **Description:** Use `django-environ` or `python-dotenv`. Move the `SECRET_KEY`, database credentials, and any third-party keys into the `.env` file. 
* **Action:** Ensure `.env` is added to `.gitignore`.

### 3. Production-Grade Database Integration
* **Task:** Configure **PostgreSQL** or **MySQL** as the primary database.
* **Description:** Transition from SQLite to a production-ready RDBMS. You must:
    * Install the appropriate driver (e.g., `psycopg2-binary`).
    * Update the `DATABASES` configuration in settings.
    * Run migrations to verify the connection.

### 4. API Documentation (Swagger/OpenAPI)
* **Task:** Integrate Swagger UI for API discovery.
* **Description:** Use `drf-spectacular` (recommended) or `drf-yasg`. Ensure all library endpoints are automatically documented and accessible via `/api/docs/` or a similar path.

### 5. Dockerization
* **Task:** Create a `Dockerfile` and `docker-compose.yml`.
* **Description:** Containerize the application. The `docker-compose` file should orchestrate both the Django web service and the database service, ensuring the project can be spun up with a single command.

### 6. Authentication & User Management (JWT)
* **Task:** Implement `Django Rest Framework SimpleJWT (djangorestframework-simplejwt)` and user identity flows.
* **Description:** Build the following functionalities:
    * **User Registration:** Endpoint to create new library members.
    * **Sign-in:** Exchange credentials for Access/Refresh JWT tokens.
    * **User Verification:** Logic to handle account activation or status checks.

### 7. Custom API Protection
* **Task:** Protect all user-facing endpoints.
* **Description:** Apply permission classes (e.g., `IsAuthenticated`) globally or to specific viewsets. Implement a custom authentication/permission class if the library logic requires specific ownership checks (e.g., "Only the user who borrowed the book can see this record").