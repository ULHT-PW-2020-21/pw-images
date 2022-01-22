# Generated by Django 4.0.1 on 2022-01-22 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picture',
            old_name='name',
            new_name='nome',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='image',
        ),
        migrations.AddField(
            model_name='picture',
            name='ano_de_criacao',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='picture',
            name='designer',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='picture',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='pictures/'),
        ),
        migrations.AddField(
            model_name='picture',
            name='website_oficial',
            field=models.URLField(null=True),
        ),
    ]
