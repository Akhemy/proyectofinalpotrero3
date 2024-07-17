from firebase_admin import firestore
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db_users = firestore.client(app=firebase_admin.get_app(name='users'))

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

def register_user(data):
    user_ref = db_users.collection('users').document()
    hashed_password = generate_password_hash(data['password'])
    user_ref.set({
        'username': data['username'],
        'dni': data['dni'],
        'email': data['email'],
        'password': hashed_password,
        'nombre': data['nombre'],
        'apellido': data['apellido'],
        'fecha_nacimiento': data['fecha_nacimiento'],
        'pais': data['pais']
    })

def login_user(username, password):
    users_ref = db_users.collection('users').where('username', '==', username).stream()
    user = next(users_ref, None)
    if user:
        user_data = user.to_dict()
        if check_password_hash(user_data['password'], password):
            return User(id=user.id, username=username, password=user_data['password'])
    return None

def load_user(user_id):
    doc = db_users.collection('users').document(user_id).get()
    if doc.exists:
        user_data = doc.to_dict()
        return User(id=user_id, username=user_data['username'], password=user_data['password'])
    return None
