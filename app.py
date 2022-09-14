#app.py
from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL,MySQLdb #pip install flask-mysqldb https://github.com/alexferl/flask-mysqldb
 
app = Flask(__name__)
        
#app.secret_key = "caircocoders-ednalan"
        
app.config['MYSQL_HOST'] = 'employee.cwxhqawvre8g.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'aws_user'
app.config['MYSQL_PASSWORD'] = 'Bait3273'
app.config['MYSQL_DB'] = 'employee'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
      
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route("/ajaxlivesearch",methods=["POST","GET"])
def ajaxlivesearch():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        search_word = request.form['query']
        print(search_word)
        if search_word == '':
            query = "SELECT * from employee ORDER BY emp_id"
            cur.execute(query)
            employee = cur.fetchall()
        else:    
            query = "SELECT * from employee WHERE first_name LIKE '%{}%' OR last_name LIKE '%{}%' OR pri_skill LIKE '%{}%' ORDER BY id DESC LIMIT 20".format(search_word,search_word,search_word)
            cur.execute(query)
            numrows = int(cur.rowcount)
            employee = cur.fetchall()
            print(numrows)
    return jsonify({'htmlresponse': render_template('response.html', employee=employee, numrows=numrows)})
     
if __name__ == "__main__":
    app.run(debug=True)