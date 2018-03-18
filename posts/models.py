from django.db import models

# Create your models here.


class Post(models.Model) :
	title = models.CharField(max_length = 100)
	pub_date = models.DateTimeField()
	image = models.ImageField(upload_to='media/')
	description = models.TextField()

	def __str__(self) :
		return self.title

	def date(self) :
		return self.pub_date.strftime('%b %e %Y')

	def summary(self) :
		return self.description[:100]