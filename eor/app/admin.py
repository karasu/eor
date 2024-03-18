""" register models for admin module """
from django.contrib import admin

# Register your models here.

from .models import Question
from .models import Choice
from .models import Factors
from .models import Team
from .models import Competition
from .models import Match
from .models import Set
from .models import MatchSetsFactors
from .models import ExchangeInfo
from .models import Exchange
from .models import PlayerFactors

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Factors)
admin.site.register(Team)
admin.site.register(Competition)
admin.site.register(Match)
admin.site.register(Set)
admin.site.register(MatchSetsFactors)
admin.site.register(ExchangeInfo)
admin.site.register(Exchange)
admin.site.register(PlayerFactors)
