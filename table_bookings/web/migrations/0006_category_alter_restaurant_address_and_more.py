# Generated by Django 4.0.2 on 2022-05-04 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_restaurant_restaurantimage_restaurant_main_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.CharField(db_index=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.category'),
        ),
    ]
