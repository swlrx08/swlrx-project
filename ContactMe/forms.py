from django import forms
from ContactMe.models import ContactMe


class ContactFormModule(forms.ModelForm):
    class Meta:
        model = ContactMe
        fields = ['first_name', 'last_name', 'email', 'message']

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'your name...',
                'id': 'fname',
                'name': 'firtsname'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'your last name...',
                'id': 'lname',
                'name': 'lastsname'
            }),

            'email': forms.TextInput(attrs={
                'placeholder': 'example@gemail.com',
                'id': 'email',
                'name': 'email'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'your message for me...',
                'row': 5,
                'id': 'subject',
                'name': 'subject'
            })
        }

    error_messages = {
        'first_name': {
            'required': "نام شما اجباری میباشد.لطفا وارد کنید "
        },
        'last_name': {
            'required': "نام خانوادگی شما اجباری میباشد.لطفا وارد کنید "
        },

        'email': {
            'required': "ایمیل شما اجباری میباشد.لطفا وارد کنید "
        },
        'message': {
            'required': "پیامی نوشته نشده! لطفا پیامی را وارد کنید "
        }
    }
