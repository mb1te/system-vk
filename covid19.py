import requests
import bs4

def get_covid(chk):
    r = requests.get('https://стопкоронавирус.рф/#')
    b = bs4.BeautifulSoup(r.text, features='lxml')
    ans = b.find_all("h2", { "class" : "cv-section__title" })[0].get_text().replace("данные", " данные").replace("По", "по") + "\n"
    for div in b.find_all("div", { "class" : "cv-countdown__item" }):
        for item in div.find_all("div"):
            #print(item)
            ans += " ".join([i for i in item.get_text().split()])
        ans += "\n"
    ans = ans.replace("Случая", " случая")
    ans = ans.replace("Чел", " чел")
    if (chk):
        ans += "\n"
        ans += b.find_all("a", { "class" : "d-open-map" })[0].get_text() + " по регионам (Заразилось/Выздоровело/Умерло)\n"
        for tr in b.find_all("tr"):
            ans += tr.find_all("th")[0].get_text() + ": "
            ans += tr.find_all("td")[0].get_text() + "/"
            ans += tr.find_all("td")[1].get_text() + "/"
            ans += tr.find_all("td")[2].get_text() + "\n"
    return ans

print(get_covid(False))