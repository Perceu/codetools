import os
import copy
from tinydb import TinyDB
from datetime import datetime
from pelican.settings import DEFAULT_CONFIG
import requests


from pelican.utils import slugify

def posts(cat):
    db = TinyDB(f'db/{cat}.json')
    contents = db.all()
    for i in contents:
        if not os.path.exists(f'content/{cat}'):
            os.mkdir(f'content/{cat}')

        with open(f'content/{cat}/{i["title"]}.md', 'w') as file:
            file.write(f"Title: {i['title']}\n")
            file.write(f"Date: {datetime.now()}\n")
            file.write(f"Category: {cat}\n")

            if i.get('tags') is not None:
                file.write(f"Tags: {','.join(i['tags'])}\n")

            if i.get('docker') is not None:
                file.write(f"Docker: {i['docker']}\n")
            
            file.write(f"Link: {i['link']}\n")
            
            if i.get('description') is not None:
                file.write(f"{i['description']}\n")

def images(cat):
    db = TinyDB(f'db/{cat}.json')
    contents = db.all()
    for i in contents:
        if not os.path.exists(f'content/images'):
            os.mkdir(f'content/images')
        response = requests.get(f"http://localhost:8050/render.jpeg?url={i['link']}&timeout=15")
        
        settings = copy.deepcopy(DEFAULT_CONFIG)

        slug = slugify(
            i['title'],
            regex_subs=settings.get("SLUG_REGEX_SUBSTITUTIONS", []),
            preserve_case=settings.get("SLUGIFY_PRESERVE_CASE", False),
            use_unicode=settings.get("SLUGIFY_USE_UNICODE", False),
        )
        print(slug)
        with open(f"content/images/{slug}.jpeg", "wb") as img:
            img.write(response.content)


def build_categories():
    files = os.listdir('db')
    for f in files:
        cat = f.replace('.json', '')
        posts(cat)

def build_images():
    files = os.listdir('db')
    for f in files:
        cat = f.replace('.json', '')
        images(cat)