from django.shortcuts import render
from django.contrib.auth.mixins LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
from .models import Group, GroupMember


class CreateGroup(LoginRequiredMixin, generic.CreateView):
  fields = ('name', 'description')
  model = Group


class SingleGroup(generic.DetailView):
  model = Group


class ListGroup(generic.ListlView):
  model = Group

