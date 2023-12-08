from django.db import models

# Create your models here.
class Service(models.Model):
    ICON_CHOICES = (
        ('twf-cleaning-1', 'twf-cleaning-1'),
        ('twf-cleaning-2', 'twf-cleaning-2'),
        ('twf-cleaning-3', 'twf-cleaning-3'),
    )

    name = models.CharField(max_length=50, null=False, blank=False)
    minimum_value = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=5)
    number_of_hours = models.IntegerField(null=False, blank=False)
    commission_percentage = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=5)

    hours_room = models.IntegerField(null=False, blank=False)
    room_value = models.DecimalField(null=False,  blank=False, decimal_places=2, max_digits=5)

    hours_hall = models.IntegerField(null=False, blank=False)
    hall_value = models.DecimalField(null=False,  blank=False, decimal_places=2, max_digits=5)

    hours_bathroom = models.IntegerField(null=False, blank=False)
    bathroom_value = models.DecimalField(null=False,  blank=False, decimal_places=2, max_digits=5)

    hours_kitchen = models.IntegerField(null=False, blank=False)
    kitchen_value = models.DecimalField(null=False,  blank=False, decimal_places=2, max_digits=5)

    hours_others = models.IntegerField(null=False, blank=False)
    others_value = models.DecimalField(null=False,  blank=False, decimal_places=2, max_digits=5)
    icon = models.CharField(null=False, blank=False, choices=ICON_CHOICES, max_length=14 )
    position = models.IntegerField(null=False)