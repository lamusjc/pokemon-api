# Pokemon API Backend

A Django-based REST API that allows listing and managing Pokemon data by consuming the PokeAPI. Built as part of the Unitips technical assessment.

## 🌟 Features

- Pokemon listing and detailed view
- Real-time import progress updates via WebSockets
- Admin interface for Pokemon management
- RESTful API endpoints
- Asynchronous task processing

## 🔧 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment tool

## 🚀 Installation

1. Clone the repository

````bash
git clone https://github.com/lamusjc/pokemon-api.git
cd pokemon-api

2. Create and activate virtual environment


For Windows:

```shellscript
python -m venv env
.\env\Scripts\activate.ps1
````

For Linux/MacOS:

```shellscript
python -m venv env
source env/bin/activate
```

3. Install dependencies

```shellscript
pip install -r requirements.txt
```

## ⚙️ Configuration

1. Apply database migrations

```shellscript
python manage.py migrate
python manage.py makemigrations
```

2. Create a superuser for admin access

```shellscript
python manage.py createsuperuser
```

3. Create a `.env` file in the root directory:

```env
SECRET_KEY=YOUR-SECRET-KEY
DEBUG=False
DB_NAME=database
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
```

## 🏃‍♂️ Running the Application

1. Start the Daphne server (WebSocket + HTTP):

```shellscript
daphne -b 0.0.0.0 -p 8000 project.asgi:application
```

2. In a separate terminal, run the static files server:

```shellscript
python manage.py runserver 8001
```

The application will be available at:

- Main API: [http://localhost:8000](http://localhost:8000)
- Admin interface: [http://localhost:8001/admin](http://localhost:8001/admin)

## 📚 API Documentation

### Endpoints

- `GET /api/pokemon/` - List all Pokemon
- `GET /api/pokemon/{id}/` - Get Pokemon details
- `POST /api/import-pokemon/` - Start Pokemon import process

### WebSocket

Connect to `ws://localhost:8000/ws/pokemon/` to receive real-time import progress updates.

## 🛠️ Development

To run tests:

```shellscript
python manage.py test
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact

Project Link: [https://github.com/lamusjc/pokemon-api](https://github.com/lamusjc/pokemon-api)