from django.shortcuts import render, redirect
from django.db import IntegrityError
from .models import ContainerType, Location, Workflow, Routine, SortArea, Analyser, Analysis, AnalysisRecord
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib import messages
from .forms import ViewForm
from django.http import HttpResponse

def login_success(request):
    if request.user.groups.filter(name="Users").exists():
        return redirect(main)
    else:
        return redirect(main_auth)

def main_auth(request):
    return render(request, "base.html")

class MyError(ValueError):
    pass

class MyCodeError(ValueError):
    pass

class ErrorName(IntegrityError):
    pass

class ErrorCode(IntegrityError):
    pass

class ErrorSMA(IntegrityError):
    pass

def main(request):
    if request.user.groups.filter(name="Users").exists():
        if request.method == "POST":
            analysis = Analysis()
            analysis.analisys_name = request.POST.get("analisys_name")
            analysis.host_code = request.POST.get("host_code")
            analysis.sma_id = request.POST.get("sma_id")
            if analysis.sma_id == "":
                analysis.sma_id = None
            analysis.container_type_main_id = request.POST.get("container_type_main")
            analysis.container_type_tr_id = request.POST.get("container_type_tr")
            analysis.dead_volume = request.POST.get("dead_volume")
            if analysis.dead_volume == "":
                analysis.dead_volume = None
            analysis.test_volume = request.POST.get("test_volume")
            if analysis.test_volume == "":
                analysis.test_volume = None
            analysis.lih_flag = request.POST.get("lih_flag")
            if analysis.lih_flag == "on":
                analysis.lih_flag = True
            else:
                analysis.lih_flag = False
            analysis.analyzer_id = request.POST.get("analyzer")
            analysis.description = request.POST.get("description")
            try:
                if analysis.analisys_name == '':
                    raise MyError("Указано пустое имя")
                if Analysis.objects.filter(analisys_name = analysis.analisys_name).exists():
                    raise ErrorName("Повтор")
                if analysis.host_code == '':
                    raise MyCodeError("Указано пустое имя")
                if Analysis.objects.filter(host_code = analysis.host_code).exists():
                    raise ErrorCode("Повтор")
                if Analysis.objects.filter(sma_id = analysis.sma_id).exists() and analysis.sma_id != None:
                    raise ErrorSMA("Повтор")
                analysis.save()
                messages.success(request, f"Анализ {analysis.analisys_name} успешно добавлен")
                return HttpResponseRedirect("/main")
            except MyError:
                messages.error(request, 'Не заполнено наименование анализа')
            except ErrorName:
                messages.error(request, f"Анализ {analysis.analisys_name} уже существует")
            except MyCodeError:
                messages.error(request, 'Не внесен хост код для методики')
            except ErrorCode:
                code = Analysis.objects.get(host_code = analysis.host_code)
                test = code.analisys_name
                messages.error(request, f"Хост код {analysis.host_code} уже существует для методики {test}")
            except ErrorSMA:
                sma = Analysis.objects.get(sma_id = analysis.sma_id)
                test = sma.analisys_name
                messages.error(request, f"Номер SMA {analysis.sma_id} уже существует для методики {test}")
        container_types_main = ContainerType.objects.all()
        container_types_tr = ContainerType.objects.all()
        analyzers = Analyser.objects.all()
        dct = {"container_types_main": container_types_main, "container_types_tr": container_types_tr, "analyzers": analyzers}
        return render(request, "main.html", dct)
    else:
        return redirect(main_auth)

def edit_analysis(request, id):
    if request.user.groups.filter(name="Users").exists():
        try:
            analysis = Analysis.objects.get(id = id)
            if request.method == "POST":
                analysis.analisys_name = request.POST.get("analisys_name")
                analysis.host_code = request.POST.get("host_code")
                analysis.sma_id = request.POST.get("sma_id")
                if analysis.sma_id == "":
                    analysis.sma_id = None
                analysis.container_type_main_id = request.POST.get("container_type_main")
                analysis.container_type_tr_id = request.POST.get("container_type_tr")
                analysis.dead_volume = request.POST.get("dead_volume")
                if analysis.dead_volume == "":
                    analysis.dead_volume = None
                analysis.test_volume = request.POST.get("test_volume")
                if analysis.test_volume == "":
                    analysis.test_volume = None
                analysis.lih_flag = request.POST.get("lih_flag")
                if analysis.lih_flag == "on":
                    analysis.lih_flag = True
                else:
                    analysis.lih_flag = False
                analysis.analyzer_id = request.POST.get("analyzer")
                analysis.description = request.POST.get("description")
                try:
                    if analysis.analisys_name == '':
                        raise MyError("Указано пустое имя")
                    if Analysis.objects.filter(analisys_name=analysis.analisys_name).exists():
                        raise ErrorName("Повтор")
                    if analysis.host_code == '':
                        raise MyCodeError("Указано пустое имя")
                    if Analysis.objects.filter(host_code=analysis.host_code).exists():
                        raise ErrorCode("Повтор")
                    if Analysis.objects.filter(sma_id=analysis.sma_id).exists() and analysis.sma_id != None:
                        raise ErrorSMA("Повтор")
                    analysis.save()
                    messages.success(request, f"Анализ {analysis.analisys_name} успешно добавлен")
                    return HttpResponseRedirect("/main")
                except MyError:
                    messages.error(request, 'Не заполнено наименование анализа')
                except ErrorName:
                    messages.error(request, f"Анализ {analysis.analisys_name} уже существует")
                except MyCodeError:
                    messages.error(request, 'Не внесен хост код для методики')
                except ErrorCode:
                    code = Analysis.objects.get(host_code=analysis.host_code)
                    test = code.analisys_name
                    messages.error(request, f"Хост код {analysis.host_code} уже существует для методики {test}")
                except ErrorSMA:
                    sma = Analysis.objects.get(sma_id=analysis.sma_id)
                    test = sma.analisys_name
                    messages.error(request, f"Номер SMA {analysis.sma_id} уже существует для методики {test}")
            else:
                container_types_main = ContainerType.objects.all()
                container_types_tr = ContainerType.objects.all()
                analyzers = Analyser.objects.all()
                dct = {"container_types_main": container_types_main, "container_types_tr": container_types_tr, "analyzers": analyzers}
                return render(request, "main.html", dct)
        except Analysis.DoesNotExist:
            messages.error(request, "Значение не найдено")
            return HttpResponseRedirect("/main")
    else:
        return redirect(main_auth)


