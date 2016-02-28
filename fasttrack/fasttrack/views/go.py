from django.http import HttpResponse
from django.views.generic.base import RedirectView

from django.core.urlresolvers import reverse


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
