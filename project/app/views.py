from django.shortcuts import render
from django.shortcuts import get_object_or_404
import stripe
from .models import *
from django.http import JsonResponse
from django.views import View
from django.urls import reverse
import environ

env = environ.Env()
environ.Env.read_env()

stripe.api_key ='sk_test_51OQGBgCLksmMuKnYIbQoXO52cr5Fp8fgQGwMj4i0keaWBwKm1vdnquUWKGGecNDnhhQCCHwwyRgyk2qH3dEHVtDU00BrJnBEfG    '

class AllItem(View):
    def get(self, request):
        items = Item.objects.all()
        print('work')
        return render(request, 'app/items.html', context={'items':items})



class Success(View):
    def get(self, request, item_id):
        item = get_object_or_404(Item, id=item_id)

        return render(request, 'success.html')
    
class Cancel(View):
    def get(self, request, item_id):
        item = get_object_or_404(Item, id=item_id)
        return render(request, 'bad.html')

# class AddView(View):
#     def get(self, request, id):


class BuyItemView(View):
    def get(self, request, id):

        item = get_object_or_404(Item, id=id)
        success = 'http://127.0.0.1:8000/success/{}/'.format(item.id)
        cancel = 'http://127.0.0.1:8000/cancel/{}/'.format(item.id)
        # success = reverse('success', args=[item.id])
        # cancel = reverse('cancel', args=[item.id])

        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'rub',
                    'product_data': {
                        'name': item.name,
                        'description': item.description,
                    },
                    'unit_amount': int(item.price * 100), 
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=success,
            cancel_url=cancel,
        )
        return JsonResponse({'session_id': session.id})
    


class ItemInfo(View):
    def get(self, request, id):
        item = get_object_or_404(Item, id=id)

        return render(request, 'app/item.html', context={'item':item})
