# Full-Stack Assignment

A full-stack web application built with Django (backend) and Vue.js (frontend).

## 🚀 Project Structure

```
assingment/
├── backend_repo/          # Django backend application
│   ├── apps/
│   │   └── demo/         # Main Django app
│   ├── demo_project/     # Django project settings
│   ├── manage.py         # Django management script
│   └── requirements.txt  # Python dependencies
└── frontend/             # Vue.js frontend application
    ├── src/              # Source code
    ├── public/           # Static assets
    ├── package.json      # Node.js dependencies
    └── vite.config.js    # Vite configuration
```

## 🛠️ Technologies Used

### Backend
- **Django** - Python web framework
- **Django REST Framework** - API development
- **SQLite** - Database
- **Python** - Programming language

### Frontend
- **Vue.js 3** - Progressive JavaScript framework
- **Vite** - Build tool and development server
- **JavaScript/HTML/CSS** - Frontend technologies

## 📋 Prerequisites

Before running this project, make sure you have the following installed:

- **Python 3.8+**
- **Node.js 16+**
- **npm** or **yarn**

## 🚀 Getting Started

### Backend Setup

1. **Navigate to the backend directory:**
   ```bash
   cd backend_repo
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the Django development server:**
   ```bash
   python manage.py runserver
   ```

   The backend will be available at `http://localhost:8000`

### Frontend Setup

1. **Navigate to the frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm run dev
   ```

   The frontend will be available at `http://localhost:5173`

## 📁 Project Components

### Backend (Django)

- **Models**: Data models for the application
- **Views**: API endpoints and business logic
- **Serializers**: Data serialization for API responses
- **Tests**: Unit tests for the application
- **Migrations**: Database schema changes

### Frontend (Vue.js)

- **Components**: Reusable Vue components
- **Assets**: Static files (images, styles)
- **Main App**: Root Vue application
- **Configuration**: Vite build configuration

## 🔧 Development

### Backend Development

- **Create new migrations:**
  ```bash
  python manage.py makemigrations
  ```

- **Run tests:**
  ```bash
  python manage.py test
  ```


### Frontend Development

- **Build for production:**
  ```bash
  npm run build
  ```

- **Preview production build:**
  ```bash
  npm run preview
  ```

## 📝 API Documentation

The Django backend provides REST API endpoints. You can access the API documentation at:
- **Django Admin**: `http://localhost:8000/admin/`
- **API Root**: `http://localhost:8000/api/`

## 🧪 Testing

### Backend Tests
```bash
cd backend_repo
python manage.py test
```

### Frontend Tests
```bash
cd frontend
npm run test
```





## 👨‍💻 Author

**Aditya Kumar Singh**
- GitHub: [@aditya-devm02](https://github.com/aditya-devm02)

## 🔗 Repository

- **GitHub**: https://github.com/aditya-devm02/assignmentss.git

---

