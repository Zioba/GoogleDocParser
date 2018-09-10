import requests, bs4

s=requests.get('https://www.wowprogress.com/character/eu/%D1%80%D0%B5%D0%B2%D1%83%D1%89%D0%B8%D0%B9-%D1%84%D1%8C%D0%BE%D1%80%D0%B4/%D0%97%D1%91%D0%B1%D0%B0')

b=bs4.BeautifulSoup(s.text, "html.parser")

p3=b.select('.temperature .p3')
pogoda1=p3[0].getText()

p4=b.select('.temperature .p4')
pogoda2=p4[0].getText()

p5=b.select('.temperature .p5')
pogoda3=p5[0].getText()

p6=b.select('.temperature .p6')
pogoda4=p6[0].getText()

print('Утром :' + pogoda1 + ' ' + pogoda2)
print('Днём :' + pogoda3 + ' ' + pogoda4)

p=b.select('.rSide .description')
pogoda=p[0].getText()

print(pogoda.strip())