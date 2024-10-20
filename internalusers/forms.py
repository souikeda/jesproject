from django import forms
from .models import User

class InternalUserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not User.objects.filter(name=name, user_type=2).exists():
            raise forms.ValidationError("このNameは内部ユーザとして登録されていません。")
        return name
