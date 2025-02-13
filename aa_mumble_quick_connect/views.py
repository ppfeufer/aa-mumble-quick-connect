"""App Views"""

# Django
from django.contrib.auth.decorators import login_required, permission_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

# AA Mumble Quick Connect
from aa_mumble_quick_connect.models import MumbleLink, Section


@login_required
@permission_required("aa_mumble_quick_connect.basic_access")
@permission_required("mumble.access_mumble")
def index(request: WSGIRequest) -> HttpResponse:
    """
    Index view
    :param request:
    :return:
    """

    channels_in_sections = Section.objects.prefetch_related("mumble_links").all()
    channels_without_sections = MumbleLink.objects.filter(section__isnull=True)

    context = {
        "channels_in_sections": channels_in_sections,
        "channels_without_sections": channels_without_sections,
    }

    return render(
        request=request,
        template_name="aa_mumble_quick_connect/index.html",
        context=context,
    )
