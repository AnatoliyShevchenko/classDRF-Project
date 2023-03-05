from django.db import models

# Create your models here.
class Students(models.Model):
    """Students Model."""

    title = models.CharField(
        max_length=5,
        verbose_name='название группы'
    )
    capacity = models.SmallIntegerField(
        verbose_name='вместимость'
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'группа'
        verbose_name_plural = 'группы'

    def __str__(self) -> str:
        return self.title