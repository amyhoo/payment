# -*- coding: utf-8 -*-
from django import forms
from billing_payment.payment.outrequest import PayMethod

class PaymentForm(forms.Form):
    user_account_id=forms.CharField(required=True)
    agented_account_id=forms.CharField(required=False)
    cash_amount=forms.DecimalField(required=True,min_value=50.00,decimal_places=2,initial=50.00)
    pay_method=forms.ChoiceField(required=True,choices=PayMethod.get_pay_choices(),initial='alipay_direct')
