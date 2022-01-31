from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
import random



class Video(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField(upload_to='uploads/video_files',
                                  validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    thumbnail = models.FileField(upload_to='uploads/thumbnails', validators=[
                                 FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    date_posted = models.DateTimeField(default=timezone.now)
    unique_key = models.CharField(max_length=7, default='0000000', editable=False)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey('Video', on_delete=models.CASCADE)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'User: {self.user} | Created On: {self.created_on.strftime("%b %d %Y %I:%M %p")}'
