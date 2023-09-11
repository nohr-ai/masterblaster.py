from __future__ import annotations
import json
from collections import abc
from typing import Any, Iterator


class Header(abc.MutableMapping):
    def __init__(self) -> None:
        self.fields: dict[str, Any] = {}

    def add(self, name: str, value: str) -> Header:
        """
        Add a header field

        Parameters
        ----------
        name : str
            The name of the header field
        value : str
            The value of the header field

        Returns
        -------
        Header
            The header object
        """
        self.fields[name] = value
        return self

    def remove(self, name: str) -> Header:
        """
        Remove a header field

        Parameters
        ----------
        name : str
            The name of the header field

        Returns
        -------
        Header
            The header object
        """
        try:
            del self.fields[name]
        except KeyError:
            pass
        finally:
            return self

    def __getitem__(self, key: str) -> Any:
        return self.fields[key]

    def __getattr__(self, key: str) -> Any:
        return self.fields[key]

    def __setitem__(self, key: str, __v: Any) -> None:
        self.fields[key] = __v

    def __delitem__(self, key: str) -> None:
        del self.fields[key]

    def __len__(self) -> int:
        return len(self.fields)

    def __iter__(self) -> Iterator[Any]:
        return iter(self.fields)

    def __str__(self) -> str:
        return json.dumps(self.fields)

    def __repr__(self) -> str:
        return json.dumps(self.fields)


if __name__ == "__main__":
    pass
