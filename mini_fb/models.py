from django.db import models

class Profile(models.Model):
    firstName = models.TextField()
    lastName = models.TextField()
    city = models.TextField()
    email = models.EmailField(unique=True)
    profile_image_url = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"