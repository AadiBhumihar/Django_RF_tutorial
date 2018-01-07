from django.db import models
from django.contrib.auth.models import User

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)

    owner = models.ForeignKey('auth.User', related_name='snippets',\
                             on_delete=models.CASCADE,null=True,blank=True)
    highlighted = models.TextField(null=True,blank=True)

    class Meta:
        ordering = ('created',)

# class Person(models.Model):
#     user = models.OneToOneField(User,null=False,blank=False,related_name="person")
#     name = models.CharField(max_length=100,null=False,blank=False)

#     def __unicode__(self):
#         return "Username is {}".format(self.name)
