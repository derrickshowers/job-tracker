from django.contrib import admin
from linkedin.models import LinkedInUser

# TODO: Show this under user, not its own thing
admin.site.register(LinkedInUser)