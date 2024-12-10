from django.test import TestCase
from django.urls import reverse
from . models import TodoList
from . form import TodoListForm
from .views import completedTodo, addTodoItem

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

        #check if all tasks are included in the context
        self.assertQuerySetEqual(
            response.context['todo_tasks'],
            TodoList.objects.order_by('id'),
            transform=lambda x:x,
        )
        self.assertIsInstance(response.context['form'], TodoListForm)

    #test adding a valid todo item
    def test_add_todo_item_view_valid_data(self):
        response = self.client.post(reverse(addTodoItem), {'text':'Task 3'})
        self.assertEqual(response.status_code, 302)

        #verify the new task was added
        self.assertEqual(TodoList.objects.count(), 3)
        self.assertTrue(TodoList.objects.filter(text="Task 3").exists())

    #test marking a valid todo item as completed
    def test_completed_todo_valid(self):
        response = self.client.post(reverse(completedTodo, args =[self.task1.id]))
        self.assertEqual(response.status_code, 302)
        self.task1.refresh_from_db()
        self.assertTrue(self.task1.completed)