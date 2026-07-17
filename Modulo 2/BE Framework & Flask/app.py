import json
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

FILE_PATH = "tasks.json"
VALID_STATUS = ["To do", "In Progress", "Done"]

def read_tasks():
    if not os.path.exists(FILE_PATH):
        return []
    
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)
    
def write_tasks(tasks):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)

def find_task_by_id(tasks, task_id):
    for task in tasks:
        if str(task["id"]) == str(task_id):
            return task
    return None

def validate_task_data(data):
    if "id" not in data:
        return "Task id is required"
    
    if "title" not in data or not data ["title"]:
        return "Task title is required"
    
    if "description" not in data or not data ["description"]:
        return "Task description is required"
    
    if "status" not in data or not data ["status"]:
        return "Task status is required"
    
    if data["status"] not in VALID_STATUS:
        return "Invalid task status"
    
    return None

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = read_tasks()
    status_filter = request.args.get("status")

    if status_filter:
        tasks =[task for task in tasks if task["status"] == status_filter]

    return jsonify({"data": tasks}), 200    

@app.route("/tasks", methods=["POST"])
def create_task():
    tasks = read_tasks()
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"message": "Invalid JSON body"}), 400

    error = validate_task_data(data)

    if error:
        return jsonify({"message": error}), 400

    existing_task = find_task_by_id(tasks, str(data["id"]))

    if existing_task:
        return jsonify({"message": "Task id already exists"}), 400

    new_task = {
        "id": str(data["id"]),
        "title": data["title"],
        "description": data["description"],
        "status": data["status"]
    } 

    tasks.append(new_task)
    write_tasks(tasks)

    return jsonify({"message": "Task created successfully", "data": new_task}), 201

@app.route("/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    tasks = read_tasks()
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"message": "Invalid JSON body"}), 400

    task = find_task_by_id(tasks, task_id)

    if not task:
        return jsonify({"message": "Task not found"}), 404
    
    if "title" in data:
        if not data["title"]:
            return jsonify({"message": "Task title cannot be empty"}), 400
        task["title"] = data["title"]

    if "description" in data:
        if not data["description"]:
            return jsonify({"message": "Task description cannot be empty"}), 400
        
        task["description"] = data["description"]

    if "status" in data:
        if data["status"] not in VALID_STATUS:
            return jsonify({"message": "Invalid task status"}), 400
        
        task["status"] = data["status"]

    write_tasks(tasks)

    return jsonify({"message": "Task updated successfully", "data": task}), 200

@app.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks = read_tasks()

    task = find_task_by_id(tasks, task_id)
    if not task: 
        return jsonify({"message": "Task not found"}), 404
    
    tasks.remove(task)
    write_tasks(tasks)

    return jsonify({"message": "Task deleted successfully"}), 200
    
if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)