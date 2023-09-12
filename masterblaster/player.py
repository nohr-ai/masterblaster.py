from datetime import datetime
from dateutil import parser
from .gameaccount import GameAccount

__all__ = [
    "Player",
]


class Player:
    """
    Class for Player objects, related to zero or more gameaccounts

    :param id: The masterblaster id of the player
    :param nickName: The internal nickname of the player
    :param avatarUrl: The avatar url of the player
    :param registered: When the player was registered
    :param isProfileComplete: Whether or not the player has completed their profile
    :param gameAccounts: List of gameaccounts related to the player
    """

    def __init__(
        self,
        id: str,
        nickName: str,
        avatarUrl: str,
        registered: str,
        isProfileComplete: bool,
        gameAccounts: list[GameAccount],
    ) -> None:
        self.id: str = id
        self.nick_name: str = nickName
        self.avatar_url: str = avatarUrl
        self.registered: datetime = parser.isoparse(registered)
        self.is_profile_complete: bool = isProfileComplete
        self.game_accounts: list[GameAccount] = [
            GameAccount(**gameAccount) for gameAccount in gameAccounts
        ]


if __name__ == "__main__":
    pass
