# from django.contrib import admin
# from .models import Info, Navigation

# # Register your models here.
# @admin.register(Info)
# class InfoAdmin(admin.ModelAdmin):
#     list_display = ('name', 'phone')
#     list_editable = ('phone',)

# @admin.register(Navigation)
# class NavigationAdmin(admin.ModelAdmin):
#     list_display = ('home', 'about', 'projects', 'services', 'contacts')
    
from django.contrib import admin
from .models import Info, Navigation, MainProjects, About, OurProjects, OurServices, Contacts, Footer

@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'vertical_text')

@admin.register(Navigation)
class NavigationAdmin(admin.ModelAdmin):
    list_display = ('home', 'about', 'projects', 'services', 'contacts', 'previous_button', 'next_button', 'look_more_button')
    list_editable = ('about', 'projects', 'services', 'contacts', 'previous_button', 'next_button', 'look_more_button')
    list_display_links = ('home',)

@admin.register(MainProjects)
class MainProjectsAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'project_desription')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'citate', 'description',)

@admin.register(OurProjects)
class OurProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_name', 'vertical_line')

@admin.register(OurServices)
class OurServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'years', 'years_title1', 'years_title2')
    

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('title', 'number1', 'number2', 'email', 'adress', 'send_button')

@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('name',)