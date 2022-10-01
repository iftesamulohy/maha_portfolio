import email
from email.mime import image
from locale import currency
from pyexpat import model
#from tkinter import Widget
from turtle import title
from unicodedata import category
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class UserDetails(models.Model):
    name = models.CharField(max_length=50)
    proffession = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=12,null=True)
    address = models.CharField(max_length=150)
    profile_image = models.ImageField(upload_to = "images/",null= True)
    facebook_link = models.URLField(max_length=100, null=True, default='#')
    twiter_link = models.URLField(max_length=100,null=True,default="#")
    github_link = models.URLField(max_length=100,null=True,default="#")
    website_link = models.URLField(max_length=100,null=True,default="#")
    description = models.CharField(max_length=1000,null=True)
    cv_file = models.FileField(upload_to="cv/",null=True)
    def __str__(self):
        return f"{self.name} {self.proffession}"
class SkillsType(models.Model):
    type = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.type}"
class Skills(models.Model):
    type = models.ForeignKey(SkillsType,on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    expertise = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    def __str__(self):
        return f"{self.name}"
class IconColor(models.Model):
    color_name = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.color_name}"
class WhatIdo(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    icon = models.CharField(max_length=35)
    color_name  = models.ForeignKey(IconColor,on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f"{self.name} {self.description} {self.icon} {self.color_name}"
class VertionColor(models.Model):
    vertion = models.CharField(max_length=12)
    def __str__(self):
        return f"{self.vertion}"
class AllColor(models.Model):
    color = models.CharField(max_length=12)
    def __str__(self):
        return f"{self.color}"
class Style(models.Model):
    vertion = models.ForeignKey(VertionColor,on_delete=models.CASCADE, null=True)
    color = models.ForeignKey(AllColor,on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f"{self.vertion} {self.color}"
class Education(models.Model):
    title = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    start_time = models.DateField()
    end_time = models.DateField()
    description = models.CharField(max_length=300)
    def __str__(self):
        return f"{self.title} {self.institution} {self.description}"

class Responsibilities(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"
class WorkExperience(models.Model):
    title = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    start_time = models.DateField()
    end_time = models.DateField()
    responsibility = models.ManyToManyField(Responsibilities)
    def __str__(self):
        return f"{self.title} {self.institution} {self.responsibility}"
class Client(models.Model):
    client_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    profile_image = models.ImageField(upload_to = "images/",null= True)
    def __str__(self):
        return f"{self.client_name}"
class Category(models.Model):
    name =  models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"

class PriceTable(models.Model):
    title= models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    currency = models.CharField(max_length=1)
    price = models.CharField(max_length=50)
    icon = models.CharField(max_length=50, null=True)
    category_name = models.ManyToManyField(Category)
    def __str__(self):
        return f"{self.title}"
class BlogImage(models.Model):
    title = models.CharField(max_length=50)
    blog_image = models.ImageField(upload_to = "blog/",null= True)
    def __str__(self):
        return f"{self.title}"
class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    category = models.ManyToManyField(Category)
    skils = models.ManyToManyField(Skills)
    button_text = models.CharField(max_length=50)
    demo_link = models.URLField(max_length=100,default="#")
    thumbnail_image = models.ImageField(upload_to = "thumbnail/",null= True)
    blog_image = models.ManyToManyField(BlogImage)
    #other_images = models.ImageField(upload_to = "allimages/",null= True)
    def __str__(self):
        return f"{self.title} {self.category}"

