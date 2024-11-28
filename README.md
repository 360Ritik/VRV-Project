
# User Registration, Authentication, and Role-Based Access Control System

This project implements a user authentication and role-based access control system using Django REST Framework (DRF) and JWT for authentication.

This is a short video demonstration of the API for the app: [API Demonstration Video](file:///home/ritik360/Videos/Screencasts/rbac.webm)
)
_link_here).
## Features

1. **User Registration**: Allows new users to register.
2. **User Login**: Validates credentials and issues JWT tokens.
3. **Role-Based Access Control**: Provides restricted access to endpoints based on user roles.

## API Endpoints

### **1. User Registration**
- **URL:** `/auth/register/`  
- **Method:** `POST`  
- **Permission:** Public  
- **Request Body Example:**
  ```json
  {
    "username": "example_user",
    "password": "secure_password",
    "role": "User"
  }
  ```
- **Response Example:**
  - **Success (201):**
    ```json
    {
      "message": "User registered successfully"
    }
    ```
  - **Error (400):**
    ```json
    {
      "username": ["This field is required."]
    }
    ```

---

### **2. User Login**
- **URL:** `/auth/login/`  
- **Method:** `POST`  
- **Permission:** Public  
- **Request Body Example:**
  ```json
  {
    "username": "example_user",
    "password": "secure_password"
  }
  ```
- **Response Example:**
  - **Success (200):**
    ```json
    {
      "refresh": "REFRESH_TOKEN",
      "access": "ACCESS_TOKEN"
    }
    ```
  - **Error (401):**
    ```json
    {
      "error": "Invalid credentials"
    }
    ```

---

### **3. Role-Protected Views**

#### **Role-Protected Endpoint**
- **URL:** `/auth/protected/`  
- **Method:** `GET`  
- **Required Roles:** `Admin`, `User`  
- **Response Example:**
  ```json
  {
    "message": "Hello, you have access!"
  }
  ```

#### **Manager and Developer Endpoint**
- **URL:** `/auth/manager-developer/`  
- **Method:** `GET`  
- **Required Roles:** `Manager`, `Developer`  
- **Response Example:**
  ```json
  {
    "message": "Hello, you have access as Manager or Developer!"
  }
  ```

#### **Manager-Only Endpoint**
- **URL:** `/auth/manager-only/`  
- **Method:** `GET`  
- **Required Role:** `Manager`  
- **Response Example:**
  ```json
  {
    "message": "Hello, you have access as Manager!"
  }
  ```

#### **Admin-Only Endpoint**
- **URL:** `/auth/admin-only/`  
- **Method:** `GET`  
- **Required Role:** `Admin`  
- **Response Example:**
  ```json
  {
    "message": "Hello, you have access as Admin!"
  }
  ```

#### **Admin and Manager Endpoint**
- **URL:** `/auth/admin-admin-only/`  
- **Method:** `GET`  
- **Required Roles:** `Admin`, `Manager`  
- **Response Example:**
  ```json
  {
    "message": "Hello, you have access as Admin only!"
  }
  ```

---

## How to Run Locally

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/360Ritik/VRV-Project.git
   cd VRV-Project
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Create Migrations**:
   ```bash
   python manage.py makemigrations

   ```
4. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access API Documentation**:  
   Use tools like Postman or Swagger to interact with the endpoints.

---

## Technologies Used

- **Backend Framework**: Django REST Framework  
- **Authentication**: JWT (JSON Web Tokens)  
- **Database**: SQLite (default) or any other database configured in Django  
- **Role-Based Permissions**: Custom permissions using `RolePermission`  

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
