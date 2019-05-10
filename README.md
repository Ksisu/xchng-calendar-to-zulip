# Exchange Calendar events to Zulip

A simple python script to:
 * connect to exchange server
 * list the current day events from a calendar
 * send to a Zulip Stream Topic

```
docker run \
  -e XCHNG_USER=off@example.com \
  -e XCHNG_PASS=secret \
  -e XCHNG_CALENDAR=Off \
  -e ZULIP_SITE=https://zulip.example.com \
  -e ZULIP_EMAIL=off-bot@zulip.example.com \
  -e ZULIP_API_KEY=secret \
  -e ZULIP_STREAM=Off \
  -e ZULIP_TOPIC=Off \
  ksisu/xchng-calendar-to-zulip
```
