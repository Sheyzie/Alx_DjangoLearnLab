from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    '''
    ManyToManyField('self'): Indicates a self-referencing many-to-many relationship.
    symmetrical=False: Means the relationship is directional (e.g., A follows B doesn’t imply B follows A).

    user.followers.all()  # Who follows this user
    user.following.all()  # Who this user follows
    '''
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='gallery')
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')
