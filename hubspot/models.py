from django.db import models
from cloudinary.models import CloudinaryField

class UploadVideo(models.Model):
	username = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	video = CloudinaryField('video', resource_type="video", folder='vids/')
	date_posted = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title