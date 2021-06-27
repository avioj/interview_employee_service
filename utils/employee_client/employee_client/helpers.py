import allure

from .errors import StatusIsNotSuccess


def check_response(resp, *args, **kwargs):
    allure.attach("method", resp.request.method)
    allure.attach("body", resp.request.body)
    allure.attach("url", resp.request.url)
    allure.attach("response body", resp.text)
    resp.raise_for_status()
    if resp.json()['status'] != "success":
        raise StatusIsNotSuccess
