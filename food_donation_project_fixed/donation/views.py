from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FoodReportForm
from .models import FoodReport, DeliveryPerson
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

@login_required
def report_food(request):
    if request.method == 'POST':
        form = FoodReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.donor = request.user
            delivery = DeliveryPerson.objects.first()
            report.delivery_person = delivery
            report.save()
            return redirect('food_detail', report_id=report.id)
    else:
        form = FoodReportForm()
    return render(request, 'report_food.html', {'form': form})

@login_required
def food_detail(request, report_id):
    report = FoodReport.objects.get(id=report_id)
    return render(request, 'food_detail.html', {'report': report})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('report_food')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
