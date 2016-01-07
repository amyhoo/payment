# -*- coding: utf-8 -*-
#######################################################################################
# 提交直接支付请求，被payment所调用
#######################################################################################
from billing_payment.alipay.conf import BANKPAY_PARAMS
from billing_payment.alipay.gatewayinfo import Alipay
from billing_payment.payment.mixins import PaySessionMan

def AlipayNetbankHandle(order_info,**kwargs):
    '''
    处理支付宝请求
    '''

    gateway_info=dict(BANKPAY_PARAMS,**{
        'service':'create_direct_pay_by_user',#跟直接付款一样
        'defaultbank':order_info['defaultbank'],
        'subject':order_info['subject'],
        'total_fee':order_info['total_fee'],
        'out_trade_no':order_info['out_trade_no'],
        'notify_url':order_info['notify_url'],
        'return_url':order_info['return_url'] ,
         })
    gateway_info={key:gateway_info[key] for key in gateway_info if gateway_info[key]!=None}
    alipay=Alipay(**gateway_info)
    return  alipay.request('get')
