# Generated by Django 4.2 on 2023-04-25 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "Form_Fornos",
            "0003_inserteddata_comp_quimica_inserteddata_densidade_esp_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="inserteddata",
            name="TEMP_VAZ_ESPECIFICADO",
            field=models.IntegerField(default=0),
        ),
    ]