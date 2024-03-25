import requests
import json
from django.http import HttpResponse
from django.views.generic import TemplateView

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View

from orders.models import Order


# URLS 
zp_api_url = "https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
zp_api_verify_url = "https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
start_pay_url = "https://sandbox.zarinpal.com/pg/StartPay/"
callback_url = 'http://127.0.0.1:8000/payment/verify'


class PaymentProcessView(View):
    def get(self,request):
        # Get order_id from session
        order_id = request.session.get('order_id')
        # Get order object
        order = get_object_or_404(Order, id=order_id)

        toman_total_price = order.get_total_price()
        # rial_total_price = toman_total_price * 10

        data = {
            'MerchantID':"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
            'Amount':toman_total_price,
            'Description':f'#{order.id}:{order.user.first_name} {order.user.last_name}',
            'CallbackURL':callback_url,
        }
        data = json.dumps(data)
        headers = {
        'content-type': 'application/json',
        'content-length': str(len(data)),
        }
        res = requests.post(zp_api_url,data=data,headers=headers)
        if res.status_code == 200:
            response = res.json()
            if response['Status'] == 100:
                url = f"{start_pay_url}{response['Authority']}"
                return redirect(url)
            pass
        else:
            return HttpResponse(str(res.json()['errors']))
    
class PaymentVerify(View):
    def get(self,request):
        authority = request.GET['Authority']
        # Get order_id from session
        order_id = request.session.get('order_id')
        # Get order object
        order = get_object_or_404(Order, id=order_id)
        toman_total_price = order.get_total_price()

        data = {
            'MerchantID':"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
            'Amount':toman_total_price,
            'Authority':authority,
        }
        data = json.dumps(data)
        headers = {
        'content-type': 'application/json',
        'content-length': str(len(data)),
        }
        res = requests.post(zp_api_verify_url,data=data,headers=headers)
        if res.status_code == 200 : 
            response = res.json()
            if response["Status"] == 100 :
                content = {'RefID':response['RefID'],'type':'success','authority':authority}
                return render(request, 'payment/payment_status.html', context=content)
            elif response["Status"] == 101 :
                content = {'RefID':response['RefID'],'type':'warning'}
                return render(request, 'payment/payment_status.html', context=content,)
            
        return render(request, 'payment/payment_status.html')