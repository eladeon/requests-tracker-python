"""The HeaderFactory presents ONE consistent Google Chrome (macOS) identity.

These lock in the fix for the earlier mismatched fingerprint: a User-Agent chosen at random from a
list of ten (one malformed), Firefox-style Accept-Language/Encoding, and no Client Hints. Now the
User-Agent, the Client Hints and the Accept-* headers all describe the same Chrome, on every request
type.
"""
from requests_tracker.headers import HeaderFactory
from requests_tracker.request import RequestSessionContext


def _factory():
    ctx = RequestSessionContext(default_referer="https://online.hl.co.uk/",
                                sensitive_values=[], sensitive_params=[])
    return HeaderFactory.create(ctx)


def test_user_agent_is_a_single_chrome_not_random():
    first = _factory()._user_agent
    second = _factory()._user_agent
    assert first == second, "the User-Agent must be fixed, not chosen at random"
    assert "Chrome/" in first and "Macintosh" in first
    assert "Firefox" not in first and "Windows" not in first


def test_doc_get_sends_chrome_client_hints_and_chrome_accept():
    headers = _factory().create_for_doc_get("https://online.hl.co.uk/my-accounts", {})
    assert "Google Chrome" in headers["Sec-Ch-Ua"]
    assert headers["Sec-Ch-Ua-Mobile"] == "?0"
    assert headers["Sec-Ch-Ua-Platform"] == '"macOS"'
    assert headers["Accept-Language"] == "en-GB,en-US;q=0.9,en;q=0.8"
    assert "zstd" in headers["Accept-Encoding"]
    assert "Sec-GPC" not in headers, "the captured Chrome did not send Sec-GPC"


def test_every_request_type_carries_the_same_identity():
    factory = _factory()
    responses = [
        factory.create_for_doc_get("https://online.hl.co.uk/x", {}),
        factory.create_for_xhr_get("https://online.hl.co.uk/x", {}),
        factory.create_for_form_post("https://online.hl.co.uk/x", {}, {"a": "b"}),
        factory.create_for_xhr_post("https://online.hl.co.uk/x", {}, {"a": "b"}),
    ]
    for headers in responses:
        assert headers["Sec-Ch-Ua-Platform"] == '"macOS"'
        assert headers["User-Agent"].startswith("Mozilla/5.0 (Macintosh")
        assert "zstd" in headers["Accept-Encoding"]


def test_additional_headers_take_priority():
    headers = _factory().create_for_doc_get("https://online.hl.co.uk/x", {"Referer": "https://custom/"})
    assert headers["Referer"] == "https://custom/"
