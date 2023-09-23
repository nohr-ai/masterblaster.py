from datetime import datetime
from dateutil import parser

from .player import Player

from typing import Optional

__all__ = [
    "Member",
]


class Member:
    """
    Class for organization members

    :param player: The player object
    :param email: The member email
    :param name: The member name
    :param playerId: The player id
    :param role: The member role
    :param addedAt: When the member was added
    :param invitedAt: When the member was invited

    :ivar player: The member's related player object
    :ivar email: The member's email-address
    :ivar name: The member's name
    :ivar player_id: The member's player id
    :ivar role: The member's role
    :ivar added_at: When the member was added
    :ivar invited_at: When the member was invited
    """

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
