from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class SideBarItems(models.Model):
    items = models.CharField(max_length=50)
    display = models.BooleanField(default=True)

    def __str__(self):
        return self.items

    def get_absolute_url(self):
        return reverse("content", kwargs={"page": self.items})


class Content(models.Model):
    side_bar_item = models.ForeignKey(SideBarItems, on_delete=models.CASCADE)
    text = RichTextUploadingField()

    def __str__(self):
        return " ".join(["Content text for", str(self.side_bar_item)])

    # def get_absolute_url(self):
    #     return reverse("content")
    
