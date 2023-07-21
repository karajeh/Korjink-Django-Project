# Generated by Django 4.2.1 on 2023-06-11 12:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0006_post_image_alter_comment_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="status",
            field=models.CharField(
                choices=[("draft", "Draft"), ("active", "Active")],
                default="active",
                max_length=10,
            ),
        ),
    ]
