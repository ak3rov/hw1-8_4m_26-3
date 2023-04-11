from django.db import models


class CustomerCL(models.Model):
    name = models.CharField('Имя заказчика', max_length=100)
    phone = models.CharField('Телефон', max_length=100)
    email = models.EmailField('Почта', blank=True)

    def __str__(self):
        return self.name


class TagCL(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class ProductCL(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    data_created = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(TagCL)

    def __str__(self):
        return self.name


class OrderCL(models.Model):
    STATUS = (
        ('На обработке', "На Обработке"),
        ("Выехал", "Выехал"),
        ("Отправлен", "Отправлен")
    )
    customer = models.ForeignKey(CustomerCL, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductCL, on_delete=models.CASCADE)
    data_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS)

    def __str__(self):
        return self.status