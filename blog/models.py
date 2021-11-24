from django.db import models

class BlogPost (models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    
    def __str__(self):
        return self.title



class CommentPost (models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    
    def __str__(self):
        return self.title
