import random

from django.core.urlresolvers import reverse
from django.db import models

class Quote(models.Model):
    text = models.TextField()
    url = models.URLField()

    class Meta:
        verbose_name = "Quote"
        verbose_name_plural = "Quotes"

    def __str__(self):
        return self.text


class Photo(models.Model):
    """Allows us to cache photo metadata so API calls are not needed for shared
    URLs."""

    alt_text = models.TextField(blank=True, null=True)
    image_url = models.URLField()
    credit_userid = models.CharField(max_length=30)
    credit_name = models.CharField(max_length=100)
    photo_id = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"

    def __str__(self):
        return '%s' % self.photo_id
    

class Inspiration(models.Model):
    """Contains all the information required to display a given inspirational
    poster."""

    FONTS = ["'Kaushan Script', cursive", "'Sue Ellen Francisco', cursive",
             "'Qwigley', cursive", "'Shadows Into Light', cursive"]

    font_index = models.IntegerField()
    quote = models.ForeignKey(Quote)
    photo = models.ForeignKey(Photo)

    class Meta:
        verbose_name = "Inspiration"
        verbose_name_plural = "Inspirations"

    def __str__(self):
        return '{self.quote.pk} / {self.photo.photo_id}'.format(self=self)

    def get_absolute_url(self):
        return reverse('citable', kwargs={'pk': self.pk})

    @classmethod
    def get_random_font(cls):
        font_index = random.randint(0, len(cls.FONTS) - 1)
        return font_index, cls.FONTS[font_index]

    @property
    def font(self):
        return self.FONTS[self.font_index]
