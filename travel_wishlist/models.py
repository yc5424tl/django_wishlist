from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)

    def __str__(self):
        return '%s visited? %s' % (self.name, self.visited)
