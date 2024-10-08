# Generated by Django 5.1.1 on 2024-10-08 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0005_alter_menu_category_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('contact', models.CharField(max_length=300, verbose_name='Phone number')),
                ('time', models.TimeField()),
                ('count', models.IntegerField()),
                ('notes', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.DeleteModel(
            name='MenuCategory',
        ),
    ]
