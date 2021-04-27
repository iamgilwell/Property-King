from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth import get_user_model
from .models import Country,Profile
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
User = get_user_model()

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email',widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Email Address'
        }
    ), required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form_control',
        'placeholder': 'Enter your Password'
    }))

class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=60,
                                 label='First Name',
                                 widget=forms.TextInput(attrs={
                                     'class': 'form_control',
                                     'placeholder': 'First name'
                                 }))
    last_name = forms.CharField(max_length=60,
                                label='Last Name',
                                widget=forms.TextInput(attrs={
                                    'class': 'form_control',
                                    'placeholder': 'Last name'
                                }))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form_control',
        'placeholder': 'Enter your email here'
    }))
    password = forms.CharField(max_length=255, label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form_control',
        'placeholder': 'Enter password'
    }))

    password = forms.CharField(max_length=255, label='Confirm Password', widget=forms.PasswordInput(attrs={
        'class': 'form_control',
        'placeholder': 'Confirm Password'
    }))


    phone = forms.CharField(label='Phone', widget=forms.TextInput(attrs={
        'class': 'form_control',
        'placeholder': 'Phone Number'
    }), required=False)
  
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    class Meta:
        model = User
        fields = ("first_name","last_name","email","password","phone")

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            # return confirm_password
            msg = u"Password and Confirm Passwords,do not match"
            # self.add_error('', msg)
            raise forms.ValidationError(msg)
            return confirm_password

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            user_exist = User.objects.get(email__iexact=email)
            if user_exist:
                msg = u"Email Address already exists"
                self.add_error('', msg)
                # raise forms.ValidationError(msg)
        except User.DoesNotExist:
            return email  

    def save(self,commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.active = False
        if commit:
            user.save()
        return user
# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=100, required=True)
#     last_name = forms.CharField(max_length=100, required=True)
#     email = forms.EmailField(max_length=254, help_text='e.g youremail@makeup.com')

#     class Meta:
#         model = User
#         fields = ('first_name','last_name','username','password1','password2')


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includea all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'email',
        )

    def clean_password2(self):
        # Check that the two passwords entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
   # password = ReadOnlyPasswordHashField()
    password = ReadOnlyPasswordHashField(label=("Password"),
        help_text=("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"../password/\">this form</a>."))

    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'active',
            'staff',
            'admin',
        )

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields=('email',)
        #exclude = ('email','password')

    # def save(self, commit=True):
    #     user = super(UserUpdateForm, self).save(commit=True)
    #     # password = self.cleaned_data["password"]
    #     # if password:
    #     #     user.set_password(password)
    #     # if commit:
    #     #     user.save()
    #     return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('password', 'active', 'admin')

    # def clean_password(self):
    #     return self.initial["password"]

class ConfirmPasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('password', )

    def clean(self):
        # Administrat0rs
        cleaned_data = super(ConfirmPasswordForm, self).clean()
        password = cleaned_data.get('password')
        #print("[ConfirmPasswordForm confirm_password]  ------> make_password:   {}  ".format(confirm_password))
       # print("[change_password]  ------> ConfirmPasswordForm self.instance.password {}".format(self.instance.password))
        # check_user_password = validators.validate_password(confirm_password, self.instance.password)
        # print("[check_user_password]  ------> {}".format(check_user_password))


        # if not check_password(confirm_password, self.instance.password):
        #     self.add_error('password', 'Password does not match.')

    # def save(self, commit=True):
    #     user = super(ConfirmPasswordForm, self).save(commit)
    #     user.last_login = timezone.now()
    #     if commit:
    #         user.save()
    #     return user

class ProfileUpdateForm(forms.ModelForm):
    country = forms.ModelChoiceField(queryset=Country.objects.filter(available=True), empty_label="(Choose field)", to_field_name="name")

    class Meta:
        model=Profile
        fields=['first_name','last_name','email','phone','bio','country','state','zip_code']

class PasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=False)
    current_password = forms.CharField(widget=forms.PasswordInput, required=False)
    # class Meta:
    #     model = User
    #     fields = ('password', ) 

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(PasswordForm, self).__init__(*args, **kwargs)

    def clean_current_password(self):
        confirm_password = self.cleaned_data['current_password']
        print("[PasswordForm clean_current_password]  ------> make_password:   {}  ".format(confirm_password))
        # If the user entered the current password, make sure it's right
        if self.cleaned_data['current_password'] and not self.user.check_password(self.cleaned_data['current_password']):
            raise ValidationError('This is not your current password. Please try again.')

        # If the user entered the current password, make sure they entered the new passwords as well
        if self.cleaned_data['current_password'] and not (self.cleaned_data['password'] or self.cleaned_data['confirm_password']):
            raise ValidationError('Please enter a new password and a confirmation to update.')

        return self.cleaned_data['current_password']

    def clean_confirm_password(self):
        # Make sure the new password and confirmation match
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')

        if password1 != password2:
            raise forms.ValidationError("Your passwords didn't match. Please try again.")

        return self.cleaned_data.get('confirm_password')


        

# # classes here 
# #  login form 
# # class CreateUserForm(UserCreationForm):
# #         class Meta:
# #             model = accounts
# #             fields = ['username', 'email', 'password1', 'password2']

# # class UpdateHoursForm(ModelForm):
# #         class Meta:
# #             model = techrecords
# #             fields = '__all__'
   

