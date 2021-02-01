import bs4
import requests

url = "https://techcrunch.com/"
response = requests.get(url)

soup = bs4.BeautifulSoup(response.text, "html.parser")

article_titles, article_contents, article_hrefs = [], [], []

for tag in soup.findAll("div", {"class": "post-block post-block--image post-block--unread"}):
    tag_header = tag.find("a", {"class": "post-block__title__link"})
    tag_content = tag.find("div", {"class": "post-block__content"})

    article_title = tag_header.get_text().strip()
    article_href = tag_header["href"]
    article_content = tag_content.get_text().strip()

    article_titles.append(article_title)
    article_contents.append(article_content)
    article_hrefs.append(article_href)

all_articles = []
article_count = int(len(article_titles))

for i in range(article_count):
  all_articles.append([])

for i in range(article_count):
  all_articles[i].append(article_titles[i])
  all_articles[i].append(article_contents[i])
  all_articles[i].append(article_hrefs[i])

with open("articles.txt",'w',encoding = 'utf-8') as f:
  for i in range(article_count):
    if i:
      f.write('\n\n\n\n')
    for j in all_articles[i]:
      f.write(f"{j} \n\n")