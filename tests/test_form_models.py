from django.test import TestCase
from django.urls import reverse

from app.forms import TaskForm
from app.models import Tag, Task


class ModelsTests(TestCase):
    def test_tag_str(self) -> None:
        tag = Tag.objects.create(name="test")

        self.assertEquals(str(tag), tag.name)

    def test_task_str(self) -> None:
        task = Task.objects.create(content="test", is_done=False)

        self.assertEquals(str(task), task.content)


class FormsTest(TestCase):
    def setUp(self) -> None:
        self.tag = Tag.objects.create(name="test")

    def test_task_creation_form_is_valid(self) -> None:
        form_data = {
            "content": "Title",
            "is_done": True,
            "tags": [self.tag.id]
        }

        form = TaskForm(data=form_data)
        is_valid = form.is_valid()
        self.client.post(reverse("app:task-create"), data=form_data)
        new_task = Task.objects.get(content=form_data["content"])

        self.assertTrue(is_valid)
        self.assertEqual(new_task.content, form_data["content"])

    def test_task_creation_form_is_not_valid(self) -> None:
        form_data = {
            "is_done": True,
            "tags": [self.tag.id]
        }
        form = TaskForm(data=form_data)

        self.assertFalse(form.is_valid())
