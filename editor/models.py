from django.db import models

class Form(models.Model):
	title = models.CharField(max_length=50)
	
class InputItem(models.Model):
	parent = models.ForeignKey(Form)
	
	question_number = models.IntegerField()
	question_text = models.CharField(max_length=3000)
	helptext = models.CharField(max_length=3000)
	form_type = models.IntegerField(max_length=20, choices=(
														(0, "TEXT"),
														(1, "LIST")
													))

	def build_choices(self, *choices):
		result = ""
		for choice in choices:
			result = "%s,%s" % (result, choice)
		
		return result

class InputText(models.Model):
	pass

class InputList(models.Model):
	choices = models.CharField(max_length=10000)


class Action(models.Model):
	