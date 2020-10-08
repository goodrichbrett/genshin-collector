# Generated by Django 3.1.2 on 2020-10-08 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_leveling'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='leveling',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='character',
            name='weapons',
            field=models.ManyToManyField(to='main_app.Weapon'),
        ),
    ]
