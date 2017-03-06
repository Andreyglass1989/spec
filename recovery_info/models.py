# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models

# Create your models here.

class OperatingSystem(models.Model):

    name = models.TextField  ( unique=True    )
    image = models.ImageField( upload_to='static/images/os' )

    def __unicode__(self):
        return self.name

    def image_img(self):
        if self.image:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url)
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True


class Device(models.Model):

    name = models.TextField( unique=True )
    os = models.ManyToManyField( OperatingSystem )
    image = models.ImageField(upload_to='static/images/devices')
    alt_image = models.TextField(null=False)

    def __unicode__(self):
        return self.name

    def image_img(self):
        if self.image:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url)
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True


class TypeDamage( models.Model ):

    name = models.TextField(unique=True)

    def __unicode__(self):
        return self.name


class File( models.Model ):

    name = models.TextField  ( unique=True    )
    image = models.ImageField( upload_to='static/images/' )
    typeFailure = models.ManyToManyField( TypeDamage )

    def __unicode__(self):
        return self.name

    def image_img(self):
        if self.image:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url)
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True

  #  def image_img(self):
   #     if self.image:
    #        return u'< img src="%s" width="100">' % self.image.url
     #   else:
      #      return '(none)'

    #image_img.short_description = 'Thumb'
    #image_img.allow_tags = True

 #   def img_add(self):
  #      return u'' % self.image.url

#    img_add.allow_tags = True


