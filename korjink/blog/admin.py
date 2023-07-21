from django.contrib import admin

from .models import Post, Category, Comment

from .models import Quote

admin.site.register(Quote)

class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ['title', 'slug', 'category', 'created_at', 'status']
    list_filter = ['category', 'created_at', 'status']
    actions = ['make_published', 'make_draft']
    inlines = [CommentItemInline]
    prepopulated_fields = {'slug': ('title',)}

    def make_published(self, request, queryset):
        queryset.update(status='published')

    def make_draft(self, request, queryset):
        queryset.update(status='draft')

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}
    


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','post','created_at']
    actions = ['make_published', 'make_draft']
    



admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
