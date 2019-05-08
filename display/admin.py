from django.contrib import admin

# Register your models here.

from .models import Plane, Pilot
# , TransactionLog, FlightTransactionTable
# Register your models here.

admin.site.register(Plane)
admin.site.register(Pilot)
