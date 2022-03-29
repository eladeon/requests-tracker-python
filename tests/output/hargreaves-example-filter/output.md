# Overview

# Request Summary

```
[GET - 200] https://online.hl.co.uk/my-accounts --> /my-accounts[1]
[POST - 200] https://online.hl.co.uk/my-accounts/pending_orders --> /my-accounts/pending_orders[1]
```

# Entries
## /my-accounts[1]

**startedDateTime** = 2022-03-28T12:51:45.656360Z

**REQUEST**

| Key | Value |
| --- | ----- |
| method | GET |
| clean_url | https://online.hl.co.uk/my-accounts |
| request_id | /my-accounts[1] |

**RESPONSE**

| Key | Value |
| --- | ----- |
| status | 200 |
| statusText | OK |
| content | [content/_my-accounts_1.html](content/_my-accounts_1.html)  |
| content[mimeType] |  text/html; charset=utf-8  |
| content[size] | 166945  |

**REQUEST Cookies**

```
    __dat = "62419f2a0f1c42.27309604"
    __dat_ses = "62419f2a0f1c42.27309604"
    __losp = "web_share%3D2-web_index%3D2"
    __mkt = "1"
    __rs = "u7TZZvdc73mCKQ6U%2FTXrOroARHTddyyM5H2VXEkgkHZOd8r11ttLUseEgh66axwMm6HmjcvXwfTRwoyY%2FLr2DA%3D%3D%7C0"
    __sp = "private_investor%3DN-web_share%3D1-web_index%3D1-token%3D"
    ADRUM_BT = "R%3A63%7Cg%3A76ac1112-9b6f-44e0-9b8d-82e52655326a1157%7Cn%3Ahl-prod_bbee1771-dc80-4328-8b4d-a5fd0d64b23b%7Ci%3A435972%7Cd%3A1331%7Ce%3A1106"
    at_check = "true"
    cookieCheck = "true"
    hl_cookie_consent = "{\"ao\": true, \"tp\": true}"
    hl_cp = "1"
    hltimer = "{\"tom\": 1648468594955, \"ot\": \"900\", \"tos\": 0, \"smc\": 0, \"HLWN553203\": {\"to\": 1648468594955, \"li\": 1, \"im\": 1, \"ia\": 0, \"ir\": 0, \"rp\": 0, \"sm\": 0, \"lp\": 0, \"lu\": 1648467754955}}"
    HLWEBsession = "01dfb0aa1a8abc7ea90873530fa6c4f7"
    invest = "{\"amount_lump\": \"0\", \"amount_regular\": \"0\", \"investment\": [], \"vmp_matrix\": \"\"}"
    jsCheck = "yes"
    wwwServer = "!/+ClT4XniA15o5raoX99Pvg73eD4QS+dT5zTwBHFetZg8/AOx2ptKxCKM1LW4YPdjg4y7HG9DA=="
```

**REQUEST Headers**

```
    Accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
    Accept-Encoding = "gzip, deflate, br"
    Accept-Language = "en-US,en;q=0.5"
    Connection = "keep-alive"
    Host = "online.hl.co.uk"
    Referer = "https://online.hl.co.uk/"
    Sec-Fetch-Dest = "document"
    Sec-Fetch-Mode = "navigate"
    Sec-Fetch-Site = "same-site"
    Sec-Fetch-User = "?1"
    Sec-GPC = "1"
    Upgrade-Insecure-Requests = "1"
    User-Agent = "Mozilla/5.0 (Linux; Android 4.4.2; GT-P5220) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36"
```
**REQUEST QueryString Param**

```
```

**RESPONSE Cookies**

```
    __rs = "%2Bb5adfQ5kUwMtmiRqwZjw9whgwToCM%2BlZ2QB1%2FnD9HXppk09oorkzbv1Sbj33%2B%2BTrvfloIcquF3d%2FK7xeHb25w%3D%3D%7C0"
    __sp = "private_investor%3D-web_share%3D-web_index%3D-token%3D"
    ADRUM_BT = "R%3A24%7Cg%3A296d2e27-eff9-4b18-a599-fb750ec1674e1183%7Cn%3Ahl-prod_bbee1771-dc80-4328-8b4d-a5fd0d64b23b%7Ci%3A435951%7Cd%3A1656%7Ce%3A587"
```

