# Exchange Calendar events to Zulip

[![](https://img.shields.io/github/release/Ksisu/xchng-calendar-to-zulip.svg)](https://github.com/Ksisu/xchng-calendar-to-zulip/releases)
[![](https://img.shields.io/docker/cloud/build/ksisu/xchng-calendar-to-zulip.svg)](https://hub.docker.com/r/ksisu/xchng-calendar-to-zulip/builds)
[![](https://img.shields.io/github/license/Ksisu/xchng-calendar-to-zulip.svg)](https://github.com/Ksisu/xchng-calendar-to-zulip/blob/master/LICENSE)

A simple python script to:
 * connect to exchange server
 * list the current day events from a calendar
 * send to a Zulip Stream Topic

```
docker run \
  -e XCHNG_USER=off@example.com \
  -e XCHNG_PASS=secret \
  -e XCHNG_CALENDAR=Off \
  -e XCHNG_TIMEZONE='Europe/Budapest' \
  -e ZULIP_SITE=https://zulip.example.com \
  -e ZULIP_EMAIL=off-bot@zulip.example.com \
  -e ZULIP_API_KEY=secret \
  -e ZULIP_STREAM=Off \
  -e ZULIP_TOPIC=Off \
  -e SCHEDULE='@daily' \
  ksisu/xchng-calendar-to-zulip
```

`SCHEDULE` is an optional setting to schedule with [crython](https://github.com/ahawker/crython) expression.

`XCHNG_TIMEZONE` is optional setting (default: `UTC`)
