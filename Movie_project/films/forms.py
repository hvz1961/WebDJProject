from .models import Films_post
from django.forms import ModelForm, TextInput, Textarea

class Films_postForm(ModelForm):
	class Meta:
		model = Films_post
		fields = ['title', 'short_description', 'review', 'author']
		widgets = {
			'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
			'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание фильма'}),
			'review': Textarea(attrs={'class': 'form-control', 'placeholder': 'Отзыв'}),
			'author': TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор'}),
		}