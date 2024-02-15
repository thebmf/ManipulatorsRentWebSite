from django.shortcuts import render
from django.views import generic
from .models import RequestManipulator
from .forms import RequestManipulatorForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class IndexView(SuccessMessageMixin, generic.CreateView):
    model = RequestManipulator
    form_class = RequestManipulatorForm
    template_name = "index.html"
    success_message = "Ваша заявка успешно отправлена!"


# def index(request):
#     return render(request, 'index.html')
