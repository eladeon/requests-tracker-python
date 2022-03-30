import http
from pathlib import Path

from requests_tracker.mocks import MockWebSession
from requests_tracker.renderers import HAR2MarkdownRenderer, Requests2HARRenderer
from requests_tracker.session import IWebSession
from requests_tracker.util import FileHelper, LogHelper

LogHelper.configure_std_out()


def assert_files_equal(expected_relative_folder: str, actual_relative_folder: str, file_name: str):
    expected_file_path = Path(__file__).parent.joinpath(expected_relative_folder, file_name)
    actual_file_path = Path(__file__).parent.joinpath(actual_relative_folder, file_name)
    expected_file_contents = FileHelper.read_file_contents(str(expected_file_path))
    actual_file_contents = FileHelper.read_file_contents(str(actual_file_path))
    assert expected_file_contents == actual_file_contents


def test_HAR2MarkdownRenderer():

    input_file = Path(__file__).parent.joinpath('input/hargreaves-example.har')
    output_folder = Path(__file__).parent.joinpath('temp/hargreaves-example')
    exclude_patterns = []

    renderer = HAR2MarkdownRenderer()
    renderer.exec(
        input_file=str(input_file),
        output_folder=str(output_folder),
        exclude_patterns=exclude_patterns
    )

    assert_files_equal('output/hargreaves-example', 'temp/hargreaves-example',
                       'output.md')
    assert_files_equal('output/hargreaves-example/content', 'temp/hargreaves-example/content',
                       '_my-accounts_1.html')
    assert_files_equal('output/hargreaves-example/content', 'temp/hargreaves-example/content',
                       '_my-accounts_pending_orders_1.html')
    assert_files_equal('output/hargreaves-example/content', 'temp/hargreaves-example/content',
                       '_my-accounts_pending_orders_account_70_1.html')
    assert_files_equal('output/hargreaves-example/content', 'temp/hargreaves-example/content',
                       '_my-accounts_pending_orders_account_70_2.html')


def test_HAR2MarkdownRenderer_with_filter():

    input_file = Path(__file__).parent.joinpath('input/hargreaves-example.har')
    output_folder = Path(__file__).parent.joinpath('temp/hargreaves-example-filter')
    exclude_patterns = ['account/70']

    renderer = HAR2MarkdownRenderer()
    renderer.exec(
        input_file=str(input_file),
        output_folder=str(output_folder),
        exclude_patterns=exclude_patterns
    )

    assert_files_equal('output/hargreaves-example-filter', 'temp/hargreaves-example-filter',
                       'output.md')
    assert_files_equal('output/hargreaves-example-filter/content', 'temp/hargreaves-example-filter/content',
                       '_my-accounts_1.html')
    assert_files_equal('output/hargreaves-example-filter/content', 'temp/hargreaves-example-filter/content',
                       '_my-accounts_pending_orders_1.html')


class MockService():
    def login_step_one(self, web_session: IWebSession):
        response = web_session.post(
            url='https://www.dummy.com/account/login-step-1',
            data={
                'username': "test-user@yahoo.com",
                'password': "1234578910",
                'date_of_birth': "1978/10/10",
                'secure-number[1]': '1',
                'secure-number[3]': '2',
                'secure-number[5]': '3'
            }
        )
        response_html = response.text
        return response_html


def test_Requests2HARRenderer():

    response_html_file_path = Path(__file__).parent.joinpath('input/requests-2-har-example.html')
    actual_har_file_path = Path(__file__).parent.joinpath('temp/requests-2-har-example.har')

    response_html = FileHelper.read_file_contents(str(response_html_file_path))

    # obfuscates sensitive values:
    sensitive_values = ['1978/10/10', '11689830']
    sensitive_params = ['username', 'password', 'secure-number[']

    with MockWebSession(sensitive_values=sensitive_values, sensitive_params=sensitive_params) as web_session:

        web_session.mock_post(
            url='https://www.dummy.com/account/login-step-1',
            response_text=response_html,
            status_code=int(http.HTTPStatus.OK)
        )

        mock_service = MockService()
        mock_service.login_step_one(web_session=web_session)

        renderer = Requests2HARRenderer()

        actual_har_json = renderer.exec(web_session.request_session_context)
        FileHelper.write_file(str(actual_har_file_path), actual_har_json)

        assert_files_equal('output/', 'temp/',
                           'requests-2-har-example.har')
