# Generated by Django 4.1.5 on 2023-01-24 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0002_noticias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='comentario',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
