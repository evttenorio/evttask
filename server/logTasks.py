import requests
import json

rq = requests.get('http://localhost:5000/tasks')
dados = rq.json()

def x():
    for listTask in dados['tasks']:
        if listTask['done'] == False:
            print("------------------------------------------")
            print("Tarefa: ", listTask['title']),
            print("Autor: ", listTask['author']),
            print("Feita?: Não"),
            print("Criada em: ", listTask['date']),
            print("------------------------------------------")
        else:
            print("Tarefa: ", listTask['title']),
            print("Autor: ", listTask['author']),
            print("Feita?: Sim"),
            print("Criada em: ", listTask['date']),
            print("------------------------------------------")

if __name__ == '__main__':
    x()