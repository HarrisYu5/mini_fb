from django.db import models

class Profile(models.Model):
    firstName = models.TextField()
    lastName = models.TextField()
    city = models.TextField()
    email = models.EmailField(unique=True)
    profile_image_url = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
    
    def get_status_message(self):
        status_messages = StatusMessage.objects.filter(profile=self)
        return status_messages

class StatusMessage(models.Model):
    timeStamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.message}, {self.timeStamp}"