def del_analysis(request, id):
    try:
        analysis = Analysis.objects.get(id=id)
        analysis.delete()
        messages.success(request, f"Анализ {analysis.analisys_name} и все его привязки успешно удалены")
        return HttpResponseRedirect("/view")
    except Analysis.DoesNotExist:
        messages.error(request, "Значение не найдено")
        return HttpResponseRedirect("/view")

def create_analysis_record(request):
    if request.user.groups.filter(name="Users").exists():
        if request.method == "POST":
            analysis_record = AnalysisRecord()
            analysis_record.analysis_id = request.POST.get("analysis")
            analysis_record.location_id = request.POST.get("location")
            analysis_record.workflow_id = request.POST.get("workflow")
            analysis_record.sort_area_id = request.POST.get("sort_area")
            try:
                test = Analysis.objects.get(id = analysis_record.analysis_id)
                location = Location.objects.get(id = analysis_record.location_id)
                analysis_records = AnalysisRecord.objects.all()
                for i in analysis_records:
                    if str(i.analysis) == str(test.analisys_name) and str(i.location) == str(location.location):
                        raise ErrorName("Повтор")
                analysis_record.save()
                messages.success(request, f"Запись для методики {test.analisys_name} в локации {location.location} успешно добавлена")
                return HttpResponseRedirect("/create")
            except ErrorName:
                messages.error(request, f"Запись для методики {test.analisys_name} в локации {location.location} уже существует")
        analyzes = Analysis.objects.all()
        locations = Location.objects.all()
        workflows = Workflow.objects.all()
        sort_areas = SortArea.objects.all()
        dct = {"analyzes": analyzes, "locations": locations, "workflows": workflows, "sort_areas": sort_areas}
        return render(request, "create.html", dct)

    else:
        return redirect(main_auth)

def edit_analysis_record(request, id):
    pass


def del_analysis_record(request, id):
    try:
        analysis_record = AnalysisRecord.objects.get(id = id)
        analysis_record.delete()
        messages.success(request, "Привязка удалена")
        return HttpResponseRedirect("/view")
    except AnalysisRecord.DoesNotExist:
        messages.error(request, "Значение не найдено")
        return HttpResponseRedirect("/view")

def viewing(request):
    if request.user.groups.filter(name="Users").exists():
        if request.method == "POST":
            submitbutton = request.POST.get("submit")
            userform = ViewForm(request.POST or None)
            try:
                if userform.is_valid():
                    name = userform.cleaned_data.get("analisys_name")
                    test = Analysis.objects.get(analisys_name=str(name))
                    analysis_records = AnalysisRecord.objects.filter(analysis=test.id)
                    dct = {"form": userform, "test": test, "analysis_records": analysis_records, 'submitbutton': submitbutton}
                    return render(request, "view.html", dct)
                else:
                    return HttpResponse("Invalid data")
            except:
                messages.error(request, "Запись не найдена")
                return HttpResponseRedirect("/view")
        else:
            userform = ViewForm()
            return render(request, "view.html", {"form": userform})
    else:
        return redirect(main_auth)


def viewing_all(request):
    if request.user.groups.filter(name="Users").exists():
        analyzes = Analysis.objects.all().order_by("sma_id")
        search_workflow = request.GET.get("search_workflow")
        analysis_records = AnalysisRecord.objects.all()
        try:
            if search_workflow:
                wf = Workflow.objects.get(workflow=str(search_workflow))
                analysis_records = AnalysisRecord.objects.filter(workflow=wf.id)
            dct = {"analyzes": analyzes, "analysis_records": analysis_records}
            return render(request, "all.html", dct)
        except:
            messages.error(request, "Запись не найдена")
            return HttpResponseRedirect("/all")
    else:
        return redirect(main_auth)






