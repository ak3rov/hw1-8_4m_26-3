from django.db import models


class Cars(models.Model):
    CAR_TYPE = (
        ('Седан', 'Седан'),
        ("Лимузин", "Лимузин"),
        ("Минивен", "Минивен"),
        ("Пикап", "Пикап"),
        ("Купе", "Купе"),
        ("Кабриолет", "Кабриолет"),
    )
    title = models.CharField("марка машины", max_length=100)
    description = models.TextField("Про машину")
    image = models.ImageField(upload_to='')
    car_type = models.CharField(max_length=100, choices=CAR_TYPE)
    created_data = models.DateTimeField(auto_now_add=True)
    cost = models.PositiveIntegerField()
    video = models.URLField()

    def __str__(self):
        return self.title