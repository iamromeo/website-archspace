from game.signals import turn
from players.signals import power

def on_turn(player, turn, **kwargs):
    for planet in player.planets.all():
        pass

turn.connect(on_turn)

def on_power(player, **kwargs):
    total_power = 0
    for planet in player.planets.all():
        total_power += planet.get_power()
    return total_power

power.connect(on_power)
