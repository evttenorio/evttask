from fpdf import FPDF
import requests
import json

title = 'evttask - Relatório'

rq = requests.get('http://127.0.0.1:5000/tasks')

dados = rq.json()

def x():
    for listTask in dados['tasks']:
        if listTask['done'] == False:
            print("Tarefa: ", listTask['title']),
            print("Autor: ", listTask['author']),
            print("Feita?: Não"),
            print("Criada em: ", listTask['date']),
            print("------------")
        else:
            print("Tarefa: ", listTask['title']),
            print("Autor: ", listTask['author']),
            print("Feita?: Sim"),
            print("Criada em: ", listTask['date']),
            print("------------")

def pdfscript(spacing=1):
#   data = [['First Name', 'Last Name', 'email', 'zip'],
#            ['Mike', 'Driscoll', 'mike@somewhere.com', '55555'],
#            ['John', 'Doe', 'jdoe@doe.com', '12345'],
#            ['Nina', 'Ma', 'inane@where.com', '54321']
#            ]

    pdf = FPDF()
    pdf.set_title(title)
    pdf.set_font('Arial', 'B', 10)
    pdf.add_page()
    x()
 
    col_width = pdf.w / 4.5
    row_height = pdf.font_size

    pdf.cell(50, 15, 'Example')
#    for row in dadosx:
#        for item in row:
#            pdf.cell(col_width, row_height*spacing,
#                     txt=item, border=1)
#        pdf.ln(row_height*spacing)
 
    pdf.output('relatorio_de_Tarefas.pdf')

if __name__ == '__main__':
    pdfscript()