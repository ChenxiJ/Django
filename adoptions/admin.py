from django.contrib import admin


from .models import Pet

# this decorator is to register the PetAdmin with admin to tell 
# which model it is associated with
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
  list_display = ['name', 'species', 'breed', 'age', 'sex']
  