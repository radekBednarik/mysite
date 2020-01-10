from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class SideBarItems(models.Model):
    items = models.CharField(max_length=50)
    display = models.BooleanField(default=True)

    def __str__(self):
        return self.items


class OnePageContent(models.Model):
    side_bar_item_id = models.ForeignKey(SideBarItems, on_delete=models.CASCADE)
    text = RichTextUploadingField()
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return " ".join(["Content text for", str(self.side_bar_item_id)])


class MultiPageContent(models.Model):
    side_bar_item_id = models.ForeignKey(SideBarItems, on_delete=models.CASCADE)
    text = RichTextUploadingField()
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return " ".join(
            ["Text created on", str(self.created), "for", str(self.side_bar_item_id)]
        )
