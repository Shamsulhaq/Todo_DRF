from django.db import models

# Create your models here.
class List(models.Model):
    keyword         = models.CharField(max_length=220,null=False,help_text="Enter TODO Title")
    remainderTime   = models.DateTimeField(auto_now=False,auto_created=False)
    details         = models.TextField()
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.keyword

