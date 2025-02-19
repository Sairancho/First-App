from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route('/')
def home():
    return "Welcome to Flask Calculator!"

@app.route('/add', methods=['GET'])
def add():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        return jsonify({"result": num1 + num2})
    except:
        return jsonify({"error": "Invalid input"}), 400

if _name_ == '_main_':
    app.run(debug=True, host='0.0.0.0', port=5000)
