# Generated by Django 4.2.3 on 2024-10-26 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parking',
            name='nome',
            field=models.CharField(default='Estacionamento Padrão', max_length=100),
        ),
        migrations.AlterField(
            model_name='parkingspace',
            name='parking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spaces', to='management.parking'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='hora_entrada',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='hora_saida',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='vaga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.parkingspace'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='valor',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
