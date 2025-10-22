from guizero import App, ListBox, Text, TextBox, PushButton, Box
from tinydb import TinyDB, Query


db = TinyDB('./db/_categories.json')

database_titles = [x.get('name') for x in db.all()]

app = App(title="Codetools Categories Editor", width=1280, height=720)


def list_click():
    Categoria = Query()
    busca = db.search(Categoria.name == list_box.value)
    name.value = busca[0].get("name")

def nova_categoria():
    Categoria = Query()
    if not len(db.search(Categoria.name == list_box.value)):  
        db.insert({'name': name.value,})
    list_box.clear()
    database_titles = [x.get('name') for x in db.all()]
    for c in database_titles:
        list_box.append(c)
    return True

def excluir_categoria():
    Categoria = Query()
    db.remove(Categoria.name == name.value)
    list_box.clear()
    database_titles = [x.get('name') for x in db.all()]
    for c in database_titles:
        list_box.append(c)
    return True

list_box = ListBox(app, items=database_titles, height="fill", align="left", width=400, command=list_click)

formBox = Box(app, width="fill", height="fill", align="left", layout='grid')

name_label = Text(formBox, text="Categoria", align='left', grid=[0, 0])
name = TextBox(formBox, width='80', grid=[1, 0])

salvar = PushButton(formBox, text='Salvar', align="left", width='80', command=nova_categoria, grid=[1, 6, 2, 1])
salvar = PushButton(formBox, text='Excluir', align="left", width='80', command=excluir_categoria, grid=[1, 7, 2, 1])

app.display()