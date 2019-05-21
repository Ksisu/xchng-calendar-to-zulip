import os, crython
from xchng_calendar import list_today_events
from zulip_mustache import send
from event_converter import create_template_data, template

schedule = os.getenv('SCHEDULE')


@crython.job(expr=schedule)
def process():
    events = list_today_events()
    data = create_template_data(events)
    send(template, data)


if __name__ == "__main__":
    if schedule is None:
        process()
    else:
        crython.start()
        crython.join()
