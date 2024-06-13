from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Tags(models.Model):
    title = models.CharField(max_length=255)


class TaggedItem(models.Model):
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)
    # Type of Product
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # ID of Product
    object_id = models.IntegerField()
    # the actual object that is tagged
    content_object = GenericForeignKey()



