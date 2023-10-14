from pyexpat import model
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import CoursesPost , StepsPost , SectionPost , ParcoursPost , LevelPost
from.import models


class ParcoursPostAdmin(SummernoteModelAdmin):
    exclude = ('slug', )
    list_display = ('id', 'title', 'Categories', 'date_created')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_per_page = 25
    summernote_fields = ('content', ) 

class LevelPostAdmin(SummernoteModelAdmin):
    exclude = ('slug', )
    list_display = ('id', 'title', 'Categories', 'date_created')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_per_page = 25
    summernote_fields = ('content', ) 


class CoursesPostAdmin(SummernoteModelAdmin):
    exclude = ('slug', )
    list_display = ('id', 'title', 'Categories', 'date_created')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_per_page = 25
    summernote_fields = ('content', ) 

class Admin(SummernoteModelAdmin):
    exclude = ('slug', )
    list_display = ('id', 'title', 'Categories', 'date_created')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_per_page = 25
    summernote_fields = ('content', ) 
class SectionPostAdmin(SummernoteModelAdmin):
    exclude = ('slug', )
    list_display = ('id', 'title', 'date_created')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_per_page = 25
    summernote_fields = ('content', )

class StepsPostAdmin(SummernoteModelAdmin):
    exclude = ('slug', )
    list_display = ('id', 'title', 'date_created')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_per_page = 25
    summernote_fields = ('content', )


admin.site.register(ParcoursPost,ParcoursPostAdmin)
admin.site.register(LevelPost,LevelPostAdmin)
admin.site.register(CoursesPost,CoursesPostAdmin)
admin.site.register(SectionPost ,SectionPostAdmin )
admin.site.register(StepsPost ,StepsPostAdmin )
admin.site.register(models.CategoriesPost)