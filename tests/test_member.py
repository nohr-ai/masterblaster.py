from masterblaster.member import Member

masterblaster_member = {
    "player": {
        "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "nickName": "name",
        "avatarUrl": "",
        "registered": "2000-01-01T00:00:00.00+00:00",
        "isProfileComplete": True,
        "gameAccounts": [
            {
                "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                "nick": "name",
                "avatarUrl": "",
                "gameId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                "isConnected": True,
                "connectedAt": "2000-01-01T00:00:00.0+00:00",
            }
        ],
    },
    "email": "email@email.com",
    "name": "name",
    "playerId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "role": 10,
    "addedAt": "2000-01-01T00:00:00.0+00:00",
    "invitedAt": None,
}


def test_init():
    Member(**masterblaster_member)


def test_str():
    member = Member(**masterblaster_member)
    assert str(member) == "name"
