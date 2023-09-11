from datetime import datetime
from dateutil import parser
from typing import Union, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from _typeshed import SupportsRead


class GameAccount:
    def __init__(
        self,
        id: str,
        nick: str,
        avatarUrl: str,
        gameId: str,
        isConnected: bool,
        connectedAt,  # <- This dude has to be typed
    ) -> None:
        self.id: str = id
        self.nick: str = nick
        self.avatar_url: str = avatarUrl
        self.game_id: str = gameId
        self.is_connected: bool = isConnected
        self.connected_at: Optional[datetime] = parser.isoparse(connectedAt)


if __name__ == "__main__":
    pass
