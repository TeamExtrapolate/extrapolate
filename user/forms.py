# Copyright 2018 Team Extrapolate Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from user.models import User
from django import forms


class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email")

    def clean_email(self):
        email = self.cleaned_data.get('email', None)
        if email:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError(
                    'A user with that email already exists.')
        return email
