# Masterblaster
Python API wrapper for masterblaster.gg
## Installation

```bash
$ pip install masterblaster.py
```

## Usage

Masterblaster is a python API wrapper for the masterblaster.gg API. It allows you to easily access the data from the API and use it in your own projects.
I.e.:

```python
import asyncio
import dotenv
import masterblaster


async def main():
    async with masterblaster.MasterBlaster(os.getenv("TOKEN"),"UiT") as m:
        for member in await m.get_members():
            print(member)

    # Alternative
    m = await masterblaster.MasterBlaster.create(os.getenv("TOKEN"),"UiT")
    for member in await m.get_members():
        print(member)
    await m.teardown()

    # Or Perhaps
    m = masterblaster.MasterBlaster(os.getenv("TOKEN"),"UiT")
    ...
    ...
    async with m:
        for member in await m.get_members():
            print(member)


if __name__ == "__main__":
    dotenv.load_dotenv()
    asyncio.run(main())
```

## Contributing

Interested in contributing? Check out the contributing guidelines. 
Please note that this project is released with a Code of Conduct. 
By contributing to this project, you agree to abide by its terms.

## License

`masterblaster` was created by Øyvind Nohr. It is licensed under the terms
of the MIT license.

## Credits
