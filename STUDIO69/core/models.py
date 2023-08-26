from django.db import models


# Create your models here.
class AbstractProduct(models.Model):
    id = models.AutoField(
        primary_key=True
    )

    title = models.CharField(
        max_length=64,
        verbose_name='Название'
    )

    icon = models.ForeignKey(
        'Images',
        on_delete=models.CASCADE,
        verbose_name='Картинка'
    )

    price = models.ForeignKey(
        'Prices',
        on_delete=models.CASCADE,
        verbose_name='Цена'
    )

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Images(models.Model):
    image = models.ImageField(
        upload_to='images/',
        default='images/testCoffee.jpg',
        verbose_name='Картинка'
    )

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Coffee(AbstractProduct):
    ROASTING_CHOISES = [
        ('Средняя', 'Средняя'),
        ('Тёмная', 'Тёмная')
    ]

    MILL_CHOICES = [
        ('Зерна', 'Зерна'),
        ('Мелкий', 'Мелкий')
    ]

    country = models.ForeignKey(
        'Country',
        on_delete=models.CASCADE,
        verbose_name='Страна'
    )

    roasting = models.CharField(
        max_length=12,
        choices=ROASTING_CHOISES,
        default='Средняя',
        verbose_name='Обжарка'
    )

    mill = models.CharField(
        max_length=12,
        choices=MILL_CHOICES,
        default='Зерна',
        verbose_name='Помол'
    )

    weight = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name='Вес'
    )


class Prices(models.Model):
    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name='Цена'
    )


class Country(models.Model):
    title = models.CharField(
        max_length=64,
        verbose_name='Название'
    )
