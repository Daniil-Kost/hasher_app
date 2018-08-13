# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Vocabulary(models.Model):
    """Vocabulary Model"""

    class Meta(object):
        """docstring for Meta"""
        verbose_name = u"Vocabulary"
        verbose_name_plural = u"Vocabularies"

    word = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Word",
        default=None)

    def __unicode__(self):
        return u"%s" % self.word


class UserProfile(models.Model):
    """User Info Model"""

    # user mapping
    user = models.OneToOneField(User)

    class Meta(object):
        verbose_name = u"User Profile"
        verbose_name_plural = u"Users Profiles"

    # extra user data
    user_vocabulary = models.ManyToManyField(
        'Vocabulary',
        verbose_name="Vocabularies",
        blank=True)

    def __unicode__(self):
        return u"%s" % self.user.username


class UserInfo(models.Model):
    """To keep extra user data"""

    # user mapping
    user = models.OneToOneField(User)

    class Meta(object):
        verbose_name = u"User Information"
        verbose_name_plural = u"Users Informations"

    hashes = models.TextField(
        blank=True,
        verbose_name=u"Hashes")

    user_ip = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"IP address")

    user_browser = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"Browser")

    user_oc = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"OC")

    user_device = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"Device")

    user_timezone = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name=u"Timezone",
        default=None)

    user_country = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name=u"Country",
        default=None)

    user_city = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name=u"City",
        default=None)

    user_cookies = models.TextField(
        blank=True,
        null=True,
        verbose_name=u"Cookies",
        default=None)

    def __unicode__(self):
        return u"%s" % self.user.username


class Hashes(models.Model):
    """Hashes Model"""

    class Meta(object):
        verbose_name = u"Hash"
        verbose_name_plural = u"Hashes"

    # extra user data
    related_user = models.ForeignKey(
        'UserProfile',
        verbose_name=u"Related User",
        blank=False,
        on_delete=models.CASCADE,
        related_name='user_hashes')

    word = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Word",
        default=' ')

    hash_md5 = models.TextField(
        blank=True,
        verbose_name="Hashes_md5")

    hash_sha1 = models.TextField(
        blank=True,
        verbose_name="Hashes_sha1")

    hash_sha224 = models.TextField(
        blank=True,
        verbose_name="Hashes_sha224")

    hash_sha256 = models.TextField(
        blank=True,

        verbose_name="Hashes_sha256")

    hash_sha512 = models.TextField(
        blank=True,
        verbose_name="Hashes_sha512")

    file = models.FileField(upload_to='files/',
                            max_length=100)

    def __unicode__(self):
        return u"%s word: %s" % (self.related_user, self.word)
