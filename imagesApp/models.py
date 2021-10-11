from django.conf import settings
from django.db import models
from time import gmtime, strftime


def directory_path(instance, filename):
    upload_time = strftime("%Y-%m-%d_%H-%M-%S", gmtime())
    return ('user_{0}/%s/{1}' % upload_time).format(instance.user.id, filename)


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to=directory_path)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    # TODO: get_absolute_url
