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
- Redis server
- PostgreSQL

### Installing PostgreSQL

#### On Ubuntu/Debian:

```shellscript
sudo apt update
sudo apt install postgresql postgresql-contrib
```

To start the PostgreSQL service:

```shellscript
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

#### On macOS (using Homebrew):

```shellscript
brew install postgresql
```

To start the PostgreSQL service:

```shellscript
brew services start postgresql
```

#### On Windows:

1. Download the PostgreSQL installer from the official PostgreSQL website ([https://www.postgresql.org/download/windows/](https://www.postgresql.org/download/windows/)).
2. Run the installer and follow the prompts.
3. During installation, you'll be asked to set a password for the database superuser (postgres).
4. After installation, you can start PostgreSQL from the Start menu or use the pgAdmin tool that comes with the installation.


### Configuring PostgreSQL

After installation, you need to create a database for your project:

1. Access the PostgreSQL prompt:

On Linux:

```shellscript
sudo -u postgres psql
```

On macOS:

```shellscript
psql postgres
```

On Windows, use pgAdmin or the SQL Shell (psql) from the Start menu.


2. Create a new database:

```sql
CREATE DATABASE pokemondb;
```


3. Create a new user:

```sql
CREATE USER pokemonuser WITH PASSWORD 'your_password';
```


4. Grant privileges to the user on the database:

```sql
GRANT ALL PRIVILEGES ON DATABASE pokemondb TO pokemonuser;
```


5. Exit the PostgreSQL prompt:

```plaintext
\q
```

### Installing Redis Server

#### On Ubuntu/Debian:

```shellscript
sudo apt update
sudo apt install redis-server
```

To start the Redis server:

```shellscript
sudo systemctl start redis-server
```

#### On macOS (using Homebrew):

```shellscript
brew install redis
```

To start the Redis server:

```shellscript
brew services start redis
```

#### On Windows:

1. Download the Redis installer from the official Redis website.
2. Run the installer and follow the prompts.
3. After installation, you can start Redis from the command prompt:

```shellscript
redis-server
```

## 🚀 Installation

1. Clone the repository

````bash
git clone https://github.com/lamusjc/pokemon-api.git
cd pokemon-api
````

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

1. Create a `.env` file in the root directory:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True # Set to False in production

# Database Configuration
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432

# Redis Configuration
REDIS_HOST=127.0.0.1

# API Keys
POKEAPI_BASE_URL=https://pokeapi.co/api/v2/pokemon

# Security Settings
ALLOWED_HOSTS=localhost,127.0.0.1

# CORS settings
CORS_ALLOW_ALL_ORIGINS=False
CORS_ALLOWED_ORIGINS=http://localhost:3000,https://yourdomain.com
```

2. Apply database migrations

```shellscript
python manage.py migrate
python manage.py makemigrations
```

3. Create a superuser for admin access

```shellscript
python manage.py createsuperuser
```

4. Generate static files for the admin panel

```shellscript
python manage.py collectstatic
```

## 🏃‍♂️ Running the Application

1. Start the Daphne server (WebSocket + HTTP):

```shellscript
daphne -b 0.0.0.0 -p 8000 project.asgi:application
```

2. Or to run the application in a development environment, use the following command (do not use in production):

```shellscript
python manage.py runserver 8000
```

The application will be available at:

- Main API: [http://localhost:8000/api](http://localhost:8000)
- Admin interface: [http://localhost:8000/admin](http://localhost:8000/admin)

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