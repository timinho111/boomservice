from django.db import models


class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)


class Player(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    age = models.IntegerField()
    nationality = models.CharField(max_length=50)
    height = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    injured = models.BooleanField()
    photo = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Team(models.Model):
    id = models.AutoField(primary_key=True)
    area = models.ForeignObject
    name = models.CharField(max_length=50)
    shortName = models.CharField(max_length=50)
    tla = models.CharField(max_length=50)
    crestUrl = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    founded = models.CharField(max_length=50)
    clubColors = models.CharField(max_length=50)
    venue = models.CharField(max_length=50)
    squad = models.ForeignKey(Player, on_delete=models.CASCADE)
