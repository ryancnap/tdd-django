# commented out for travvy and his merry landscapers
from django.db import models

# Create your models here.
class Item(models.Model):
	# Let's give our Items a text attribute, that way we can call .text on
	# any instances of Item (ie, our DB objects). this is called a TypeField.
	text = models.TextField(default = '')
	# We need to supply a default field for Django to populate the DB.
