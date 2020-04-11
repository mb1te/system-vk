import requests
import bs4

def get_covid(chk):
    r = requests.get('https://стопкоронавирус.рф/#')
    b = bs4.BeautifulSoup(r.text, features='lxml')
    ans = b.find_all("div", { "class" : "d-map__title" })[0].get_text(separator=u"<br/>").replace("<br/>", " ") + "\n\n"

    #for i in b.find_all("span", { "class" : "d-map__indicator" }):
    #    print(i)
    cnt = 0
    for div in b.find_all("div", { "class" : "cv-countdown__item" }):
        if cnt == 0:
            cnt += 1
            continue
        for item in div.find_all("div"):
            #print(item)
            ans += " ".join([i for i in item.get_text().split()])
        ans += "\n"
    ans = ans.replace("Случ", " случ")
    ans = ans.replace("Чел", " чел")
    if (chk):
        ans += "\n"
        ans += b.find_all("a", { "class" : "d-open-map" })[0].get_text() + " по регионам (Заразилось/Выздоровело/Умерло)\n"
        for tr in b.find_all("div", { "class" : "d-map__list" })[0].find_all("tr"):
            ans += tr.find_all("th")[0].get_text() + ": "
            ans += tr.find_all("td")[0].get_text() + "/"
            ans += tr.find_all("td")[1].get_text() + "/"
            ans += tr.find_all("td")[2].get_text() + "\n"
    return ans

print(get_covid(True))