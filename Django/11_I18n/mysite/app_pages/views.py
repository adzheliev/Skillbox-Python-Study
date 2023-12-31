import datetime
from django.utils.translation import gettext as _
from django.utils.formats import date_format

from django.shortcuts import render

def translation_example(request, *args, **kwargs):
    return render(request, 'app_pages/translation_example.html')

def greetings_page(request, *args, **kwargs):
    greetings_message = _('Hello there! Today is %(date)s %(time)s') % {
        'date': date_format(datetime.datetime.now().date(), format='SHORT_DATE_FORMAT', use_l10n=True),
        'time': datetime.datetime.now().time(),
    }
    return render(request, 'app_pages/greetings.html', context={
        'greetings_message': greetings_message,
    })

