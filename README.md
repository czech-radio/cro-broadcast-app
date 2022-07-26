# cro-broadcast

The application (microservice) with information about available shows and stations shared amongs other organization services.

Development notes in [Google document](https://docs.google.com/document/d/1ukPolDfobIMXkMWHVxxz5TauZBDoz4eOFM8uUFd5B9Y/edit?usp=sharing)

## Motivation

Chceme mít ověřený přehled vysíláných pořadů na jednotlivých stanicích pro snadné
vyhledávaní relevantních informací potřebných k analýze obsahu vysílání.

## Solution

Softwarový balík `cro.broadcast` je aplikace, která využívá, mimo jiné, knihovnu (SDK) `cro.schedule.sdk` [^1] a slouží k archivaci a anotaci vysílacích schémat příslušných stanic.
Nad touto knihovnou je postavěná služba která za a) pravidelně stahuje a zálohuje dostupné programy b) poskytuje REST rozhraní pro další služby c) umožňuje snadnou zprávu a přidávání dalších informací k takto získanému vysílacímu schematu. Vysílací schema je na každé stanici tvořeno jednotlivými pořady. Pořady mají určen svůj čas začátků a konce v daném dni a na dané stanici. U pořadu nás zajímá jeho název, popis a žánrové zařazení. Dála nás zajímá počet očekávaných mluvčí v daném pořadu tj. případní moderátoři a respondenti. Pořady můžeme zařadit podle času vysílání do ranní, dopolední, odpolední, večerní a noční relace (DOPLNIT rozsah časů).

[^1]:
    Knihovna `cro.schedule.sdk` je aplikačním rozhraním a obalem nad veřejně sotupným HTTP REST API [ODKAZ]. Poskytuje klienta a doménový model,
    se kterým se dobře pracuje v dalších programech.

## Features

- Stáhuj periodicky dostupná schemata vysílání (historické od začátku roku 2022).
- Pro získané vysílací schema proveď automatické zařazení pořadů:
  - Přiřaď pořad k námi vytvořenému a udržoovanému výčtu. U toho sledujeme zejména žánr a očekávaný počet mluvčích, časy repríz.
- Umožni dodatečné korekce automaticky provedených úprav a zkus je nějak zužitkovat jako
  zpětnou vazbu pro automatické zpracování.
- K pořadu přiřaď dostupný textový přepis. Z něho se dají zjistit mluvčí a téma pořadu.
- Pro pořad s respondenty proveď určení (identifikaci) těchto respondentů pomocí databáze osob.

- [ ] _Find_ all _shows_.
      e.g.
      `python def get_shows() -> List[Shows]: ... `

- [ ] _Find_ all _stations_.
      e.g.
      `python def get_stations() -> List[Stations]: ... `

## Glossary

- schema vysílání (vysílací schema); program vysílání [_schedule_]
- mluvčí [_speaker_], respondent [_respondent_], moderátor [_moderator_]
- stanice [_station_]

## Installation

### Prerequisities

- Python 3.10+, Git, Docker

### Production

```powershell
pip install git+https://github.com/czech-radio/cro-general-app.git
```

### Development

#### Project structure

```
src/
    general/
        domain.py
        server.py
LICENSE
README.md
setup.py
```

#### Getting started

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
$ py -3.10 -m venv --upgrade-deps .venv
```

Activate virtual environment.

```powershell
$ .\.venv\Scripts\activate
```

Install the package in editable mode.

```powershell
$ pip install -e '.[dev]'
```

## Usage

```python
def todo():
    print("Write usage!")
```

&hellip;
