# Masterblaster.py
## Latest
[![](https://readthedocs.org/projects/masterblasterpy/badge/?version=latest)](https://masterblasterpy.readthedocs.io/en/latest/?badge=latest)
## Beta
[![Documentation Status](https://readthedocs.org/projects/masterblasterpy/badge/?version=beta)](https://masterblasterpy.readthedocs.io/en/beta/?badge=beta)

Python API wrapper for masterblaster.gg
## Installation

```bash
$ python -m pip install masterblaster.py
```

## Usage

Masterblaster.py is a python API wrapper for the masterblaster.gg API. It allows you to easily access the data from the API and use it in your own projects.
I.e.:

```python
import asyncio
import masterblaster


async def main():
    async with masterblaster.MasterBlaster("MY-TOKEN-HERE","MY-ORGANIZATION-HERE") as m:
        for member in await m.get_members():
            print(member)

    # Alternative
    m = await masterblaster.MasterBlaster.create("MY-TOKEN-HERE","MY-ORGANIZATION-HERE")
    for member in await m.get_members():
        print(member)
    await m.teardown()

    # Or Perhaps
    m = masterblaster.MasterBlaster("MY-TOKEN-HERE","MY-ORGANIZATION-HERE")
    ...
    ...
    async with m:
        for member in await m.get_members():
            print(member)


if __name__ == "__main__":
    asyncio.run(main())
```

## Contributing

Interested in contributing? Check out the contributing guidelines. 
Please note that this project is released with a Code of Conduct. 
By contributing to this project, you agree to abide by its terms.

## License

`masterblaster.py` was created by Øyvind Nohr. It is licensed under the terms
of the MIT license.

## Credits

## Links
[Documentation](https://masterblasterpy.readthedocs.io/en/latest/)
