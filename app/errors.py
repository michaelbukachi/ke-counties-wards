from werkzeug.exceptions import NotFound, Unauthorized, Conflict


def before_send(event, hint):
    if 'exc_info' in hint:
        exc_type, exc_value, tb = hint['exc_info']
        if isinstance(exc_value, (NotFound, Unauthorized, Conflict)):
            return None
    return event
