from django.contrib import admin

from .models import Language, ProductLanguage, Genre, SubGenre

class GenreAdmin(admin.ModelAdmin):
    
    class Meta():
        madels = Genre
   
        
class SubGenreAdmin (admin.ModelAdmin):
    
    class Meta():
        models = SubGenre

class LanguageAdmin(admin.ModelAdmin):
    pass

class ProductLanguageAdmin(admin.ModelAdmin):
    pass



admin.site.register(Language, LanguageAdmin)
admin.site.register(ProductLanguage, ProductLanguageAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(SubGenre, SubGenreAdmin)

    

        

