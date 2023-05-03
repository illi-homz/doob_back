from django.db import models


class Banner(models.Model):
    title = models.CharField(max_length=50, default='')
    img = models.ImageField(upload_to='banners', verbose_name='Баннер')
    is_main = models.BooleanField(verbose_name='Главный баннер', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Главные баннеры'
        verbose_name_plural = 'Главные баннеры'