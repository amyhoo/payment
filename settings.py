# -*- coding:utf-8 -*-
#######################################################################################
# 基本设置项
#######################################################################################

"""
Django settings for temp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
import logging
import hashlib
location = lambda x:os.path.join(os.path.dirname(__file__), x)
#运行基本信息
ROOT_URLCONF = 'payment.urls'
WSGI_APPLICATION = 'billing_payment.wsgi.application'
#SECRET_KEY = 'd(gs9s)+a4x%*x*jdvefat#*yqy#uo_(h0nrulg=9tyzrw5_%$'

#网站设置信息
SITE_ID = 1#站点id

# 应用定义
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

#中间件定义
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)


#静态文件设置
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/payment/static/'
ADMIN_MEDIA_PREFIX='/payment/static/admin/'
MEDIA_URL="/media/"
MEDIA_ROOT=location("media")#
TEMPLATE_DIRS = (location('templates'),)# 在1.8中改变设置位置

#模板设置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [location('templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                #'django.core.context_processors.i18n',
                'django.core.context_processors.static',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.csrf',#如果使用RequestContext就可以不使用
                "billing_payment.settings.extern_context",
            ],
            },
        },
    ]

LOCALE_PATHS = ('locale/',)


try:
    sys.path.append("/etc/billing")
    from settings_billing_payment import *
    ImportFromEtcSuccess=True
except ImportError:
    ImportFromEtcSuccess=False
    logging.warning("Error import local_settings from /etc/billing")

try:
    if not ImportFromEtcSuccess:
        from .local.settings_billing_payment import *
except ImportError:
    logging.warning("No local_settings file found.")

def extern_context(request):
    """
    Add some generally useful metadata to the template context
    """
    def getMD5(str):
        '''
        在用户费用管理界面中的md5算法，需要调回到该页面
        :param str:
        :return:
        '''
        m2 = hashlib.md5()
        m2.update(str)
        return m2.hexdigest()
    account_id=request.session.get("account_id")
    sign=getMD5(account_id+MD5_KEY)
    center_request_url=BILL_CENTER_URL+"?account_id=%s&sign=%s"%(account_id,sign)
    return {"root_url":BASE_URL,'tz':TIME_ZONE,'center_url':center_request_url}

# 语言国际化
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = TIME_ZONE#Asia/Shanghai UTC
USE_I18N = True
USE_L10N = True
USE_TZ = True

#默认django.contrib.sessions.serializers.JSONSerializer不能处理特别对象
#SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'
SESSION_ENGINE="django.contrib.sessions.backends.cache"


#安全性设置
DEBUG = True
TEMPLATE_DEBUG = False
DJANGO_LOG_LEVEL='INFO'
ALLOWED_HOSTS = [
    "0.0.0.0",
]

#STATIC_ROOT=location('static')# #静态文件根目录,发布时候使用collectstatic 将程序外模块的静态文件收集到一起使用
STATICFILES_DIRS=(location('static'),)