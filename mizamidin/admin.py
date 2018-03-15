from django.contrib import admin

from .models import Seller, Type, Car, MarkInstance

#admin.site.register(Car)
#admin.site.register(Seller)
admin.site.register(Type)
#admin.site.register(MarkInstance)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'phone','email')
    fields = ['first_name', 'last_name', ('date_of_birth','phone','email')]

admin.site.register(Seller, SellerAdmin)
class CarsInstanceInline(admin.TabularInline):
    model = MarkInstance
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_title', 'seller', 'display_type')
    inlines = [CarsInstanceInline]

@admin.register(MarkInstance) 
class MarkInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('car','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )