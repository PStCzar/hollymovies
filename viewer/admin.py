from django.contrib.admin import ModelAdmin

class MovieAdmin(ModelAdmin):
  fieldsets = [
    (None, {'fields': ['title', 'created']}),
    (
      'External Information',
      {
        'fields': ['genre', 'released'],
        'description': (
          'These fields are going to be filled with data parsed '
          'from external databases.'
        )
      }
    ),
    (
      'User Information',
      {
        'fields': ['rating', 'description'],
        'description': 'These fields are intended to be filled in by our users.'
      }
    )
  ]
  readonly_fields = ['created']






