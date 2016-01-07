# -*- coding: utf-8 -*-
#######################################################################################
# 《多种支付方式选择界面》《出错界面》 《支付成功界面》《支付失败界面》《支付回调处理》
#######################################################################################
from django.views import generic
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django.shortcuts import render_to_response
from payment.outrequest import *
from alipay import *
from payment.forms import PaymentForm
from hashlib import md5
from payment.mixins import PaySessionMixin
from payment.keymap import *
from django.utils.translation import ugettext as _ #ugettext_lazy
from django.shortcuts import render_to_response,render
import logging
from django.conf import settings

class PaymentMethodView(PaySessionMixin,generic.TemplateView):
    '''
    支付方法选择
    '''
    template_name = 'paymentmethod.html'
    MD5_KEY=settings.MD5_KEY

    def _md5_check(self):
        '''
        :return:
        '''
        params={key:line for key,line in self.request.GET.items()} #必须深拷贝才能修改
        try:
            sign=params.pop("sign")
        except:
            return False

        if sign==PaymentMethodView._generate_md5_sign(params):
            return True
        else:
            return False

    @staticmethod
    def _generate_md5_sign(params):
        #md5加密生成签名
        src = '&'.join(['%s=%s' % (key, value) for key,value in sorted(params.items())]) + PaymentMethodView.MD5_KEY
        return md5(src.encode('utf-8')).hexdigest()

    def get_context_data(self, **kwargs):
        context=super(PaymentMethodView,self).get_context_data(**kwargs)
        form=PaymentForm()
        pass
        context['netbank']=PayMethod.get_netbank_context()
        return context

    def get(self, request, *args, **kwargs):
        if not self._md5_check():
            self.save("error_message",_("you failed in security check!"))
            return HttpResponseRedirect(reverse('errors'))
        else:
            return super(PaymentMethodView,self).get(request, *args, **kwargs)

class PaymentSubmitView(PaySessionMixin,generic.FormView):
    '''
    支付提交，调用具体的支付请求函数
    '''
    form_class = PaymentForm
    def post(self, request, *args, **kwargs):
        '''
        '''
        form=PaymentForm(request.POST)
        if form.is_valid():
            key1=form.cleaned_data['']
            key2=float(form.cleaned_data[''])
            key3=form.cleaned_data['']
            order_info=RechargeRequest.order_request(key1,key2,key3)
            result=self.handle(order_info)
            if isinstance(result,HttpResponseRedirect) :#如果返回的是重定向
                return result
            elif isinstance(result,HttpResponse):#
                return result
            else:#字符串形式的
                return HttpResponse(result)
        else:
            return HttpResponse("输入数值有错")

    def handle(self,order_info):
        '''
        处理订单信息
        有可能会redirect
        '''
        pay_method={
            'alipay_direct':AlipayDirectHandle,
            'alipay_netbank':AlipayNetbankHandle,#value 为netbank 具体银行名称
        }
        selected_value=order_info.get("pay_method")
        choose_key=[item for item  in  pay_method.keys() if item in selected_value][0]
        paymethod=pay_method.get(choose_key)
        order_info['response']=self.respond_url()
        alipay_info=output_info(order_info,[],REQUEST_ALIPAY_INTERFACE)
        alipay_info["defaultbank"]=PayMethod.get_alipay_dict().get(alipay_info.get("defaultbank"))
        self.save("order_info",order_info)
        logging.info('it is ok for info')
        logging.warning("order request to alipay::"+";".join([str(key)+" : "+str(order_info[key]) for key in order_info]))
        return paymethod(alipay_info)

    def base_url(self):
        '''
        '''
        if settings.DEBUG:
            # Determine the localserver's hostname to use when
            # in testing mode8
            base_url = 'http://%s' % self.request.get_host()
        else:
            base_url = 'https://%s' % Site.objects.get_current().domain
        return base_url

    def respond_url(self):
        '''
        '''
        return "%s%s" % (self.base_url(), reverse("response"))

class PaymentFeedbackView(PaySessionMixin,generic.View):
    '''
    支付回调，支付请求函数负责设置好回调功能
    '''
    from alipay.gatewayinfo import Alipay
    from alipay.conf import BASIC_PARAMS
    alipay=Alipay(**BASIC_PARAMS)

    def taobao_info_handle(self,taobao_info):
        return {key:line[0] for key,line in taobao_info.items() if len(line)>0}#如果taobao_info是Query_Dict会出现错误

    def log(self,request,log_info,user_info):
        pass
    def get(self, request, *args, **kwargs):
        '''
        针对return_url
        '''
        context_data=self.clear()
        if PaymentFeedbackView.alipay.verify_notify(**request.GET):
            alipay_info=self.taobao_info_handle(dict(request.GET))
            order_info=collect_info(alipay_info,[],RESPONSE_ALIPAY_INTERFACE)
            pass
            if RechargeRequest.order_update(order_info):
                return HttpResponseRedirect(reverse('success',context_data))
            else:
                return HttpResponseRedirect(reverse('fail',context_data))
        else:
            context_data.update({"error_message":_("backend error!")})
            return HttpResponseRedirect(reverse('fail',context_data))

    def post(self, request, *args, **kwargs):
        '''
        针对notify_url
        '''
        context_data=self.clear()
        if PaymentFeedbackView.alipay.verify_notify(**request.POST):
            alipay_info=self.taobao_info_handle(dict(request.POST))
            order_info=collect_info(alipay_info,[],RESPONSE_ALIPAY_INTERFACE)
            if RechargeRequest.order_update(order_info):
                return HttpResponse("success")
            else:
                return HttpResponse("fail")
        else:
            return HttpResponse("fail")


class ErrorsHandleView(PaySessionMixin,generic.TemplateView):
    '''
    错误处理页面
    '''
    template_name = 'errors.html'
    def get_context_data(self, **kwargs):
        context=super(ErrorsHandleView,self).get_context_data(**kwargs)
        return context

class PaymentSuccessView(PaySessionMixin,generic.TemplateView):
    '''
    支付成功页面
    '''
    template_name = 'pay_success.html'
    def get_context_data(self, **kwargs):
        context=super(PaymentSuccessView,self).get_context_data(**kwargs)
        context.update(kwargs)
        return context

class PaymentFailView(PaySessionMixin,generic.TemplateView):
    '''
    支付失败页面
    '''
    template_name = 'pay_fail.html'
    def get_context_data(self, **kwargs):
        context=super(PaymentFailView,self).get_context_data(**kwargs)
        context.update(kwargs)
        return context
