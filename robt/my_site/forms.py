from .models import Review, Call
from django.forms import ModelForm, TextInput, Textarea


class ReviewForm(ModelForm):
	class Meta:
		model = Review
		fields = ['title', 'content']
		widgets = {
			'title': TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Введите ваше имя'
		}),

			'content': Textarea(attrs={
				'class': 'form-control',
				'placeholder': 'Напишите отзыв'
		}),
		}

class CallForm(ModelForm):
	class Meta:
		model = Call
		fields = ['name', 'number', 'message']
		widgets = {
			'name': TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Как вас зовут?'
		}),

			'number': TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Напишите ваш номер телефона'
		}),
			'message': Textarea(attrs={
				'class': 'form-control',
				'placeholder': 'Опишите вашу проблему (необязательно)'
			}),
		}

