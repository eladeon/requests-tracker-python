from urllib.parse import urlencode

from .request import RequestSessionContext, UrlHelper
from .util import DictionaryHelper


class IHeaderFactory:

    def create_for_doc_get(self, url: str, additional_headers: dict) -> dict:
        pass

    def create_for_xhr_get(self, url: str, additional_headers: dict) -> dict:
        pass

    def create_for_form_post(self, url: str, additional_headers: dict, data: dict) -> dict:
        pass

    def create_for_xhr_post(self, url: str, additional_headers: dict, data: dict) -> dict:
        pass


class HeaderFactory(IHeaderFactory):
    """Builds request headers for ONE consistent browser identity: Google Chrome on macOS.

    The User-Agent, the Client Hints and the Accept-* headers all describe the same browser, so the
    traffic looks like a real Chrome. Previously a User-Agent was chosen at random from a list of ten
    (one entry malformed, two merged by a missing comma) while Firefox-style Accept-Language/Encoding
    and no Client Hints were sent regardless -- a mismatched fingerprint any site could spot. The
    values below track a real captured Chrome session; when the emulated Chrome version moves,
    update the User-Agent and the Sec-Ch-Ua version together.
    """

    USER_AGENT = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36')
    SEC_CH_UA = '"Google Chrome";v="155", "Chromium";v="155", "Not(A:Brand";v="24"'
    SEC_CH_UA_MOBILE = '?0'
    SEC_CH_UA_PLATFORM = '"macOS"'
    ACCEPT_LANGUAGE = 'en-GB,en-US;q=0.9,en;q=0.8'
    ACCEPT_ENCODING = 'gzip, deflate, br, zstd'
    ACCEPT_DOCUMENT = ('text/html,application/xhtml+xml,application/xml;q=0.9,image/jxl,image/avif,'
                       'image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7')

    _user_agent: str
    _request_session_context: RequestSessionContext

    def __init__(self, request_session_context: RequestSessionContext, user_agent: str):
        self._request_session_context = request_session_context
        self._user_agent = user_agent

    def _client_hints(self) -> dict:
        """Chrome sends the low-entropy Client Hints on every request."""
        return {
            'Sec-Ch-Ua': HeaderFactory.SEC_CH_UA,
            'Sec-Ch-Ua-Mobile': HeaderFactory.SEC_CH_UA_MOBILE,
            'Sec-Ch-Ua-Platform': HeaderFactory.SEC_CH_UA_PLATFORM,
        }

    def create_for_doc_get(self, url: str, additional_headers: dict) -> dict:
        default_headers = {
            'Host': UrlHelper.get_host(url),
            'Connection': 'keep-alive',
            **self._client_hints(),
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': self._user_agent,
            'Accept': HeaderFactory.ACCEPT_DOCUMENT,
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': self._request_session_context.get_last_referer(),
            'Accept-Encoding': HeaderFactory.ACCEPT_ENCODING,
            'Accept-Language': HeaderFactory.ACCEPT_LANGUAGE,
        }

        return DictionaryHelper.merge_with_priority(additional_headers, default_headers)

    def create_for_xhr_get(self, url: str, additional_headers: dict) -> dict:
        default_headers = {
            'Host': UrlHelper.get_host(url),
            'Connection': 'keep-alive',
            **self._client_hints(),
            'Accept': 'text/javascript, application/javascript, */*',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': self._user_agent,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': self._request_session_context.get_last_referer(),
            'Accept-Encoding': HeaderFactory.ACCEPT_ENCODING,
            'Accept-Language': HeaderFactory.ACCEPT_LANGUAGE,
        }

        return DictionaryHelper.merge_with_priority(additional_headers, default_headers)

    def create_for_form_post(self, url: str, additional_headers: dict, data: dict) -> dict:

        default_headers = {
            'Host': UrlHelper.get_host(url),
            'Connection': 'keep-alive',
            'Content-Length': str(len(urlencode(data))),
            **self._client_hints(),
            'Upgrade-Insecure-Requests': '1',
            'Origin': UrlHelper.get_origin(url),
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': self._user_agent,
            'Accept': HeaderFactory.ACCEPT_DOCUMENT,
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': self._request_session_context.get_last_referer(),
            'Accept-Encoding': HeaderFactory.ACCEPT_ENCODING,
            'Accept-Language': HeaderFactory.ACCEPT_LANGUAGE,
        }

        return DictionaryHelper.merge_with_priority(additional_headers, default_headers)

    def create_for_xhr_post(self, url: str, additional_headers: dict, data: dict) -> dict:

        default_headers = {
            'Host': UrlHelper.get_host(url),
            'Connection': 'keep-alive',
            'Content-Length': str(len(urlencode(data))),
            **self._client_hints(),
            'Accept': '*/*',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': self._user_agent,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': UrlHelper.get_origin(url),
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': self._request_session_context.get_last_referer(),
            'Accept-Encoding': HeaderFactory.ACCEPT_ENCODING,
            'Accept-Language': HeaderFactory.ACCEPT_LANGUAGE,
        }

        return DictionaryHelper.merge_with_priority(additional_headers, default_headers)

    @staticmethod
    def create(request_session_context: RequestSessionContext):
        return HeaderFactory(request_session_context, HeaderFactory.USER_AGENT)
