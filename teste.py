from flask import Flask, render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = '195.154.173.6'
app.config['MYSQL_USER'] = 'evttenorio'
app.config['MYSQL_PASSWORD'] = 'S'
app.config['MYSQL_DB'] = 'intranet_dev'

mysql = MySQL(app)

@app.route('/')
def aniversariantes():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT colaboradores.nome, colaboradores.data_nascimento
FROM colaboradores
WHERE colaboradores.id IN (SELECT contratos_colaboradores.colaborador_id FROM contratos_colaboradores WHERE status = 1)
AND MONTH(colaboradores.data_nascimento) = MONTH(CURRENT_DATE())
AND colaboradores.status = 1''')
    rv = cur.fetchall()
    cur.close()
    return render_template('aniversariantes.html', colaboradores=rv)
    #return str(rv)
    

if __name__ == '__main__':
    app.run(debug = True)
