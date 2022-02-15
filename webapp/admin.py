from django.contrib import admin
from .models import PostModel, WorkModel, Comment

#post to published
def make_published(modeladmin, request, queryset):
    queryset.update(status = "p")
make_published.short_description = "change to published"

#post to draft
def make_drafted(modeladmin, request, queryset):
    queryset.update(status = "d")
make_drafted.short_description = "change to drafted"

class PostAdmin(admin.ModelAdmin):
    search_field = ['title']
    list_display = ['title', 'thumbnail_tag', 'date', 'author', 'status']
    list_filter = ['date']
    actions = [make_published, make_drafted]
    fieldsets = (
        ('title info', {'fields':['title']}),
        ('content info', {'fields':['content']}),
        ('slug info', {'fields':['slug']}),
        ('thumbnail info', {'fields':['thumbnail']}),
        ('status info', {'fields':['status']}),
        ('author info', {'fields': ['author']}),
    )

class WorkAdmin(admin.ModelAdmin):
    search_field = ['skills']
    list_display = ['skills', 'cost']
    list_filter = ['cost']
    
    fieldsets = (
        ('skill info', {'fields':['skills']}),
        ('duration info', {'fields':['duration']}),
        ('cost info', {'fields':['cost']}),
        ('github info', {'fields':['github']}),
        ('github url', {'fields':['github_url']}),
        ('about info', {'fields':['about']}),
        ('image info', {'fields':['image']}),

    )



class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(PostModel, PostAdmin)
admin.site.register(WorkModel, WorkAdmin)
admin.site.register(Comment, CommentAdmin)