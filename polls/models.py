from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
     button_click_count = models.PositiveIntegerField(default=0) 
     dobre = models.PositiveIntegerField(default=0) 
     zle = models.PositiveIntegerField(default=0) 
     stosunek = models.IntegerField(default=0)

     def save(self, *args, **kwargs):


        self.stosunek = self.dobre - self.zle  
        super().save(*args, **kwargs) 



































#STARE MODELE (używane jako inspiracja)
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Vote', related_name='votes')

    def score(self):
        return self.likes - self.dislikes  

    def __str__(self):
        return self.title

class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=[('like', 'like'), ('dislike', 'dislike')])

    class Meta:
        unique_together = ('user', 'post')  # użytkownik może polubić/nie polubić raz
