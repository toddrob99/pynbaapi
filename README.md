# pynbaapi

Python Wrapper for NBA API

Created by Todd Roberts

## Installation
Install from pip:

```
pip install pynbaapi
```

or

```
py -m pip install pynbaapi
```

## Use
See `examples.py` in the `examples` folder for some example uses.

There are other methods in the `pynba.nba.NBA()` object, and the `pynba.api.API()` object has a `from_url` method that can be used to retrieve arbitrary URLs (as long as the response is in nested json format, which many of the NBA API endpoints are not).

## Support
I do not provide support related to NBA API. There is good documentation on the [swar/nba_api](https://github.com/swar/nba_api) repo, and this package was only created because the nba_api package does not (appear to) return API responses in recursive objects.

## Copyright Notice
This package and its author are not affiliated with NBA or any NBA team. This API wrapper interfaces with NBA's API. Use of NBA data is subject to copyright by NBA.
