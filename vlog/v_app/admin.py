from django.contrib import admin

# Register your models here.
from v_app.models import Post, Category, Komment, Author

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Komment)
admin.site.register(Author)