from django.db import models

# Create your models here.


class Website(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    link = models.SlugField()

    def __str__(self):
        return self.name


class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to="photos/")
    categories = models.ManyToManyField(Category)

    def get_absolute_uri(self, request):
        return request.build_absolute_uri(self.photo.url)

    def __str__(self):
        return self.title


class Contact(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class About(models.Model):
    text = models.TextField()
    photo = models.ImageField(upload_to="profilephoto/")

    def get_absolute_uri(self, request):
        return request.build_absolute_uri(self.photo.url)

    def __str__(self):
        return self.text
