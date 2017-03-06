from django import models

class Category(models.Model):

	slug = models.slugField( unique=True )
	name = models.TextField()