from pymongo import MongoClient
import configparser


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
