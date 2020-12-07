from os.path import splitext

from django.db import models
from django.utils.translation import ugettext_lazy as _


def logo_upload_to(instance, filename):
    """Rename uploaded files with the object's slug."""
    _, extension = splitext(filename)
    name = instance.slug
    filename = 'programs/{}_logo{}'.format(name, extension)
    return filename


class Program(models.Model):
    """Represents a single aid program.

    Real-life examples of such programs:
      - Territoires d'Industrie
      - Action Cœur de Ville

    Aid programs regroup new or existing aids, and generally
    are limited to a specific perimeter.
    """

    name = models.CharField(
        _('Name'),
        max_length=256)
    slug = models.SlugField(
        _('Slug'))
    logo = models.FileField(
        _('Logo'),
        null=True, blank=True,
        upload_to=logo_upload_to,
        help_text=_('Make sure the file is not too heavy. Prefer svg files.'))
    short_description = models.CharField(
        _('Short description'),
        help_text=_('Will only appear in search results. 300 chars. max.'),
        max_length=300)
    description = models.TextField(
        _('Description'))

    class Meta:
        verbose_name = _('Aid program')
        verbose_name_plural = _('Aid programs')

    def __str__(self):
        return self.name
