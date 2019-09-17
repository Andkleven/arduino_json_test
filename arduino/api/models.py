from django.db import models

class Arduino(models.Model):
    test                                    = models.CharField(max_length=200, default='')

