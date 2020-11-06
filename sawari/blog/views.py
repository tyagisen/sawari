from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import *
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, RedirectView, TemplateView
from blog.models import Blog as BlogModel


# Create your views here.

# def home(request):
#     return render(request,'index.html')

# class Home(ListView):
#     model = Blog
#     context_object_name = 'home'
#     template_name = 'index.html'

class BlogView(TemplateView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'blog.html'

    def get(self, request):
        context = {
            'blog': BlogModel.objects.all()
        }
        return render(request, self.template_name, context)


def blog_details(request, id):
    # data = Blog.objects.get(pk=id) #SELECT * FROM 'blog'
    data = get_object_or_404(Blog, pk=id)
    context = {
        'blog_detail': data
    }
    return render(request, 'blogdetail.html', context)
