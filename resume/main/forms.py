from django import forms
from . models import Contact, Conversation


class ContactForm(forms.ModelForm):

    name = forms.CharField(max_length=100, required=True,
                           widget=forms.TextInput(attrs={
                               'placeholder': 'Full name..',
                               'class': 'form-control',
                           }))
    
    email = forms.EmailField(max_length=100, required=True,
                             widget=forms.EmailInput(attrs={
                                 'placeholder': 'Email address..',
                                 'class': 'form-control',
                                 }))
    
    message = forms.CharField(max_length=1000, required=True,
                              widget=forms.Textarea(attrs={
                                  'placeholder': 'Message..',
                                  'class': 'form-control',
                                  'rows': 6
                                  }))

    class Meta:
        model = Contact
        fields = ('name', 'email', 'message',)



class ChatForm(forms.Form):
    body = forms.CharField(
        max_length=300,
        widget=forms.TextInput(attrs={
            'placeholder': 'Type your message here...',
            'class': 'form-control p-3 text-dark',
            'autocomplete': 'on',
            'autofocus': 'on',
            'id': 'chat_message'
        })
    )