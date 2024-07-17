from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import firebase_admin
from firebase_admin import credentials
from api_consumers.users import register_user, login_user, load_user
from api_consumers.courses import get_courses, add_course

# Iniciar Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

# Inicialización de Firebase para users
cred_users = credentials.Certificate("firebase/apiprueba1tpfinal-firebase-adminsdk-8sx2e-5225658030.json")
firebase_admin.initialize_app(cred_users, name='users')

# Inicialización de Firebase para courses
cred_courses = credentials.Certificate("firebase/apicursos-5596f-firebase-adminsdk-vc49w-3dd851350a.json")
firebase_admin.initialize_app(cred_courses, name='courses')

# Iniciar JWT y Login manager
jwt = JWTManager(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

@login_manager.user_loader
def load_user(user_id):
    return load_user(user_id)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/courses')
def courses_page():
    courses = get_courses()
    return render_template('courses.html', courses=courses)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = login_user(username, password)
        if user:
            login_user(user)
            access_token = create_access_token(identity=user.id)
            return redirect(url_for('courses_page'))
        flash('Credenciales incorrectas')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_data = {
            'username': request.form['username'],
            'dni': request.form['dni'],
            'email': request.form['email'],
            'password': request.form['password'],
            'nombre': request.form['nombre'],
            'apellido': request.form['apellido'],
            'fecha_nacimiento': request.form['fecha-nac'],
            'pais': request.form['pais-origen']
        }
        register_user(user_data)
        flash('Usuario registrado con éxito')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/api/login', methods=['POST'])
def api_login():
    username = request.form.get('username')
    password = request.form.get('password')
    token = login_user(username, password)
    if token:
        return jsonify({'access_token': token}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/api/register', methods=['POST'])
def api_register():
    user_data = {
        'username': request.form.get('username'),
        'dni': request.form.get('dni'),
        'email': request.form.get('email'),
        'password': request.form.get('password'),
        'nombre': request.form.get('nombre'),
        'apellido': request.form.get('apellido'),
        'fecha_nacimiento': request.form.get('fecha-nac'),
        'pais': request.form.get('pais-origen')
    }
    register_user(user_data)
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/api/courses', methods=['GET'])
def api_get_courses():
    courses = get_courses()
    return jsonify(courses), 200

@app.route('/api/courses', methods=['POST'])
@jwt_required()
def api_add_course():
    course_data = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'image_url': request.form.get('image_url')
    }
    add_course(course_data)
    return jsonify({'message': 'Course added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)


