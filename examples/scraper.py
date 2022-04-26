import logging
import time
import traceback
from pathlib import Path

from requests_tracker.request import WebRequestType
from requests_tracker.session import WebSessionFactory
from requests_tracker.storage import convert_HAR_to_markdown, write_HAR_to_local_file, CookiesFileStorage
from requests_tracker.util import LogHelper

if __name__ == '__main__':

    logger = LogHelper.configure(logging.DEBUG)

    session_cache_path = Path(__file__).parent.parent.joinpath('session_cache')

    cookies_storage = CookiesFileStorage(session_cache_path)

    # creates session and pre-loads cookies from persisted local cookie storage
    web_session = WebSessionFactory.create(
        cookies_storage,
        default_referer='https://www.jet2holidays.com',
        sensitive_values=[], sensitive_params=[])

    try:
        response1 = web_session.get('https://www.jet2holidays.com')

        # print(response1.text)

        time.sleep(1)

        response2 = web_session.post(
            url='https://www.jet2holidays.com/api/jet2/sitesearch/HotelAndRegionList',
            request_type=WebRequestType.XHR,
            data={
                'term': 'radi',
                'maxResults': 30
            }
        )

        print(response2.text)

    except Exception as ex:
        logger.error(traceback.print_exc())
    finally:
        # persists cookies to local file
        cookies_storage.save(web_session.cookies)
        # writes to 'session-cache/session-DD-MM-YYYY HH-MM-SS.har' file
        write_HAR_to_local_file(session_cache_path, web_session.request_session_context)
        # converts HAR file to markdown file + response files in folder 'session-cache/session-DD-MM-YYYY HH-MM-SS/'
        convert_HAR_to_markdown(session_cache_path, web_session.request_session_context)
