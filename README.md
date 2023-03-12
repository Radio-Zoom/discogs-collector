# discogs-collector

Uses Discogs-API to collect information from your collection on Discogs.

## Set up a virtual environment [Optional]:

1. On Ubuntu/Debian: install venv package

    ```sh
    sudo apt install python<VERSION>-venv
    ```

    e.g.: `sudo apt install python3.10-venv`

2. setup venv in project folder:

    ```sh
    python3 -m venv <VENV_NAME>
    ```

    e.g.: `python3 -m venv venv`

3. activate the environment (for bash/zsh, more [here](https://docs.python.org/3/library/venv.html#how-venvs-work))
center
4. deactivate the environment after usage

    ```sh
    deactivate
    ```

## Installation

```sh
pip install -r packages.txt
```

## Execution

```sh
python3 main.py
```

- or once `chmod +x main.py` and then `./main.py`
  
> **_NOTE:_**  sometimes certain proxies cause problems. In this case, it may help to simply run the program again, as other proxies will then be randomly selected. 

## Usage

Input: <a href="https://www.discogs.com/de/settings/developers">Discogs Token</a>

Output: CSV of all your tracks from your whole collection with following data

Name | Comment | Implementation status
:-|:-:|:-:
ID||✔️
Title||✔️
Artist||✔️
Comment|»Vinyl«|✔️
Duration|Milliseconds|✔️
Genre||✔️
Track||✔️
Year||✔️
Album||✔️
Label||✔️
Catalog No.|Label code|✖️ |
Date downloaded/created||✖️
Date added||✖️
Style/Subgenre||✖️
Format||✖️
RPM||✖️
Century||✖️
