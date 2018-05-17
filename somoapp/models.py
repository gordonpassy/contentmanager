from django.db import models

# Create your models here.
class Pages(models.Model):
    video = models.FileField()
    image = models.ImageField() 
    text = models.TextField(max_length=300)
    def __str__(self):
        return self.text
    

class Topics(models.Model):
    name = models.CharField(max_length=30)
    page = models.ForeignKey(Pages)

    def __str__(self):
        return self.name

    
class Chapters(models.Model):
    chaptername = models.CharField(max_length=100)
    topic = models.ForeignKey(Topics)

    def __str__(self):
        return self.chaptername


class Subject(models.Model):
    subjetname = models.TextField(max_length=100)
    chapter = models.ForeignKey(Chapters)

    def __str__(self):
        return self.subjetname



