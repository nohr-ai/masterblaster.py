from datetime import datetime
from dateutil import parser
from typing import Optional

__all__ = [
    "GameAccount",
]


class GameAccount:
    """
    Class for GameAccount objects, related to one player

    Supported games: ["Counter-Strike", "Rocket League", "Chess"]

    :param id: The gameaccount id
    :param nick: The gameaccount nickname
    :param avatarUrl: The gameaccount avatar url
    :param gameId: The game id
    :param isConnected: Whether or not the gameaccount is connected
    :param connectedAt: When the gameaccount was connected

    :ivar id: The gameaccount id
    :ivar nick: The gameaccount nickname
    :ivar avatar_url: The gameaccount avatar url
    :ivar gameId: The game id
    :ivar isConnected: Whether or not the gameaccount is connected
    :ivar connectedAt: When the gameaccount was connected
    """

    def __init__(
        self,
        id: str,
        nick: str,
        avatarUrl: str,
        gameId: str,
        isConnected: bool,
        connectedAt: Optional[datetime],
    ) -> None:
        self.id: str = id
        self.nick: str = nick
        self.avatar_url: str = avatarUrl
        self.game_id: str = gameId
        self.is_connected: bool = isConnected
        self.connected_at: Optional[datetime] = parser.isoparse(connectedAt)
