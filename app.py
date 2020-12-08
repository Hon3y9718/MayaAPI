from flask import Flask, jsonify, request
from flask.wrappers import Response
from ClassMaya import MayaResponseGetter

Getter = MayaResponseGetter()

app = Flask(__name__)

@app.route('/api')
def Maya():
    country = ''
    category = ''
    sentence = request.args.get('Query')
    result = Getter.Response(sentence)
    try:
        country = result[0]
    except:
        country = None
    try:
        category = result[-1]
    except:
        category = None
    status = 'OK'
    if result == None:
        status = 'NotUnderstandablebyAPI'
    return jsonify(country = country, category = category, copyright = 'Hon3y@Techicous', status = status)

if __name__ == "__main__":
    app.run()