**RESPONSE Headers**

```
    Cache-Control = "no-store, no-cache, must-revalidate"
    Connection = "Keep-Alive"
    Content-Encoding = "gzip"
    Content-Security-Policy = "script-src 'self' 'unsafe-inline' 'unsafe-eval' https://cdn.appdynamics.com https://www.googleadservices.com https://ssl.google-analytics.com https://*.akamai.net http://*.hl.co.uk https://*.hl.co.uk https://*.verisign.com https://*.websecurity.symantec.com https://*.websecurity.norton.com https://ping.chartbeat.net https://cdn.tt.omtrdc.net https://hargreaveslansdownpl.tt.omtrdc.net https://assets.adobedtm.com https://dpm.demdex.net https://apis.google.com https://www.googletagmanager.com https://*.facebook.net https://www.facebook.com https://googleads.g.doubleclick.net https://www.google.com https://www.google.co.uk https://static.chartbeat.com https://js.stripe.com https://polyfill.io https://static.hl.co.uk/; style-src 'self' 'unsafe-inline' http://*.hl.co.uk https://*.hl.co.uk https://fonts.googleapis.com https://fonts.gstatic.com https://static.hl.co.uk/; frame-ancestors 'self' http://*.hl.co.uk https://*.hl.co.uk"
    Content-Type = "text/html; charset=utf-8"
    Date = "Mon, 28 Mar 2022 11:51:45 GMT"
    Expires = "Thu, 19 Nov 1981 08:52:00 GMT"
    Keep-Alive = "timeout=2, max=100"
    Pragma = "no-cache"
    Server = "Apache"
    Set-Cookie = "__sp=private_investor%3D-web_share%3D-web_index%3D-token%3D; expires=Mon, 28-Mar-2022 12:06:45 GMT; Max-Age=900; path=/; domain=.hl.co.uk, __rs=%2Bb5adfQ5kUwMtmiRqwZjw9whgwToCM%2BlZ2QB1%2FnD9HXppk09oorkzbv1Sbj33%2B%2BTrvfloIcquF3d%2FK7xeHb25w%3D%3D%7C0; path=/; domain=.hl.co.uk, ADRUM_BT=deleted; expires=Thu, 01-Jan-1970 00:00:01 GMT; Max-Age=0; path=/, ADRUM_BT=R%3A24%7Cg%3A296d2e27-eff9-4b18-a599-fb750ec1674e1183%7Cn%3Ahl-prod_bbee1771-dc80-4328-8b4d-a5fd0d64b23b%7Ci%3A435951%7Cd%3A1656%7Ce%3A587; expires=Mon, 28-Mar-2022 11:52:17 GMT; Max-Age=30; path=/; secure"
    Transfer-Encoding = "chunked"
    Vary = "Accept-Encoding"
    X-Content-Security-Policy = "script-src 'self' 'unsafe-inline' 'unsafe-eval' https://cdn.appdynamics.com https://www.googleadservices.com https://ssl.google-analytics.com https://*.akamai.net http://*.hl.co.uk https://*.hl.co.uk https://*.verisign.com https://*.websecurity.symantec.com https://*.websecurity.norton.com https://ping.chartbeat.net https://cdn.tt.omtrdc.net https://hargreaveslansdownpl.tt.omtrdc.net https://assets.adobedtm.com https://dpm.demdex.net https://apis.google.com https://www.googletagmanager.com https://*.facebook.net https://www.facebook.com https://googleads.g.doubleclick.net https://www.google.com https://www.google.co.uk https://static.chartbeat.com https://js.stripe.com https://polyfill.io https://static.hl.co.uk/; style-src 'self' 'unsafe-inline' http://*.hl.co.uk https://*.hl.co.uk https://fonts.googleapis.com https://fonts.gstatic.com https://static.hl.co.uk/; frame-ancestors 'self' http://*.hl.co.uk https://*.hl.co.uk"
    X-UA-Compatible = "IE=edge"
```
## /my-accounts/pending_orders[1]

