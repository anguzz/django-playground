from django.db import models

# Create your models here.
class Page(models.Model):               
    title = models.CharField(max_length=60) #page title to be used in html
    permalink = models.CharField(max_length=12, unique=True)   #permalink 
    update_date = models.DateTimeField('Last Updated')          #update date
    bodytext = models.TextField('Page Content', blank = True)   #bodytext
    
    def __str__(self):
            return self.title

