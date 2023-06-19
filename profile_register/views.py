from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import profilesform
from .models import profile
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html" 

def login(request):
    return render(request, 'login.html')

@login_required
def home(request):
    context = {'user': request.user}
    return render (request, "home.html", context)

def list(request):
    context = {'list': profile.objects.filter(user_id = request.user.id)}
    return render(request, "list.html", context)

def form(request, id = 0):
    if request.method == "GET":
        if id == 0:
            try: 
                profile.objects.get(user_id = request.user.id)
                messages.info(request, 'You can\'t add a new profile as one already exists ')
                return redirect('/list')
            except profile.DoesNotExist:
                form = profilesform(initial={'user_id': request.user})
        else:
            profilee = profile.objects.get(pk = id)
            form = profilesform(instance = profilee)
        return render(request, "form.html", {'form': form})
    
    else:
        if id == 0:
            print(request.POST)
            form = profilesform(request.POST)
        else:
            profilee = profile.objects.get(pk = id)
            form = profilesform(request.POST, instance = profilee)
        #if form.is_valid():
        form.save()
        return redirect('/list') 

def delete(request, id):
    profilee = profile.objects.get(pk = id)
    profilee.delete()
    return redirect('/list')