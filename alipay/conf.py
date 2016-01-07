# -*- coding:utf-8 -*-
#######################################################################################
#淘宝接口参数意义
#######################################################################################
from django.conf import settings
import sys
# 合作者身份 ID，以 2088 开头的 16 位纯数字组成
ALIPAY_PARTNER = settings.ALIPAY_SELL_ID

# 支付宝网关
ALIPAY_GATEWAY = 'https://mapi.alipay.com/gateway.do'
ALIPAY_WAP_GATEWAY = 'http://wappaygw.alipay.com/service/rest.htm'
#通知网关
NOTIFY_GATEWAY_URL = 'https://mapi.alipay.com/gateway.do?service=notify_verify&partner=%s&notify_id=%s'

# COD Cash On Delivery 货到付款

#卖家信息
ALIPAY_SELL_EMAIL=settings.ALIPAY_SELL_EMAIL
ALIPAY_SELL_ID=settings.ALIPAY_SELL_ID

#字符集
ALIPAY_INPUT_CHARSET = 'utf-8'
ALIPAY_SIGN_TYPE = 'MD5'

# 访问模式,根据自己的服务器是否支持ssl访问，若支持请选择https；若不支持请选择http
ALIPAY_TRANSPORT='https'

# 安全检验码，以数字和字母组成的32位字符
ALIPAY_KEY = settings.ALIPAY_KEY

# 付完款后跳转的页面（同步通知） 要用 http://格式的完整路径，不允许加?id=123这类自定义参数
ALIPAY_RETURN_URL=''

# 交易过程中服务器异步通知的页面 要用 http://格式的完整路径，不允许加?id=123这类自定义参数
ALIPAY_NOTIFY_URL=''
ALIPAY_SHOW_URL=''

ALIPAY_DATE_FORMAT = ('%Y-%m-%d %H:%M:%S',)

#支付宝接口定义
SERVICE = (
        'create_direct_pay_by_user',    # 即时到帐
        'create_partner_trade_by_buyer',    # 担保交易
        'send_goods_confirm_by_platform',   # 确认发货
        'trade_create_by_buyer',            # 标准双接口
        'alipay.mobile.qrcode.manage', #二维码管理
        )

PAYMENT_TYPE = (
    ('商品购买','1'),    #商品购买
    ('服务购买','2'),    #服务购买
    ('网络拍卖','3'),    #网络拍卖
    ('捐赠','4'),    #捐赠
    ('邮费补偿','5'),    #邮费补偿
    ('奖金','6'),    #奖金
    ('基金购买','7'),       #基金购买
    ('机票购买','8'),    #机票购买
        )
PAYMETHOD = (
        'creditPay',    # 'credit payment'    # 需开通信用支付
        'directPay',    # 'direct payment'    # 余额支付，不能设置 defaultbank 参数
        'bankPay',      # 'bank payment directly'   # 需开通纯网关，需设置 defaultbank
        'cash',         # 'paid by cash'
        'cartoon',      # 'paid by bank card thourgh alipay gateway'
        )

LOGISTICS_TYPE = (
        'POST',     # 平邮
        'EXPRESS',  # 其他快递
        'EMS',      # EMS
        )
LOGISTICS_PAYMENT = (
        'BUYER_PAY',    # 物流买家承担运费
        'SELLER_PAY',   # 物流卖家承担运费
        'BUYER_PAY_AFTER_RECEIVE',  # 买家到货付款，运费显示但不计入总价
        )

#交易状态
TRADE_STATUS = (
        'WAIT_BUYER_PAY',           #等待买家付款
        'WAIT_SELLER_SEND_GOODS',   #买家已付款，等待卖家发货
        'WAIT_BUYER_CONFIRM_GOODS', #卖家已发货，等待买家收货
        'TRADE_FINISHED',           #买家已收货，交易完成
        'TRADE_CLOSED',             #交易中途关闭（已结束，未成功完成）
        'COD_WAIT_SELLER_SEND_GOODS',   # 等待卖家发货（货到付款）
        'COD_WAIT_BUYER_PAY',           # 等待买家签收付款（货到付款）
        'COD_WAIT_SYS_PAY_SELLER',      # 签收成功等待系统打款给卖家（货到付款）
        )

