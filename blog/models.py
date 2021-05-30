from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.name


"""

    def get_absolute_url(self):
        return reverse("home")
"""


class Post(models.Model):
    category = models.CharField(max_length=255, default="")
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_added"]


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date_added"]
