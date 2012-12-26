from .forms import OrderForm


def pie_form(request):
    return {'order_form': OrderForm(), 'magic_number': 42}
