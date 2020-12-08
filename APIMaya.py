from flask import Flask, jsonify, request
from flask.wrappers import Response
from ClassMaya import MayaResponseGetter

Getter = MayaResponseGetter()

app = Flask(__name__)

@app.route('/api')
def Maya():
    sentence = request.args.get('Query')
    result = Getter.Response(sentence)
    status = 'OK'
    if result == None:
        status = 'NotUnderstandablebyAPI'
    return jsonify(Response = result, copyright = 'Hon3y@Techicous', status = status)

if __name__ == "__main__":
    app.run()
