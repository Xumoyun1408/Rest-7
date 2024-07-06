from django.db import models

class Header(models.Model):
    logo = models.ImageField(upload_to="logo")
    phone_number = models.CharField(max_length=13)
    telegram_link = models.URLField(max_length=200)

    def __str__(self):
        return self.phone_number

class Navbar(models.Model):
    background_image = models.ImageField(upload_to="media")
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TravelPackage(models.Model):
    CATEGORY_CHOICES = [
        ('EKONOM', 'Ekonom'),
        ('KOMFORT', 'Komfort'),
        ('LYUKS', 'Lyuks'),
    ]

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category2 = models.CharField(max_length=7, choices=CATEGORY_CHOICES)
    narx = models.DecimalField(max_digits=10, decimal_places=2)
    aviakompaniya = models.CharField(max_length=50)
    davomiyligi = models.IntegerField()
    ovqatlanish = models.IntegerField()
    viza_kiritilgan = models.BooleanField()
    tibbiy_yordam = models.BooleanField()
    tajribali_yolboshchi = models.BooleanField()
    zamzam_suvi = models.BooleanField()
    jilet = models.BooleanField()
    sumka_va_nishon = models.BooleanField()

    def __str__(self):
        return f"{self.category.name} - {self.narx}$"
