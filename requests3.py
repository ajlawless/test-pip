import requests


r = requests.get('https://www.actaturcica.com/wp-content/uploads/2018/04/Colorful-Smoke-PNG-Image.png')

#with open('comic.png','wb') as f:
    #f.write(r.content)
f = open('comic.png','wb')
f.write(r.content)
