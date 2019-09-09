from django.db import models
from django_mysql.models import ListCharField
import uuid
from django.utils import timezone


# Create your models here.
class Task(models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task            = models.CharField(max_length=128, null=False)
    author          = ListCharField(models.CharField(max_length=128),size=4, max_length=(4 * 129))
    status          = models.IntegerField(default=0, null=False)
    created_at      = models.DateTimeField(default=timezone.now, null=False)
    last_update     = models.DateTimeField(default=timezone.now, null=False)
