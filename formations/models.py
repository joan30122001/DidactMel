from django.db import models

# Create your models here.

class Formation(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    # image = models.ImageField()
    

class Course(models.Model):
    GENRE_CHOICES = (
        ('pdf', 'Pdf'),
        ('image', 'Image'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    types = models.CharField(max_length=10,
                             choices=GENRE_CHOICES,
                             default='pdf'
    )
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)
    
    

class Exercise(models.Model):
    EXERCISE_CHOICES = (
        ('qcm', 'Qcm'),
        ('drag-drop', 'Drag-drop'),
        ('crossed-word', 'Crossed-word'),
        ('find-word', 'Find-word'),
        ('link-card', 'Link-card'),
        ('search-word', 'Search-word'),
    )
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    types = models.CharField(max_length=15,
                            choices=EXERCISE_CHOICES,
                            default='qcm'
    )
    data = models.TextField() 
    