from django.db import models
from ckeditor.fields import RichTextField


class Blog(models.Model):
	title = models.CharField('Заголовок', max_length=50)
	content = RichTextField('Описание')
	created = models.DateTimeField('Дата создания', auto_now_add=True)
	photo = models.ImageField('Фото', upload_to='photos/%y/%m/%d/', blank=True)
	published = models.BooleanField('Опубликовано', default=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'

class Review(models.Model):
	title = models.CharField('Имя', max_length=50)
	content = models.TextField('Отзыв', blank=True)

	def __str__(self):
		return self.title

class Call(models.Model):
	name = models.CharField('Имя', max_length=50)
	number = models.CharField('Номер телефона', max_length=17)
	message = models.TextField('Сообщение', blank=True)

	def __str__(self):
		return self.number

	class Meta:
		verbose_name = 'Заявка'
		verbose_name_plural = 'Заявки'