**startedDateTime** = 2022-03-28T12:51:49.907893Z

**REQUEST**

| Key | Value |
| --- | ----- |
| method | POST |
| clean_url | https://online.hl.co.uk/my-accounts/pending_orders |
| request_id | /my-accounts/pending_orders[1] |

**RESPONSE**

| Key | Value |
| --- | ----- |
| status | 200 |
| statusText | OK |
| content | [content/_my-accounts_pending_orders_1.html](content/_my-accounts_pending_orders_1.html)  |
| content[mimeType] |  text/html; charset=utf-8  |
| content[size] | 133832  |

**REQUEST Cookies**

```
    __dat = "62419f2a0f1c42.27309604"
    __dat_ses = "62419f2a0f1c42.27309604"
    __losp = "web_share%3D2-web_index%3D2"
    __mkt = "1"
    __rs = "%2Bb5adfQ5kUwMtmiRqwZjw9whgwToCM%2BlZ2QB1%2FnD9HXppk09oorkzbv1Sbj33%2B%2BTrvfloIcquF3d%2FK7xeHb25w%3D%3D%7C0"
    __sp = "private_investor%3DN-web_share%3D1-web_index%3D1-token%3D"
    ADRUM_BT = "R%3A62%7Cg%3A296d2e27-eff9-4b18-a599-fb750ec1674e1184%7Cn%3Ahl-prod_bbee1771-dc80-4328-8b4d-a5fd0d64b23b%7Ci%3A435972%7Cd%3A1256%7Ce%3A1106"
    at_check = "true"
    cookieCheck = "true"
    hl_cookie_consent = "{\"ao\": true, \"tp\": true}"
    hl_cp = "1"
    hltimer = "{\"tom\": 1648468594955, \"ot\": \"900\", \"tos\": 0, \"smc\": 0, \"HLWN553203\": {\"to\": 1648468594955, \"li\": 1, \"im\": 1, \"ia\": 0, \"ir\": 0, \"rp\": 0, \"sm\": 0, \"lp\": 0, \"lu\": 1648467754955}}"
    HLWEBsession = "01dfb0aa1a8abc7ea90873530fa6c4f7"
    invest = "{\"amount_lump\": \"0\", \"amount_regular\": \"0\", \"investment\": [], \"vmp_matrix\": \"\"}"
    jsCheck = "yes"
    wwwServer = "!/+ClT4XniA15o5raoX99Pvg73eD4QS+dT5zTwBHFetZg8/AOx2ptKxCKM1LW4YPdjg4y7HG9DA=="
```

**REQUEST Headers**

```
    Accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
    Accept-Encoding = "gzip, deflate, br"
    Accept-Language = "en-US,en;q=0.5"
    Connection = "keep-alive"
    Content-Length = "216"
    Content-Type = "application/x-www-form-urlencoded"
    Host = "online.hl.co.uk"
    Origin = "https://online.hl.co.uk"
    Referer = "https://online.hl.co.uk/my-accounts/pending_orders/account/70"
    Sec-Fetch-Dest = "document"
    Sec-Fetch-Mode = "navigate"
    Sec-Fetch-Site = "same-origin"
    Sec-Fetch-User = "?1"
    Sec-GPC = "1"
    Upgrade-Insecure-Requests = "1"
    User-Agent = "Mozilla/5.0 (Linux; Android 4.4.2; GT-P5220) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36"
```
**REQUEST QueryString Param**

```
```

**REQUEST Post Param**

```
    action = "cancel"
    bref = "152147834"
    152147834_trade_type[] = "B"
    152147834_sedol[] = "BDBFK59"
    152147834_stoktitle[] = "Mammoth Energy Services Inc"
    152147834_quantity[] = "50.0"
    152147834_qty_is_money[] = "0"
    cancel = "cancel"
```

**RESPONSE Cookies**

