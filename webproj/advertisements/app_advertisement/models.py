from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model

# Заголовок 
# Описание
# Цена
# Дата создания 
# Дата обновления 
# Торг

User = get_user_model()

# Create your models here.
class Advertisement(models.Model):
    title = models.CharField("заголовок", max_length=128)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=10,decimal_places=2)
    auction = models.BooleanField("торг", help_text='Торг')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField('image', upload_to='app_advertisement/')

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')

    

    def __str__(self):
        return f"Advertisements(id = {self.id}, title = {self.title}, price = {self.price})"

    class Meta:
        db_table = "advertisements"

    @admin.display(description='date')
    def cr_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.created_at.date() == timezone.now().date():
            created_time = self. created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span stile="color: green"; font=weight: bold;">Today a {}</span>', created_time

            )
    @admin.display(description='update')
    def up_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.updated_at.date() == timezone.now().date():
            up_time = self. updated_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span stile="color: green"; font=weight: bold;">Today a {}</span>', up_time

            )


