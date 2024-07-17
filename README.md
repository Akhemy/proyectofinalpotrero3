Proyecto Final de Potrero Digital: Cursos Web
Descripción del Proyecto

Este proyecto consiste en una plataforma web para la gestión de cursos, desarrollada como parte del trabajo final para Potrero Digital. La aplicación permite a los usuarios registrarse, iniciar sesión, y ver una lista de cursos disponibles. Además, los administradores pueden agregar nuevos cursos a la plataforma. El backend de la aplicación está construido con Flask y utiliza Firebase como base de datos para gestionar los usuarios y los cursos.
Características Principales

    Registro de Usuarios: Los nuevos usuarios pueden registrarse proporcionando su información personal.
    Inicio de Sesión: Los usuarios registrados pueden iniciar sesión en la plataforma.
    Visualización de Cursos: Los usuarios pueden ver una lista de cursos disponibles.
    Adición de Cursos: Los administradores pueden agregar nuevos cursos a la plataforma.
    Seguridad: La aplicación utiliza JWT para la autenticación y autorización de usuarios.

Estructura del Proyecto 
tp_final_protrero
       app.py                  # Archivo principal de Flask
        requirements.txt        # Dependencias del proyecto
        estructura del proyecto # estructura de carpetas y archivos

templates               # Carpeta para las plantillas HTML
       index.html
      courses.html
       login.html
       register.html

static                  # Carpeta para archivos estáticos (CSS, JS, imágenes)
      css
      login.css
      register.css
      styles.css
  js
      main.js
  img

firebase                # Carpeta para los archivos de credenciales de Firebase
      apiprueba1tpfinal-firebase-adminsdk-8sx2e-5225658030.json
      apicursos-5596f-firebase-adminsdk-vc49w-3dd851350a.json

api_consumers           # Carpeta para los archivos de Python que consumen la API
     __init__.py         # Indica que este directorio es un paquete
      users.py            # Funciones relacionadas con usuarios
      courses.py          # Funciones relacionadas con cursos


Rutas Principales

    GET /: Muestra la página de inicio.
    GET /courses: Muestra la lista de cursos disponibles.
    GET /login: Muestra la página de inicio de sesión.
    POST /login: Maneja la lógica de inicio de sesión.
    GET /register: Muestra la página de registro.
    POST /register: Maneja la lógica de registro.
    GET /logout: Cierra la sesión del usuario.
    GET /api/courses: Devuelve la lista de cursos en formato JSON.
    POST /api/courses: Agrega un nuevo curso (requiere autenticación).

Detalles Técnicos
app.py

Este archivo contiene la configuración principal de Flask, las rutas y la lógica para manejar las solicitudes de los usuarios y los cursos.
api_consumers/users.py

Contiene funciones relacionadas con la gestión de usuarios, incluyendo registro, inicio de sesión y carga de usuarios.
api_consumers/courses.py

Contiene funciones relacionadas con la gestión de cursos, incluyendo la obtención y adición de cursos.
templates

Contiene los archivos HTML que conforman la interfaz de usuario de la aplicación.
static

Contiene los archivos estáticos como CSS y JavaScript utilizados en la aplicación.
firebase

Contiene los archivos de credenciales de Firebase necesarios para interactuar con las bases de datos de usuarios y cursos.
