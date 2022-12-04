from django.db import models


class Projects(models.Model):
    title = models.CharField(max_length=255)
    intro = models.TextField()
    date = models.DateField()
    link=models.URLField()
    image=models.CharField(max_length=255, default='pythonimg.png')
