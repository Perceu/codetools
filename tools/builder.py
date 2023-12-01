import os
from tinydb import TinyDB, Query
from datetime import datetime

def build(cat):
    db = TinyDB(f'db/{cat}.json')
    contents = db.all()
    for i in contents:
        if not os.path.exists(f'content/{cat}'):
            os.mkdir(f'content/{cat}')
        with open(f'content/{cat}/{i["title"]}.md', 'w') as file:
            file.write(f"Title: {i['title']}\n")
            file.write(f"Date: {datetime.now()}\n")
            file.write(f"Category: {cat}\n")
            file.write(f"Link: {i['link']}\n")
            if hasattr(i, 'docker'):
                file.write(f"Docker: {i['docker']}\n")
            if hasattr(i, 'description'):
                file.write(f"{i['description']}\n")


def build_categories():
    files = os.listdir('db')
    print(files)
    for f in files:
        cat = f.replace('.json', '')
        build(cat)