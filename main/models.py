from django.db import models
from django.urls import reverse

class Store(models.Model):
    storeName = models.CharField(max_length=50)
    

    class Meta:
        verbose_name = "Store"
        verbose_name_plural = "Stores"

    def __str__(self):
        return self.storeName

    def get_absolute_url(self):
        return reverse("Store_detail", kwargs={"pk": self.pk})
    
class Group(models.Model):
    groupName = models.CharField(max_length=50)
    

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def __str__(self):
        return self.groupName

    def get_absolute_url(self):
        return reverse("Group_detail", kwargs={"pk": self.pk})


class Item(models.Model):
    itemName = models.CharField(max_length=50)
    itemDescription = models.TextField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
    actualCount = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return self.itemName

    def get_absolute_url(self):
        return reverse("Item_detail", kwargs={"pk": self.pk})
    
    @property
    def diff(self):
        return self.count - self.actualCount


