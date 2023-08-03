from django.db import models
from django.contrib import admin

# Заголовок 
# Описание
# Цена
# Дата создания 
# Дата обновления 
# Торг

# Create your models here.
class Advertisement(models.Model):
    title = models.CharField("заголовок", max_length=128)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=10,decimal_places=2)
    auction = models.BooleanField("торг", help_text='Торг')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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


