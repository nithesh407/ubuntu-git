from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import AllCourses


def home(request):
    ac = AllCourses.objects.all()
    template = loader.get_template('Calc/Courses.html')
    context = {
        'ac': ac,
    }
    return HttpResponse(template.render(context, request))


def detail(request, course_id):
    course =get_object_or_404(AllCourses, pk=course_id)
    return render(request, 'Calc/detail.html', {'course': course})


def yourchoice(request, course_id):
    course = get_object_or_404(AllCourses, pk=course_id)
    try:
        selected_ct = course.details_set.get(pk=request.POST['choice'])
    except (KeyError, AllCourses.DoesNotExist):
        return render(request, 'Calc/detail.html', {
            'course': course,
            'error_message': "select a valid option"
        })
    else:
        selected_ct.your_choice=True
        selected_ct.save()
        return render(request, 'Calc/detail.html', {'course': course})
