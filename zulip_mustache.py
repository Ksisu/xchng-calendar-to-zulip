import os, pystache, zulip

stream = os.environ['ZULIP_STREAM']
topic = os.environ['ZULIP_TOPIC']
# ZULIP_SITE - zulip client
# ZULIP_EMAIL - zulip client
# ZULIP_API_KEY - zulip client


def send(template, data):
    msg = pystache.render(template, data).rstrip()
    if msg:
        request = {
            "type": "stream",
            "to": stream,
            "subject": topic,
            "content": msg
        }
        client = zulip.Client()
        client.send_message(request)
