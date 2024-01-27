from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat.db' # Пример использования SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


def initialize_database():
    with app.app_context():
        inspector = inspect(db.engine)
        existing_tables = inspector.get_table_names()
        if not existing_tables:  # Если таблиц нет, создаем их
            db.create_all()
        print("База данных инициализирована.")
        
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        new_user = User(username=data['username'])
        new_user.set_password(data['password'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        # Вывод деталей ошибки в консоль или журнал ошибок
        print(e)
        return jsonify({'error': 'Internal Server Error'}), 500


@app.route('/get_users', methods=['GET'])
def get_users():
    try:
        # Извлечение всех пользователей
        users = User.query.all()
        users_data = [{"id": user.id, "username": user.username, "password": user.password_hash} for user in users]
        return jsonify(users_data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500



@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        data = request.json
        new_message = Message(
            content=data['content'],
            sender_id=data['sender_id'],
            receiver_id=data['receiver_id']
        )
        db.session.add(new_message)
        db.session.commit()
        return jsonify({'message': 'Message sent successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@app.route('/get_messages', methods=['GET'])
def get_messages():
    try:
        # Извлечение всех сообщений
        messages = Message.query.all()
        messages_data = [
            {
                "id": message.id, 
                "content": message.content, 
                "sender_id": message.sender_id, 
                "receiver_id": message.receiver_id
            } 
            for message in messages
        ]
        return jsonify(messages_data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/receive_message', methods=['GET'])
def receive_message():
    # Здесь должна быть логика для получения и расшифровки сообщения
    # Например, можно извлекать сообщения из базы данных

    # В этом примере просто возвращаем пример сообщения
    sample_message = {
        "from": "user123",
        "message": "Привет! Это тестовое сообщение."
    }
    return jsonify({"status": "Message received", "message": sample_message})

# Запуск сервера
if __name__ == '__main__':
    initialize_database()  # Проверка и инициализация БД перед запуском сервера
    app.run()