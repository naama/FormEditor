from django.db import models

class Form(models.Model):
	title = models.CharField(max_length=50)
	
class InputItem(models.Model):
	parent = models.ForeignKey(Form)
	description = models.CharField(max_length=3000)
	form_type = models.IntegerField(max_length=20, choices=(
														(0, "TEXTBOX"),
														(1, "TEXTAREA"),
														(2, "RADIOBUTTONS"),
														(3, "CHECKBOXES"),
														(4, "PULLDOWN")
														))
	choices = models.CharField(max_length=10000)
	
	def build_choices(self, *choices):
		result = ""
		for choice in choices:
			result = "%s,%s" % (result, choice)
		
		return result