from flask import Flask

#Create template using HTML and CSS --
from flask import Flask, render_template

#-----------
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

#------------
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello World!"
