from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class OpenIDStore(models.Model):
    server_url = models.CharField(max_length=190)
    handle = models.CharField(max_length=190)
    secret = models.TextField()
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.TextField()

    def __str__(self):
        return self.server_url


@python_2_unicode_compatible
class OpenIDNonce(models.Model):
    server_url = models.CharField(max_length=190)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=190)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.server_url
