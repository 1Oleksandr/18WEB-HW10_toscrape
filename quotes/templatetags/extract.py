from bson.objectid import ObjectId

from django import template
# from ..utils import get_mongodb
from ..models import Quote, Author, Tag

register = template.Library()

# Сделано Mongo
# def get_author(id_):
#     db = get_mongodb()
#     author = db.authors.find_one({'_id': ObjectId(id_)})
#     return author['fullname']


def get_author(id_):
    author = Author.objects.get(pk=id_)
    return author.fullname

def get_tags(quote):
    tags_for_quote = quote.tags.all()
    return tags_for_quote

# def get_fullname(author_obj):
#     fullname = author_obj.fullname
#     return fullname

register.filter('author', get_author)
register.filter('tagss', get_tags)
# register.filter('fullname', get_fullname)
