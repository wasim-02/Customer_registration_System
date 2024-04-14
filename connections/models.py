from django.db import models

# Create your models here.
  
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.IntegerField()
    issue = models.TextField()

    def __str__(self):
        return self.name
    

class connect (models.Model):
    name = models.CharField(max_length=30)
    pincode = models.IntegerField()
    zonetype = models.TextChoices("zonetype","GEC1 GEC2 Rangia Bongaigaon Mangaldai Kokrajhar Barpeta Tezpur Nagaon Morigaon Kanch Cachar Badarpur NLakhimpur Sibsagar Jorhat Golaghat Dibrugarh Tinsukia")
    zone = models.CharField(choices=zonetype.choices, max_length=20,null=True, blank=True)


class Zone (models.Model):
    name = models.CharField(max_length=20,null=True, blank=True)

    def __str__(self):
        return self.name
    
class Division (models.Model):
    zone = models.ForeignKey(Zone,on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=20,null=True, blank=True)

    def __str__(self):
        return self.name
    
class SubDivision (models.Model):
    division = models.ForeignKey(Division,on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=20,null=True, blank=True)

    def __str__(self):
        return self.name
    
class Consumer (models.Model):
    name = models.CharField(max_length=30,null=True, blank=True)
    address = models.TextField(max_length=100)
    zone = models.ForeignKey(Zone,on_delete=models.CASCADE, blank=True)
    division = models.ForeignKey(Division,on_delete=models.CASCADE, blank=True)
    subdivision = models.ForeignKey(SubDivision,on_delete=models.CASCADE, blank=True,null=True)

    def __str__(self):
        return self.name
        