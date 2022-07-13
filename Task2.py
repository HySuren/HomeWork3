import functools

def cache(func):
    """Кэш предыдущих вызовов функций"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper.cache:
            wrapper.cache[cache_key] = func(*args, **kwargs)
        return wrapper.cache[cache_key]
    wrapper.cache = dict()
    return wrapper

@cache
def multiplier(number: int):
    return number * 2

print(multiplier(10))
print(multiplier(5))
print(multiplier(23))
print(multiplier(10))