#网银混合渠道代码
NETBANK_MIX=(
    ('ICBCBTB','中国工商银行B2B'),
    ('ABCBTB','中国农业银行B2B',),
    ('CCBBTB','中国建设银行B2B',),
    ('SPDBB2B','上海浦东发展银行B2B',),
    ('BOCBTB','中国银行B2B',),
    ('CMBBTB','招商银行B2B',),
    ('BOCB2C','中国银行',),
    ('ICBCB2C','中国工商银行',),
    ('CMB','招商银行',),
    ('CCB','中国建设银行',),
    ('ABC','中国农业银行',),
    ('SPDB','上海浦东发展银行',),
    ('CIB','兴业银行',),
    ('GDB','广东发展银行',),
    ('FDB','富滇银行',),
    ('HZCBB2C','杭州银行',),
    ('SHBANK','上海银行',),
    ('NBBANK','宁波银行',),
    ('SPABANK','平安银行',),
    ('POSTGC','中国邮政储蓄银行',),
    ('abc1003','visa',),
    ('abc1004','master',),
)
NETBANK_DEBIT=(
    ('CMB-DEBIT','招商银行'),
    ('CCB-DEBIT','中国建设银行'),
    ('ICBC-DEBIT','中国工商银行'),
    ('COMM-DEBIT','交通银行'),
    ('GDB-DEBIT','广东发展发银行'),
    ('BOC-DEBIT','中国银行'),
    ('CEB-DEBIT','中国光大银行'),
    ('SPDB-DEBIT','上海浦东发展银行'),
    ('PSBC-DEBIT','中国邮政储蓄银行'),
    ('BJBANK','北京银行'),
    ('SHRCB','上海农商银行'),
    ('WZCBB2C-DEBIT','温州银行'),
    ('COMM','交通银行'),
    ('CMBC','中国民生银行'),
    ('BJRCB','北京农村商业银行'),
    ('SPA-DEBIT','平安银行'),
    ('CITIC-DEBIT','中信银行'),

)
#基本参数,所有标记为None值在业务逻辑执行时赋值,或者被删除
BASIC_PARAMS={
        #基本参数
        '_input_charset': ALIPAY_INPUT_CHARSET,
        'partner': ALIPAY_PARTNER,
        'payment_type': dict(PAYMENT_TYPE)['商品购买'],
        'sign_type':ALIPAY_SIGN_TYPE, #加密方式
        'sign':None,

        #卖家参数，seller_id,seller_account_name,seller_email必须且只需要一个
        'seller_id':ALIPAY_SELL_ID,
        'seller_account_name':None,
        'seller_email':ALIPAY_SELL_EMAIL,
        #请求所需参数
        'key':ALIPAY_KEY,
}


#即时到帐参数
DIRECT_PARAMS=dict(BASIC_PARAMS,**{
    #即时到帐特有参数
    'paymethod' : 'directPay',   # 默认支付方式，四个值可选：bankPay(网银); cartoon(卡通); directPay(余额); CASH(网点支付)
})

#网银接口参数
BANKPAY_PARAMS=dict(BASIC_PARAMS,**{
    #即时到帐特有参数
    'paymethod' : 'bankPay',   # 默认支付方式，四个值可选：bankPay(网银); cartoon(卡通); directPay(余额); CASH(网点支付)
    'defaultbank' : None,          # 默认网银代号，代号列表见http://club.alipay.com/read.php?tid=8681379，在纯网关网银接口中必须赋值

})



EXTEND_PARAMS={

    # 扩展功能参数——防钓鱼
    'anti_phishing_key':None,
    'exter_invoke_ip': None,
    # 扩展功能参数——自定义参数
    'buyer_email':None,
    'extra_common_param':None,
    # 扩展功能参数——分润
    'royalty_type':None,
    'royalty_parameters':None,
}

#确认发货接口参数
LOG_PARAMS={
    #基本参数
    'service':'send_goods_confirm_by_platform',
    'partner':ALIPAY_PARTNER,
    'input_charset':ALIPAY_INPUT_CHARSET,
    'sign':None,
    'sign_type':ALIPAY_SIGN_TYPE,

    #业务参数
    'trade_no':None,
    'logistics_name':None,
    'transport_type':None,
}
