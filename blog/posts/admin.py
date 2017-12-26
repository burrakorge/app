from django.contrib import admin

# Register your models here.
from .models import posts



class PostAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","titolo"]
    list_filter = ["data"]
    search_fields = ["titolo","contenuto"]
    prepopulated_fields = {"slug": ("titolo",)}

    class Meta:
        model = posts

admin.site.register(posts,PostAdmin)
