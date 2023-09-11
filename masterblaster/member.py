from datetime import datetime
from dateutil import parser

from .player import Player

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from _typeshed import SupportsRead


class Member:
    def __init__(
        self,
        player: dict,
        email: str,
        name: str,
        playerId: str,
        role: int,
        addedAt: str,
        invitedAt,  # Union[str, bytes, SupportsRead[Union[str, bytes]]],
    ) -> None:
        self.player: Player = Player(**player)
        self.email: str = email
        self.name: str = name
        self.player_id: str = playerId
        self.role: int = role
        self.added_at: datetime = parser.isoparse(addedAt)
        self.invited_at: Optional[datetime] = (
            None if not invitedAt else parser.isoparse(invitedAt)
        )

    def __str__(self) -> str:
        return f"{self.name}"


if __name__ == "__main__":
    pass
