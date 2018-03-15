from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True)
    bio = models.CharField(max_length=1000, default='')
    profile_img= models.ImageField(upload_to='profile_image',blank=True,null=True)
    def __str__(self):
        return self.user.username
    @classmethod
    def search_by_grammer(cls,search_term):
        query = cls.objects.filter(bio__icontains=search_term)
        return query
    def save_image(self):
            self.save()




            
    @classmethod
    def get_profiles(cls):
        '''
        Fucntion that gets all the profiles in the app
        Return
            profiles : list of all Profile obejcts in the database
        '''
        profiles = Profile.objects.all()

        return profiles

    
    @classmethod
    def search_profile(cls, search_term):
        profile = cls.objects.filter(user__username__icontains=search_term)
        return profile   



        
def Create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(Create_profile,sender=User)