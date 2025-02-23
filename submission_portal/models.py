from django.db import models

# Data Entry Model
# content -> TextField Content
# category -> Category field to choose between Text and Image URL
# is_reviewd -> Defaults to False
# Updated -> Will be time-stamped on changes
# Created -> Will be time-stamped upon creating

class DataEntry(models.Model):
    content = models.TextField(default="Default")
    category = models.CharField(max_length=10, choices=[('text', 'Text'), ('image_url', 'Image URL')], default='text')
    is_reviewed = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)