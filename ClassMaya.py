from typing import Counter


class MayaResponseGetter():
    def __init__(self):
        self.countryCategory = ''
        self.countryDict = {'us':
                            ['us', 'usa', 'america', 'american'],
                            'in':
                            ['india', 'bharat', 'hindustan',
                                'aryavarta', 'aryavrat', 'aryavart'],
                            'ae':
                            ['uae', 'ae', 'arab', 'united arab'],
                            'ar': ['argentina'],
                            'at': ['austria'],
                            'au':['australia'],
                            'be':['belgium'],
                            'bg' : ['bulgeria'],
                            'br':['brazil'],
                            'ca':['canada'],
                            'ch':['switzerland'],
                            'cn':['china','chinese'],
                            'co':['colombia'],
                            'cu':['cuba'],
                            'cz':['czech', 'czech republic'],
                            'de':['germany'],
                            'eg':['egypt'],
                            'fr':['france','french'],
                            'gb':['united kingdom', 'britain','uk'],
                            'gr':['greece'],
                            'hk':['hong kong'],
                            'hu':['hungary'],
                            'id':['indonesia'],
                            'ie':['ireland'],
                            'il':['israel'],
                            'it':['italy', 'italian'],
                            'jp':['japan','japanese'],
                            'kr':['korea', 'south korea'],
                            'lt':['lithuania'],
                            'lv':['latvia'],
                            'ma':['morocco'],
                            'mx':['mexico', 'mexican'], 
                            'my':['malaysia'],
                            'ng':['nigeria'], 
                            'nl':['netherlands'],
                            'no':['norway'],
                            'nz':['new zealand'],
                            'ph':['philippines'],
                            'pl':['poland'],
                            'pt':['portugal'],
                            'ro':['romania', 'romanian'],
                            'rs':['serbia'],
                            'ru':['russian federation', 'russia', 'ruse', 'russian'],
                            'sa':['saudi arabia'],
                            'se':['sweden'],
                            'sg':['singapore'],
                            'si':['slovenia'],
                            'sk':['slovakia'],
                            'th':['thailand'],
                            'tr':['turkey'],
                            'tw':['taiwan'], 
                            'ua':['ukraine'],
                            've':['venezuela'], 
                            'za':['south africa']
                            }

        self.categoryList = ['general', 'business', 'technology',
                             'entertainment', 'health', 'science', 'sports']
        self.Data = {
            'call': [
                'make a phone call',
                'call',
                'phone call',
                'phone',
                'contact',
                'making a phone call'
            ],
            'news-sentence': [
                f'show me {self.countryCategory} news',
                f'{self.countryCategory} news',
                f'news of {self.countryCategory}',
                f'news from {self.countryCategory}',
                f'{self.countryCategory} news',
                f'headlines in {self.countryCategory}',
                f'headlines of {self.countryCategory}',
            ],
        }
    # def Response(self, sentence):
    #     for key in self.Data.keys():
    #         for value in self.Data[key]:
    #             if value in sentence.lower():
    #                 return key
    #     return None

    def Response(self, sentence):
        Resp = ''
        Respo = []
        # Extraction of Country
        for key in self.countryDict.keys():
            for value in self.countryDict[key]:
                if value in sentence.lower():
                    self.country = key
                    Resp = key

        # Extraction of News Sent.
        for k in self.Data.keys():
            for value in self.Data[k]:
                if value in sentence.lower():
                    Respo.append(Resp)

        # Extract Category
        cat = ''
        for item in self.categoryList:
            if item in sentence.lower():
                self.countryCategory = item
                cat = item

        # Extraction of Sent.
        for k in self.Data.keys():
            for value in self.Data[k]:
                if value in sentence.lower():
                    Respo.append(cat)

        return Respo
