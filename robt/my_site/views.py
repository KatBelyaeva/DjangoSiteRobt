from django.shortcuts import render, redirect
from .models import Blog, Review, Call
from .forms import ReviewForm, CallForm
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import CreateView

def index(request):
    return render(request, 'my_site/index.html')

def contact(request):
	if request.method == 'GET':
		form = CallForm()
		return render(request, 'my_site/contact.html', {'form': form})
	elif request.method == 'POST':
		form = CallForm(request.POST)
		if form.is_valid():
			call_name = form.cleaned_data['name']
			call_number = form.cleaned_data['number']
			call_message = form.cleaned_data['message']
			subject = f'Новая заявка на консультацию от {call_name}. Телефон отправитель: {call_number}. Текст: {call_message}.'
			try:
				send_mail('Новая заявка', subject, settings.EMAIL_HOST_USER, ['beliayeva85@mail.ru'])
				form.save()
				return redirect('contact')
			except:
				return redirect('contact')

def price(request):
    return render(request, 'my_site/price.html')

def review(request):
	if request.method == 'POST':
		form = ReviewForm(request.POST)
		if form.is_valid():
			form.save()
			review_name = form.cleaned_data['title']
			review_message = form.cleaned_data['content']
			subject = f'Новый отзыв от {review_name}: {review_message}.'
			send_mail('Новый отзыв', subject, settings.EMAIL_HOST_USER, ['beliayeva85@mail.ru'])
	all_form = Review.objects.all()
	new_form = ReviewForm()

	return render(request, 'my_site/review.html', {'new_form': new_form, 'all_form': all_form})

def my_blog(request):
	blog = Blog.objects.all()
	context = {'blog': blog}
	return render(request, 'my_site/blog.html', context)

class CallCreate(CreateView):
    model = Call
    form_class = CallForm






