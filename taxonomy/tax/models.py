from django.db import models

# Create your models here.

class Node(models.Model):
	p=models.ForeignKey('self',null=True,on_delete=models.CASCADE)
	rank=models.CharField(max_length=200)

class Name(models.Model):
	node=models.OneToOneField(Node,on_delete=models.CASCADE,primary_key=True)
	text=models.CharField(max_length=1000)

class Image(models.Model):
	node=models.OneToOneField(Node,on_delete=models.CASCADE,primary_key=True)
	url=models.CharField(max_length=5000)

