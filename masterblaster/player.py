from datetime import datetime
from dateutil import parser
from .gameaccount import GameAccount


class Player:
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
