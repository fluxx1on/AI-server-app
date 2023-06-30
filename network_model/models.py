from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from typing import List, Literal
from network_model.managers import CustomUserManager
from server import settings

class Creature(models.Model):

    @staticmethod
    def redis_serializer() -> tuple:
        return ('id', 'health', 'attack')

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

    @staticmethod
    def format() -> tuple[Literal, Literal]:
        return settings.MAP_FORMAT   # (X, Y)


    name = models.CharField("Name", max_length=63, unique=True)
    description = models.CharField("Description", max_length=511, unique=True)
    background = models.FileField("Map Image", upload_to='./')

    allowed_creatures = models.ManyToManyField(
        Creature, help_text="Ocurred mobs for this location", related_name="residence"
    )

    def __str__(self) -> str:
        return "%s_%s" % (self.name, self.description)

    class Meta:
        verbose_name = "Map"
        verbose_name_plural = "Maps"

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField("Username", max_length=24, unique=True, null=False)
    health = models.IntegerField("Health", null=False, default=35)
    attack = models.IntegerField("Attack", null=False, default=5)

    current_location = models.ForeignKey(
        Location, verbose_name='Current location', on_delete=models.DO_NOTHING, null=True
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "username"

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name = "Player"
        verbose_name_plural = "Players"

class FightLog(models.Model):

    created_at = models.DateTimeField('Ended', auto_created=True)
    result = models.JSONField('Result', null=True, blank=True)

    players = models.ManyToManyField(
        User, verbose_name='Players', related_name='fights'
    )

    mobs = models.ManyToManyField(
        Creature, verbose_name='Mobs'
    )

    location = models.ForeignKey(
        Location, verbose_name="Location", related_name='fights_on_map',
        on_delete=models.DO_NOTHING
    )

    def serialize(
        self, opposites: dict, map_id: int,
        mobs_stats : List[dict]
    ) -> None:
        try:
            player = User.objects.get(pk=opposites['human1'])
            location = Location.objects.get(pk=map_id)
        except Exception as exc:
            raise ValueError('Неподходящие данные') from exc
        
        self.players.add(*[player])
        self.save()
        

    def __str__(self) -> str:
        return self.created_at

    class Meta:
        verbose_name = "Fight"
        verbose_name_plural = "Fights"
