""" Models module """

from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class PlayerStatus(models.Model):
    """ Stores player status """
    player = models.ForeignKey(
        User, on_delete=models.CASCADE)
    motivated = models.BooleanField()
    activated = models.BooleanField()
    concentrated = models.BooleanField()
    confident = models.BooleanField()
    competitive = models.BooleanField()
    demorged = models.BooleanField()
    cohesioned = models.BooleanField()

class Team(models.Model):
    """ Store team info """
    name = models.CharField(max_length=200)

class Competition(models.Model):
    """ Store competition info """
    name = models.CharField(max_length=200)

class Match(models.Model):
    """ Generic match info """
    competition = models.ForeignKey(
        Competition, on_delete=models.CASCADE)
    home = models.ForeignKey(
        Team, related_name='home_team', on_delete=models.CASCADE)
    visitor = models.ForeignKey(
        Team, related_name='visitor_team', on_delete=models.CASCADE)
    date = models.DateField()
    jornada = models.IntegerField()

class Set(models.Model):
    """ Stores ended set info """
    match = models.ForeignKey(
        Match, on_delete=models.CASCADE)
    num_set = models.IntegerField()
    home_points = models.IntegerField()
    visitor_points = models.IntegerField()

class SetPlayerStatus(models.Model):
    """ Store factors for each set """
    set = models.ForeignKey(Set, on_delete=models.CASCADE)
    factors = models.ForeignKey(PlayerStatus, on_delete=models.CASCADE)

class ExchangeInfo(models.Model):
    """ Info to store in each exchange of points (each row)"""
    team = models.ForeignKey(Match, on_delete=models.CASCADE)
    is_change = models.BooleanField()
    is_time_out = models.BooleanField()
    points = models.IntegerField()

class Exchange(models.Model):
    """ Match row """
    time = models.DateTimeField(default=now)
    set = models.ForeignKey(Set, on_delete=models.CASCADE)
    home_info = models.ForeignKey(
        ExchangeInfo, related_name='home_exchange_info', on_delete=models.CASCADE)
    visitor_info = models.ForeignKey(
        ExchangeInfo, related_name='visitor_exchange_info', on_delete=models.CASCADE)

class ExchangePlayerStatus(models.Model):
    """ Player factors in a point exchange """
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    factors = models.ForeignKey(PlayerStatus, on_delete=models.CASCADE)
