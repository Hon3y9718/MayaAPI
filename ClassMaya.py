class MayaResponseGetter():
    def __init__(self):
        self.Data = {
            'call': [
                'make a phone call',
                'call',
                'phone call',
                'phone',
                'contact',
                'making a phone call'
            ],
            'us-news':[
                'show me us news',
                'american news',
                'usa news',
                'news of us',
                'news of usa',
                'news from usa',
                'news from us',
                'us news',
                'america news',
                'news of america',
                'news from america'
                'headlines in us',
                'headlines in usa',
                'headlines of america',
            ],
        }
    def Response(self, sentence):
        for key in self.Data.keys():
            for value in self.Data[key]:
                if value in sentence.lower():
                    return key
        return None






