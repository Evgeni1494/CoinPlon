# Generated by Django 4.1.2 on 2022-10-10 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0077_alter_revision_user'),
        ('wagtailimages', '0024_index_image_file_hash'),
        ('home', '0003_homepage_lead_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner_background_image',
            field=models.ForeignKey(blank=True, help_text='bannière arrière plan', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='button',
            field=models.ForeignKey(blank=True, help_text='Sélectionner une page à linker', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='button_text',
            field=models.CharField(default='Read More', help_text='Bouton pour le texte', max_length=50),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='lead_text',
            field=models.CharField(blank=True, help_text='Sous-titre sous la bannière', max_length=140),
        ),
    ]
