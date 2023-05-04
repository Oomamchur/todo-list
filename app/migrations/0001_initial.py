# Generated by Django 4.2.1 on 2023-05-04 12:39

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                ("datetime", models.DateTimeField(auto_now_add=True)),
                ("deadline", models.DateTimeField(blank=True, null=True)),
                ("is_done", models.BooleanField()),
                ("tags", models.ManyToManyField(related_name="tasks", to="app.tag")),
            ],
            options={
                "ordering": ["datetime"],
            },
        ),
    ]
