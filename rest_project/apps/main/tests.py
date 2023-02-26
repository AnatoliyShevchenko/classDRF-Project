# Django
from django.test import TestCase

# Local
from .models import (
    Player,
    Stadium,
    Team
)

import math


class PlayerTestCase(TestCase):

    def setUp(self):
        self.player = Player.objects.create(
            name='name',
            surname='surname',
            power=Player.ADULT_TEAM_MIN_POWER,
            age=Player.ADULT_TEAM_MIN_AGE
        )
        self.player2 = Player.objects.create(
            name='name 2',
            surname='surname 2',
            power=Player.ADULT_TEAM_MIN_POWER,
            age=Player.ADULT_TEAM_MIN_AGE
        )
        self.stadium = Stadium.objects.create(
            title='Stadium 1',
            capacity=80000,
            city='Milan'
        )
        self.team = Team.objects.create(
            title='Team 1',
            stadium=self.stadium
        )
        self.stadium2 = Stadium.objects.create(
            title='Stadium 2',
            capacity=80000,
            city='Milan'
        )

    # def test_player_creation(self):
    #     self.assertEqual(self.player.id, 1)
    #     self.assertEqual(self.player2.id, 2)

    # def test_player_fullname(self):
    #     expected_fullname = f'{self.player.name} {self.player.surname}'
    #     self.assertEqual(self.player.fullname, expected_fullname)

    # def test_player_free(self):
    #     self.assertEqual(self.player.status, Player.STATUS_FREE_AGENT)
    #     self.player.free()
    #     self.assertEqual(self.player.status, Player.STATUS_FREE_AGENT)

    # def test_player_retire(self):
    #     self.assertEqual(self.player.status, Player.STATUS_FREE_AGENT)
    #     self.player.retire()
    #     self.assertEqual(self.player.status, Player.STATUS_RETIRED)

    # def test_team(self):
    #     self.assertEqual(self.team.stadium.id, self.stadium.id)
    #     self.team.stadium = self.stadium2
    #     self.assertEqual(self.team.stadium.id, self.stadium2.id)

    # def test_team_power(self):
    #     team = Team.objects.get(id=1)
    #     total = 0
    #     for player in team.players.all():
    #         total += player.power

    #     power = math.ceil(total / 11)
    #     self.assertEqual(team.power, power)

    # def test_change_team(self):
    #     self.assertEqual(self.player.team, self.team1)
    #     self.assertEqual(self.player2.team, self.team2)
    #     self.player.team = self.team2
    #     self.player2.team = self.team
    #     self.assertEqual(self.player.team, self.team1)
    #     self.assertEqual(self.player2.team, self.team2)

    # def test_delete_player(self):
    #     retired = Player.objects.filter(status=Player.STATUS_RETIRED)
    #     team_members = Player.objects.filter(status=Player.STATUS_TEAM_MEMBER)
    #     for player in retired:
    #         player.delete()
    #     for other_player in team_members:
    #         other_player.delete()
        
    #     self.assertTrue(Player.STATUS_RETIRED not in [i.status for i in retired])
    #     self.assertTrue(Player.STATUS_TEAM_MEMBER not in [i.status for i in team_members])

    def test_team_max_power(self):
        team = Team.objects.get(id=1)
        total = 0
        for player in team.players.all():
            total += player.power

        power = math.ceil(total / 11)
        self.assertLessEqual(power, 11)