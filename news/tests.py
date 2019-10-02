import datetime

from django.test import TestCase

from .models import Editor, Article, tags

ed = Editor(id=1, first_name='James', last_name='Kamau', email='jk@gmail.com')


class EditorTestClass(TestCase):
    def setUp(self):
        self.James = Editor(id=1, first_name='James', last_name='Kamau', email='jk@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.James, Editor))

    def test_save_editor(self):
        before = Editor.objects.count()
        self.James.save_editor()
        after = Editor.objects.count()
        self.assertTrue(before < after)

    def test_editor_delete(self):
        self.James.delete_editor()
        self.assertTrue(len(Editor.objects.all()) < 1)

    def tearDown(self):
        Editor.objects.all().delete()


class TagsTestClass(TestCase):
    def setUp(self) -> None:
        self.tag = tags(id=1, name='code')

    def test_tag_instance(self):
        self.assertTrue(isinstance(self.tag, tags))

    def test_tag_save(self):
        before = tags.objects.count()
        self.tag.save_tag()
        after = tags.objects.count()
        self.assertTrue(before < after)

    def tearDown(self) -> None:
        tags.objects.all().delete()


class TestArticleClass(TestCase):
    def setUp(self):
        self.article = Article(title='Django the King of web',
                               post='Code is always awesome,but have you checked out django?',
                               pub_date=datetime.datetime.now()
                               )
        self.article.save()

        self.new_tag = tags(name='code')
        self.new_tag.save_tag()
        self.article.tags.add(self.new_tag)
        self.article.save()

        self.new_editor = Editor(first_name='vick', last_name='kamau', email='kamauvick@outlook.com')
        self.new_editor.save_editor()
        self.article.editor = self.new_editor
        self.article.save()

    def test_article_instance(self):
        self.assertTrue(isinstance(self.article, Article))

    def test_article_save(self):
        self.article.save_article()
        self.assertTrue(len(Article.objects.all()) > 0)

    def test_article_delete(self):
        before = Article.objects.count()
        self.article.delete_article()
        after = Article.objects.count()
        self.assertTrue(after < before)

    def test_get_news_by_date(self):
        test_date = '2019-10-01'
        date = datetime.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)

    def tearDown(self):
        Article.objects.all().delete()
