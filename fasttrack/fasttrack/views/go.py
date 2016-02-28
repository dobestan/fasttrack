from django.http import HttpResponse
from django.views.generic.base import RedirectView

from django.core.urlresolvers import reverse


from faker import Faker


class GoView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):

        to_url = self.request.GET.get("to", self.request.META.get("HTTP_HOST"))
        from_url = self.request.GET.get("from", reverse("home"))

        # Suppose that user does not append "http://" text on url.
        if not to_url.startswith("http"):
            to_url = "http://" + to_url

        if not from_url.startswith("http"):
            from_url = "http://" + from_url

        return to_url


class GoRandomView(GoView):

    def get_redirect_url(self, *args, **kwargs):
        redirect_url = super(GoRandomView, self).get_redirect_url(*args, **kwargs)

        fake = Faker()

        utm_source = fake.text().split(" ")[0].lower()
        utm_medium = fake.text().split(" ")[0].lower()
        utm_campaign = fake.text().split(" ")[0].lower()

        utm_paramters = "utm_source={utm_source}&utm_medium={utm_medium}&utm_campaign={utm_campaign}".format(
            utm_source=utm_source,
            utm_medium=utm_medium,
            utm_campaign=utm_campaign,
        )

        if not "?" in redirect_url:
            redirect_url = redirect_url + "?" + utm_paramters
        else:
            redirect_url = redirect_url + "&" + utm_paramters

        print(redirect_url)

        return redirect_url
