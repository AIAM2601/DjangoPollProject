from django.contrib import admin

from .models import Question

admin.site.register(Question) 
#import model of question so that question objects can be seen by the admin

# Register your models here.