```
    __sp = "private_investor%3DN-web_share%3D1-web_index%3D1-token%3D"
    ADRUM_BT = "R%3A61%7Cg%3A296d2e27-eff9-4b18-a599-fb750ec1674e1185%7Cn%3Ahl-prod_bbee1771-dc80-4328-8b4d-a5fd0d64b23b%7Ci%3A435972%7Cd%3A1365%7Ch%3Ae%7Ce%3A1106"
```

**RESPONSE Headers**

```
    Cache-Control = "no-store, no-cache, must-revalidate"
    Connection = "Keep-Alive"
    Content-Encoding = "gzip"
    Content-Security-Policy = "script-src 'self' 'unsafe-inline' 'unsafe-eval' https://cdn.appdynamics.com https://www.googleadservices.com https://ssl.google-analytics.com https://*.akamai.net http://*.hl.co.uk https://*.hl.co.uk https://*.verisign.com https://*.websecurity.symantec.com https://*.websecurity.norton.com https://ping.chartbeat.net https://cdn.tt.omtrdc.net https://hargreaveslansdownpl.tt.omtrdc.net https://assets.adobedtm.com https://dpm.demdex.net https://apis.google.com https://www.googletagmanager.com https://*.facebook.net https://www.facebook.com https://googleads.g.doubleclick.net https://www.google.com https://www.google.co.uk https://static.chartbeat.com https://js.stripe.com https://polyfill.io https://static.hl.co.uk/; style-src 'self' 'unsafe-inline' http://*.hl.co.uk https://*.hl.co.uk https://fonts.googleapis.com https://fonts.gstatic.com https://static.hl.co.uk/; frame-ancestors 'self' http://*.hl.co.uk https://*.hl.co.uk"
    Content-Type = "text/html; charset=utf-8"
    Date = "Mon, 28 Mar 2022 11:51:50 GMT"
    Expires = "Thu, 19 Nov 1981 08:52:00 GMT"
    Keep-Alive = "timeout=2, max=98"
    Pragma = "no-cache"
    Server = "Apache"
    Set-Cookie = "__sp=private_investor%3DN-web_share%3D1-web_index%3D1-token%3D; expires=Mon, 28-Mar-2022 12:06:50 GMT; Max-Age=900; path=/; domain=.hl.co.uk, ADRUM_BT=deleted; expires=Thu, 01-Jan-1970 00:00:01 GMT; Max-Age=0; path=/, ADRUM_BT=R%3A61%7Cg%3A296d2e27-eff9-4b18-a599-fb750ec1674e1185%7Cn%3Ahl-prod_bbee1771-dc80-4328-8b4d-a5fd0d64b23b%7Ci%3A435972%7Cd%3A1365%7Ch%3Ae%7Ce%3A1106; expires=Mon, 28-Mar-2022 11:52:21 GMT; Max-Age=30; path=/; secure"
    Transfer-Encoding = "chunked"
    Vary = "Accept-Encoding"
    X-Content-Security-Policy = "script-src 'self' 'unsafe-inline' 'unsafe-eval' https://cdn.appdynamics.com https://www.googleadservices.com https://ssl.google-analytics.com https://*.akamai.net http://*.hl.co.uk https://*.hl.co.uk https://*.verisign.com https://*.websecurity.symantec.com https://*.websecurity.norton.com https://ping.chartbeat.net https://cdn.tt.omtrdc.net https://hargreaveslansdownpl.tt.omtrdc.net https://assets.adobedtm.com https://dpm.demdex.net https://apis.google.com https://www.googletagmanager.com https://*.facebook.net https://www.facebook.com https://googleads.g.doubleclick.net https://www.google.com https://www.google.co.uk https://static.chartbeat.com https://js.stripe.com https://polyfill.io https://static.hl.co.uk/; style-src 'self' 'unsafe-inline' http://*.hl.co.uk https://*.hl.co.uk https://fonts.googleapis.com https://fonts.gstatic.com https://static.hl.co.uk/; frame-ancestors 'self' http://*.hl.co.uk https://*.hl.co.uk"
    X-UA-Compatible = "IE=edge"
```