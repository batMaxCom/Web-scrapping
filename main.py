import bs4
import requests


HEADERS = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

base_url = "https://habr.com"
url = base_url + '/ru/all/'

response = requests.get(url, headers=HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text, features="html.parser")
articles = soup.find_all('article')
result_all = []
for article in articles:
    titles = article.find('h2').find('span').text
    hrefs = article.find(class_='tm-article-snippet__title-link').attrs['href']
    hubs = article.find_all(class_="tm-article-snippet__hubs-item")
    hubs = [hub.find('span').text for hub in hubs]
    pr_texts = article.find(class_="tm-article-body tm-article-snippet__lead").text
    datatimes = article.find(class_="tm-article-snippet__meta").find(class_="tm-article-snippet__datetime-published").find('time')['datetime']
    # print(f'{titles}\n{base_url+hrefs}\n{hubs}\n{pr_texts}\n{datatimes}\n')
    for hub in hubs:
        if hub.lower() in KEYWORDS:
            result = f"<{datatimes}> - <{titles}> - <{base_url + hrefs}>"
            if result not in result_all:
                result_all.append(result)
    for title in titles.split():
        if title.lower() in KEYWORDS:
            result = f"<{datatimes}> - <{titles}> - <{base_url + hrefs}>"
            if result not in result_all:
                result_all.append(result)
    for pr_text in pr_texts.split():
        if pr_text.lower() in KEYWORDS:
            result = f"<{datatimes}> - <{titles}> - <{base_url + hrefs}>"
            if result not in result_all:
                result_all.append(result)


print(result_all)


