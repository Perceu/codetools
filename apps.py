from guizero import App, ListBox, Text, TextBox, PushButton, Box, Combo
from tinydb import TinyDB, Query
from datetime import datetime


apps_db = TinyDB('./db/_database.json')
categorias_db = TinyDB('./db/_categories.json')

apps_titles = [x.get('Title') for x in apps_db.all()]
categories_titles = [x.get('name') for x in categorias_db.all()]

app = App(title="Codetools Editor", width=1280, height=720)


def list_click():
    Sistema = Query()
    busca = apps_db.search(Sistema.Title == list_box.value)
    print(busca[0])
    titulo.value = busca[0].get("Title")
    categoria.value = busca[0].get("Category")
    tags.value = '|'.join(busca[0].get("Tags"))
    site.value = busca[0].get("Link")
    docker.value = busca[0].get("Docker")
    summary.value = busca[0].get("Summary")

def salvar_click():
    Sistema = Query()
    if len(apps_db.search(Sistema.Title == titulo.value)) > 0:
        print('alterou')
        apps_db.update(
            {
                'Category': categoria.value,
                'Tags': tags.value.split('|'),
                'Link': site.value,
                'Docker': docker.value,
                'Summary': summary.value,
                'Description': summary.value,
                'Date': datetime.now().isoformat(),
            },
            Sistema.Title == titulo.value
        )
    else:
        print('inseriu')
        apps_db.insert(
            {
                'Title': titulo.value,
                'Category': categoria.value,
                'Tags': tags.value.split('|'),
                'Link': site.value,
                'Docker': docker.value,
                'Summary': summary.value,
                'Description': summary.value,
                'Date': datetime.now().isoformat(),
            },
        )

    return True
list_box = ListBox(app, items=apps_titles, height="fill", align="left", width=400, command=list_click)

formBox = Box(app, width="fill", height="fill", align="left", layout='grid')

titulo_label = Text(formBox, text="Titulo", align='left', grid=[0, 0])
titulo = TextBox(formBox, width='80', grid=[1, 0])

categoria_label = Text(formBox, text="Categoria", align='left', grid=[0, 1])
categoria = Combo(formBox, width='80', grid=[1, 1], options=categories_titles)

tags_label = Text(formBox, text="Tags", align='left', grid=[0, 2])
tags = TextBox(formBox, width='80', grid=[1, 2])

site_label = Text(formBox, text="Site", align='left', grid=[0, 3])
site = TextBox(formBox, width='80', grid=[1, 3])

docker_label = Text(formBox, text="Docker", align='left', grid=[0, 4])
docker = TextBox(formBox, width='80', grid=[1, 4])

summary_label = Text(formBox, text="Resumo", align='left', grid=[0, 5, 2, 1])
summary = TextBox(formBox, multiline = True, width='100', height='fill', grid=[0, 6, 2, 1])

salvar = PushButton(formBox, text='Salvar', align="left", width='80', command=salvar_click, grid=[1, 7, 2, 1])

app.display()