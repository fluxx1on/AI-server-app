import asyncio
from typing import List, TypeVar
from . import redis_client
from .models import FightLog
from .consumers import MapUpdatesConsumer

def get_fight_fr(
    map_id: str | int,
    fight_id: str | int
) -> str:
    return f'map:{str(map_id)}:fight:{str(fight_id)}'

def get_human_fr(
    user_id: str | int
) -> str:
    return f'user:{str(user_id)}'

def get_mob_fr(
    map_id: str | int,
    mob_id: str | int
) -> str:
    return f'map:{str(map_id)}:mob:{str(mob_id)}'

class Battle:
     
    def __init__(
        self, consumer: MapUpdatesConsumer, mob_id: int
    ) -> None:
        # Wait for PvP
        # self.consumers: List[MapUpdatesConsumer] = [consumer]
        self.consumer: MapUpdatesConsumer = consumer
        self.mobs_id: List[int] = [mob_id]
        self.fight_id: int
        self.postinit()
            
    def postinit(self) -> None:

        def try_to_setid(new_id) -> None:
            if redis_client.hsetnx(
                get_fight_fr(self.consumer.map_id, self.fight_id), mapping=data
            ) == 0:
                return try_to_setid(new_id=new_id+1)
            else:
                return new_id

        data = {
            'human1': str(self.consumer.user_id),
            'mob1': str(self.mobs_id[0])
        }
        new_id = redis_client.hlen(f'map:{str(self.consumer.map_id)}:fight')
        self.fight_id = try_to_setid(new_id=new_id)

    def attack(self) -> int:
        pass

    def __del__(self) -> None:
        pipeline = redis_client.pipeline()
        pipeline.hgetall(get_fight_fr(self.consumer.map_id, self.fight_id))
        for mob_id in self.mobs_id:
            pipeline.hget(get_mob_fr(self.consumer.map_id, mob_id))
        fight_data = pipeline.execute()
        opposites, mobs_stats = fight_data[0], fight_data[1::]
        fight = FightLog()
        fight.save()
        fight.serialize(opposites=opposites, map_id=self.consumer.map_id, mobs_stats=mobs_stats)