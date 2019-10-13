from django.db import models

# Create your models here.
class About(models.Model):
	title=models.CharField(max_length=70)
	sub_title=models.CharField(max_length=70)
	description=models.TextField()
	image=models.ImageField(upload_to='about')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name='About Company'
		verbose_name_plural='About Company'