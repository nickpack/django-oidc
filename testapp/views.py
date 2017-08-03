from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response


@login_required
def home(request):
    # Old: opresult.mako
    return render_to_response(
        "testapp/result.html", {
            "userinfo": request.session['userinfo'] if 'userinfo' in request.session.keys() else None})


def unprotected(request):
    return render_to_response("testapp/unprotected.html")
