from .errors import StatusIsNotSuccess


def check_response(resp, *args, **kwargs):
    # TODO: log a request which were made before
    resp.raise_for_status()
    if resp.json()['status'] != "success":
        raise StatusIsNotSuccess
