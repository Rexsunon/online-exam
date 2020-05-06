from flask import Flask, jsonify, request
from flask_cors import CORS

from entities.entity import Session, engine, Base
from entities.exam import Exam, ExamSchema

# Create flask appliction
app = Flask(__name__)
# init CORS
CORS(app)

# Generate datebase schema
Base.metadata.create_all(engine)

@app.route('/exams')
def get_exams():
    # Fetch from DB
    session = Session()
    exam_objects = session.query(Exam).all()

    # Transform into json-serialized objects
    schema = ExamSchema(many=True)
    exams = schema.dump(exam_objects)

    # serializing as JSON
    session.close()
    return jsonify(exams)

@app.route('/exams', methods=['POST'])
def add_exam():
    # mount exam object
    post_exam = ExamSchema(only=('title', 'description'))\
        .load(request.get_json())

    exam = Exam(**post_exam, created_by='HTTP post request')

    # Presist exam
    session = Session()
    session.add(exam)
    session.commit()

    # return created exam
    new_exam = ExamSchema().dump(exam)
    session.close()
    return jsonify(new_exam), 201

# Run script
if __name__ == '__main__':
    app.run(debug=True)
