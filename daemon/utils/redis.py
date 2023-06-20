import functools

def async_redis_method(func):

    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            result = await func(*args, **kwargs)
        except Exception as exc:
            raise ConnectionError('Redis have problems') from exc
        return result

    return wrapper
