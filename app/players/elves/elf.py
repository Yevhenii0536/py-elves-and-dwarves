from app.players.player import Player


class Elf(Player):
    def __init__(
        self,
        nickname: str,
        musical_instrument: str,
    ) -> None:
        super().__init__(nickname=nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(
            f"{self._nickname} is playing a "
            f"song on the {self._musical_instrument}"
        )

    def player_info(self) -> None:
        pass

    def get_rating(self) -> None:
        pass
