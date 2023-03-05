from django.contrib import admin

from .models import Choice, Question

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}), 
        ('Date information', {'fields': ['pub_date'], 'classes':
                              ['collapse']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'was_published_recently') #displays header in topbar
    list_filter = ['pub_date'] #adds a filter 
    search_fields = ['question_text'] #adds search box for questions

admin.site.register(Question, QuestionAdmin) 

#import model of question so that question objects can be seen by the admin

# Register your models here.
