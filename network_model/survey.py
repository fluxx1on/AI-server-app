from channels.layers import get_channel_layer
from . import redis_client

class Battle:
     
    def __init__(self, user_id: int, mob_id: int) -> None:
        super().__init__(user_id=user_id,
                         mob_id=mob_id)

