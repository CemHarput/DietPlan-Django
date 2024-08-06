from django.db import models
class BaseModel(models.Model):
    creation_date = models.DateTimeField(blank=True,auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True