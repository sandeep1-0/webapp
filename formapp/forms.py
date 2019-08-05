from django import forms
import re

#form classes
#form.Form
#form.ModelForm

class UserProfileForm(forms.Form):


    cn=(
        ('', '--select option--'),
        ('sbc', 'Banglore'),
        ('chn', 'Chennai'),
        ('hyd', 'Hyderabad'),
        ('myr', 'Mysore')

    )

    city=forms.ChoiceField(choices=cn)
    city2=forms.ChoiceField(choices=cn, widget=forms.RadioSelect)


    is_active=forms.BooleanField()


    username=forms.CharField(
        required=True,
        min_length=6,
        max_length=20,
        label="Name",
        help_text="Please enter atleast 8 characters",
        error_messages={
            "required":"This field cannot be blank",
            "min_length":"Enter minimum of 6 characters"
        },
        widget=forms.TextInput(attrs={
            'placeholder':'Enter name...'
        })

    )
    email=forms.EmailField(
        widget=forms.TextInput(attrs={
            'placeholder' : 'Enter email...'
    }))

    address=forms.CharField(
        widget=forms.Textarea
        )
    password=forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder':'required min 8'
        }),
        help_text="should be a combination of letters and numbers",
    )
    def clean(self):

        def check_name(formInput):
            res = re.findall('[^A-Z^a-z]',formInput)
            return res
        def check_email(formInput) :
            res1=re.findall('^[A-Za-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$',formInput)
            return res1

        formInput=self.cleaned_data
        if 'username' in formInput and check_name(formInput['username'])!=[]:
            self.errors['username'] = ['Enter a valid name']

        if 'email' in formInput and check_email(formInput['email'])==[]:
            self.errors['email']=["Not a valid email address!"]

        return formInput