import os
import pytest
from dotenv import load_dotenv, find_dotenv
from masterblaster import MasterBlaster
from masterblaster import Header
from masterblaster import Team


@pytest.fixture(autouse=True)
def setup():
    load_dotenv(find_dotenv(".env.test"))
    yield


@pytest.mark.asyncio
async def test_init():
    headers = (
        Header()
        .add("Authorization", f"Bearer {os.getenv('ACCESS_TOKEN')}")
        .add("User-Agent", "MasterBlaster-python")
        .add("Accept", "application/json")
        .add("Content-Type", "application/json")
        .add("Connection", "keep-alive")
    )
    async with MasterBlaster(os.getenv("ACCESS_TOKEN")) as mb:
        assert mb.access_token == os.getenv("ACCESS_TOKEN")
        assert mb.headers == headers
        assert mb._session is not None


@pytest.mark.asyncio
async def test_init_no_access_token():
    with pytest.raises(TypeError):
        MasterBlaster.create()


@pytest.mark.asyncio
async def test_setup():
    headers = (
        Header()
        .add("Authorization", f"Bearer {os.getenv('ACCESS_TOKEN')}")
        .add("User-Agent", "MasterBlaster-python")
        .add("Accept", "application/json")
        .add("Content-Type", "application/json")
        .add("Connection", "keep-alive")
    )
    mb = await MasterBlaster.create(os.getenv("ACCESS_TOKEN"))
    assert mb._session is not None
    assert mb.headers == headers
    await mb.teardown()


@pytest.mark.asyncio
async def test_teardown():
    mb = await MasterBlaster.create(os.getenv("ACCESS_TOKEN"))
    assert mb._session is not None
    await mb.teardown()
    assert mb._session is None


@pytest.mark.asyncio
async def test_get_all_orgs():
    async with MasterBlaster(os.getenv("ACCESS_TOKEN")) as mb:
        orgs = await mb.get_all_orgs()
        assert len(orgs) == 1
        assert orgs[0].name == os.getenv("ORG_NAME")
        assert orgs[0].id == os.getenv("ORG_ID")


@pytest.mark.asyncio
async def test_get_all_orgs_invalid_token():
    with pytest.raises(Exception):
        async with MasterBlaster(os.getenv("NOT-A-TOKEN")) as mb:
            await mb.get_all_orgs()


@pytest.mark.asyncio
async def test_get_org():
    async with MasterBlaster(os.getenv("ACCESS_TOKEN")) as mb:
        org = await mb.get_org(os.getenv("ORG_ID"))
        assert org.name == os.getenv("ORG_NAME")
        assert org.id == os.getenv("ORG_ID")


@pytest.mark.asyncio
async def test_get_org_not_found():
    with pytest.raises(ValueError):
        async with MasterBlaster(os.getenv("ACCESS_TOKEN")) as mb:
            await mb.get_org("notfound")


@pytest.mark.asyncio
async def test_get_org_by_name():
    async with MasterBlaster(os.getenv("ACCESS_TOKEN")) as mb:
        org = await mb.get_org_by_name(os.getenv("ORG_NAME"))
        assert org.name == os.getenv("ORG_NAME")
        assert org.id == os.getenv("ORG_ID")


@pytest.mark.asyncio
async def test_get_org_by_name_not_found():
    with pytest.raises(ValueError):
        async with MasterBlaster(os.getenv("ACCESS_TOKEN")) as mb:
            await mb.get_org_by_name("notfound")


@pytest.mark.asyncio
async def test_set_access_token():
    async with MasterBlaster("NOT-A-TOKEN") as mb:
        assert mb.access_token == "NOT-A-TOKEN"
        await mb.set_access_token(os.getenv("ACCESS_TOKEN"))
        assert mb.access_token == os.getenv("ACCESS_TOKEN")


@pytest.mark.asyncio
async def test_set_access_token_setup():
    header_before = (
        Header()
        .add("Authorization", "Bearer NOT-A-TOKEN")
        .add("User-Agent", "MasterBlaster-python")
        .add("Accept", "application/json")
        .add("Content-Type", "application/json")
        .add("Connection", "keep-alive")
    )
    header_expected = (
        Header()
        .add("Authorization", f"Bearer {os.getenv('ACCESS_TOKEN')}")
        .add("User-Agent", "MasterBlaster-python")
        .add("Accept", "application/json")
        .add("Content-Type", "application/json")
        .add("Connection", "keep-alive")
    )
    async with MasterBlaster("NOT-A-TOKEN") as mb:
        assert mb.headers == header_before
        await mb.set_access_token(os.getenv("ACCESS_TOKEN"))
        assert mb.headers == header_expected


@pytest.mark.asyncio
async def test_get_all_members():
    expected = 11
    async with MasterBlaster(os.getenv("ACCESS_TOKEN")) as mb:
        org = await mb.get_org(os.getenv("ORG_ID"))
        members = await org.get_members()
        assert len(members) == expected


@pytest.mark.asyncio
async def test_get_all_teams():
    expected = 1
    async with MasterBlaster(os.getenv("ACCESS_TOKEN")) as mb:
        orgs = await mb.get_all_orgs()
        for org in orgs:
            teams = await org.get_teams()
            assert len(teams) == expected
