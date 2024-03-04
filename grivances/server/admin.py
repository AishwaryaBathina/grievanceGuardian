from django.contrib import admin

from .models import StudentModel
admin.site.register(StudentModel)

from .models import ComplaintModel
admin.site.register(ComplaintModel)

from .models import FacultyModel
admin.site.register(FacultyModel)

from .models import phoneModel
admin.site.register(phoneModel)

from .models import UsersModel
admin.site.register(UsersModel)