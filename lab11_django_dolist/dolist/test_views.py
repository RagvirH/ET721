from django.test import TestCase
from django.urls import reverse
from . models import TodoList
from . form import TodoListForm, completedTodo

class TodoViewsTestCase(TestCase):
    def setUp(self):
        # create initial data for testing
        self.task1 = TodoList.objects.create(text="Task 1", completed = False)
        self.task2 = TodoList.objects.create(text="Task 2", completed = False)
        self.task3 = TodoList.objects.create(text="Task 3", completed = True)

        #test the index view renders the correct context and template

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')