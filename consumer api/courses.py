from firebase_admin import firestore

db_courses = firestore.client(app=firebase_admin.get_app(name='courses'))

def get_courses():
    courses_ref = db_courses.collection('courses')
    courses = [doc.to_dict() for doc in courses_ref.stream()]
    return courses

def add_course(data):
    course_ref = db_courses.collection('courses').document()
    course_ref.set({
        'title': data['title'],
        'description': data['description'],
        'image_url': data['image_url']
    })
