# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home_screen_view(request):
    print(request.headers)
    page = request.GET.get("page")
    return render (request,"./base.html",{})