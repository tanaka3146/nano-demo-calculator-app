from flask import Flask,jsonify,request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "hello world!"

@app.route("/calculator/add", methods=['POST'])
def add():
    a=request.json.get("first")
    b=request.json.get("second")
    return jsonify({"result":str(a+b)})

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    a=request.json.get("first")
    b=request.json.get("second")
    return jsonify({"result":str(a-b)}) #ret

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
