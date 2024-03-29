# Generated by Django 5.0.3 on 2024-03-19 12:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(verbose_name='Дата оплаты')),
                ('amount_payment', models.PositiveIntegerField(verbose_name='сумма оплаты')),
                ('type_payment',
                 models.CharField(choices=[('CASH', 'Наличка'), ('CARD', 'Оплата картой')], max_length=50,
                                  verbose_name='способ оплаты')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                             related_name='payment', to='vehicle.course',
                                             verbose_name='Оплаченный курс')),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                             related_name='payment', to='vehicle.lesson',
                                             verbose_name='Оплаченный урок')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment',
                                           to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Оплата',
                'ordering': ('-payment_date',),
            },
        ),
    ]
