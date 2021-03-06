# Generated by Django 2.2.5 on 2019-09-28 10:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('buy_ticket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='price',
            field=models.FloatField(default=30, verbose_name='Preço Ingresso'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='show',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Show Ativo'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='code',
            field=models.CharField(default=uuid.uuid4, max_length=50, unique=True),
        ),
    ]
