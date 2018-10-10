from django.shortcuts import render , redirect
from .models import Car
from .forms import CarForm
from django.contrib import messages

def car_list(request):
	cars = Car.objects.all()
	context = {
		"cars": cars,
	}
	return render(request, 'car_list.html', context)


def car_detail(request, car_id):
	car = Car.objects.get(id=car_id)
	context = {
		"car": car,
	}
	return render(request, 'car_detail.html', context)


def car_create(request):
	#Complete Me
	form = CarForm()
	if request.method == "POST":
		form = CarForm(request.POST, request.FILES or None)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, 'Car added successsfully')
			return redirect('car-list')
		messages.add_message(request,messages.ERROR, form.errors)
	context = {
	"form":form,
	}

	return render(request,'car_create.html',context)


def car_update(request, car_id):
	#Complete Me
	car_obj = Car.objects.get(id=car_id)
	form = CarForm(instance = car_obj)
	if request.method == "POST":
		form = CarForm(request.POST, request.FILES, instance = car_obj)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, 'Car updated successsfully')
			return redirect('car-list')
		messages.add_message(request,messages.ERROR, form.errors)
	context = {
		'form' : form,
		'car_obj' : car_obj,
	}
	return render(request, 'car_update.html', context)


def car_delete(request, car_id):
	#Complete Me
	car_obj= Car.objects.get(id = car_id).delete()
	messages.add_message(request, messages.SUCCESS, 'Car deleted successsfully')
	return redirect ('car-list')