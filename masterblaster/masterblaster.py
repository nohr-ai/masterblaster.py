import aiohttp
from .member import Member
from .image import Image
from .headers import Header
from typing import Any, Optional

BASE = "https://app.masterblaster.gg/api"


class MasterBlaster:
    def __init__(self, access_token: Optional[str], org_name: str) -> None:
        self.id: str = ""
        self.name: str = org_name
        self.is_admin: bool = False
        self.access_token: Optional[str] = access_token
        self.members: list[Member] = []
        self.images: list[Image] = []
        self.headers: Header = Header()
        self._session: aiohttp.ClientSession | None = None

    async def __aenter__(self) -> "MasterBlaster":
        await self._setup(self.name)
        return self

    async def __aexit__(self, exc_type, exc_value, traceback) -> None:
        await self._session.close()

    async def teardown(self) -> None:
        """
        Close the session

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        await self._session.close()

    @classmethod
    async def create(cls, access_token: str, org_name: str) -> "MasterBlaster":
        """
        Create a new MasterBlaster instance

        Parameters
        ----------
        access_token : str
            The access token for the organization
        org_name : str
            The name of the organization

        Returns
        -------
        MasterBlaster
            A new MasterBlaster instance
        """
        self = cls(access_token, org_name)
        await self._setup(org_name)
        return self

    async def _setup(self, org_name: str) -> "MasterBlaster":
        if not self._session.closed:
            await self._session.close()
        self.name = org_name
        self.headers = (
            Header()
            .add("Authorization", f"Bearer {self.access_token}")
            .add("User-Agent", f"MasterBlaster-python {self.name}")
            .add("Accept", "application/json")
            .add("Content-Type", "application/json")
            .add("Connection", "keep-alive")
        )
        self._session = aiohttp.ClientSession(headers=self.headers)
        await self._set_org_id(self.name)
        await self._set_org_members()
        await self._set_org_images()
        return self

    async def get_org(self, org_id: str) -> dict[str, str | dict]:
        """
        Returns the organization for the given organization id

        Parameters
        ----------
        org_id (str): The organization id

        Returns
        -------
        json
            Information about the organization
        """
        r = await self._session.get(f"{BASE}/organization/{org_id}")
        match r.status:
            case 200:
                return await r.json()
            case _:
                raise Exception(
                    f"Unable to fetch organization: {org_id} code: {r.status} err: {await r.text()}"
                )

    async def get_all_orgs(self) -> list[dict[str, Any]]:
        """
        Returns all organizations related to the current token

        Parameters
        ----------
        None

        Returns
        -------
        json
            Short information about all organizations related to current token
        """
        r = await self._session.get(f"{BASE}/organization/player")
        match r.status:
            case 200:
                return await r.json()
            case _:
                raise Exception(
                    f"Unable to fetch organization {self.name} code: {r.status} err: {await r.text()}"
                )

    async def change_org(self, org_name: str) -> None:
        """
        Change the organization
        Will re-initialize the organization: id, members, and images

        Parameters
        ----------
        org_name : str
            Name of the organization to change to

        Returns
        -------
        None
        """
        await self._setup(org_name)

    async def _set_org_id(self, org_name: str) -> None:
        orgs = await self.get_all_orgs()
        for org in orgs:
            # Parse out the one we want
            if org["name"] == org_name:
                self.id = org["id"]
                self.is_admin = org["isAdmin"]
                break

        if not self.id:
            raise Exception(f"Organization '{org_name}' not found for current token")

    async def _set_org_members(self) -> None:
        org_info = await self.get_org(self.id)
        self.members = [Member(**member) for member in org_info["members"]]

    async def _set_org_images(self) -> None:
        org_info = await self.get_org(self.id)
        self.images = [Image(**image) for image in org_info["images"]]

    async def _update_members(self) -> None:
        members = await self.get_org(self.id)
        self.members = [Member(**member) for member in members["members"]]

    async def get_members(self) -> list[Member]:
        """
        Returns all members of the organization

        Parameters
        ----------
        None

        Returns
        -------
        members: List[Member]
            A list of all members in the organization
        """
        await self._update_members()
        return self.members

    async def _update_images(self) -> None:
        images = await self.get_org(self.id)
        self.images = [Image(**image) for image in images["images"]]

    async def get_images(self) -> list[Image]:
        """
        Returns images of the organization

        Parameters
        ----------
        None

        Returns
        -------
        images: list[Image]
            A list of all images in the organization
        """
        await self._update_images()
        return self.images


if __name__ == "__main__":
    pass
