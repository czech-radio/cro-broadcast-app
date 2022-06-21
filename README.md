# cro-general-app

The application (microservice) with information about available shows and stations shared amongs other organization services.

Development notes in [Google document](https://docs.google.com/document/d/1ukPolDfobIMXkMWHVxxz5TauZBDoz4eOFM8uUFd5B9Y/edit?usp=sharing)

## Features

- [ ] _Find_ all _shows_.
      e.g.
      `python def get_shows() -> List[Shows]: ... `

- [ ] _Find_ all _stations_.
      e.g.
      `python def get_stations() -> List[Stations]: ... `

## Installation

### Prerequisities

- Python 3.10+, Git, Docker

### Production

```powershell
pip install git+https://github.com/czech-radio/cro-general-app.git
```

### Development

Clone the repository.

```powershell
$ git clone https://github.com/czech-radio/cro-general-app.git
```

Change the directory.

```powershell
$ cd cro-general-app
```

Create virtual environment.

```powershell
$ py -3.10 -m venv .venv
```

Activate virtual environment.

```powershell
$ .\.venv\Scripts\activate
```

Install the package in editable mode.

```powershell
$ pip install -e .'[dev]'
```

## Usage

```python
def todo():
    print("Write usage!")
```

&hellip;
