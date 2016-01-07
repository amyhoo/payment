# -*- coding: utf-8 -*-
#######################################################################################
# RedirectSessionMixin未被恰当在view中调用
#######################################################################################
class PaymentException(Exception):
    '''支付模块base异常'''

class OrderCreateException(PaymentException):
    '''支付模块订单创建异常'''

class OrderUpdateException(PaymentException):
    '''支付模块订单更新异常'''

class UserInfoException(PaymentException):
    '''支付模块用户信息获取异常'''

class PaymentMethodException(PaymentException):
    '''支付方法异常'''

class PaymentInnerException(PaymentException):
    '''内部异常'''
