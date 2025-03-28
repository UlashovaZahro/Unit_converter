from django.db import models


class UnitConverter(models.Model):
    CATEGORY_CHOICES = [
        ('Length', 'LENGTH'),
        ('Weight', 'WEIGHT'),
        ('Temperature', 'TEMPERATURE'),
    ]

    from_unit = models.CharField(max_length=25)
    to_unit = models.CharField(max_length=25)
    value = models.FloatField()
    convert_type = models.CharField(max_length=25, choices=CATEGORY_CHOICES, default="Length" )
    result = models.FloatField()

    def __str__(self):
        return f'Convert from {self.from_unit} to {self.to_unit}'




