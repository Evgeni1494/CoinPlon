from distutils.errors import LinkError
from operator import truediv
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel,PageChooserPanel
# import du FieldPanel.
from wagtail.models import Page


class HomePage(Page):
    lead_text = models.CharField(
        max_length = 140, # longuer max
        blank = True, # autorisation de laisser le champ vide
        help_text = "sous-titre sous la bannière" # text d'aide ou tooltip.
    )   # donner un nom au champ et un sous-titre

    button = models.ForeignKey(
        'wagtailcore.Page',
        blank = True,
        null = True,
        related_name="+",
        help_text = "selectionner une page a Linker",
        on_delete = models.SET_NULL
    )# ajouter un bouton

    button_text = models.CharField(
        max_length =50,
        default = "Read More",
        blank = True,
        help_text ="bouton pour le texte"
    ) # Ajouter un bouton pour mettre du text.

    banner_background_image = models.ForeignKey(
        'wagtailimages.Image',
        blank = False,
        null= True,
        related_name = "+",
        help_text="banniere arriere plan",
        on_delete = models.SET_NULL

    ) # Ajouter la possibilité de mettre une image de fond
    content_panels = Page.content_panels + [
        FieldPanel("lead_text"),
        PageChooserPanel("button"),
        FieldPanel("button_text"),
        FieldPanel("banner_background_image")
        
    ]
        # permet d'exposer notre champ lead text.
        # !!! RESPECTER LES TABULATIONS !!!

