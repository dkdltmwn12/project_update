from bs4 import BeautifulSoup
from selenium import webdriver
import time
from urllib.request import urlopen
import requests


def danggn(search):
    query_txt = search

    url = "https://www.daangn.com/search/{}".format(query_txt)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    dgdata = []
    n = 1
    for item in soup.select("a[href*=articles]"):
        dgdata.append("https://www.daangn.com" + item.get("href", "/"))
        n += 1
        if n > 6:
            break

    dgimgurl = []
    n = 1
    for i in soup.find_all(class_="card-photo"):
        dgimgurl.append(i.find("img")["src"])
        n += 1
        if n > 6:
            break

    dgtitle = []
    n = 1
    for i in soup.find_all("span", {"class": "article-title"}):
        dgtitle.append(str(i.text))
        n += 1
        if n > 6:
            break

    dgcost = []
    n = 1
    for i in soup.find_all("p", {"class": "article-price"}):
        dgcost.append(str(i.text))
        n += 1
        if n > 6:
            break

    return dgimgurl, dgdata, dgtitle, dgcost


def hellomarket(search):
    query_txt = search

    path = "C:\\Users\\dydtj\\Desktop\\test\\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://www.hellomarket.com/search?q=" + query_txt)

    full_html = driver.page_source
    soup = BeautifulSoup(full_html, "html.parser")

    hdata = []
    n = 1
    for item in soup.select("a[href*=item]"):
        hdata.append("https://www.hellomarket.com" + item.get("href", "/"))
        n += 1
        if n > 6:
            break

    himgurl = []
    n = 1
    for i in soup.find_all(class_="image_centerbox"):
        himgurl.append(i.find("img")["src"])
        n += 1
        if n > 6:
            break

    htitle = []
    n = 1
    for i in soup.find_all("div", {"class": "item_title"}):
        htitle.append(str(i.text))
        n += 1
        if n > 6:
            break

    hcost = []
    n = 1
    for i in soup.find_all("div", {"class": "item_price"}):
        hcost.append(i.text)
        n += 1
        if n > 6:
            break

    return himgurl, hdata, htitle, hcost


def sellit(search):
    query_txt = search

    path = "C:\\Users\\dydtj\\Desktop\\test\\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://www.withsellit.com/search?query=" + query_txt)

    full_html = driver.page_source
    soup = BeautifulSoup(full_html, "html.parser")

    sdata = []
    n = 0
    for item in soup.select("a[href*=products]"):
        sdata.append("https://www.withsellit.com" + item.get("ng-href", "/"))
        if sdata[n] == "https://www.withsellit.com/":
            del sdata[n]
            n = n - 1
        n = n + 1
        if n > 5:
            break

    simgurl = []
    n = 1
    for i in soup.find_all(class_="gdidx-img"):
        simgurl.append(i.find("img")["src"])
        n += 1
        if n > 6:
            break

    stitle = []
    n = 1
    for i in soup.find_all("div", {"class": "gdidx-name ng-binding"}):
        stitle.append(str(i.text))
        n += 1
        if n > 6:
            break

    scost = []
    n = 1
    for i in soup.find_all("div", {"class": "gdidx-original-price ng-binding"}):
        scost.append(i.text)
        n += 1
        if n > 6:
            break

    return simgurl, sdata, stitle, scost
