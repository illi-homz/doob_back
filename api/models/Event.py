from django.db import models

class Event(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=200, blank=True, null=True, default=None)
    caption = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена', default=300)
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    photo = models.ImageField(verbose_name='Баннер (изображение)', blank=True, null=True, upload_to='events')
    video = models.FileField(verbose_name='Баннер (видео)', blank=True, null=True, upload_to='events')
    timestamp = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(verbose_name='Теги', max_length=200, blank=True, null=True, default=None, help_text='Через пробел')
    address = models.CharField(verbose_name='Адрес', max_length=200, blank=True, null=True, default='ул.Гвардейская 2, "Таксопарк"')
    is_complete = models.BooleanField(verbose_name='Состоялось', editable=False, default=False)
    message_id=models.SmallIntegerField(editable=False, default=0)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'