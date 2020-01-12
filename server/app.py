from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


TASKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'Criar, visualizar, atualizar e remover algumas tarefas na ferramenta: evttask',
        'author': 'Jubileu',
        'done': False
    },
]

def remove_task(task_id):
    for task in TASKS:
        if task['id'] == task_id:
            TASKS.remove(task)
            return True
    return False

# sanity check route
@app.route('/', methods=['GET'])
def hello():
    response_object = {'Message': 'Hello'}
    return jsonify(response_object)

@app.route('/tasks', methods=['GET', 'POST'])
def all_tasks():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        TASKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'done': post_data.get('done')
        })
        response_object['message'] = 'Task added!'
    else:
        response_object['tasks'] = TASKS
    return jsonify(response_object)

@app.route('/tasks/<task_id>', methods=['PUT', 'DELETE'])
def single_task(task_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_task(task_id)
        TASKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'done': post_data.get('done')
        })
        response_object['message'] = 'Task updated!'
    if request.method == 'DELETE':
        remove_task(task_id)
        response_object['message'] = 'Task removed!'
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()
