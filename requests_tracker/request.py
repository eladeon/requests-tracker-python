import logging
import socket
from datetime import datetime
from enum import Enum
from http.cookiejar import CookieJar
from typing import List
from urllib.parse import urlparse, parse_qs, urlencode

import requests

logger = logging.getLogger(__name__)


class UrlHelper:
    @staticmethod
    def get_origin(url: str):
        parsed_url = urlparse(url)
        return f"{parsed_url.scheme}://{parsed_url.hostname}"

    @staticmethod
    def get_host(url: str):
        parsed_url = urlparse(url)
        return parsed_url.hostname

    @staticmethod
    def get_referrer(previous_url: str):
        parsed_url = urlparse(previous_url)
        return f"{parsed_url.scheme}://{parsed_url.hostname}{parsed_url.path}"


class NetworkHelper:
    @staticmethod
    def get_local_ip_address():
        try:
            ip_address = socket.gethostbyname(socket.gethostname())
        except socket.error as err_msg:
            logger.warning(f"Failed to retrieve IP address for local host {err_msg}")
            ip_address = '0.0.0.0'
        return ip_address

    @staticmethod
    def get_remote_server_ip_address(remote_url: str):
        remote_host = None
        try:
            parsed_uri = urlparse(remote_url)
            remote_host = parsed_uri.netloc
            ip_address = socket.gethostbyname(remote_host)
        except socket.error as err_msg:
            logger.warning(f"Failed to retrieve IP address for remote-url ({remote_url}),"
                           f" remote-host ({remote_host}): {err_msg}")
            ip_address = '0.0.0.0'
        return ip_address


class WebRequestType(Enum):
    Document = 'document'
    XHR = 'xhr'

    def __str__(self):
        return self.name


class HttpRequestEntry:
    _request: requests.Request
    _request_cookies: CookieJar
    _response: requests.Response
    _start_time: datetime
    _response_time_ms: float
    _server_ip_address: str
    _local_ip_address: str

    def __init__(self,
                 request: requests.Request,
                 request_cookies: CookieJar,
                 response: requests.Response,
                 start_time: datetime,
                 response_time_ms: float,
                 server_ip_address: str,
                 local_ip_address: str,
                 ):
        self._request = request
        self._request_cookies = request_cookies
        self._response = response
        self._start_time = start_time
        self._response_time_ms = response_time_ms
        self._server_ip_address = server_ip_address
        self._local_ip_address = local_ip_address

    @property
    def request(self):
        return self._request

    @property
    def request_cookies(self):
        return self._request_cookies

    @property
    def response(self):
        return self._response

    @property
    def start_time(self):
        return self._start_time

    @property
    def response_time_ms(self):
        return self._response_time_ms

    @property
    def server_ip_address(self):
        return self._server_ip_address

    @property
    def local_ip_address(self):
        return self._local_ip_address

    def get_query_string_parameters(self) -> dict:
        parsed_url = urlparse(self._request.url)
        return parse_qs(parsed_url.query)

    def get_post_param_as_text(self) -> str:
        return urlencode(self._request.params)


class RequestSessionContext:
    _session_start_time: datetime
    _default_referer: str
    _sensitive_values: list
    _sensitive_params: list
    _entries: List[HttpRequestEntry]

    def __init__(self,
                 default_referer: str,
                 sensitive_values: list = None,
                 sensitive_params: list = None):
        self._session_start_time = datetime.now()
        self._default_referer = default_referer
        self._sensitive_values = sensitive_values if sensitive_values is not None else []
        self._sensitive_params = sensitive_params if sensitive_params is not None else []
        self._entries = []

    @property
    def session_start_time(self):
        return self._session_start_time

    @property
    def entries(self):
        return self._entries

    def append(self, http_entry: HttpRequestEntry):
        return self._entries.append(http_entry)

    def get_last_referer(self) -> str:
        last_response_url = next((http_entry.response.url for http_entry in reversed(self._entries)
                                  if 'ajax' not in http_entry.response.url), None)

        if last_response_url is not None:
            return UrlHelper.get_referrer(last_response_url)

        return self._default_referer

    @property
    def sensitive_values(self):
        return self._sensitive_values

    @property
    def sensitive_params(self):
        return self._sensitive_params
