from django import forms


class UserRegistrationForm(forms.Form):
    PLAN_CHOICES = (
        ('basic', 'normal'),
        ('premium', 'Premium '),
        ('deluxe', 'super'),
    )

    ADDITIONAL_OPTIONS_CHOICES = (
        ('stockage', 'more stockage'),
        ('stoackege lux', 'more more stockage'),
        ('family aboonement', 'more abbonement'),
    )

    name = forms.CharField(label='Your name', max_length=50)
    email = forms.EmailField(label='Your email', max_length=50)
    signup_to_newsletter = forms.BooleanField(label='Signup to newsletter', required=False)
    plan = forms.ChoiceField(label='Your plan', choices=PLAN_CHOICES)
    additional_options = forms.MultipleChoiceField(
        label='Additional options',
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=ADDITIONAL_OPTIONS_CHOICES,
    )

