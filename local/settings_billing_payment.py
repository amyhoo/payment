# -*- coding:utf-8 -*-

BILLING_BASE_URL=""

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': [''],
    }
}
TIME_ZONE="Asia/Shanghai"
#卖家信息
ALIPAY_SELL_EMAIL=""
ALIPAY_SELL_ID=""
ALIPAY_KEY =""

SESSION_COOKIE_DOMAIN=''
#SESSION_COOKIE_NAME='sessionId'
MD5_KEY=""
SECRET_KEY = ''
BASE_URL=""
LOG_BASE_URL = ''
BILL_CENTER_URL=""