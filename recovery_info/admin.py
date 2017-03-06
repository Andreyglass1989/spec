from django.contrib import admin
from recovery_info.models import TypeDamage, File, OperatingSystem, Device
# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ('name','image', 'image_img' )

admin.site.register( Device, ImageAdmin          )
admin.site.register( OperatingSystem, ImageAdmin )
admin.site.register( File, ImageAdmin)
admin.site.register( TypeDamage      )