from django.db import models

class Films_post(models.Model):
	title = models.CharField('Название фильма', max_length=50)
	short_description = models.CharField('Краткое описание фильма', max_length=245)
	review = models.TextField('Отзыв о фильме')
	author = models.CharField('Автор', max_length=50)
	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Отзыв'
		verbose_name_plural = 'Отзывы'


# Create your models here.
