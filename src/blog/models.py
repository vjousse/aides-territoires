from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from model_utils import Choices
from django_xworkflows import models as xwf_models


class BlogPostWorkflow(xwf_models.Workflow):
    """Defines statuses for Posts."""

    log_model = ''

    states = Choices(
        ('draft', 'Brouillon'),
        ('reviewable', 'En revue'),
        ('published', 'Publié'),
        ('deleted', 'Supprimé'),
    )
    initial_state = 'draft'
    transitions = (
        ('submit', 'draft', 'reviewable'),
        ('publish', 'reviewable', 'published'),
        ('unpublish', ('reviewable', 'published'), 'draft'),
    )


class BlogPostQuerySet(models.QuerySet):

    def published(self):
        """Only returns published objects."""

        return self.filter(status=BlogPostWorkflow.states.published.name)


class BlogPost(xwf_models.WorkflowEnabled, models.Model):

    title = models.CharField(
        _('Title'),
        max_length=256,
        db_index=True)
    slug = models.SlugField(
        _('Slug'),
        help_text=_('Let it empty so it will be autopopulated.'),
        blank=True)
    short_text = models.TextField(
        _('Short text'),
        help_text=_('A short, concise introduction'),
        max_length=256,
        null=True, blank=True)
    text = models.TextField(
        _('Full text of the post'),
        blank=False)

    category = models.ForeignKey(
        'BlogPostCategory',
        null=True, blank=True,
        verbose_name=_('Post category'),
        related_name='categories',
        on_delete=models.PROTECT)

    status = xwf_models.StateField(
        BlogPostWorkflow,
        verbose_name=_('Status'))

    # SEO
    meta_title = models.CharField(
        _('Meta title'),
        max_length=180,
        blank=True, default='',
        help_text=_('This will be displayed in SERPs. '
                    'Keep it under 60 characters. '
                    'Leave empty and we will reuse the post\'s title.'))
    meta_description = models.TextField(
        _('Meta description'),
        blank=True, default='',
        max_length=256,
        help_text=_('This will be displayed in SERPs. '
                    'Keep it under 120 characters.'))

    date_created = models.DateTimeField(
        _('Date created'),
        default=timezone.now)
    date_updated = models.DateTimeField(
        _('Date updated'),
        auto_now=True)
    date_published = models.DateTimeField(
        _('First publication date'),
        null=True, blank=True)

    class Meta:
        verbose_name = 'BlogPost'
        verbose_name_plural = 'BlogPosts'

    def __str__(self):
        return self.title

    def set_slug(self):
        """Set the object's slug if it is missing."""
        if not self.slug:
            self.slug = slugify(self.title)[:50]

    def save(self, *args, **kwargs):
        self.set_slug()
        return super().save(*args, **kwargs)

    def is_draft(self):
        return self.status == BlogPostWorkflow.states.draft

    def is_published(self):
        return self.status == BlogPostWorkflow.states.published

    def set_publication_date(self):
        if self.is_published() and self.date_published is None:
            self.date_published = timezone.now()


class BlogPostCategory(models.Model):

    name = models.CharField(
        _('Name'),
        max_length=256,
        db_index=True)
    slug = models.SlugField(
        _('Slug'),
        help_text=_('Let it empty so it will be autopopulated.'),
        blank=True)
    description = models.TextField(
        _('Description of the category'),
        blank=False)
    date_created = models.DateTimeField(
        _('Date created'),
        default=timezone.now)

    class Meta:
        verbose_name = 'BlogPostCategory'
        verbose_name_plural = 'BlogPostCategories'

    def __str__(self):
        return self.name

    def set_slug(self):
        """Set the object's slug if it is missing."""
        if not self.slug:
            self.slug = slugify(self.name)[:50]

    def save(self, *args, **kwargs):
        self.set_slug()
        return super().save(*args, **kwargs)
