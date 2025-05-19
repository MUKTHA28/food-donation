from django.db import models
from django.contrib.auth.models import User

class DeliveryPerson(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    current_location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

class FoodReport(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(help_text="In number of meals or kg")
    timestamp = models.DateTimeField(auto_now_add=True)
    delivery_person = models.ForeignKey(DeliveryPerson, on_delete=models.SET_NULL, null=True, blank=True)
    is_picked_up = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.donor.username} - {self.quantity} units"
