# Generated by Django 2.1.7 on 2019-03-20 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(help_text='Enter the language (e.g Portuguese)', max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='idiom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Languages'),
        ),
    ]
