from abc import abstractmethod, ABC


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self._nickname = nickname

    @abstractmethod
    def get_rating(self) -> None:
        pass

    @abstractmethod
    def player_info(self) -> None:
        pass
