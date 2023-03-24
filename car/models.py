from django.db import models


class CarShop(models.Model):
    CAR_TYPE = (
        ('Седан', 'Седан'),
        ("Лимузин", "Лимузин"),
        ("Минивен", "Минивен"),
        ("Пикап", "Пикап"),
        ("Купе", "Купе"),
        ("Кабриолет", "Кабриолет"),
    )
    title = models.CharField("Model Name", max_length=100)
    description = models.TextField("About auto")
    image = models.ImageField(upload_to='')
    car_type = models.CharField(max_length=100, choices=CAR_TYPE)
    created_date = models.DateTimeField(auto_now_add=True)
    cost = models.PositiveIntegerField()
    video = models.URLField()
    specifications = models.TextField("Characteristic", null=True)
    model_year = models.TextField("Build year", null=True)
    manufacturing_country = models.TextField("Country", null=True)

    def __str__(self):
        return self.title