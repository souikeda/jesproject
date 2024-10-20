from django.contrib import admin
from .models import TMstCustomer

class TMstCustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'nameryaku', 'address1', 'telno')
    search_fields = ('user__email', 'nameryaku', 'telno')
    ordering = ('nameryaku',)

admin.site.register(TMstCustomer, TMstCustomerAdmin)
