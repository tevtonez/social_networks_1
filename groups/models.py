# GROUPS MODELS

from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth import get_user_model
from django import template
import misaka

User = get_user_model()
register = template.Library()

class Group(models.Model):
  name = models.CharField(max_length = 75, unique = True)
  slug = models.SlugField(allow_unicod = True, unique = True)
  description = models.TextField(blank=True, default = '')
  description_html = models.TextField(editable = False, default = '', blank = True)
  members = models.ManyToManyField(User, through = 'GroupMember')

  def __str__(self):
    return self.name

  def save(self, *agrs, **kwargs):
    self.slug = slugify(self.name)
    self.description_html = misaka.html(self.description)
    super().save(*agrs, **kwargs)

  def get_absolute_url(self):
    return reverse('groups:single', kwargs = {'slug':self.slug})

  class Meta:
    ordering = ['name' ]

class GroupMember(models.Model):
  group = models.FroeignKey(Group, related_name = 'memberships')
  user = models.FroeignKey(User, related_name = 'user_groups')

  def __str__(self):
    return self.user.username

  class Meta:
    unique_together = ('group', 'user')

