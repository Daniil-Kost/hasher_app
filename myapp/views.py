# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import UpdateView
from django.forms import ModelForm
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper
from django.core.urlresolvers import reverse
from crispy_forms.bootstrap import FormActions
from django.http import HttpResponseRedirect
import hashlib
import json
import os
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.core.files import File
from .util import get_user_info, WORDS, write_to_json
from models import *


# Create your views here.
def main(request):
    data = get_user_info(request)
    hashes = None
    if request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
        except ObjectDoesNotExist:
            user_profile = UserProfile(user=request.user)
            user_profile.save()
            user_info = UserInfo(
                user=request.user,
                user_ip=data["ip"],
                user_browser=data["browser"],
                user_oc=data["oc"],
                user_device=data["device"],
                user_timezone=data["timezone"],
                user_country=data["country"],
                user_city=data["city"],
                user_cookies=data["cookies"]
            )
            user_info.save()

        if len(user_profile.user_vocabulary.all()) > 0:
            for vocabulary in user_profile.user_vocabulary.all():
                if vocabulary.word not in WORDS:
                    md5 = hashlib.md5(vocabulary.word)
                    sha1 = hashlib.sha1(vocabulary.word)
                    sha224 = hashlib.sha224(vocabulary.word)
                    sha256 = hashlib.sha256(vocabulary.word)
                    sha512 = hashlib.sha512(vocabulary.word)
                    my_file = json.dumps(
                        {
                         'word': vocabulary.word,
                         'md5': md5.hexdigest(),
                         'sha1': sha1.hexdigest(),
                         'sha224': sha224.hexdigest(),
                         'sha256': sha256.hexdigest(),
                         'sha512': sha512.hexdigest()})
                    f = write_to_json(my_file)
                    local_file = open(f)
                    my_hash = Hashes(
                        related_user=user_profile,
                        word=vocabulary.word,
                        hash_md5=md5.hexdigest(),
                        hash_sha1=sha1.hexdigest(),
                        hash_sha224=sha224.hexdigest(),
                        hash_sha256=sha256.hexdigest(),
                        hash_sha512=sha512.hexdigest(),
                        file=File(local_file)
                    )
                    my_hash.file.name = my_hash.file.name.replace(os.path.abspath(os.curdir) + '/media/', '')
                    my_hash.save()
                    user_info = UserInfo.objects.get(user=request.user)
                    curr_user = UserProfile.objects.get(user=request.user)
                    words_and_hashes = {}
                    for v in curr_user.user_vocabulary.all():
                        h = Hashes.objects.all()[0]
                        words_and_hashes['{}'.format(v.word)] = {
                                         'md5': h.hash_md5,
                                         'sha1': h.hash_sha1,
                                         'sha224': h.hash_sha224,
                                         'sha256': h.hash_sha256,
                                         'sha512': h.hash_sha512}
                    user_info.hashes = words_and_hashes
                    user_info.save()
                    if vocabulary.word not in WORDS:
                        WORDS.append(vocabulary.word)
                else:
                    pass
        hashes = Hashes.objects.filter(related_user=user_profile)
        data = serializers.serialize("xml", UserInfo.objects.all())
    file_path = os.path.abspath(os.curdir) + '/media/files/info.xml'
    path = 'files/info.xml'
    with open(file_path, 'w') as fp:
        try:
            fp.write(data)
        except TypeError:
            pass
    return render(request, 'index.html', {'hashes': hashes, 'path': path})


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile

        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # set from tag attributes
        self.helper.form_action = reverse('profile', kwargs={'pk': kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-4 control label'
        self.helper.field_class = 'col-sm-8'

        # add buttons
        self.helper.layout.append(FormActions(
            Submit('add_button', u'Save',
                   css_class="btn save btn-primary"),
            Submit('cancel_button', u'Cancel',
                   css_class="btn cancel btn-danger"), ))


class UserProfileView(UpdateView):
    """docstring for GroupUpdateView"""
    model = UserProfile
    template_name = 'form_user.html'

    exclude = ("user",)

    form_class = UserProfileForm

    success_url = '/'

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(reverse(
                'home'))
        else:
            return super(
                UserProfileView, self).post(request, *args, **kwargs)



