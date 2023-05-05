from django.test import TestCase
from django.urls import reverse

from app.models import Tag, Task

TASK_URL = reverse("app:index")


class TaskTests(TestCase):
    def setUp(self) -> None:
        self.tag = Tag.objects.create(name="test")
        self.task = Task.objects.create(content="test", is_done=False)

    def test_task_list(self) -> None:
        response = self.client.get(TASK_URL)
        tasks = Task.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["task_list"]), list(tasks))
        self.assertTemplateUsed(response, "app/index.html")

    def test_create_task(self) -> None:
        new_data = {
            "content": "Create",
            "is_done": False,
            "tags": [self.tag.id]
        }
        response = self.client.post(reverse("app:task-create"), new_data)
        task = Task.objects.get(content=new_data["content"])

        self.assertRedirects(response, TASK_URL)
        self.assertEqual(task.content, new_data["content"])

    def test_update_task_form(self) -> None:
        response = self.client.get(reverse(
            "app:task-update",
            kwargs={"pk": self.task.pk}
        ))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/task_form.html")

    def test_update_task(self) -> None:
        new_data = {
            "content": "Update",
            "is_done": True,
            "tags": [self.tag.id]
        }
        response = self.client.post(
            reverse("app:task-update", kwargs={"pk": self.task.pk}),
            new_data
        )
        updated_task = Task.objects.get(pk=self.task.pk)

        self.assertRedirects(response, TASK_URL)
        self.assertEqual(updated_task.content, new_data["content"])
        self.assertEqual(updated_task.is_done, new_data["is_done"])
