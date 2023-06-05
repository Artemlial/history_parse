from requests_html import HTML
from json_combine.new_anses import ans_dict_match,ans_dict_mchoices
anses = {'matches':ans_dict_match,'mchoices':ans_dict_mchoices,'shanses':{}}
def match(html):
    res = html.find(f'.que.match.deferredallnothing')
    dickt={}
    for i in res:
        key = HTML(html=i.html).find('.qtext',first=True).text+i.attrs['id']
        correctness = {"correct":not("incorrect" in i.attrs["class"])}
        correctness.update({HTML(html=j.html).find('.text',first=True).text:[HTML(html=j.html).find('option[selected=selected]',first=True).text,HTML(html=j.html).find('td[class^="control"]',first=True).attrs["class"][-1]] for j in HTML(html=i.html).find('tr[class^=r]')})
        dickt.update({key:correctness})
    return dickt
def multichoice(html):
    res = html.find(f'.que.multichoice.deferredallnothing')
    dickt = {}
    for i in res:
        key = HTML(html=i.html).find('.qtext',first=True).text+i.attrs['id']
        correctness = {"correct":not("incorrect" in i.attrs["class"])}
        correctness.update({"answers":[[j.text,j.attrs["class"][-1]] for j in HTML(html=i.html).find(f'div.answer > div[class^="r"]') if j.attrs["class"][-1] not in ('r0','r1')]})
        dickt.update({key:correctness})
    return dickt
def shortanswer(html):
    res = html.find(f'.que.shortanswer.deferredallnothing')
    dickt = {HTML(html=i.html).find('.qtext',first=True).text+i.attrs['id']:HTML(html=i.html).find('input[type=text]',first=True).attrs['value'] for i in res}
    return dickt

