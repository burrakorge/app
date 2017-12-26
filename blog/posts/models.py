from django.db import models
from django.core.urlresolvers import reverse

class posts(models.Model):
    titolo = models.CharField(max_length = 200)
    contenuto = models.TextField()
    data = models.DateTimeField(auto_now = False, auto_now_add = True)
    slug = models.SlugField()

    def __unicode__(self):
        return self.titolo

    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        return reverse("singolo",kwargs = {"id": self.id, "slug":self.slug})



