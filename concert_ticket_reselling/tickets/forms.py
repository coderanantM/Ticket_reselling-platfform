from django import forms
from .models import Ticket
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SellerRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    contact_info = forms.CharField(max_length=255, required=True, help_text="Enter your contact info (e.g., WhatsApp number)")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'contact_info']

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['event_name', 'event_date', 'venue', 'price', 'seller_name', 'quantity', 'category']
        
