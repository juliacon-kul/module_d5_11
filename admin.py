from django.contrib import admin
from p_library.models import Book, Author, Publisher, Friend, Abonement


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # list_display = ('title', 'author')
    pass
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    pass
@admin.register(Abonement)
class Abonement(admin.ModelAdmin):
    pass


# @admin.register(Inspiration)
# class InspirationAdmin(admin.ModelAdmin):
#     pass
