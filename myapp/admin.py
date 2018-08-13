# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

# Register your models here.
admin.site.register(Vocabulary)
admin.site.register(UserProfile)
admin.site.register(Hashes)
admin.site.register(UserInfo)