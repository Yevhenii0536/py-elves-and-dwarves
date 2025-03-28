from players.player import Player
from players.elves.elf import Elf
from players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: [Player]) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elves: [Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: [Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
