from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def home_page_view(request): # new
    context = {  # new
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
        "greeting": "THAnk you FOR visitING.",
    }

    return render(request, "home.html",context)


class AboutPageView(TemplateView): # new
    template_name = "about.html"

    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)

        context["contact_address"] = "123 Main Street"
        context["phone_number"] = "555-555-5555"
        return context

def window_page_view(request) :# new
    return render(request, "window.html")



def payment_view(request) :# new
    return render(request, "payment.html")


def address_view(request) :# new
    return render(request, "address.html")