from django.db import models

class Quote(models.Model):
    text = models.TextField()
    url = models.URLField()

    class Meta:
        verbose_name = "Quote"
        verbose_name_plural = "Quotes"

    def __str__(self):
        return self.text
    