import os
import copy
from tinydb import TinyDB
from datetime import datetime
from time import sleep
from pelican.settings import DEFAULT_CONFIG
from selenium import webdriver


from pelican.utils import slugify


def posts():
    full_db = TinyDB("db/_database.json")
    contents = full_db.all()
    for i in contents:
        category = i.get("Category", '')
        title = i.get("Title", '')
        date = i.get("Date", '')
        docker = i.get("Docker", '')
        link = i.get("Link", '')
        summary = i.get("Summary", '')
        description = i.get("Description", '')
        tags = i.get("Tags", [])

        if not os.path.exists(f"content/{category}"):
            os.mkdir(f"content/{category}")

        with open(f'content/{category}/{title}.md', "w") as file:
            file.write(f"Title: {title}\n")
            file.write(f"Date: {date}\n")
            file.write(f"Category: {category}\n")

            if len(tags) > 0:
                file.write(f"Tags: {','.join(tags)}\n")

            if docker != "":
                file.write(f"Docker: {docker}\n")

            if link != "":
                file.write(f"Link: {link}\n")

            if summary != "":
                file.write(f"{summary}\n")

            if description != "":
                file.write(f"{description}\n")


def images():
    full_db = TinyDB("db/_database.json")
    contents = full_db.all()
    
    options = webdriver.FirefoxOptions()
    driver = webdriver.Remote(options=options)
    driver.maximize_window()

    if not os.path.exists("content/images"):
        os.mkdir("content/images")

    for i in contents:
        title = i.get("Title", '')
        link = i.get("Link", '')
        driver.get(link)

        settings = copy.deepcopy(DEFAULT_CONFIG)

        slug = slugify(
            title,
            regex_subs=settings.get("SLUG_REGEX_SUBSTITUTIONS", []),
            preserve_case=settings.get("SLUGIFY_PRESERVE_CASE", False),
            use_unicode=settings.get("SLUGIFY_USE_UNICODE", False),
        )
        print(slug)
        sleep(5)
        driver.save_screenshot(f"content/images/{slug}.png")
        print("=" * 50)
    driver.quit()

def build_categories():
    posts()


def build_images():
    images()
