from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Product')
    content = models.TextField(null=True, blank=True, verbose_name='Description')
    price = models.FloatField(null=True, blank=True, verbose_name='Price')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='When published')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Rubric',
                               # limit_choices_to={'name': 'Transport'}
                               )

    class Meta:
        verbose_name_plural = 'Announcements'
        verbose_name = 'Announcement'
        ordering = ['-published']

    def __str__(self):
        return self.title

    class Kinds(models.IntegerChoices):
        BUY = 1, 'Buy',
        SELL = 2, 'Sell',
        EXCHANGE = 3, 'Exchange',
        RENT = 4

    kind = models.SmallIntegerField(choices=Kinds.choices, default=Kinds.SELL)



class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Title')

    class Meta:
        verbose_name_plural = 'Rubrics'
        verbose_name = 'Rubric'
        ordering = ['name']

    def __str__(self):
        return self.name
