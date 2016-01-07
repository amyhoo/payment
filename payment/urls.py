# -*- coding: utf-8 -*-
from django.conf.urls import *
from billing_payment.payment import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = patterns('',

    url(r'^checkout', views.PaymentMethodView.as_view(),name='paymethod'),#选择支付方式结帐 (?P<account>[a-zA-Z0-9_\-]+)
    url(r'^submit$', views.PaymentSubmitView.as_view(),name='submit'),#提交
    url(r'^response$', csrf_exempt(views.PaymentFeedbackView.as_view()),name='response'),#回复
    url(r'^errors', views.ErrorsHandleView.as_view(),name='errors'),#错误
    url(r'^success$', views.PaymentSuccessView.as_view(),name='success'),#成功
    url(r'^fail$', views.PaymentFailView.as_view(),name='fail'),#失败

    #url(r'^ajax/order/$', views.order_request,name='order'),#
)
