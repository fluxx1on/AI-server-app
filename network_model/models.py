from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser

class Creature(models.Model):

    @staticmethod
    def redis_serializer():
        return [
            'id', 'health', 'attack'
        ]

    class friendship(models.IntegerChoices):
        peaceful = 0, _("Peaceful")
        neutral = 1, _("Neutral")
        agressive = 2, _("Agressive")

    name = models.CharField("Name", max_length=63, unique=True)
    description = models.CharField("Description", max_length=511, default="Common creature")
    health = models.IntegerField("Health", null=False)
    attack = models.IntegerField("Attack", null=False)

    activity = models.IntegerField("Activity", choices=friendship.choices,
                                   default=friendship.neutral)

    def __str__(self) -> str:
        return "%s_%s" % (self.name, self.activity)

    class Meta:
        verbose_name = "Creature"
        verbose_name_plural = "Creatures"


class Location(models.Model):

    name = models.CharField("Name", max_length=63, unique=True)
    description = models.CharField("Description", max_length=511, unique=True)
    background = models.FileField("Map Image", upload_to='./media/')

    allowed_creatures = models.ManyToManyField(
        Creature, description="Ocurred mobs for this location", related_name="residence"
    )

    def __str__(self) -> str:
        return "%s_%s" % (self.name, self.description)

    class Meta:
        verbose_name = "Map"
        verbose_name_plural = "Maps"

class User(AbstractBaseUser):

    nickname = models.CharField("Nickname", max_length=24, unique=True)
    health = models.IntegerField("Health", null=False, default=35)
    attack = models.IntegerField("Attack", null=False, default=5)

    def __str__(self) -> str:
        return self.nickname

    class Meta:
        verbose_name = "Player"
        verbose_name_plural = "Players"