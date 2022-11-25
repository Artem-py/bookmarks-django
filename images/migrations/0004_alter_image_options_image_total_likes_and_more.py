# Generated by Django 4.1.2 on 2022-11-24 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_contact_contact_images_cont_created_afa5d7_idx'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='image',
            name='total_likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddIndex(
            model_name='image',
            index=models.Index(fields=['-created'], name='images_imag_created_d57897_idx'),
        ),
        migrations.AddIndex(
            model_name='image',
            index=models.Index(fields=['-total_likes'], name='images_imag_total_l_0bcd7e_idx'),
        ),
    ]