import datetime

from django.db import models


# Create your models here.

class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)

    def save_editor(self):
        self.save()

    def delete_editor(self):
        self.delete()

    def __repr__(self):
        return f'Editor name: {self.first_name}'

    def __str__(self):
        return f'Editor name: {self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name']
        db_table = 'news_editors'


class tags(models.Model):
    name = models.CharField(max_length=30)

    def save_tag(self):
        self.save()

    def delete_tag(self):
        self.delete()

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Tag name: {self.name}'

    class Meta:
        db_table = 'news_tags'


class Article(models.Model):

    title = models.CharField(max_length=25, default='title')
    post = models.TextField(blank=True)
    editor = models.ForeignKey(Editor, null=True)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField()
    article_image = models.ImageField(upload_to='articles/', blank=True)

    def __repr__(self):
        return f'''
                Title: {self.title}
                Post: {self.post}
                '''

    def save_article(self):
        self.save()

    def delete_article(self):
        self.delete()

    @classmethod
    def query(cls):
        articles = Article.objects.all()
        return articles

    @classmethod
    def todays_news(cls):
        todays_date = datetime.date.today()
        news = cls.objects.filter(pub_date__date=todays_date)
        return news

    @classmethod
    def days_news(cls, date):
        news = cls.objects.filter(pub_date__date = date)
        return news

    @classmethod
    def search(cls, search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news

    class Meta:
        db_table = 'news_articles'
        ordering = ['-pub_date']
