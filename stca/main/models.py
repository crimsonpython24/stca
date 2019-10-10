from django.db import models

from random import randrange
# Create your models here.
class Carousel(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150, blank=True)
    text = models.CharField(max_length=300)
    btn_text = models.CharField(max_length=50)
    btn_link = models.CharField(max_length=300, blank=True)
    pub_date = models.DateTimeField('date published')
    num = randrange(5) + 82
    img_path = models.CharField(max_length=300, default=("https://mdbootstrap.com/img/Photos/Others/images/%s.jpg") % (num))

    def __str__(self):
        return self.title


class Notice(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=300)
    btn_text = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    btn_link = models.CharField(max_length=300, blank=True)
    align_types = (('left', 'left'), ('right', 'right'), ('center', 'middle'))
    align_type = models.CharField(max_length=10, choices=align_types)
    btn_types = ((' ', 'default'), ('btn-rounded', 'round'))
    btn_type = models.CharField(max_length = 20, choices=btn_types)
    btn_style = models.CharField(max_length=40, help_text="""For simplicity reasons, no defaults are assigned. Please visit https://mdbootstrap.com/docs/jquery/components/buttons/ for more information.""")
    hoveff_types = (('rgba-black-strong', 'strong'), ('rgba-black-light', 'light'),
                    ('rgba-black-slight', 'slight'), ('zoom', 'zoom'), (' ', 'none'))
    hov_eff = models.CharField(max_length=40, choices=hoveff_types)

    def __str__(self):
        return self.title