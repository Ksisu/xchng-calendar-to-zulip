import os, datetime
from exchangelib import Credentials, Account, EWSDateTime, EWSTimeZone, UTC

user = os.environ['XCHNG_USER']
password = os.environ['XCHNG_PASS']
calendar = os.environ['XCHNG_CALENDAR']
timezone = os.getenv('XCHNG_TIMEZONE')

if timezone is None:
    timezone = UTC
else:
    timezone = EWSTimeZone.timezone(timezone)


def list_today_events():
    credentials = Credentials(user, password)
    account = Account(user, credentials=credentials, autodiscover=True)

    calendar_folder = account.public_folders_root / calendar

    now = datetime.datetime.now()
    year, mount, day = now.year, now.month, now.day

    items = calendar_folder.view(
        start=timezone.localize(EWSDateTime(year, mount, day, 0, 0, 1)),
        end=timezone.localize(EWSDateTime(year, mount, day, 23, 59, 59))
    ).order_by('subject')

    return list(items)
