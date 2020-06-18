from django.db import models

# Create your models here.
class Button(models.Model):
    value=models.BooleanField()
    last_changed= models.DateTimeField('date edited')
    def __str__(self):
        return(str(self.value)+" last_changed@"+str(self.last_changed))
    def getValue(self):
        return int(self.value)
    def switch(self):
        self.value=not self.value
    def turnOn(self):
        self.value=True
    def turnOff(self):
        self.value=False
    def getLastEdited(self):
        return self.last_changed