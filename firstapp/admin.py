from django.contrib import admin
from .models import CustomUser, Profile
from .custom_model import Category, Product, Review


admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)
