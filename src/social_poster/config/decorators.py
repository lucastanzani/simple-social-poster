import inspect
from functools import wraps


def at_most_one_defined_true(keyword, *keywords):
    keywords = (keyword,) + keywords

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if sum(
                    k in keywords for k in kwargs if
                    isinstance(kwargs[k], bool)
                    and kwargs[k] is not None
                    and kwargs[k] is True
            ) > 1:
                raise TypeError('You must specify at most one of "{}" as true'.format(', '.join(keywords)))
            return func(*args, **kwargs)

        return inner

    return wrapper


def exactly_one_defined(keyword, *keywords):
    keywords = (keyword,) + keywords

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if sum(k in keywords for k in kwargs if k in kwargs and kwargs[k] is not None) != 1:
                raise TypeError('You must specify exactly one one of "{}"'.format(', '.join(keywords)))
            return func(*args, **kwargs)

        return inner

    return wrapper


def at_least_one_defined(keyword, *keywords):
    keywords = (keyword,) + keywords

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if sum(k in keywords for k in kwargs if k in kwargs and kwargs[k] is not None) < 1:
                raise TypeError('You must specify exactly one one of "{}"'.format(', '.join(keywords)))
            return func(*args, **kwargs)

        return inner

    return wrapper


def get_default_args(func):
    signature = inspect.signature(func)
    return {
        k: v.default
        for k, v in signature.parameters.items()
        if v.default is not inspect.Parameter.empty
    }


def all_defined(keyword, *keywords):
    keywords = (keyword,) + keywords

    def wrapper(func):
        defaults = get_default_args(func=func)

        @wraps(func)
        def inner(*args, **kwargs):
            if any([k in keywords and k is not None for k in kwargs]):
                if sum(k in keywords for k in kwargs if
                       kwargs[k] is not None or
                       (k in defaults and defaults[k] != kwargs[k])) != len(keywords):
                    raise TypeError('You must specify all of "{}"'.format(', '.join(keywords)))
            return func(*args, **kwargs)

        return inner

    return wrapper
