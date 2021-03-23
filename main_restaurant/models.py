from django.db import models
from uuid import uuid4
from os import path


# Create your models here.
class Category(models.Model):

    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f"{uuid4()}.{ext}"
        return path.join("media/images/categories", filename)

    title = models.CharField(max_length=20, unique=True)
    photo = models.ImageField(upload_to=get_file_name)
    category_order = models.IntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.category_order}. {self.title}"


class Dish(models.Model):

    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f"{uuid4()}.{ext}"
        return path.join("media/images/dishes", filename)

    title = models.CharField(max_length=25, unique=True)
    photo = models.ImageField(upload_to=get_file_name)
    dish_order = models.IntegerField()
    is_visible = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}: {self.price}"


class Story(models.Model):
    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f"{uuid4()}.{ext}"
        return path.join("media/images/story", filename)

    photo = models.ImageField(upload_to=get_file_name)
    story = models.CharField(max_length=500)
    is_visible = models.BooleanField(default=True)


class Team(models.Model):
    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f"{uuid4()}.{ext}"
        return path.join("media/images/team", filename)

    photo = models.ImageField(upload_to=get_file_name)
    team_info = models.CharField(max_length=500)
    is_visible = models.BooleanField(default=True)


class Phone(models.Model):
    phone = models.CharField(max_length=13)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.phone}"


class Address(models.Model):
    city = models.CharField(max_length=25)
    street = models.CharField(max_length=40)
    home = models.CharField(max_length=8)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.city}; {self.street}; {self.home}"


class OpeningHours(models.Model):
    day = models.CharField(max_length=10)
    hours_start = models.CharField(max_length=5)
    hours_end = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.day}: {self.hours_start}-{self.hours_end}"


class RestInfo(models.Model):
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone_id = models.ForeignKey(Phone, on_delete=models.CASCADE)


class Message(models.Model):
    user_name = models.CharField(max_length=30)
    user_email = models.EmailField()
    user_message = models.CharField(max_length=400)

    pub_date = models.DateField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user_name} | {self.user_email} | {self.user_message[:20]}"

