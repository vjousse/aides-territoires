from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Project(models.Model):

    name = models.CharField(
        _('Name'),
        max_length=256,
        db_index=True)
    slug = models.SlugField(
        _('Slug'),
        help_text=_('Let it empty so it will be autopopulated.'),
        blank=True)
    description = models.TextField(
        _('Full description of the project'),
        default='', blank=True)
    categories = models.ManyToManyField(
        'categories.Category',
        verbose_name=_('Categories'),
        related_name='projects',
        blank=True)

    is_suggested = models.BooleanField(
        _('Is a suggested project?'),
        default=False,
        help_text=_(
            'If the project is suggested by a user'))

    date_created = models.DateTimeField(
        _('Date created'),
        default=timezone.now)

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self):
        return self.name

    def set_slug(self):
        """Set the object's slug if it is missing."""
        if not self.slug:
            self.slug = slugify(self.name)[:50]

    def save(self, *args, **kwargs):
        self.set_slug()
        return super().save(*args, **kwargs)