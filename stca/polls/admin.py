from django.contrib import admin

from .models import Choice, Question, Vote

class VoteInline(admin.StackedInline):
    model = Vote
    extra = 0

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['created'], 'classes': ['collapse']}),
        ('User',             {'fields': ['user']}),
        ('State',            {'fields': ['state']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'created', 'user', 'state')


class ChoiceAdmin(admin.ModelAdmin):
    inlines = [VoteInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Vote)