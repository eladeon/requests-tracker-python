import datetime
import logging
from http.cookiejar import CookieJar
from urllib.parse import urlencode

import requests
from requests import Response, Session, Request
from requests_mock import Mocker

from request import WebRequestType, RequestSessionContext, HttpRequestEntry
from session import IWebSession

logger = logging.getLogger(__name__)


class MockWebSession(IWebSession):
    _session: Session
    _mock_request: Mocker
    _request_session_context: RequestSessionContext

    def __init__(self,
                 default_referer: str = "https://www.mock.com",
                 sensitive_values: list = None,
                 sensitive_params: list = None):
        self._session = requests.Session()
        self._mock_request = Mocker()
        self._request_session_context = RequestSessionContext(
            default_referer=default_referer,
            sensitive_values=sensitive_values,
            sensitive_params=sensitive_params
        )

    def mock_get(self, url: str, status_code: int, params=None, headers=None, response_text=None):
        params = params if params is not None else {}
        headers = headers if headers is not None else {}
        if params is None:
            request_url = url
        else:
            request_url = f"{url}?{urlencode(params)}"
        self._mock_request.get(
            url=request_url,
            headers=headers,
            status_code=status_code,
            text=response_text
        )
        return self._mock_request

    def mock_post(self, url: str, status_code: int, headers=None, response_text=None):
        # data = data if data is not None else {}
        headers = headers if headers is not None else {}
        # self.__mock_request.add_matcher()
        self._mock_request.post(
            url,
            headers=headers,
            status_code=status_code,
            text=response_text
        )
        return self._mock_request

    def _add_http_entry(self, request: Request, response: Response):
        self._request_session_context.append(HttpRequestEntry(
            request=request,
            request_cookies=response.cookies,
            response=response,
            start_time=datetime.datetime.strptime('2022-03-29T14:34:51', '%Y-%m-%dT%H:%M:%S'),  # freeze time
            response_time_ms=50,  # freeze response time
            server_ip_address='127.0.0.1',
            local_ip_address='127.0.0.1'
        ))

    def get(self, url: str, request_type: WebRequestType = WebRequestType.Document,
            params=None, headers=None) -> Response:
        response = self._session.get(url, params=params, headers=headers)

        request = Request(
            url=url,
            method="GET",
            params=params,
            headers=headers
        )

        self._add_http_entry(request, response)

        return response

    def post(self, url: str, request_type: WebRequestType = WebRequestType.Document,
             data=None, headers=None) -> Response:
        response = self._session.post(url, data=data, headers=headers)

        request = Request(
            url=url,
            method="POST",
            data=data,
            headers=headers
        )

        self._add_http_entry(request, response)

        return response

    def __enter__(self):
        self._mock_request.__enter__()
        return self

    def __exit__(self, the_type, value, traceback):
        self._mock_request.__exit__(the_type, value, traceback)

    @property
    def cookies(self) -> CookieJar:
        return self._session.cookies

    @property
    def request_session_context(self) -> RequestSessionContext:
        return self._request_session_context
