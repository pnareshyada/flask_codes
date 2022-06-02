from flask import *

app=Flask(__name__)


# redirection of the url
"""@app.route('/admin')
def admin():
    return 'this is admin'

@app.route('/student')
def student():
    return "this is student"

@app.route('/staff')
def staff():
    return "this is staff"

@app.route('/user/<name>')
def user(name):
    if name=='admin':
        return redirect(url_for('admin'))
    if name=='student':
         return redirect(url_for('student'))
    if name=='staff':
        return redirect(url_for('staff'))

@app.route('/hello/<name>')
def naresh(name):
    return 'HELLO WELCOME TO FLASK' +name
"""
#appending the integer into the message
"""@app.route('/hello/<int:sub>')
def int(sub):
    return "this is integer value=%d"%sub
   """
#access with url
"""def naresh():
    return 'hello user'
app.add_url_rule('/maresh','maresh',naresh)
"""
#usage of rendertemplate
@app.route('/login',methods=['Post'])
def login():
    uname=request.args.get('uname')
    passwrd=request.args.get('pass')
    if uname=='Naresh' and passwrd=="naresh":
        return "Welcome %s" %uname
    else:
          return "invalid %s" %uname
    return render_template('base.html')


#usage of delimitor
"""@app.route('/user/<name>')
def message(name):
    return render_template('base.html',name=name)
"""


if __name__ == '__main__':
    app.run(debug=True)