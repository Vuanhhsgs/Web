from flask import Flask, render_template, request, jsonify
from waitress import serve

app = Flask(__name__, template_folder="../Front end", static_folder="../Front end", static_url_path='')

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json() 
    commands = ["A=(0,0)", "B=(4,0)", "C=(2,3)"]
    return jsonify(result=commands)

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)