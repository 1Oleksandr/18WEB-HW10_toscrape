from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .models import Quote, Author, Tag
# from .utils import get_mongodb
from .forms import QuoteForm, AuthorForm, TagForm


# Сделано для MongoDB 
# def main(request, page=1):
#     db = get_mongodb()
#     quotes = db.quotes.find()
#     per_page = 10
#     paginator = Paginator(list(quotes), per_page)
#     quotes_on_page = paginator.page(page)
#     return render(request, "quotes/index.html", context={'quotes': quotes_on_page})

def top_ten_tags():
    dict_tags = {}
    tags = Tag.objects.all()
    for tag in tags:
        quantity = Tag.objects.get(id=tag.id).quote_set.all().count()
        dict_tags[tag.name] = quantity
    sorted_tuple_tags = sorted(dict_tags.items(), key=lambda x: x[1], reverse=True)[:10]
    top_tags = []
    for tag in sorted_tuple_tags:
        top_tags.append(tag[0])
    return top_tags


def main(request, page=1):
    quotes = Quote.objects.all()
    top_tags = top_ten_tags()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, "quotes/index.html", context={'quotes': quotes_on_page, 'tags': top_tags})

def author(request, author_id):
    author = Author.objects.get(pk=author_id)
    return render(request, "quotes/author.html", context={'author': author})

def by_tag(request, tag_name):
    quotes = Tag.objects.get(name=tag_name).quote_set.all()
    top_tags = top_ten_tags()
    # per_page = 10
    # paginator = Paginator(list(quotes), per_page)
    # quotes_on_page = paginator.page(page)
    # print(quotes_on_page)
    return render(request, "quotes/tag.html", context={'tag': tag_name, 'quotes': quotes, 'tags': top_tags})

@login_required
def load_author(request):
    form_author = AuthorForm()
    if request.method == 'POST':
        form_author = AuthorForm(request.POST)
        if form_author.is_valid():
            form_author.save()
            return redirect(to='quotes:root')
    return render(request, 'quotes/add_author.html',
                  context={'form_author': form_author})


def tag_normalize(tags): 
    t1 = tags.replace(',' , ' ')
    t2 = t1.replace('.', ' ')
    tags = t2.strip().split()
    return tags

@login_required
def upload(request):
    form_quote = QuoteForm()
    if request.method == 'POST':
        form_quote = QuoteForm(request.POST)
        tags = request.POST['tags']
        if tags == '':
            return render(request, 'quotes/add_quote.html',
                  context={'form_quote': form_quote})
        list_tags = tag_normalize(tags)
        if form_quote.is_valid():
            quote = form_quote.save(commit=False)
            # quote.user = request.user
            quote.save()
            for t in list_tags:
                tag = Tag.objects.get_or_create(name = t)
                quote.tags.add(tag[0])
            return redirect(to='quotes:root')
    return render(request, 'quotes/add_quote.html',
                  context={'form_quote': form_quote})