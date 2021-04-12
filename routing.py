from flask import Flask, render_template 
app = Flask(__name__) 

@app.route('/')
def hello_world():
    return render_template("about_python.html")

@app.route('/dojo')
def dojo():
    return 'dojo'

@app.route('/<name>')
def hello_person(name):
    return render_template("about_python.html", name_provided=name)

@app.route('/say/<name>')
def greeting(name):
    return f'Hi {name}!'

@app.route('/repeat/<int:times>/<string>')
def repeating(times, string):
    return int(times) * string


if __name__=="__main__":  
    app.run(debug=True)