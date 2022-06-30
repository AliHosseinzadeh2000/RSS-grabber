from django.db import models


class Rss(models.Model):
    press_name = models.CharField(max_length=200)
    link = models.URLField(max_length=200)

    class Meta:
        verbose_name = 'RSS'
        verbose_name_plural = 'RSSs'

    def __str__(self):
        return self.press_name



class News(models.Model):
    title = models.CharField(max_length=300)
    link = models.URLField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=200)
    publish_date = models.DateTimeField()

    class Meta:
        ordering = ['-publish_date']
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title
