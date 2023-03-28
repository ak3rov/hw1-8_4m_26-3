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
    title = models.CharField("Марка Авто", max_length=100)
    description = models.TextField("Оо этой машине")
    image = models.ImageField(upload_to='')
    car_type = models.CharField(max_length=100, choices=CAR_TYPE)
    created_data = models.DateTimeField(auto_now_add=True)
    cost = models.PositiveIntegerField()
    video = models.URLField()
    reviews = models.TextField('reviews', blank=True, null=True)

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField("Your name: ", max_length=100)
    lastname = models.CharField("Your surname: ", max_length=100)
    email = models.CharField("Your e-mail: ", max_length=100)
    feedback_text = models.TextField("Your review: ", max_length=200)

    def __str__(self):
        return self.title