class Config:
    # Строка подключения к PostgreSQL
    SQLALCHEMY_DATABASE_URI = 'postgresql://flask_user:flask_secure_password123@localhost/flask_transaction_system_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Конфигурация для Celery
    CELERY_BROKER_URL = 'redis://localhost:6379/0'  # Используем Redis как брокер для Celery

    # Секретный ключ для приложения Flask
    SECRET_KEY = 'mysecretkey'
