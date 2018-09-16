# alertifyTwilio
Used Twilio API to call and check in on fall victim.

**Note** small bug in API voice callback so use
```
curl 'https://api.twilio.com/2010-04-01/Accounts/AC6dde4f2c5dec01ff9c5c650567f2e811/Calls.json' -X POST \
--data-urlencode 'To=17472558546' \
--data-urlencode 'From=+15052787618' \
--data-urlencode 'ApplicationSid=AP7c382977057944c9bcb2367679f8fabb' \
--data-urlencode 'Method=GET' \
-u AC6dde4f2c5dec01ff9c5c650567f2e811:5f5708895de328cd555d6184a5e539b1
```
