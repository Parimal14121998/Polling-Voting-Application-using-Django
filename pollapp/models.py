from django.db import models

class pollmodel(models.Model):
	qts=models.TextField()
	op1=models.CharField(max_length=50)
	op2=models.CharField(max_length=50)
	op3=models.CharField(max_length=50)
	op1c=models.IntegerField(default=0)
	op2c=models.IntegerField(default=0)
	op3c=models.IntegerField(default=0)

	def __str__(self):
		return self.qts