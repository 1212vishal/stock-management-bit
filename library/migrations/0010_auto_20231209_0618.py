# Generated by Django 3.0.5 on 2023-12-09 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_auto_20230812_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('education', 'Education'), ('entertainment', 'Entertainment'), ('comics', 'Comics'), ('biography', 'Biography'), ('history', 'History'), ('novel', 'Novel'), ('fantasy', 'Fantasy'), ('thriller', 'Thriller'), ('romance', 'Romance'), ('scifi', 'Sci-Fi')], default='education', max_length=30),
        ),
    ]
