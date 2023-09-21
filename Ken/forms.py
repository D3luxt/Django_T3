from django import forms
from django.contrib.auth.forms import UserCreationForm
from advice.models import *
gender = [
    ('male','male'),
    ('female','female'),
    ('other','other')
]
approvedstatus = [
    ('approved','approved'),
    ('waiting','waiting'),
    ('rejected','rejected')
]
amount_pro = [
    ('instock','instock'),
    ('sold','sold'),
    ('processing','processing'),
]
save_yet = [
    ('saved','saved'),
    ('notyet','notyet'),
]

class DateInput(forms.DateInput):
    input_type = 'date'

class UserDetail(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email','first_name','last_name',)

class UserDetailExtended(forms.ModelForm):
    gender = forms.ChoiceField(choices=gender,required=True)
    class Meta:
        model = usernotebook
        fields = ('gender', 'phone','profile_pic',)

class UserCre(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

class ProAddAdmin(forms.ModelForm):
    amount = forms.ChoiceField(choices=amount_pro)
    approvedstatus = forms.ChoiceField(choices=approvedstatus)
    class Meta:
        model = productitem
        widgets = {
            'pro_desc': forms.Textarea(attrs={'rows': 4, 'cols': 30}),
        }
        fields = ('pro_name','brand','pro_desc','price','amount','pro_pic','approvedstatus',)

class ProAdd(forms.ModelForm):
    class Meta:
        model = productitem
        widgets = {
            'pro_desc': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }
        fields = ('pro_name','brand','pro_desc','price','pro_pic')



class paymentMethodForm(forms.ModelForm):
    class Meta:
        model = paymentMethod
        fields = ('bank_account_number','bank_account',)


class OrderAdd(forms.ModelForm):
    class Meta:
        model = ordernotebook
        fields = ('or_sale','deli_address','bank_select','payslip_pic',)

class OrderAddAdmin(forms.ModelForm):
    status = forms.ChoiceField(choices=approvedstatus)
    class Meta:
        model = ordernotebook
        fields = ('deli_address','bank_select','payslip_pic','status')

class sumsalevalue(forms.ModelForm):
    class Meta:
        model = totaltransaction
        fields = ('totalsale','totalorder')


'''class OrderAddAdmin(forms.ModelForm):
    class Meta:
        model = ordernotebook
        fields = ('status','payslip_pic','price','pro_pic')'''