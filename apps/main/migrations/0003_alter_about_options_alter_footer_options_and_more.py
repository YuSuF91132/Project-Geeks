# Generated by Django 5.1.6 on 2025-03-02 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_about_contacts_footer_info_mainprojects_navigation_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'О Нас', 'verbose_name_plural': 'О Нас'},
        ),
        migrations.AlterModelOptions(
            name='footer',
            options={'verbose_name': 'Футер', 'verbose_name_plural': 'Футеры'},
        ),
        migrations.AlterModelOptions(
            name='mainprojects',
            options={'verbose_name': 'Главный Проэкт', 'verbose_name_plural': 'Главные Проэкты'},
        ),
        migrations.AlterModelOptions(
            name='ourprojects',
            options={'verbose_name': 'Наши Проэкты', 'verbose_name_plural': 'Наши Проэкты'},
        ),
    ]
