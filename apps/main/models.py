from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.CharField(
        max_length=55,
        verbose_name="Имя Компании"
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Телофонный Номер"
    )
    vertical_text = models.CharField(
        max_length=100,
        verbose_name="Вертикальный Текст"
    )
    class Meta:
        verbose_name = "Информация"
        verbose_name_plural = "Информации"
    def __str__(self):
        return self.name

class Navigation(models.Model):
    home = models.CharField(
        max_length=55,
        verbose_name="1 Навигационная Кнопка"
    ) 
    about = models.CharField(
        max_length=55,
        verbose_name="2 Навигационная Кнопка"
    )
    projects = models.CharField(
        max_length=55,
        verbose_name="3 Навигационная Кнопка"
    )
    services = models.CharField(
        max_length=55,
        verbose_name="4 Навигационная Кнопка"
    )
    contacts = models.CharField(
        max_length=55,
        verbose_name="5 Навигационная Кнопка"
    )
    previous_button = models.CharField(
        max_length=55,
        verbose_name="Предыдущая Кнопка"
    )
    next_button = models.CharField(
        max_length=55,
        verbose_name="Следующая Кнопка"
    )
    look_more_button = models.CharField(
        max_length=35,
        verbose_name="Кнопка Смотреть Дальше"
    ) 
    def __str__(self):
        return self.home
    
    class Meta:
        verbose_name = "Навигация"
        verbose_name_plural = "Навигации"

class MainProjects(models.Model):
    image = models.ImageField(
        verbose_name="Фото Проэкта"
    )
    project_name = models.CharField(
        max_length=100,
        verbose_name="Имя Проэкта"
    )
    project_desription = models.TextField(
        verbose_name="Описание Проэкта"
    )
    def __str__(self):
        return self.project_name
    class Meta:
        verbose_name = "Главный Проэкт"
        verbose_name = "Главные Проэкты"

class About(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовок"
    )
    citate = models.CharField(
        max_length=155,
        verbose_name="Цитата"
    )
    description = models.TextField(
        verbose_name="Описания О Нас"
    )
    specialization_title = models.CharField(
        max_length=55,
        verbose_name="Наши Специальности"
    )
    specialization = models.CharField(
        max_length=55,
        verbose_name="Специальности"
    )
    logo = models.ImageField(
        verbose_name="Лого"
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "О нас"

class OurProjects(models.Model):
    title = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Заголовок"
    )
    image = models.ImageField(
        verbose_name="Фото Проэкта"
    ) 
    project_name = models.CharField(
        max_length=100,
        verbose_name="Названия Проэкта"
    )
    vertical_line = models.CharField(
        max_length=55,
        verbose_name="Вертикальная Линия"
    )      
    def __str__(self):
        
        return self.title
    
    class Meta:
        verbose_name = "Наши Проэкты"


class OurServices(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок"
    )
    years = models.IntegerField(
        verbose_name = "Годы"
    ) 
    years_title1 = models.CharField(
        max_length=100,
        verbose_name="Заголовок лет 1"
    )  
    years_title2 = models.CharField(
        max_length=100,
        verbose_name="Заголовок лет 2"
    )   

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Наш Сервис"
        verbose_name_plural = "Наши сервисы"  

class Contacts(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок"
    )
    number1 = models.CharField(
        max_length=100,
        verbose_name="1 Номер"
    )
    number2 = models.CharField(
        max_length=100,
        verbose_name="2 Номер"
    ) 
    email = models.EmailField(
        verbose_name="Эл.Почта"
    )
    adress = models.CharField(
        max_length=255,
        verbose_name="Адрес"
    ) 
    send_button = models.CharField(
        max_length=55,
        verbose_name="Кнопка Отправить"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"    

class Footer(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Имя Компании"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Футер"