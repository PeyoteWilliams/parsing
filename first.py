import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml

class Question():
    def __init__(self, tema = "", id_voprosa = "", vopros = "", reshenie = "", otvet1 = "", otvet2 = "", otvet3 = "", otvet4 = ""):
        self.id = id_voprosa
        self.tema = tema
        self.vopros = vopros
        self.reshenie = reshenie
        self.otvet_yes = otvet_yes
        self.otvet2 = otvet2
        self.otvet3 = otvet3
        self.otvet4 = otvet4

all_hrefs = list()
for i in range(1,13):
    url = 'https://ravanda.ru/i-exam/p/%D0%9C%D0%B5%D1%82%D1%80%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F,%20%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F,%20%D1%81%D0%B5%D1%80%D1%82%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D1%8F/'+str(i)  # url страницы
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    items = soup.find_all('a', {'class': 'sub_question'})
    for j in items:
        all_hrefs.append(j.get('href'))

all_questions = list()
n = 0
for i in all_hrefs:
    n+=1
    try:
        print(n, " / ", len(all_hrefs))
        url = 'https://ravanda.ru'+i
        r = requests.get(url)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, 'html.parser')
        q_div = soup.find('div', {'class': 'question_block'})
        temy = q_div.find_all("div", {'class': 'tema'})

        id_voprosa = i.split("/")[-1]
        tema_voprosa = temy[1].find("div", {'class': 'tema_text'}).text
        vopros = temy[2].find("div", {'class': 'tema_text'}).text
        reshenie = soup.find('div', {'class': 'solution_block'}).\
            find('div', {'class': 'tema'}).find("div", {'class': 'tema_text'}).text
        otvet1 = soup.find('div', {'class': 'answer_block'}).\
            find('div', {'class': 'answer'}).find_all('div', {'class': 'otvet'})[0].text
        otvet2 = soup.find('div', {'class': 'answer_block'}).\
            find('div', {'class': 'answer'}).find_all('div', {'class': 'otvet'})[1].text
        otvet3 = soup.find('div', {'class': 'answer_block'}).\
            find('div', {'class': 'answer'}).find_all('div', {'class': 'otvet'})[2].text
        otvet4 = soup.find('div', {'class': 'answer_block'}).\
            find('div', {'class': 'answer'}).find_all('div', {'class': 'otvet'})[3].text
        all_questions.append([vopros, otvet1, otvet2, otvet3, otvet4, id_voprosa, tema_voprosa, reshenie])
    except Exception:
        print(n, " / ", len(all_hrefs), " mistakenly")

    
df = pd.DataFrame(all_questions, columns =['вопрос', 'ответ1','ответ2','ответ3','ответ4', 'id','тема','решение'])
df.to_csv("output_metrologiya_otvety.xlsx", index=False)
df.to_csv("output_metrologiya_otvety.csv", index=False)  
#print(all_hrefs)
#result = pd.DataFrame()
#print(soup.find_all('a', {'class': 'sub_question'}))
#with open('test.html', 'w', encoding="utf-8") as output_file:
#  for item in items:
#      output_file.write(soup.prettify())

#with open('test.html', 'w', encoding="utf-8") as output_file:
#  output_file.write(r.text)

