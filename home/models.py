from django.db import models

# Create your models here.

class Contact(models.Model):
    name      = models.CharField(max_length=122)
    email_id  = models.EmailField(max_length=122) 
    mobile_no = models.CharField(max_length=12)
    message   = models.TextField()
    date      = models.DateField()

    def __str__(self):
        return self.name

class Services(models.Model):
    title       = models.CharField(max_length=130)
    technology  = models.CharField(max_length=20)
    description = models.TextField()
    image       = models.ImageField(upload_to="static/media/services", default="")

    def __str__(self):
        return self.title

    
