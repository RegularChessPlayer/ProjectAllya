# Generated by Django 2.2.5 on 2019-09-28 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buy_ticket', '0004_auto_20190928_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='qtd_max_ticket',
            field=models.IntegerField(default=100, verbose_name='Quantidade disponível ingressos'),
        ),
        migrations.AlterField(
            model_name='show',
            name='theater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='show', to='buy_ticket.Theater'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='buy_ticket.Show'),
        ),
    ]
