from django.contrib import admin

# Register your models here.
from .models import profile
from .models import product
from .models import Category



class profileAdmin(admin.ModelAdmin):
    class Meta:
        model = profile


admin.site.register(profile, profileAdmin)


class productAdmin(admin.ModelAdmin):
    class Meta:
        model = product


admin.site.register(product, productAdmin)


class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)
