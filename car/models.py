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
    title = models.CharField("Название модели", max_length=100)
    description = models.TextField("Описание авто")
    image = models.ImageField(upload_to='')
    car_type = models.CharField(max_length=100, choices=CAR_TYPE)
    created_date = models.DateTimeField(auto_now_add=True)
    cost = models.PositiveIntegerField()
    video = models.URLField()
    specifications = models.TextField("Характеристика", null=True)
    model_year = models.TextField("Год сборки", null=True)
    manufacturing_country = models.TextField("Страна", null=True)

    def __str__(self):
        return self.title