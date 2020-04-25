from django.shortcuts import render
from django.http import HttpResponse #just need to response
from .models import Post #import post class and its database



#dummies for testing
'''
posts = [
    {
      'pots'
       'author': 'GermainMP',
       'title': 'Blog Post 1',
       'content': 'First post content',
       'date_posted': 'August 27, 2018'
    },
    {
       'author': 'Bond',
       'title': 'James Bond Films',
       'content': 'Second post content',
       'date_posted': 'August 28, 2018'
    }
] 
'''

# Create your views here.
def home(request):
    posts = {'posts': Post.objects.all()}

    return render(request, 'blog/home.html', posts)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'} )


def test(request):
    return HttpResponse('<h1>Testing</h1>')
