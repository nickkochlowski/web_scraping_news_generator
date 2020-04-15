import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
import os
from break_line import break_line
from gradient_photo import gradient_photo
from spacing import spacing


URL = "https://www.lavoz.com.ar/politica"

img_destination = "/Users/nicolaskochlowski/Desktop/web_scraper/"

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15"}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

#Get the first four politics news posts
first_article = soup.find("article", class_="media")
second_article = first_article.next_sibling.next_sibling
third_article = second_article.next_sibling.next_sibling
fourth_article = third_article.next_sibling.next_sibling

#Create an array with the four posts
articles = [first_article, second_article, third_article, fourth_article]

#Go through each post and scrape out title, description and image link
#Overwrite values in articles
i = 0
for article in articles:
    title, lines_in_title = break_line(article.find("h2", class_="title is-marginless is-size-6-mobile is-size-4-tablet").get_text().lstrip(), 5)
    description, lines_in_description = break_line(article.find("div", class_="summary").get_text().lstrip(), 8)
    photo = article.find("div", class_="media-right")
    photo = photo.find("amp-img", class_="image image-cover")
    photo = photo['src']
    articles[i] = [title, description, photo, lines_in_title, lines_in_description]
    i += 1

# Print all the data for the four posts
for article in articles:
    for k in article:
        print(k)
    print("\n")


#Get each post image and add gradient, text and then export as PNG
j = 0
for article in articles:
    response = requests.get((articles[j])[2])
    img = Image.open(BytesIO(response.content))
    newsize = (10000,10000)
    img.thumbnail(newsize)
    box = ((img.size[0]/2)-450, 0, (img.size[0]/2)+450, 900)
#    box = ((img.size[0]/2)-300, (img.size[1]/2)-300, (img.size[0]/2)+300, (img.size[1]/2)+500)
    region = img.crop(box)
    region.save(img_destination + str(j) + ".PNG", "PNG", subsampling=0, quality=100)
    gradient_photo(img_destination + str(j) + ".PNG")
    region = Image.open(img_destination + str(j) + ".PNG")

    font1 = ImageFont.truetype("/Users/nicolaskochlowski/Desktop/web_scraper/font_open/OpenSans-Light.ttf", 50)
    font2 = ImageFont.truetype("/Users/nicolaskochlowski/Desktop/web_scraper/font_open/OpenSans-Light.ttf", 30)

    title_height, description_height, line_height = spacing((articles[j])[3], (articles[j])[4])

    draw = ImageDraw.Draw(region)
    draw.text((45, title_height), (articles[j])[0], font=font1) #draw title
    draw.text((45, description_height), (articles[j])[1], font=font2) #draw description
    draw.line((45, line_height, 650, line_height), fill=(255,255,255), width=1) #draw dividing line

    region.save(img_destination + str(j) + ".PNG", "PNG", subsampling=0, quality=100) #export high-res image
    j += 1
