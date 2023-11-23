from django.db import models

class Shortner(models.Model):
    long_url = models.URLField()
    short_code = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Short code: {self.short_code}, Long URL: {self.long_url}"