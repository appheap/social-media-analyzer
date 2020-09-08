import json
import typing
from collections import OrderedDict
from sortedcontainers import SortedDict
import os


def default(obj):
    if obj is None:
        return None
    if isinstance(obj, bytes):
        return repr(obj)

    # https://t.me/pyrogramchat/167281
    # Instead of re.Match, which breaks for python <=3.6
    if isinstance(obj, typing.Match):
        return repr(obj)
    return OrderedDict({
        "_": obj.__class__.__name__,
        **{
            attr: getattr(obj, attr)
            for attr in filter(lambda x: not x.startswith("_"), obj.__dict__)
            if getattr(obj, attr) is not None
        }
    }) if hasattr(obj, '__dict__') else None


def prettify(obj, sort_keys=False):
    return json.dumps(obj, indent=4, default=default, sort_keys=sort_keys, ensure_ascii=False)


from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)
