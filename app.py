from flask import Flask, json, jsonify, request
from flask.wrappers import Response
from ClassMaya import MayaResponseGetter
import requests

Getter = MayaResponseGetter()
country = ''
category = ''

app = Flask(__name__)

@app.route('/news', methods=['GET'])
def ReqNews():
    daTa = {}
    List = []
    country = request.args.get('country')
    if country == None:
        country = 'in'
    category = request.args.get('category')
    if category == None:
        category = 'general'
    urlnews = requests.get(f'http://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey=f623a55d481c4466b5e85ea7b71ab8b6').text
    jsonObj = json.loads(urlnews)
    for article in jsonObj['articles']:
        daTa = {'source' : article['source']['name'],
        'title' : article['title'],
        'content' : article['content'],
        'description' : article['description'],
        'url' : article['url'],
        'urlToImage' : article['urlToImage']}
        List.append(daTa)
    returnData = {'status': 'OK','totalResults': len(List), 'articles': List}
    return jsonify(returnData)

@app.route('/api')
def Maya():
    sentence = request.args.get('Query')
    Countryresult = Getter.CountryResp(sentence)
    Categoryresult = Getter.CategoryResp(sentence)
    status = 'OK'
    if Countryresult or Categoryresult == None:
        status = 'NotUnderstandablebyAPI'
    daTa = {}
    List = []
    urlnews = requests.get(f'http://newsapi.org/v2/top-headlines?country={Countryresult}&category={Categoryresult}&apiKey=f623a55d481c4466b5e85ea7b71ab8b6').text
    jsonObj = json.loads(urlnews)
    for article in jsonObj['articles']:
        daTa = {'source' : article['source']['name'],
        'title' : article['title'],
        'content' : article['content'],
        'description' : article['description'],
        'url' : article['url'],
        'urlToImage' : article['urlToImage']}
        List.append(daTa)
    returnData = {'status': status,'totalResults': len(List), 'articles': List}
    return jsonify(returnData)


if __name__ == "__main__":
    app.run()
