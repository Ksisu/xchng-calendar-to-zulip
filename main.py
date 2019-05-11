from exchangelib import Credentials, Account, EWSDateTime
import os, datetime, zulip, crython

user = os.environ['XCHNG_USER']
password = os.environ['XCHNG_PASS']
calendar = os.environ['XCHNG_CALENDAR']

stream = os.environ['ZULIP_STREAM']
topic = os.environ['ZULIP_TOPIC']

schedule = os.getenv('SCHEDULE')


# ZULIP_SITE - zulip client
# ZULIP_EMAIL - zulip client
# ZULIP_API_KEY - zulip client


def list_today_items():
    credentials = Credentials(user, password)
    account = Account(user, credentials=credentials, autodiscover=True)

    calendar_folder = account.public_folders_root / calendar

    now = datetime.datetime.now()
    year, mount, day = now.year, now.month, now.day

    items = calendar_folder.all().filter(
        end__gt=account.default_timezone.localize(EWSDateTime(year, mount, day)),
        start__lt=account.default_timezone.localize(EWSDateTime(year, mount, day + 1))
    ).order_by('subject')

    return list(map(lambda i: i.subject, items))


def convert_to_message(items):
    return '\n'.join(list(map(lambda i: ' * ' + i, items)))


def send_to_zulip(msg):
    request = {
        "type": "stream",
        "to": stream,
        "subject": topic,
        "content": msg
    }
    client = zulip.Client()
    client.send_message(request)


@crython.job(expr=schedule)
def process():
    items = list_today_items()
    msg = convert_to_message(items)
    send_to_zulip(msg)

if __name__ == "__main__":
    if schedule is None:
        process()
    else:
        crython.start()
        crython.join()
