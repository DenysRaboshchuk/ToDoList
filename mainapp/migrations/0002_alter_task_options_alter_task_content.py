# Generated by Django 4.2.7 on 2023-11-09 09:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ("task_done", "datetime_field")},
        ),
        migrations.AlterField(
            model_name="task",
            name="content",
            field=models.CharField(max_length=255),
        ),
    ]
