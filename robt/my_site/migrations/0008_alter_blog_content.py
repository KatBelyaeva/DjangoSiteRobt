# Generated by Django 4.1 on 2022-09-16 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0007_alter_blog_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]