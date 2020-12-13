from flask import Flask, json, jsonify, request
from flask.wrappers import Response
from ClassMaya import MayaResponseGetter
import requests
from dataBase import getCountry, getCategory, setCategory, setCountry

Getter = MayaResponseGetter()
country = ''
category = ''

app = Flask(__name__)

@app.route('/news', methods=['GET'])
def ReqNews():
    daTa = {}
    List = []
    country = request.args.get('country')
    print(country, type(country))
    category = request.args.get('category')
    if country != None:
        if country != 'null':
            setCountry(country)
    if category != None:
        if category != 'null':
            if category != '':
                setCategory(category)
    if country == None or country == 'null' or country == '':
        country = getCountry()
    if category == None or category == 'null' or category == '':
        category = getCategory()
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
    returnData = {'status': 'OK','totalResults': len(List), 'articles': List, 'country': country, 'category': category}
    return jsonify(returnData)

@app.route('/api')
def Maya():
    sentence = request.args.get('Query')
    Countryresult = Getter.CountryResp(sentence)
    Categoryresult = Getter.CategoryResp(sentence)
    status = 'OK'
    if Countryresult != None:
        setCountry(Countryresult)
    if Categoryresult != None:
        setCategory(Categoryresult)
    if Categoryresult == None:
        Categoryresult = getCategory()
    if Countryresult == None:
        Countryresult = getCountry();
    daTa = {}
    List = []
    urlnews = requests.get(f'http://newsapi.org/v2/top-headlines?country=in&apiKey=f623a55d481c4466b5e85ea7b71ab8b6').text
    if Countryresult != None and Categoryresult != None:
        urlnews = requests.get(f'http://newsapi.org/v2/top-headlines?country={Countryresult}&category={Categoryresult}&apiKey=f623a55d481c4466b5e85ea7b71ab8b6').text
    elif Countryresult != None and Categoryresult == None:
        urlnews = requests.get(f'http://newsapi.org/v2/top-headlines?country={Countryresult}&apiKey=f623a55d481c4466b5e85ea7b71ab8b6').text
    elif Categoryresult != None and Countryresult == None:
        urlnews = requests.get(f'http://newsapi.org/v2/top-headlines?country=in&category={Categoryresult}&apiKey=f623a55d481c4466b5e85ea7b71ab8b6').text
    else:
        urlnews = requests.get(f'http://newsapi.org/v2/top-headlines?country=in&apiKey=f623a55d481c4466b5e85ea7b71ab8b6').text
    jsonObj = json.loads(urlnews)
    for article in jsonObj['articles']:
        daTa = {'source' : article['source']['name'],
        'title' : article['title'],
        'content' : article['content'],
        'description' : article['description'],
        'url' : article['url'],
        'urlToImage' : article['urlToImage']}
        List.append(daTa)
    returnData = {'status': status,'totalResults': len(List), 'articles': List, 'country': Countryresult, 'category': Categoryresult}
    return jsonify(returnData)


if __name__ == "__main__":
    app.run()
