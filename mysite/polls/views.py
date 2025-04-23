from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Question

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', {'questions': latest_questions})
