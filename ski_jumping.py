import requests
from bs4 import BeautifulSoup

competition = 'https://www.fis-ski.com/DB/general/results.html?sectorcode=JP&raceid=6506'
jumpers = 51

def parse(arg):
    fu = arg.split()
    fu[0] = fu[0].capitalize()
    return fu[0]
    
def parse_bros(arg):
    fu = arg.split()
    fu[0] = fu[0].capitalize() + ' ' + fu[1][0]
    return fu[0]

def main(html):
    r = requests.get(html)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    
    top10 = {}
    
    for position in range(1, jumpers+1):
        full_name = soup.select(f'#events-info-results > div > a:nth-child({position}) > div > div > div.g-lg.g-md.g-sm.g-xs.justify-left.bold')[0].text
        if "KOBAYASHI" in full_name:
            name = parse_bros(full_name)
        elif "SATO" in full_name:
            name = parse_bros(full_name)
        else:
            name = parse(full_name)
        top10[name] = position

    #print (top10)
    return top10

ranking = main(competition)

Mateusz = ["Granerud", "Kraft", "Zajc", "Kobayashi R", "Kubacki", "Wellinger", "Forfang", "Stoch", "Tschofenig", "Geiger"]
Adrian = ["Granerud", "Kraft", "Lanisek", "Geiger", "Wellinger", "Kubacki", "Kobayashi R", "Stoch", "Zajc", "Tschofenig"]
Aleksandra = ["Granerud", "Kraft", "Lanisek", "Geiger", "Kubacki", "Wellinger", "Zajc", "Tschofenig", "Stoch", "Kobayashi R"]
Aneczka = ["Granerud", "Zajc", "Kraft", "Kubacki", "Lanisek", "Fettner", "Wellinger", "Geiger", "Sundal", "Stoch"]
Aleksander = ["Granerud", "Zajc", "Lanisek", "Kraft", "Wellinger", "Kubacki", "Geiger", "Stoch", "Kobayashi R", "Tschofenig"]
Martyna = ["Granerud", "Kraft", "Lanisek", "Kobayashi R", "Geiger", "Kubacki", "Wellinger", "Zajc", "Tschofenig", "Stoch"]

def calc_points(player):
    position = 0
    score = 0
    for jumper in player:
        position += 1
        score += abs(ranking[jumper] - position)
    return (100-score)
    
print (f'Mateusz: {calc_points(Mateusz)}')
print (f'Adrian: {calc_points(Adrian)}')
print (f'Aleksandra: {calc_points(Aleksandra)}')
print (f'Aneczka: {calc_points(Aneczka)}')
print (f'Aleksander: {calc_points(Aleksander)}')
print (f'Martyna: {calc_points(Martyna)}')