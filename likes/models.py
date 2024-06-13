from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class LikedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # object type
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id
    object_id = models.IntegerField()
    # the actual object which is liked
    content_object = GenericForeignKey()

