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
    Countryresult = Getter.CountryResp(sentence)
    Categoryresult = Getter.CategoryResp(sentence)
    status = 'OK'
    if Countryresult or Categoryresult == None:
        status = 'NotUnderstandablebyAPI'
    return jsonify(country = Countryresult, category = Categoryresult, copyright = 'Hon3y@Techicous', status = status)

if __name__ == "__main__":
    app.run()
