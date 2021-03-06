# Generated by Django 3.1.7 on 2021-05-07 11:26

from django.db import migrations


def delete_records(apps, schema_editor):
    core_models = apps.get_app_config("core").get_models()
    for model in core_models:
        model.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(delete_records),
        migrations.AlterUniqueTogether(
            name="sfibersstackcalibratorpar",
            unique_together={("version", "valid_from")},
        ),
        migrations.AlterUniqueTogether(
            name="sfibersstackddlookuptable",
            unique_together={("version", "valid_from")},
        ),
        migrations.AlterUniqueTogether(
            name="sfibersstackddunpackerpar",
            unique_together={("version", "valid_from")},
        ),
        migrations.AlterUniqueTogether(
            name="sfibersstackdigitizerpar",
            unique_together={("version", "valid_from")},
        ),
        migrations.AlterUniqueTogether(
            name="sfibersstackgeompar",
            unique_together={("version", "valid_from")},
        ),
        migrations.AlterUniqueTogether(
            name="sfibersstackhitfinderfiberpar",
            unique_together={("version", "valid_from")},
        ),
        migrations.AlterUniqueTogether(
            name="sfibersstackhitfinderpar",
            unique_together={("version", "valid_from")},
        ),
    ]
