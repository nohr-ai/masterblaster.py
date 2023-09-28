# Masterblaster.py

[![Actions Status](https://img.shields.io/github/actions/workflow/status/Askepios-ai/masterblaster/build.yml?branch=beta&logo=github&style=flat-square)](https://github.com/Askepios-ai/masterblaster.py)
[![CodeCov](https://img.shields.io/codecov/c/gh/Askepios-ai/masterblaster.py/tree/beta?logo=codecov&style=flat-square)](https://app.codecov.io/gh/Askepios-ai/masterblaster.py)
[![PyPI](https://img.shields.io/pypi/v/masterblaster.py?logo=python&style=flat-square)](https://pypi.org/project/masterblaster.py)
![Docs](https://img.shields.io/readthedocs/masterblasterpy?label=Docs&link=https%3A%2F%2Fmasterblasterpy.readthedocs.io%2Fen&style=flat-square)
![DocsBeta](https://img.shields.io/readthedocs/masterblasterpy%2Fbeta?label=BetaDocs&link=https%3A%2F%2Fmasterblasterpy.readthedocs.io%2Fen%2Fbeta%2F&style=flat-square)

Python API wrapper for masterblaster.gg

## Installation

```bash
$ python -m pip install masterblaster.py
```

## Usage

Masterblaster.py is a python wrapper for the masterblaster.gg API. It allows you to easily access the data from the API and use it in your own projects.
I.e.:

```python
import asyncio
import masterblaster


async def main():
    async with masterblaster.MasterBlaster("MY-TOKEN-HERE") as m:
        for org in await m.get_all_orgs():
            for member in await org.get_members():
                print(member)


    # Alternative
    m = await masterblaster.MasterBlaster.create("MY-TOKEN-HERE")
    org = await m.get_org("MY-ORG-ID"):
    for member in await org.get_members():
        print(member)

    # Or Perhaps
    m = masterblaster.MasterBlaster("MY-TOKEN-HERE")
    ...
    ...
    async with m:
        org = await m.get_org_by_name("MY_ORG-NAME")
        for member in await org.get_members():
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

## Contributors
[![Contributors](https://img.shields.io/github/contributors/askepios-ai/masterblaster.py)](https://github.com/skepios-ai/masterblaster.py/graphs/contributors)


## Links
[Documentation](https://masterblasterpy.readthedocs.io/en/latest/)
