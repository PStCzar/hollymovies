from django.db.models import (
    DO_NOTHING, CharField, DateField, DateTimeField, ForeignKey, IntegerField,
    Model, TextField, Model, AutoField
)


class Genre(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=128)

    def __str__(self):
        return str(self.name)


class Movie(Model):
    id = AutoField(primary_key=True)
    title = CharField(max_length=128)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rating = IntegerField()
    released = DateField()
    description = TextField()
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


from django.contrib.admin import ModelAdmin
class MovieAdmin(ModelAdmin):
  @staticmethod
  def released_year(obj):
    return obj.released.year
  @staticmethod
  def cleanup_description(modeladmin, request, queryset):
    queryset.update(description=None)
  ordering = ['id']
  list_display = ['id', 'title', 'genre', 'released_year']
  list_display_links = ['id', 'title']
  list_per_page = 20
  list_filter = ['genre']
  search_fields = ['title']
  actions = ['cleanup_description']