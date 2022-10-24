import requests
from bs4 import BeautifulSoup
from time import sleep

data = []
l = 0
count = 0
p = 0
for k in range(1, 6):
    url = f'https://myanimelist.net/topanime.php?limit={count}'

    r = requests.get(url=url)
    sleep(2)
    soup = BeautifulSoup(r.text, 'lxml')
    status_one = soup.findAll('tr', class_='ranking-list')
    count += 50
    p += 1
    print(p)
    for i in status_one:
        l += 1
        position_beta = i.find('span', class_=f'lightLink top-anime-rank-text rank{1}')
        if position_beta == None:
            position_beta = i.find('span', class_=f'lightLink top-anime-rank-text rank{2}')
        
        if l >= 100:
            position_beta = i.find('span', class_=f'lightLink top-anime-rank-text rank{3}')

        position = position_beta.text

        link = i.find('a', class_="hoverinfo_trigger fl-l ml12 mr8").get('href')

        beta_names = i.find('a', class_="hoverinfo_trigger fl-l ml12 mr8").find('img').get('alt')
        names = beta_names.split(' ', 1)[1]

        score_beta = i.find('td', class_="score ac fs14").text
        score = score_beta.rstrip()

        details_list = []
        details_beta = i.find('div', class_='detail').text
        details_alfa = details_beta.split('\n', 4)[4]
        details_gama = details_alfa.rstrip() + ','
        details_delta = details_gama.replace(' ', '')
        details_list.append(details_delta)

        data.append([position, link, names, score, details_list])

print(data)