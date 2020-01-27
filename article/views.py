from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .forms import ArticleForm
from .models import Article,Comment
from django.contrib.auth.decorators import login_required
# Create your views here.

def articles(request):
    keyword=request.GET.get("keyword")
    if keyword:
        articles=Article.objects.filter(title__contains=keyword)
        return render(request,"articles.html",{"articles":articles})
    articles=Article.objects.all()
    return render(request,"articles.html",{"articles":articles})

def index(request):
    return render(request,"index.html")

def about(request):
    context={
        "number1":10,
        "number2":20,
        "numbers":[1,2,3,4,5,6]
    }
    return render(request,"about.html",context)


@login_required(login_url="user:login")         #execute fonction qui suis, si pas logué va au page  login sous user
def dashboard(request):
    articles=Article.objects.filter(author=request.user)
    context={
        "articles":articles
    }
    return render(request,"dashboard.html",context)

def addArticles(request):
    form=ArticleForm(request.POST or None)      #form est cree
    if form.is_valid():
        article=form.save(commit=False)         #cree objet mais ne sauvegarde pas
        article.author=request.user
        article.save()
        messages.success(request,"Article has beed saved")
        return redirect("index")
    return render(request,"addarticle.html",{"form":form})  #form envoyer vers le html

def detail(request,id):
    article=get_object_or_404(Article,id=id)                    #si id exist met dans id sinon envois erreur 404
    comments=article.comments.all
    return  render(request,"detail.html",{"article":article,"comments":comments})

def updateArticle(request,id):                      #request recu de urls.py
    article=get_object_or_404(Article,id=id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():                         #request.POST : envois les nouveau valeur
        article=form.save(commit=False)         #cree objet mais ne sauvegarde pas
        article.author=request.user             #instance : load les ancien valeurs
        article.save()
        messages.success(request,"Article has beed updated")
        return redirect("index")
    return render(request,"update.html",{"form":form})            #request envoyé a update.html


def deleteArticle(request,id):                      #request recu de urls.py
    article=get_object_or_404(Article,id=id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance=article)
    article.delete()
    messages.success(request,"Article has beed deleted")
    return redirect("article:dashboard")    #va  au dashboard qui est sous article

def addComment(request,id):
    article=get_object_or_404(Article,id=id)
    if request.method== "POST":                         #request.POST : envois les nouveau valeur
        comment_author=request.POST.get("comment_author")
        comment_content=request.POST.get("comment_content")
        newComment=Comment(comment_author=comment_author,comment_content=comment_content)
        newComment.article=article
        newComment.save()         #cree objet mais ne sauvegarde pas
    return redirect(reverse("article:detail",kwargs={"id":id}))


#a partir de navbar :  href="/article/dashboard/  , path /article/ envois vers article/url.py selon blog/urls.py
#dans url.py   path  dashboard/  views.dashboard  envois vers fichier  article/views.py fonction dashboard()
#avec attribue  dashboard
#dans article/views.py  le fonction dashboard est executé avec attribue dashboard
#form.save()  article objet cree et sauvé
