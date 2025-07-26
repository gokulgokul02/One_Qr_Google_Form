from django.db import models

class UserLogin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    qr_image = models.ImageField(upload_to='qr_images/')

    def __str__(self):
        return self.name
class Admin(models.Model):
    course_name= models.CharField(max_length=100)
    date=models.DateField()
    qr_change=models.ImageField(upload_to='admin_qr/')
    def __str__(self):
        return self.course_name