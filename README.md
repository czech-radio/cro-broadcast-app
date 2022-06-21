# cro-general-app

The general microservice with information about available shows and stations.

Development notes in [Google document](https://docs.google.com/document/d/1ukPolDfobIMXkMWHVxxz5TauZBDoz4eOFM8uUFd5B9Y/edit?usp=sharing)

## Features

- Show (entity)
- Stations (entity)

---

- [ ] Get available shows. (_Find_ all _shows_.)

```python
def get_shows() -> List[Shows]:
    ...
```

- [ ] Get available stations. (_Find_ all _stations_.)

```python
def get_stations() -> List[Stations]:
    ...
```

## Installation

```
$ git clone https://github.com/czech-radio/cro-general-app.git # Clone the repository.

$ cd cro-general-app                                           # Change the directory.

$ py -3.10 -m venv .venv $                                     # Create virtual environment.

$ .\.venv\Scripts\activate                                     # Activate virtual environment.

(.venv) $ ...

```

## Usage

```python
def todo():
    print("Write usage!")
```

&hellip;
