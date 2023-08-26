# Generated by Django 4.2.4 on 2023-08-13 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='images/testCoffee.jpg', upload_to='images/', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64, verbose_name='Название')),
                ('roasting', models.CharField(choices=[('Средняя', 'Средняя'), ('Тёмная', 'Тёмная')], default='Средняя', max_length=12, verbose_name='Обжарка')),
                ('mill', models.CharField(choices=[('Зерна', 'Зерна'), ('Мелкий', 'Мелкий')], default='Зерна', max_length=12, verbose_name='Помол')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Вес')),
                ('country', models.ForeignKey(choices=[('Индия', 'Индия'), ('Испания', 'Испания')], on_delete=django.db.models.deletion.CASCADE, to='core.country', verbose_name='Страна')),
                ('icon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.images', verbose_name='Картинка')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.prices', verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'abstract': False,
            },
        ),
    ]