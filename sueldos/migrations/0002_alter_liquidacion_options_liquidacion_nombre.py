# Generated by Django 4.2.2 on 2024-08-07 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sueldos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='liquidacion',
            options={'verbose_name': 'Liquidacion', 'verbose_name_plural': 'Liquidaciones'},
        ),
        migrations.AddField(
            model_name='liquidacion',
            name='nombre',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
