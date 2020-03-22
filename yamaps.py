import requests
import bs4

def get_covid(chk):
    r = requests.get('https://yandex.ru/maps/covid19')
    b = bs4.BeautifulSoup(r.text, features='lxml')
    tm = b.find_all("div", { "class" : "covid-panel-view__subtitle" })
    #print(tm)
    #print([i for i in tm])
    ans = "Данные по РФ, актуальные на " + " ".join(i.get_text() for i in tm).replace("источники", ", источники") + "\n\n"
    stat = b.find_all("div", { "class" : "covid-panel-view__stat" })
    #print(stat)
    #ans += stat[0].get_text() + "\n"
    for div in stat[0].find_all("div", { "class" : "covid-panel-view__stat-item" }):
        left = div.find_all("div", { "class" : "covid-panel-view__stat-item-value" })[0].get_text()
        right = div.find_all("div", { "class" : "covid-panel-view__stat-item-title" })[0].get_text()
        if "за" in right:
            right = right.replace("за", " за")
        ans += left + " " + right + "\n"
    ans += "\n"
    if (chk):
        ans += "Подтверждённые случаи заражений по регионам России:\n"
        for div in b.find_all("div", { "class" : "covid-panel-view__item" }):
            left = div.find("div", { "class" : "covid-panel-view__item-name" }).get_text()
            right = div.find("div", { "class" : "covid-panel-view__item-cases" }).get_text()
            ans += left + " " + right + "\n"
    return ans