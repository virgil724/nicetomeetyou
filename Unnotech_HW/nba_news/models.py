from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=30)
    url = models.URLField(unique=True)
    content = models.TextField()
    update_time = models.DateTimeField()
    paper = models.CharField(max_length=10)
    author = models.CharField(max_length=10)


class News_Photo(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    imgUrl = models.URLField()
    comment = models.CharField(max_length=20)
