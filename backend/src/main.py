from flask import Flask, jsonify, request

from .entities.entity import Session, engine, Base
from .entities.exam import Exam, ExamSchema

# Create flask appliction
app = Flask(__name__)

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
    return jsonify(exams.data)
