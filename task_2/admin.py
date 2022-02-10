from django.contrib import admin

from task_2 import models

admin.site.register(models.UserProfile)
admin.site.register(models.Category)
admin.site.register(models.Course)
admin.site.register(models.Article)
admin.site.register(models.Partner)
