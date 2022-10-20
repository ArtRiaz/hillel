import functools


class UnexpectedTypeException(Exception):
    pass


def expected(expected_types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func_result = func(*args, **kwargs)
            if not isinstance(func_result, expected_types):
                raise Exception
            else:
                func(*args, **kwargs)

        return wrapper

    return decorator


@expected((str, int))
def func(value):
    return value


func(("34", 45, 65786, "i love"))