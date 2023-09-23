import pytest
import os
import aiohttp
from dotenv import load_dotenv, find_dotenv
from masterblaster.team import Team
from masterblaster.headers import Header

masterblaster_team = {
    "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "ownerPlayerId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "organizationOwnerId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "name": "name",
    "tag": None,
    "flag": None,
    "shortHandle": "name",
    "avatarImageId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "bannerImageId": None,
    "socialLinks": [],
    "gameId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "players": [
        {
            "playerId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
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
                        "connectedAt": "2000-01-01T00:00:00.00+00:00",
                    }
                ],
            },
            "pendingInvitation": False,
            "isAdministrator": False,
        },
        {
            "playerId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
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
                        "connectedAt": "2000-01-01T00:00:00.00+00:00",
                    }
                ],
            },
            "pendingInvitation": False,
            "isAdministrator": False,
        },
        {
            "playerId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
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
                        "connectedAt": "2000-01-01T00:00:00.00+00:00",
                    }
                ],
            },
            "pendingInvitation": False,
            "isAdministrator": False,
        },
        {
            "playerId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
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
                        "connectedAt": "2000-01-01T00:00:00.00+00:00",
                    }
                ],
            },
            "pendingInvitation": False,
            "isAdministrator": False,
        },
        {
            "playerId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
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
                        "connectedAt": "2000-01-01T00:00:00.00+00:00",
                    }
                ],
            },
            "pendingInvitation": False,
            "isAdministrator": False,
        },
        {
            "playerId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
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
                        "connectedAt": "2000-01-01T00:00:00.00+00:00",
                    }
                ],
            },
            "pendingInvitation": False,
            "isAdministrator": False,
        },
        {
            "playerId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
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
                        "connectedAt": "2000-01-01T00:00:00.00+00:00",
                    }
                ],
            },
            "pendingInvitation": False,
            "isAdministrator": False,
        },
        {
            "playerId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
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
                        "connectedAt": "2000-01-01T00:00:00.00+00:00",
                    }
                ],
            },
            "pendingInvitation": False,
            "isAdministrator": False,
        },
        {
            "playerId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
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
                        "connectedAt": "2000-01-01T00:00:00.00+00:00",
                    }
                ],
            },
            "pendingInvitation": False,
            "isAdministrator": False,
        },
        {
            "playerId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
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
                        "connectedAt": "2000-01-01T00:00:00.00+00:00",
                    }
                ],
            },
            "pendingInvitation": False,
            "isAdministrator": False,
        },
    ],
    "createdAt": "2000-01-01T00:00:00.00+00:00",
}


@pytest.fixture(autouse=True)
def load_env():
    load_dotenv(find_dotenv(".env.test"))
    yield


def test_init():
    Team(**masterblaster_team)


def test_str():
    team = Team(**masterblaster_team)

    assert str(team) == masterblaster_team["name"]


@pytest.mark.asyncio
async def test_get_schedule():
    header = (
        Header()
        .add("Authorization", f"Bearer {os.getenv('ACCESS_TOKEN')}")
        .add("User-Agent", "MasterBlaster-python")
        .add("Accept", "application/json")
        .add("Content-Type", "application/json")
        .add("Connection", "keep-alive")
    )
    team = Team(**masterblaster_team)
    team.session = aiohttp.ClientSession(headers=header)
    schedule = await team.get_schedule()
    assert schedule is not None
    await team.session.close()


@pytest.mark.asyncio
async def test_get_schedule_fail():
    with pytest.raises(ValueError):
        team = Team(**masterblaster_team)
        team.session = aiohttp.ClientSession(headers=Header())
        await team.get_schedule()
    await team.session.close()
