# Generated by Django 3.1.7 on 2021-03-13 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_transportitems'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transportitems',
            old_name='Location',
            new_name='location',
        ),
        migrations.AlterField(
            model_name='driver',
            name='deliver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='loc', to='app.locations'),
        ),
        migrations.AlterField(
            model_name='transportitems',
            name='drive',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='driver_name', to='app.driver'),
        ),
        migrations.AlterField(
            model_name='transportitems',
            name='farmer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aadhar', to='app.aadhar'),
        ),
    ]
