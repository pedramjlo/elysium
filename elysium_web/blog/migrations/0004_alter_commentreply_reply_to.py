# Generated by Django 5.0 on 2024-02-16 11:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_alter_comment_comment_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commentreply",
            name="reply_to",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="blog.comment",
            ),
        ),
    ]
