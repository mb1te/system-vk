import requests
import bs4
import random

def get_dvach(chk):
    r = requests.get('https://2ch.hk/b/')
    b = bs4.BeautifulSoup(r.text, features='lxml')
    ans = []
    for div in b.find_all("div", { "class" : "thread" }):
        cur = ""
        arr = div.find_all("article")
        cur += arr[0].get_text()
        print(arr)
        if chk:
            for i in range(1, len(arr)):
                cur += arr[i].get_text()
        ans.append(cur)
    return ans[random.randint(0, len(ans) - 1)]
                
    '''
    ans = b.find_all("h2", { "class" : "cv-section__title" })[0].get_text().replace("данные", " данные").replace("По", "по") + "\n"
    for div in b.find_all("div", { "class" : "cv-countdown__item" }):
        for item in div.find_all("div"):
            #print(item)
            ans += " ".join([i for i in item.get_text().split()])
        ans += "\n"
    ans = ans.replace("Случ", " случ")
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
    '''

#print(get_dvach(False))