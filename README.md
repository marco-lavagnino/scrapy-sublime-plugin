# Scrapy Snippets for Sublime Text

This package provides handy snippets for working with [scrapy](http://scrapy.org/), the python tool for making web spiders. It also provides palette commands for parsing request parameters from [Postman](https://www.getpostman.com/).

## Installation

Clone this package in your `Packages/` directory. No Package Control support yet :)

## Snippets

Snippets assume your spider has a `BASE_URL`attribute. This prevents code repetition and makes your code easily portable in case the website changes it's base url.

Snippets for the most common requests are provided:
- _Get_: for sending a request with url request parameters, like mysite.com?parameter=value
- _Post_: for `X-www-Form-Urlencoded` requests
- _Json_: for POST requests with `application/json` content-type
- A 'redirect' method, useful when you need to send a GET request without parameters.
- A 'last' method that opens up the received response in the browser and starts an ipdb shell, useful for debugging the response or playing around with xpaths.
- A asp parameter extractor, for easily getting `__VIEWSTATE`, `__VIEWSTATEGENERATOR` and `__EVENTVALIDATION` from a response.

## Commands

#### Format from Postman
If you're using Postman to inspect your requests to a site, you can copy & paste the parameters in 'bulk-edit' mode, and paste them into your spider. Then, select all the lines you just pasted and from the command palette execute `Scrapy: Format from Postman`. The parameters will be formatted as python's dictionary keys and values.

#### Instance Item

Copy an item class definition in your spider. Then, select all the class definition lines and execute `Scrapy: Yield Item`. The definition will be formatted into a `yield ClassInstance()` statement.
