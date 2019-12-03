from urllib import request
from bs4 import BeautifulSoup


quotes_page = ''
connect = request.urlopen(quotes_page)
page_html = connect.read()
connect.close()

page_soup = BeautifulSoup(page_html, "html.parser")
heading = page_soup.h1.text.strip()
print(heading)
quotes_div = page_soup.findAll("div", {"class":"quotes"})

for quote in quotes_div:

    quotes_only = quote.findAll(("p", {"class":"aquote"}))
    quotes = quotes_only[0].text.strip()

    author_only = quote.findAll(("p", {"class": "author"}))
    authors = author_only[1].text.strip()

    print(quotes)
    print(authors)
