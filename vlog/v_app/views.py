from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from v_app.forms import CatForm, AddCatForm, AddAuthorForm
from v_app.models import Post, Category, Author


@login_required(login_url='signin')
def info_category(request):
    category = Category.objects.all()
    authors = Author.objects.all()
    return render(request, 'v_app/info_category.html', {'category': category, 'authors': authors})

def info_post_about_cat(request, cat_id):
    cat = Category.objects.get(pk=cat_id)
    posts = Post.objects.filter(category=cat)
    return render(request, 'v_app/info_post_about_cat.html', {'category': cat, 'posts': posts})

def add_category(request):
   name_log = AddCatForm()
   if request.method == 'POST':
       name_log = AddCatForm(request.POST)
       if name_log.is_valid():
           cat_name = name_log.cleaned_data['name']
           name = Category(name=cat_name)
           if name:
               Category.objects.create(name=name)
           return redirect('info_category')
   return render(request, 'v_app/add_cat.html', {'form': name_log})


def del_category(request, cat_id):
    category = get_object_or_404(Category, pk=cat_id)
    category.delete()
    return redirect('info_category')


def info_post_about_avtor(request, author_id):
    item = Category.objects.get(pk=author_id)
    posts = Post.objects.filter(author=item)
    return render(request, 'v_app/info_post_about_cat.html', {'authors': item, 'posts': posts})

def add_avtor(request):
   avtor_log = AddAuthorForm()
   if request.method == 'POST':
       avtor_log = AddAuthorForm(request.POST)
       if avtor_log.is_valid():
           avtor_name = avtor_log.cleaned_data['name']
           name = Author(name=avtor_name)
           if name:
               Author.objects.create(name=name)
           return redirect('info_category')
   return render(request, 'v_app/add_avtor.html', {'form': avtor_log})


def del_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    author.delete()
    return redirect('info_category')