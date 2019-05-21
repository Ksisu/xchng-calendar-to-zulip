import os
from xchng_calendar import timezone

template = os.getenv('TEMPLATE')

if template is None:
    template = '{{#events}} * {{o.subject}}\n{{/events}}'


def __to_date_string(dt):
    return dt.ewsformat()[0:10]


def __to_time_string(dt):
    return dt.ewsformat()[11:16]


def __convert(event):
    start = event.start.astimezone(timezone)
    end = event.end.astimezone(timezone)
    return {
        'o': event,
        'start_date': __to_date_string(start),
        'end_date': __to_date_string(end),
        'start_time': __to_time_string(start),
        'end_time': __to_time_string(end),
        'start': start,
        'end': end,
    }


def create_template_data(events):
    items = list(map(__convert, events))
    return {'events': items}
