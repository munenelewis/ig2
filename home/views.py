from home.forms import Homeform,ImageForm,ProfileForm
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from . models import Post,Friend,Image,Company
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.generic.edit import UpdateView,CreateView
from instapp.models import Profile


# Create your views here.
class Homeview(TemplateView):
    template_name = 'home.html'

        
    def get(self,request):
        current_user = request.user

        form = Homeform()
        images = Image.objects.all().order_by('-created')
        posts = Post.objects.all().order_by('created')
        #print(posts)
        profile = Profile.objects.all().filter(user_id=current_user)

        users = User.objects.exclude(id=request.user.id)
        # friend = Friend.objects.get(current_user=request.user)
        
        # friends = friend.users.all()
        return render(request, self.template_name,{'form':form, 'posts':posts,'users':users,'images':images,'profile':profile,})
        
    def post(self, request):
        form = Homeform(request.POST)

        if form.is_valid():
            post=form.save(commit=False)
            post.user = request.user
            post.save()
            post = form.cleaned_data['post']
            form = Homeform
            return redirect('home')

        return render(request, self.template_name,{'form':form, 'text':text})


def post(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('home')
    else:
        form = ImageForm()
    arg = {
        "post_form": form,
    }
    return render(request, 'image_form.html', arg)



def newprofile(request):
    current_user = request.user
    test = 'hi'
    profile = Profile.objects.all().filter(user_id=current_user)
    image = Image.objects.all().filter(user_id=current_user)

    print(image)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            prf = form.save(commit=False)
            prf.user = current_user
            prf.save()
            return redirect('profile')
    else:
        form = ProfileForm()
    content = {
        'profile':profile,
        "profile_form": form,
         "test": test,
         "image":image
    }
    
    return render(request, 'profile.html', content)


    



class AlbumUpdate(UpdateView):
    model = Profile
    fields = ['bio','profile_img']



def detail(request, image_id):
    try:
        images = Image.objects.get(pk=image_id)
    except Image.DoesNotExist:
        raise Http404('bye')
    return render(request, 'details.html', {'images':images})


def photos(request,photo_id):
    try:
        photo = Image.objects.get(id = photo_id)
        print(photo.location)
    except DoesNotExist:
        raise Http404()
    return render(request,"search.html", {"photo":photo})
