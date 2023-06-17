from aioredis import Redis, ConnectionPool
from django.conf import settings

# Short-live substances
pool = ConnectionPool.from_url(settings.REDIS_DB)
redis_client = Redis(connection_pool=pool)
