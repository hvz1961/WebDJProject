from .models import News_post
from django.forms import ModelForm, TextInput, Textarea, DateInput, TimeInput

class News_postForm(ModelForm):
	class Meta:
		model = News_post
		fields = ['title', 'short_description', 'text', 'author', 'pub_date', 'pub_time']
		widgets = {
			'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок новости'}),
			'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание новости'}),
			'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Содержание новости'}),
			'author': TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор'}),
			'pub_date': DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Дата публикации'}),
			'pub_time': TimeInput(attrs={'class': 'form-control', 'type': 'time', 'placeholder': 'Время публикации'}),
		}