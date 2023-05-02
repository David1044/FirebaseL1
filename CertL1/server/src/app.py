from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def indeex():
    return render_template('indeex.html')

if __name__ == '_main_':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
