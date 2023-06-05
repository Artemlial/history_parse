from requests_html import HTMLSession
import json

session = HTMLSession()
r = session.get('https://campus.fa.ru/my/')
input_ = r.html.find('#login > input[type=hidden]',first=True)
logintoken = input_.attrs['value']
payload={'logintoken':logintoken,'username': 
222603,
'password': 
'OBfo5466'}
session.post('https://campus.fa.ru/login/index.php',data=payload,allow_redirects=True)
page = session.get('https://campus.fa.ru/my/')
all = {}
for i in range(285029,285037):
    root = f'https://campus.fa.ru/mod/quiz/view.php?id={i}'
    sesskey = session.get(root).html.find('#page-content > div:nth-child(2) > div.box.py-3.quizattempt > div > form > input[type=hidden]:nth-child(2)',first=True).attrs['value']
    data = {'cmid':i,'sesskey':sesskey}
    attempt=session.post('https://campus.fa.ru/mod/quiz/startattempt.php',data=data,allow_redirects=True).html.find('input[name=attempt]',first=True).attrs['value']
    session.post(f'https://campus.fa.ru/mod/quiz/processattempt.php?cmid={i}',data={'attempt':attempt,'finishattempt':1,'timeup':0,'slots':None,'cmid':i,'sesskey':sesskey},allow_redirects=True)
    session.get(f'https://campus.fa.ru/mod/quiz/review.php?attempt={attempt}&cmid={i}')
    ans_page = session.get(f'https://campus.fa.ru/mod/quiz/review.php?attempt={attempt}&cmid={i}&showall=1',headers={'referer':f'https://campus.fa.ru/mod/quiz/review.php?attempt={attempt}&cmid={i}'})
    ques =list(map(lambda x: x.text, ans_page.html.find('div.formulation.clearfix')))
    ans =list(map(lambda x: x.text, ans_page.html.find('div.outcome.clearfix')))
    all[f'Тест {i-285028}'] = dict(zip(ques,ans))

with open('history.json','w',encoding='utf-8') as file:
    json.dump(all,file)

