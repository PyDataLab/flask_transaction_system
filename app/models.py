from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'  # Устанавливаем явное имя таблицы

    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Numeric(10, 2), default=0)  # Используем тип Numeric для точности с плавающей запятой
    commission_rate = db.Column(db.Numeric(5, 2), default=0.01)  # Тип Numeric для комиссий
    webhook_url = db.Column(db.String(255))

    def __repr__(self):
        return f'<User {self.id}, Balance {self.balance}, Commission {self.commission_rate}>'

class Transaction(db.Model):
    __tablename__ = 'transactions'  # Устанавливаем явное имя таблицы

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric(10, 2))  # Используем Numeric для сумм транзакций
    commission = db.Column(db.Numeric(10, 2))  # Комиссия для транзакции
    status = db.Column(db.String(20), default='Ожидание')  # Статус транзакции (Ожидание, Подтверждена, Отменена, Истекла)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # Связь с таблицей пользователей
    user = db.relationship('User', backref=db.backref('transactions', lazy=True))

    def __repr__(self):
        return f'<Transaction {self.id}, Amount {self.amount}, Status {self.status}>'
