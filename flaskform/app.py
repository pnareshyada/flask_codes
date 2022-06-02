from flask import Flask, render_template, request, flash
from form import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY']='skey'


@app.route("/")
def home():
    return "welcome to flask"

@app.route("/contact",methods=['GET','POST'])
def contact():
    form=ContactForm()
    
    if request.method=='POST':
        if form.validate()==False:
            flash("all fields are mandatory")
            return render_template("contact.html",form=form)
        else:
            return 'form posted successfully'
    return render_template('contact.html',form=form)
    
if __name__=='__main__':
    app.run(debug=True)