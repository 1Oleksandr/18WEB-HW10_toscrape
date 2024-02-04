import os
import django
from pymongo import MongoClient
import configparser

# устанавливаем переменную окружения
# os.environ.setdefault( key: 'DJANGO_SETTINGS_MODULE', value: 'toscrape.settings')
# django.setup()
# только теперь можно импортировать модели
from quotes.models import Quote, Tag, Author

def get_mongodb():
    config = configparser.ConfigParser()
    config.read('config.ini')

    mongo_user = config.get('DB', 'user')
    mongodb_pass = config.get('DB', 'pass')
    db_name = config.get('DB', 'db_name')
    domain = config.get('DB', 'domain')

    print(mongo_user, mongodb_pass, db_name, domain)

    client = MongoClient(
        f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority""", ssl=True)

    db = client.HW10_Toscrape
    return db

db = get_mongodb()
authors = db.authors.find()
for author in authors:
    Author.objects.get_or_create(
        fullname= author['fullname'],
        born_date= author['born_date'],
        born_location= author['born_location'],
        description= author['description']
    )

quotes = db.quotes.find()
for quote in quotes:
    tags = []
    for tag in quote['tags']:
        t, *_ = Tag.objects.get_or_create(name = tag)
        tags.append(t)

    exist_quote = bool(len(Quote.objects.filter(quote=quote['quote'])))

    if not exist_quote:
        author = db.authors.find_one({'_id': quote['author']})
        a = Author.objects.get(fullname = author['fullname'])
        q = Quote.objects.create(
            quote=quote['quote'],
            author = a
        )
        for tag in tags:
            q.tags.add(tag)
            