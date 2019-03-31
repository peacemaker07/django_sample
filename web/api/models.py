from django.db import models


class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)
    creator_name = models.TextField(null=False)
    modifier_name = models.TextField(null=False)

    class Meta:
        abstract = True
        app_label = 'api'


class Book(BaseModel):

    title = models.CharField(max_length=255, unique=True)
    is_display = models.BooleanField(default=False)


class Content(BaseModel):

    content = models.CharField(max_length=255)
    book = models.ForeignKey(Book,
                             related_name='contents',
                             on_delete=models.CASCADE)
