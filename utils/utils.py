import json
import typing
from collections import OrderedDict


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


def default_no_class_name(obj):
    if obj is None:
        return None
    if isinstance(obj, bytes):
        return repr(obj)

    # https://t.me/pyrogramchat/167281
    # Instead of re.Match, which breaks for python <=3.6
    if isinstance(obj, typing.Match):
        return repr(obj)
    return OrderedDict({
        **{
            attr: getattr(obj, attr)
            for attr in filter(lambda x: not x.startswith("_"), obj.__dict__)
            if getattr(obj, attr) is not None
        }
    }) if hasattr(obj, '__dict__') else None


def prettify(obj, sort_keys=False, include_class_name=True):
    return json.dumps(obj,
                      indent=4,
                      default=default if include_class_name else default_no_class_name,
                      sort_keys=sort_keys,
                      ensure_ascii=False)
