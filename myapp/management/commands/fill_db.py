# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from myapp.models import Vocabulary


class Command(BaseCommand):
    help = "Create some vocabularies in the DB."

    # Array with vocabularies arguments
    vocabularies = [u'Python', u'Redis', u'Frontend', u'Javascript',
                    u'bootstrap', u'programmer', u'developer', u'ajax', u'urllib',
                    u'parser', u'token', u'django']

    def handle(self, *args, **options):

        self.stdout.write(
            u'Function of automatic filling of the Database.')
        for word in self.vocabularies:
            vocabulary = Vocabulary(word=word)
            vocabulary.save()
            self.stdout.write(
                u'Objects %s create in database' % vocabulary)
