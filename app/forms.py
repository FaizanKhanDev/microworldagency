from .models import ContactsForm,BlogSubscribe
from django import forms


class ContactUs(forms.ModelForm):
    class Meta:
        model = ContactsForm
        fields = ['yourName','email','Phonenumber','Subject','companyname','budget','Message']
        labels = {
            "yourName":"Full Name",
            "email":"Email",
            "companyname":"Company Name",
            "Phonenumber":"Mobile Number",
            "Subject":"Subject",
            "Message":"Message"
        }
        widgets = {
            "yourName": forms.TextInput(attrs={"Placeholder":"Enter Your Full Name"}),
            "email":forms.EmailInput(attrs={"placeholder":"Enter a Valid Email"}),
            "Phonenumber":forms.TextInput(attrs={"placeholder":"Enter Your Phone Number"}),
            "Subject":forms.TextInput(attrs={"placeholder":"Subject"}),
            "companyname":forms.TextInput(attrs={"placeholder":"Company Name (Optional)"}),
            "budget":forms.TextInput(attrs={"placeholder":"Your Budget (Optional)"}),
            "Message" : forms.Textarea(attrs={"placeholder":"Tell Us About Your Projects"})
        }
class BlogEmail (forms.ModelForm):
    class Meta:
        model = BlogSubscribe
        fields = ['email']
        widgets = {
            "email":forms.EmailInput(attrs={"placeholder":"Enter Your Email for Subscriptions","id":"blogemail"})
        }