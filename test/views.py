from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

#here you create basic pages


#home page
class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse("test"))
        return super().get(request, *args, **kwargs)



#thanks page (aka after user has signed out page, thank them for visiting)
class ThanksPage(TemplateView):
    template_name = "thanks.html"

# contact page
class ContactPage(TemplateView):
    template_name = 'contact.html'

class TestPage(TemplateView):
    template_name = 'test.html'



