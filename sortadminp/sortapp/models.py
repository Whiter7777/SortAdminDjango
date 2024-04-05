from django.db import models

class ContainerType(models.Model):
    container_type = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.container_type

class Location(models.Model):
    location = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.location

class Workflow(models.Model):
    workflow = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=50, blank=True)
    location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.workflow

class Routine(models.Model):
    routine_name = models.CharField(max_length=50, unique=True)
    location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.routine_name

class SortArea(models.Model):
    sort_area = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=50, blank=True)
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)

    def __str__(self):
        return self.sort_area


class Analyser(models.Model):
    analyser_name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.analyser_name

class Analysis(models.Model):
    sma_id = models.PositiveIntegerField(unique=True, blank=True, null=True, default="Null")
    analisys_name = models.CharField(max_length=50, unique=True)
    host_code = models.CharField(max_length=10, unique=True)
    container_type_main = models.ForeignKey(ContainerType, null=True, on_delete=models.SET_NULL, related_name="main")
    container_type_tr = models.ForeignKey(ContainerType, null=True, on_delete=models.SET_NULL, related_name="transport")
    # workflow = models.ManyToManyField(Workflow, through="Analysis_Workflow")
    # sortarea = models.ManyToManyField(SortArea, through="Analysis_SortArea")
    dead_volume = models.PositiveSmallIntegerField(blank=True, null=True)
    test_volume = models.PositiveSmallIntegerField(blank=True, null=True)
    lih_flag = models.BooleanField(default=False)
    analyzer = models.ForeignKey(Analyser, null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.analisys_name

# class Analysis_Workflow(models.Model):
#     analisys_name = models.ForeignKey(Analysis, on_delete=models.CASCADE())
#     workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE())
#
# class Analysis_SortArea(models.Model):
#     analisys_name = models.ForeignKey(Analysis, on_delete=models.CASCADE())
#     sortarea = models.ForeignKey(SortArea, on_delete=models.CASCADE())

class AnalysisRecord(models.Model):
    analysis = models.ForeignKey(Analysis, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)
    workflow = models.ForeignKey(Workflow, null=True, on_delete=models.SET_NULL)
    sort_area = models.ForeignKey(SortArea, null=True, on_delete=models.SET_NULL)



