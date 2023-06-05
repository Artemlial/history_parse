from requests_html import HTML
import os
from json_combine.test_parse import anses,match,multichoice,shortanswer
import re
# print(list(os.walk('check')))
def checker(func,type):
    if type == 'matches':
        for i in anses1[type].values():
            if func[1]==i:
                return False
        return True
    if type == 'mchoices':
        if re.sub('question\-\d+\-\d+.*','',func[0]) in list(map(lambda x: re.sub('question\-\d+\-\d+.*','',x),anses1[type].keys())):
            for i in anses1[type].values():
                if set(func[1])==set(i):
                    return False
            return True
        return True
    if re.sub('question\-\d+\-\d+.*','',func[0]) in list(map(lambda x: re.sub('question\-\d+\-\d+.*','',x),anses1[type].keys())):
        return False
    return True

# def checker_wrong(func,type):
#     if type == 'matches':
#         for i in wrongs[type].values():
#             if func[1]==i:
#                 return False
#         return True
#     if type == 'mchoices':
#         if re.sub('question\-\d+\-\d+','',func[0]) in list(map(lambda x: re.sub('question\-\d+\-\d+','',x),wrongs[type].keys())):
#             for i in wrongs[type].values():
#                 if set(func[1])==set(i):
#                     return False
#             return True
#         return True
#     if re.sub('question\-\d+\-\d+','',func[0]) in list(map(lambda x: re.sub('question\-\d+\-\d+','',x),wrongs[type].keys())):
#         return False
#     return True

anses1 = anses
# wrongs = {}

for l,m,files in os.walk('check'):
    for file in files:
        with open('check\\'+file,'r',encoding='utf-8') as opened:
            print(file)
            html = HTML(html=''.join(opened.readlines()))
            a,b,c = match(html),multichoice(html),shortanswer(html)
            for i,k in zip((a,b,c),('matches','mchoices','shanses')):
                anses1[k].update(dict(filter(lambda x: checker(x,k),i.items())))
            
            # d,e,f = match(html,correctness = 'incorrect'),multichoice(html,correctness = 'incorrect'),shortanswer(html,correctness = 'incorrect')
            # for i,k in zip((d,e,f),('matches','mchoices','shanses')):
            #     wrongs[k].update(dict(filter(lambda x: checker_wrong(x,k),i.items())))





if __name__=='__main__':
    print(len(anses1['matches'])+len(anses1['mchoices'])+len(anses1['shanses']))
            