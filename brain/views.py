# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import JsonResponse

from collegeBot.bot import college_bot


def perform_message(request):
    message = request.GET.get('query')
    unicode_message = unicode(message)
    response = college_bot(unicode_message)
    return  JsonResponse({'statusCode': response})

