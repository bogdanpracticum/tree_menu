from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.


class main_menu(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    url = models.CharField('Сcылка', max_length=255)
    position = models.PositiveIntegerField('Позиция', default=1)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',)

    class MPTTMeta:
        order_insertion_by = ['position']

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
