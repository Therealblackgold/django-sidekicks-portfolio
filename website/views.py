from django.shortcuts import render
from django.views.generic import DetailView
from .models import Post
from django.core.mail import send_mail


# Create your views here.
def home(request):
    post = Post.objects.all()
    return render(request, 'home.html', {'post':post})

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'

def pricing(request):
    return render(request, 'pricing.html', {})

def about(request):
    return render(request, 'about.html', {})

def project_one(request):
    return render(request, 'project_one.html', {})

def project_two(request):
    return render(request, 'project_two.html', {})

def project_three(request):
    return render(request, 'project_three.html', {})


def project_four(request):
    return render(request, 'project_four.html', {})

def project_five(request):
    return render(request, 'project_five.html', {})

def project_one(request):
    return render(request, 'project_one.html', {})        

def contact(request):
    if request.method == "POST":
        #do stuff
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        #send email
        send_mail(
            message_name,# subject
            message,# message
            message_email,# from email
            ['sidekicksdev01@gmail.com'],# to email
            fail_silently=False,
            )
        return render(request, 'contact.html', {'message_name': message_name})
    else:
        #return the page
        return render(request, 'contact.html', {})


