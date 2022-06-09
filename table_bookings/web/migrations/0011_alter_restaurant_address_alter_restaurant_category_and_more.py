# Generated by Django 4.0.2 on 2022-06-08 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_review_booking_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.CharField(db_index=True, max_length=300, verbose_name='주소'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.category', verbose_name='카테고리'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='생성 일시'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='description',
            field=models.TextField(null=True, verbose_name='설명'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='latitude',
            field=models.FloatField(default=None, null=True, verbose_name='위도'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='longitude',
            field=models.FloatField(default=None, null=True, verbose_name='경도'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='main_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_image', to='web.restaurantimage', verbose_name='메인 이미지'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='menu_info',
            field=models.TextField(null=True, verbose_name='메뉴 정보'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='이름'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='연락처'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='수정 일시'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='visible',
            field=models.BooleanField(default=True, verbose_name='표시 여부'),
        ),
    ]
