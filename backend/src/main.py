from .entities.entity import Session, engine, Base
from .entities.exam import Exam

# Generate datebase schema
Base.metadata.create_all(engine)

# Start session
session = Session()

# Check for existing data
exams = session.query(Exam).all()

if len(exams) == 0:
    # Create and presist dummy exam
    test_exam = Exam('Dummy exam', 'Test your knowledge on dummy exam.', 'Author')
    session.add(test_exam)
    session.commit()
    session.close()

    # Reload exams
    exams = session.query(Exam).all()

# Show existing exmas
print('### Exams:')
for exam in exams:
    print(f'({exam.id}) {exam.title} - {exam.description}')
