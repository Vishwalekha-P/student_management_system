from flask import Flask, request, jsonify

app = Flask(__name__)

students = []
next_id = 1

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)

@app.route("/students", methods=["POST"])
def add_student():
    global next_id
    data = request.json
    student = {
        "id": next_id,
        "name": data["name"],
        "age": data["age"],
        "grade": data["grade"]
    }
    students.append(student)
    next_id += 1
    return jsonify(student), 201

@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.json
    for student in students:
        if student["id"] == student_id:
            student.update(data)
            return jsonify(student)
    return jsonify({"error": "Student not found"}), 404

@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    global students
    students = [s for s in students if s["id"] != student_id]
    return jsonify({"message": "Deleted"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)