# Generated by Django 3.1.5 on 2021-04-04 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('body', models.TextField()),
                ('image', models.ImageField(default='', null=True, upload_to='pictures/')),
                ('date', models.DateTimeField()),
                ('author', models.CharField(max_length=20)),
            ],
        ),
    ]
