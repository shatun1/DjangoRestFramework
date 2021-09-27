from django.db import models
from users.models import CustomUser
# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=256)
    link_to_repo = models.URLField(max_length=1024, blank=True)
    users = models.ManyToManyField(CustomUser)


class TODO(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.CharField(max_length=10000)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, blank=True)
    # user = models.OneToO(CustomUser, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_active = models.BooleanField()



