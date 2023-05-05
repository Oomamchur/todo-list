from django.test import TestCase
from django.urls import reverse

from app.models import Tag

TAG_URL = reverse("app:tag-list")


class TagTests(TestCase):
    def setUp(self) -> None:
        self.tag = Tag.objects.create(name="test")

    def test_tag_list(self) -> None:
        response = self.client.get(TAG_URL)
        tags = Tag.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["tag_list"]), list(tags))
        self.assertTemplateUsed(response, "app/tag_list.html")

    def test_create_tag(self) -> None:
        new_data = {"name": "Create"}
        response = self.client.post(reverse("app:tag-create"), new_data)
        tag = Tag.objects.get(name=new_data["name"])

        self.assertRedirects(response, TAG_URL)
        self.assertEqual(tag.name, new_data["name"])

    def test_update_tag_form(self) -> None:
        response = self.client.get(reverse(
            "app:tag-update",
            kwargs={"pk": self.tag.pk}
        ))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/tag_form.html")

    def test_update_tag(self) -> None:
        new_data = {"name": "Update"}
        response = self.client.post(
            reverse("app:tag-update", kwargs={"pk": self.tag.pk}),
            new_data
        )
        updated_tag = Tag.objects.get(pk=self.tag.pk)

        self.assertRedirects(response, TAG_URL)
        self.assertEqual(updated_tag.name, new_data["name"])
