from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Blog
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, RedirectView, TemplateView
<<<<<<< HEAD
from blog.models import Blog as BlogModel
<<<<<<< HEAD
from django.http import *
=======
=======
# from blog.models import Blog as BlogModel
>>>>>>> 45bf2b0d54292b39e934e83913b3e23dcda0e171


>>>>>>> 1cc369c8818e57e33a71f2dccfb67378b1d297cb
# Create your views here.

# def home(request):
#     return render(request,'index.html')

# class Home(ListView):
#     model = Blog
#     context_object_name = 'home'
#     template_name = 'index.html'

<<<<<<< HEAD
=======
# class BlogView(TemplateView):
#     model = Blog
#     context_object_name = 'blog'
#     template_name = 'blog.html'

#     def get(self,request):
#         context={
#             'blog': BlogModel.objects.all()
#         }
#         return render(request, self.template_name,context)

>>>>>>> 45bf2b0d54292b39e934e83913b3e23dcda0e171
class BlogView(ListView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'blog.html'
<<<<<<< HEAD
    ordering=['id']
    paginate_by=3
    paginate_orphans=1

<<<<<<< HEAD
    def get_context_data(self, *args,**kwargs):
        try:
            return super(BlogView, self).get_context_data(*args,**kwargs)
        except Http404:
            self.kwargs['page']=1
            return super(BlogView, self).get_context_data(*args,**kwargs)
=======
    def get(self, request):
        context = {
            'blog': BlogModel.objects.all()
        }
        return render(request, self.template_name, context)
=======
    paginate_by = 2

    # def get(self, request):
    #     context = {
    #         'blog': BlogModel.objects.all()
    #     }
    #     return render(request, self.template_name, context)
>>>>>>> 45bf2b0d54292b39e934e83913b3e23dcda0e171

>>>>>>> 1cc369c8818e57e33a71f2dccfb67378b1d297cb

   
def blog_details(request, id):
    # data = Blog.objects.get(pk=id) #SELECT * FROM 'blog'
    data = get_object_or_404(Blog, pk=id)
    context = {
        'blog_detail': data
    }
    return render(request, 'blogdetail.html', context)
