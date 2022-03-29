# requests-tracker-python

This library is useful when you develop / run web scrapers. It allows you to:

| Phase       | Description                                                                                                                                                                                                            |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Analysis    | Convert & filter the HAR file you recorded in your browser to a human-readable markdown file                                                                                                                           |
| Development | Record scraper requests via the WebSession class + convert to a markdown file and compare to the initial recorded version to spot differences. Best done in x2 different tabs in the browser                           |
| Production  | Record scrapers in production & save request history to a HAR file: Useful when debugging bugs / extending your scraper. For example you can add an AWS S3 implementation (implement IRequestSessionStorage interface) |


## HAR Files Explained

HTTP Archive (HAR) format files are an industry standard for exchanging information about HTTP requests and HTTP responses. A HAR file's content is JSON formatted, containing browser interactions with a web site.
https://w3c.github.io/web-performance/specs/HAR/Overview.html

Most browsers will now allow you to record web requests via a "Developer Tools" and then 
allow you to save the set of requests to a single ".har" file

PLEASE NOTE: Unfortunately Google Chrome has a long-standing bug which removes response
content once you navigate away from the page, so we will be using Firefox for recording examples

## Google HAR Viewer

You can use the Google HAR Analyzer: https://toolbox.googleapps.com/apps/har_analyzer/
to view HAR files.

Unfortunately it is not very user-friendly when developing scrapers
* Basic set of filters - would have been nice to add file patterns to exclude files you are not interested in (i.e. '.css', '.js')
* Too 'noisy' when trying to compare sets of headers/cookies/parameters
* There is a security concern that you might be uploading recorded HAR files containing sensitive information 

Which is why a local markdown version is preferable for our purposes.

## Examples:

**1) Converting a recorded HAR file to Markdown:**

```
python3 requests_tracker/har2md.py tests/input/hargreaves-example.har -o session_cache/my_example --v 
```

**2) Run scraper code, save requests to HAR file, convert to Markdown :**

```
python3 examples/scraper.py 
```

# Inspired by:

https://github.com/S1M0N38/har2py

# How to record a HAR file

In this example we are using Firefox Inspect Development Tools to record a HAR file.

```
    Open Inspector ("Right-Click Window > Inspect")
	On "Storage" tab
		Clear *.hl.co.uk" Cookies
	On "Network" tab:
	    Click on gear on the right
		Check "Perist Logs"
		On the right, clickon the the dustbin icon to clear logs
	Address Bar: 
		Start user journey with first URL
	....
	[When you are finished with journey]
	Inspect Tools -> Network Tab:
		Click on the gear icon on the right
		Click on the "Save All As HAR"
```


# Viewing markdown files in your browser

You may need to install the markdown viewer extension +
configure it to work with local files (https://addons.mozilla.org/en-GB/firefox/addon/markdown-viewer-webext/)

* Save the HAR file ('example.har') to a local temporary folder (i.e. "session_cache")
* Use the har2md.py script to convert it to a markdown file

```
python3 har2md.py ../../session_cache/example.har --v
```
* Open the markdown file in the browser

```
* file:///[MY LOCATION]/session_cache/example/output.md
```

# Known Issues

https://github.com/elastic/ecs/pull/1804

Affects Jinja2 2.x

ERROR:
```
ImportError: cannot import name 'soft_unicode' from 'markupsafe'
```

WORKAROUND:
```
pip uninstall MarkupSafe
pip install MarkupSafe==2.0.0
```
