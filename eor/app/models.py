""" Models module """

from django.db import models

from django.contrib.auth.models import User

class Question(models.Model):
    """ Stores a poll question """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    """ Stores a question answer (choice) """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Factors(models.Model):
    """ Stores player status """
    player = models.ForeignKey(User, on_delete=models.CASCADE)
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

class Match(models.Model):
    """ Generic match info """
    competition = models.CharField(max_length=200)
    jornada = models.IntegerField()
    date = models.DateField()
    home = models.ForeignKey(Team, on_delete=models.CASCADE)
    visitant = models.ForeignKey(Team, on_delete=models.CASCADE)

class Set(models.Model):
    """ Stores ended set info """
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    num_set = models.IntegerField()
    home_points = models.IntegerField()
    visitor_points = models.IntegerField()

class MatchSetsFactors(models.Model):
    """ Store factors for each match set """
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    set = models.ForeignKey(Set, on_delete=models.CASCADE)
    factors = models.ForeignKey(Factors, on_delete=models.CASCADE)

class ExchangeInfo(models.Model):
    """ Info to store in each exchange of points """
    # instant = match row entry
    instant = models.IntegerField()
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    team = models.ForeignKey(Match, on_delete=models.CASCADE)
    is_change = models.BooleanField()
    is_time = models.BooleanField()
    points = models.IntegerField()

class MatchExchange(models.Model):
    """ Match row """
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    instant = models.IntegerField()
    home_info = models.ForeignKey(ExchangeInfo, on_delete=models.CASCADE)
    visitor_info = models.ForeignKey(ExchangeInfo, on_delete=models.CASCADE)
