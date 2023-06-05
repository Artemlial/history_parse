import os
from bs4 import BeautifulSoup as BS
from bs4 import Comment

starter = '''<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
                /* variables */

        :root{
            --correct_bg:#1D8348;
            --incorrect_bg:#C0392B;
            --correct:#00FF00;
            --incorrect:#FF0066;
        }

        /* styles for correct answers */
        .deferredallnothing.correct{background-color:var(--correct_bg);}
        td.control.correct * {background:var(--correct); border: 5px solid black; font-weight:bold; color:black}
        input.d-inline.correct{background-color:var(--correct); color:black !important}
        div.r0.correct{background-color:var(--correct); color:black}
        div.r1.correct{background-color:var(--correct); color:black}
        p{font-weight:bold}

        /* style for incorrect answers */
        .deferredallnothing.incorrect{background-color:var(--incorrect_bg);}
        td.control.incorrect * {background:var(--incorrect); border: 5px solid black; font-weight:bold; color:black}
        input.d-inline.incorrect{background-color:var(--incorrect); color:black}
        div.r0.incorrect{background-color:var(--incorrect); color:black}
        div.r1.incorrect{background-color:var(--incorrect); color:black}
    </style>
</head>
<body>
    
</body>
</html>'''

output = BS(starter,features="lxml")

for l,m,files in os.walk('check'):
    for file in files:
        with open('check\\'+file,'r',encoding='utf-8') as opened:
            print(file)
            soup = BS(opened.read(),'lxml')
            [x.extract() for x in soup.find_all('script')]
            [x.extract() for x in soup.find_all('noscript')]
            [x.extract() for x in soup.find_all(text=lambda text: isinstance(text,Comment))]
            for i in soup.body.find_all('div',role='main'):
                output.body.extend(i)

with open('merged.html','w',encoding='utf-8') as f:
    f.write(str(output))
