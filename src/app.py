from flask import Flask,request,jsonify
from flask_mysqldb import MySQL
import src.config as config
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

#MySQL Connection:
app.config['MYSQL_HOST']=os.getenv('MYSQL_HOST')
app.config['MYSQL_USER']=config.os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD']=os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB']=os.getenv('MYSQL_DB')
mysql = MySQL(app)

#Routes:
#Route to show all the contacts:
@app.route('/api/contacts',methods=['GET'])
def get_contacts():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    dataList = []
    for i in range(len(data)): 
        response = {
            '_id':data[i][0],
            "fullname":data[i][1],
            "phone":data[i][2],
            "email":data[i][3]
        }
        dataList.append(response)
    return jsonify(dataList)
    
#Route to create a new contact:
@app.route('/api/contacts',methods=['POST'])
def create_contact():
    fullname = request.json['fullname']
    phone = request.json['phone']
    email = request.json['email']
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO contacts (name,phone,email) VALUES (%s,%s,%s)',
                    (fullname,phone,email))
    mysql.connection.commit()
    return jsonify({'status':'New contact added'})

#Route to show an specific contact:
@app.route('/api/contacts/<id>',methods=['GET'])
def show_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = %s',(id))
    data = cur.fetchall()
    response = {
            '_id':data[0][0],
            "fullname":data[0][1],
            "phone":data[0][2],
            "email":data[0][3]
    }
    return jsonify(response)

#Route to update a specific contact:
@app.route('/api/contacts/<id>',methods=['PUT'])
def update_contact(id):
    fullname = request.json['fullname']
    phone = request.json['phone']
    email = request.json['email']
    cur = mysql.connection.cursor()
    cur.execute(""" 
            UPDATE contacts
            SET name=%s,
                phone=%s,
                email=%s
            WHERE id=%s
        """,(fullname,phone,email,id))
    mysql.connection.commit()
    return jsonify({'status':'Contact updated'})

#Route to delete a specfic contact:
@app.route('/api/contacts/<string:id>',methods=['DELETE'])
def deleteContact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    return jsonify({'status':'Contact deleted'})


#Initialize the server:
if(__name__=='__main__'):
    app.run(port=4500,debug=True)


