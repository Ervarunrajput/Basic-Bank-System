from django.db import models

# Create your models here.
class Detail(models.Model):
    clientid = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=20)
    email = models.EmailField()
    bankbalance = models.BigIntegerField()

    def __str__(self):
        return self.Name

class Record(models.Model):
    sno = models.AutoField(primary_key=True)
    sendername = models.CharField(max_length=20)
    receivername = models.CharField(max_length=20)
    amount = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sendername