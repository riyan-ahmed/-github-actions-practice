from flask import Flask, render_template
app = Flask(__name__)

#joshhh
#fllflfsl
@app.route('/')
def hello_world():
    return render_template('index.html')

if(def-0); then
fi


@app.route('/health')
def health():
    return 'Server is up and running'
