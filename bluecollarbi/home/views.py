from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string


def home(request):
    return render(request, 'home/index.html')

def elements(request):
    return render(request, 'home/elements.html')

def about(request):
    return render(request, 'home/about.html')

