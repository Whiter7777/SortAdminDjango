from django.contrib import admin
from .models import ContainerType, Location, Workflow, Routine, SortArea, Analyser, Analysis, AnalysisRecord

# Register your models here.

admin.site.register(ContainerType)
admin.site.register(Location)
admin.site.register(Workflow)
admin.site.register(Routine)
admin.site.register(SortArea)
admin.site.register(Analyser)
admin.site.register(Analysis)
admin.site.register(AnalysisRecord)

