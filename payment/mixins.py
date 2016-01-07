# -*- coding: utf-8 -*-
#######################################################################################
# session管理
# 暂存订单号以及淘宝验证数据
# PaySessionMan为session数据操作
# PaySessionMixin与view一起使用的mixin
#######################################################################################
import json

class PaySessionMan(object):
    '''
    支付模块session操作控件
    '''
    SESSION_KEY="payment"

    def __init__(self,request):
        if request:
            self.session = request.session
        if self.SESSION_KEY not in self.session:
            self.session[self.SESSION_KEY] = {}

    def save(self,key,data):
        if self.if_session_key():
            payment=self.session[self.SESSION_KEY]
            payment[key]=data
            self.session[self.SESSION_KEY]=payment
        else:
           self.session[self.SESSION_KEY] = {key:data}


    def if_session_key(self):
        return True if self.SESSION_KEY in self.session else False

    def pop(self,key):
        try:
            payment=self.session[self.SESSION_KEY]
            value=payment.pop(key)
            self.session[self.SESSION_KEY]=payment
            return value
        except:
            return None

    def get(self,key):
        try:
            return self.session[self.SESSION_KEY].get(key)
        except:
            return None

    def clear(self):
        try:
            return self.session.pop(self.SESSION_KEY)
        except:
            return None
    def all(self):
        try:
            return self.session.get(self.SESSION_KEY)
        except:
            return None

class PaySessionMixin(object):
    '''
    与view一起使用，支付模块session操作控件
    '''
    def dispatch(self, request, *args, **kwargs):
        # Assign the checkout session manager so it's available in all checkout
        # views.
        self.checkout_session = PaySessionMan(request)
        return super(PaySessionMixin, self).dispatch(request, *args, **kwargs)

    def save(self,key,data):
        self.checkout_session.save(key,data)

    def pop(self,key):
        return self.checkout_session.pop(key)

    def get_key(self,key):
        return self.checkout_session.get(key)

    def clear(self):
        return self.checkout_session.clear()

    def all(self):
        return self.checkout_session.all()