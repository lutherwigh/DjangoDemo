from django.contrib import admin
from app.models import Article
from app.models import Person

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','content','time']

class PersonAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','time']

admin.site.register(Article,ArticleAdmin)

admin.site.register(Person,PersonAdmin)
