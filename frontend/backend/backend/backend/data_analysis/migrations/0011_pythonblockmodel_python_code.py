# Generated by Django 4.2.6 on 2023-10-30 18:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("data_analysis", "0010_rename_blockmodel_pythonblockmodel"),
    ]

    operations = [
        migrations.AddField(
            model_name="pythonblockmodel",
            name="python_code",
            field=models.TextField(null=True),
        ),
    ]