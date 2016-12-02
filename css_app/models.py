from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime


class CSSFile(models.Model):
	vote_count = models.IntegerField(default=0)
	title = models.CharField(max_length=200)
	host = models.CharField(max_length=200)
	css_text = models.TextField()
  	user = models.ForeignKey(settings.AUTH_USER_MODEL)
  	created_at = models.DateTimeField('date published', default=datetime.now, blank=True)

  	def __str__(self):
  		return self.title + " " + self.host


