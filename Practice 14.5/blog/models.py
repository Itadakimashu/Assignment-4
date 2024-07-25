from django.db import models

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    aurthor = models.CharField(max_length=50)
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField(auto_now=True)
    body = models.CharField(max_length=25000)

    def __str__(self):
        return self.title