from django.contrib import admin

# Register your models here.

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    #fields = ["pub_date", "question_text"]
    """
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]"""    
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

class ChoiceAdmin(admin.ModelAdmin):
    """
    fieldsets = [
        (None, {"fields": ["question"]}),
        ("Choice text", {"fields": ["choice_text"]}),
        ("Votes", {"fields": ["votes"]}),
    ]"""
    list_display = ["question", "choice_text", "votes"]

#admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
