# Generated by Django 2.1.2 on 2018-10-24 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_auto_20181024_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='tipo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='producto.Tipo'),
        ),
    ]