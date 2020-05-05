# Generated by Django 3.0.5 on 2020-05-04 20:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='owner',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='authentication.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='directions',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(null=True),
        ),
    ]