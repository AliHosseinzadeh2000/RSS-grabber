# Generated by Django 4.0.5 on 2022-06-30 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=300, unique=True),
        ),
        migrations.AddConstraint(
            model_name='news',
            constraint=models.UniqueConstraint(fields=('title', 'link', 'description', 'author', 'publish_date'), name='unique_title_link_description_author_publish_date'),
        ),
    ]
