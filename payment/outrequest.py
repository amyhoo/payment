# -*- coding: utf-8 -*-
#######################################################################################
# 向后台生成1.订单生成请求 2.用户信息请求 3.订单信息更新，支付信息更新
#
#######################################################################################
import json
from billing_payment.payment.exceptions import *
import requests
import random
from billing_payment.payment.keymap import *
from django.conf import settings

#向付费模块提交请求
class RechargeRequest():
    URL=settings.BILLING_BASE_URL
    @staticmethod
    def user_info_request(user_account_id):
        '''
        :param user_md5:用户id的md信息
        :param agented_md5: 被代理的用户的md信息
        :return:user_info,用户信息,代理用户信息
        '''
        #return user_info
        pass

    @staticmethod
    def order_request(key1="",key2="",key3=0):
        '''
        该函数根据输入参数请求订单信息，然后根据订单信息向支付接口请求
        user 用户
        pay_option 订单支付方法
        cash_amount 支付金额
        '''
        pass

    @staticmethod
    def order_update(order_info):
        '''
        该函数更新订单状态
        :return:
        '''
        pass

class PayMethod():
    #第一列(本模块代码,template变量,传递给付费模块支付方式,css中类名);第二列 (支付宝中代码) 第三列 中文名
    PAY_DEF=(
        ('alipay_direct','create_direct_pay_by_user','支付宝即时到帐',),
        #......
    )

    #获取网络银行的template变量列表
    @staticmethod
    def get_netbank_context():
        return [line[0] for line in PayMethod.PAY_DEF[1:]]

    #获取内部的变量与计费模块的映射字典
    @staticmethod
    def get_pay_dict():
        return {line[0]:line[0] for line in PayMethod.PAY_DEF}

    #获取付费模块名称
    @staticmethod
    def get_alipay_dict():
        return {line[0]:line[1] for line in PayMethod.PAY_DEF}

    #获取form的value值与表现值
    @staticmethod
    def get_pay_choices():
        return [(line[0],line[2]) for line in PayMethod.PAY_DEF]

#支付宝请求与内部数据库信息转换
REQUEST_ALIPAY_INTERFACE=(
    ("order_number","out_trade_no"),
    #...
)

#支付宝回复信息与数据库信息交换
RESPONSE_ALIPAY_INTERFACE=(
    ("bank_number","bank_seq_no"),
    #...
)
