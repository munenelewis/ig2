from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
from pyuploadcare.dj.forms import FileWidget
from django.template.defaultfilters import slugify
from instapp.models import Profile


class Photo(models.Model):
    title = models.CharField(max_length=255)
    photo = ImageField()

class Post(models.Model):
    post = models.CharField(max_length=500)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', null=True)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)

class Like(models.Model):
    like = models.TextField(max_length=2)


class Image(models.Model):
    image = models.ImageField()
    image_name= models.TextField(max_length=500)
    image_caption = models.TextField(max_length=1000)
    likes = models.IntegerField(default=0)
    post = models.ForeignKey(Post ,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile ,null=True)



    class meta:
        odering = ['-time']

    def save_image(self):
        self.save()

    def total_likes(self):
        return self.likes.count()

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(user__user__icontains=search_term)
        return news

class Company(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    likes = models.ManyToManyField(User, related_name='likes')

    @property
    def total_likes(self):
        """
        Likes for the company
        :return: Integer: Likes for the company
        """
        return self.likes.count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Company, self).save(*args, **kwargs)


class Follow(models.Model):
    '''
    Class that store a User and Profile follow status
    '''
    user = models.ForeignKey(User)
    profile = models.ForeignKey(Profile)


    def __str__(self):
        return self.user.username

    @classmethod
    def get_following(cls,user_id):
        following =  Follow.objects.filter(user=user_id).all()
        return following