from django.contrib import admin
from .models import Article,Comment


# Register your models here.
admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date","content"]      #ajoute des contenue dans la liste
    list_display_links =["title","author","created_date","content"] #ajoute link partout
    search_fields = ["title"]       #ajoute recherche avec les infos titles
    list_filter = ["created_date"]  #ajoute filtre de temps

    class Meta:
        model=Article               #ArticleAdmin se join Article

