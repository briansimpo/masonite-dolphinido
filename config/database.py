import os
from dotenv import load_dotenv
from masoniteorm.connections import ConnectionResolver

load_dotenv()

DATABASES = {
  "default": os.getenv("DB_CONNECTION", "sqlite"),
  "mysql": {
    "driver": "mysql",
    "host": os.getenv("DB_HOST", "127.0.0.1"),
    "database": os.getenv("DB_DATABASE", "dolphinido"),
    "user": os.getenv("DB_USERNAME", "root"),
    "password": os.getenv("DB_PASSWORD", "root"),
    "port": os.getenv("DB_PORT", 3306),
    "log_queries": False,
    "options": {
      #
    }
  },
  "postgres": {
    "driver": "postgres",
    "host": os.getenv("DB_HOST", "127.0.0.1"),
    "database": os.getenv("DB_DATABASE", "dolphinido"),
    "user": os.getenv("DB_USERNAME", "root"),
    "password": os.getenv("DB_PASSWORD", "root"),
    "port": os.getenv("DB_PORT", 5432),
    "log_queries": False,
    "options": {
      #
    }
  },
  "sqlite": {
    "driver": "sqlite",
    "database": os.getenv("DB_DATABASE", "databases/dolphinido.db"),
  }

}

DB = ConnectionResolver().set_connection_details(DATABASES)
