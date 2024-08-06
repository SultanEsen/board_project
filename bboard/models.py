from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.core import validators


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Product',
                             validators=[validators.RegexValidator(regex='^.{4,}')],
                             error_messages={'invalid': 'Wrong title of product'})
    content = models.TextField(null=True, blank=True, verbose_name='Description')
    price = models.FloatField(null=True, blank=True, verbose_name='Price')
    email = models.EmailField(null=True, blank=True, max_length=50, verbose_name='Email', validators=[validators.EmailValidator(
        message=None, code=None, allowlist=None)]
                              )

    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='When published')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Rubric',
                               related_name='entries',
                               # limit_choices_to={'name': 'Transport'}
                               )

    class Meta:
        verbose_name_plural = 'Announcements'
        verbose_name = 'Announcement'
        ordering = ['-published']
        unique_together = (
            'title', 'price'
        )
        # constraints = (
        #     models.CheckConstraint(check=models.Q(price_gte=0) & \
        #         models.Q(price_lte=1000000),
        #         name='bboard_rubric_price_constraints'),
        # )

    def __str__(self):
        return self.title

    class Kinds(models.IntegerChoices):
        BUY = 1, 'Buy'
        SELL = 2, 'Sell'
        EXCHANGE = 3, 'Exchange'
        RENT = 4

    kind = models.SmallIntegerField(choices=Kinds.choices, default=Kinds.SELL)

    def title_and_price(self):
        if self.price:
            # return '%s price is %.0f USD' % (self.title, self.price)
            return f'{self.title} is for {self.kind}, price is {self.price}'
        else:
            return self.title

    title_and_price.short_description = 'Название и цена'

    def clean(self):
        errors = {}
        if not self.content:
            errors['content'] = ValidationError('Укажите описание продаваемого товара')
        if self.price and self.price < 0:
            errors['price'] = ValidationError('Укажите неотрицательное значение цены')
        if errors:
            raise ValidationError(errors)


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Title')

    class Meta:
        verbose_name_plural = 'Rubrics'
        verbose_name = 'Rubric'
        ordering = ['name']
        unique_together = ['name']

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return 'bboard/%s' % self.pk


class AdvUser(models.Model):
    is_activated = models.BooleanField(default=True)
    users = models.OneToOneField(User, on_delete=models.CASCADE)


class Spare(models.Model):
    name = models.CharField(max_length=50)


class Machine(models.Model):
    name = models.CharField(max_length=30)
    spares = models.ManyToManyField(Spare)
