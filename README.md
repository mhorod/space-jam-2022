# Spacejam 2022 project

## Team: ksisiamisiabela

- Izabela Kręc
- Dominika Gwóźdź
- Krzysztof Pęczek
- Michał Horodecki

# Installation

Python and pygame are required to run the game.

```
pip3 install -r requirements.txt
```

# Gameplay

This is a point-and-click game - you explore the world by clicking at the
environment. Additionally you can change locations by pressing left and right
arrows.

# Development

## Downloading

1. Clone the repository `git clone git@github.com:mhorod/space-jam-2022.git`
2. Create python virtual environment and install dependencies with:

**linux**

```sh
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

**windows**

```
python3 -m venv venv
source venv/bin/Activate.ps1
pip3 install -r requirements.txt
```

## Before push

```
pip3 freeze > requirements.txt
```
