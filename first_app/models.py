from django.db import models

#django.db is a package where database related all files are available.
#models is a class so we are importing models class from django.db .
#Models is an instance of django.db.models.
#By models.Model we are inheriting django.db.models features.
#An object is an instance of a class.
#So we are creating new object and put them as new entry in database table

# Create your models here.
class Musician(models.Model):
    #id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name+" "+self.last_name


class Album(models.Model):
    # id = models.AutoField(primary_key=True)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date=models.DateField()

    #<option value='1'>Worst</option>
    choices=(
        (1, "Worst"),
        (2, "Bad"),
        (3, "Not Bad"),
        (4, "Good"),
        (5, "Excellent")
    )
    #values are integer thats why we used IntegerField().
    #We must use CharField() for Charecter type values ex: ("1", "worst")
    ratings=models.IntegerField(choices=choices, default="Worst")

    def __str__(self):
        return self.name+", Rating:"+str(self.ratings)
