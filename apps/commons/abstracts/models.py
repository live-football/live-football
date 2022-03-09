from .choices import ADDRESS_TYPE
from .choices import PUBLISHED_STATE
from .choices import THAI_PROVICE
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import F
from django.db.models import Max
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from uuid import uuid4


class AbstractOrdering(models.Model):
    sequence = models.IntegerField(
        editable=False,
        db_index=True,
        null=True,
        verbose_name=_('Sequnce')
    )

    class Meta:
        abstract = True

    def get_ordering_queryset(self):
        raise NotImplementedError(_("Unknown ordering queryset"))

    def get_max_sequence(self, qs):
        existing_max = qs.aggregate(Max("sequence"))
        existing_max = existing_max.get("sequence__max")
        return existing_max

    def save(self, *args, **kwargs):
        if self.pk is None:
            qs = self.get_ordering_queryset()
            existing_max = self.get_max_sequence(qs)
            self.sequence = 0 if existing_max is None else existing_max + 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.sequence is not None:
            qs = self.get_ordering_queryset()
            qs.filter(sequence__gt=self.sequence).update(
                sequence=F("sequence") - 1
            )
        super().delete(*args, **kwargs)


class AbstractToken(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)

    class Meta:
        abstract = True


class AbstractPublishState(models.Model):
    publish_state = models.CharField(
        max_length=20,
        choices=PUBLISHED_STATE,
        default=PUBLISHED_STATE.DRAFT,
        verbose_name=_("Publish State")
    )
    published_at = models.DateTimeField(null=True, blank=True, verbose_name=_("Published at"))

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.publish_state == PUBLISHED_STATE.PUBLISHED:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)


class AbstractExpirable(models.Model):
    expiration_date = models.DateField(null=True, blank=True, verbose_name=_("Expiration Date"))

    class Meta:
        abstract = True


class AbstractUTM(models.Model):
    """
        UTM (https://ga-dev-tools.appspot.com/campaign-url-builder/)
    """

    utm_source = models.CharField(
        max_length=255,
        default="opendurian",
        help_text=_("Use utm_source to identify a search engine, newsletter name, or other source. Example: google, newsletter"),
        verbose_name=_("UTM Source")
    )
    utm_medium = models.CharField(
        max_length=255,
        help_text=_("Use utm_medium to identify a medium such as email or cost-per- click. Example: cpc, banner, email"),
        verbose_name=_("UTM Medium")
    )
    utm_campaign = models.CharField(
        max_length=255,
        help_text=_("Used for keyword analysis. Use utm_campaign to identify a specific product promotion or strategic campaign. Example: utm_campaign=spring_sale"),
        verbose_name=_("UTM Campaign")
    )
    utm_term = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Used for paid search. Use utm_term to note the keywords for this ad."),
        verbose_name=_("UTM Term")
    )
    utm_content = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Used for A/B testing and content-targeted ads. Use utm_content to differentiate ads or links that point to the same URL. Examples: logolink or textlink"),
        verbose_name=_("UTM Content")
    )

    class Meta:
        abstract = True


class AbstractLinkable(models.Model):
    web_url = models.URLField(blank=True, verbose_name=_("Web URL"))

    class Meta:
        abstract = True


class AbstractEnable(models.Model):
    enable = models.BooleanField(default=True, verbose_name=_("Enable"))

    class Meta:
        abstract = True


class AbstractExternalAds(models.Model):
    enable_external_ads = models.BooleanField(default=True, verbose_name=_("Enable External Ads"))

    class Meta:
        abstract = True


class AbstractAddress(models.Model):
    address_name = models.CharField(max_length=255, verbose_name=_("Callin Address Name"))
    address_type = models.CharField(
        max_length=50,
        choices=ADDRESS_TYPE,
        default=ADDRESS_TYPE.DEFAULT_ADDRESS,
        verbose_name=_("Address Type")
    )
    street = models.TextField(blank=True, verbose_name=_("Street"))
    province = models.IntegerField(
        choices=THAI_PROVICE,
        default=THAI_PROVICE.BANGKOK,
        verbose_name=_("Province")
    )
    zipcode = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(10000),
            MaxValueValidator(99999)
        ],
        verbose_name=_("Zipcode")
    )

    class Meta:
        abstract = True


class AbstractContact(models.Model):
    email_contact = models.EmailField(null=True, blank=True, verbose_name=_("Email Contact"))
    telephone_contact = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name=_("Telephone Contact")
    )

    class Meta:
        abstract = True


class AbstractSEO(models.Model):

    # title_seo = models.CharField(u"SEO Title", max_length=70, unique=True)
    # seo_description = models.CharField(u"SEO Description", max_length=255, null=True, blank=True)
    # seo_keywords = models.CharField(u"SEO Keywords", max_length=255, null=True, blank=True)

    class Meta:
        abstract = True
