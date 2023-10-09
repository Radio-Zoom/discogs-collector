# discogs-collector

Uses Discogs-API to collect information from your collection on Discogs.

## Requirements

- Python (we recommend the newest version)
- Pip (package manager for python)

## Set up a virtual environment [Optional]

1. On Linux: install venv package with your package manager (e.g. apt or pacman)

    ```sh
    sudo apt install python<VERSION>-venv
    ```

    e.g.: `sudo apt install python3.10-venv`

2. Setup venv in project folder:

    ```sh
    python3 -m venv <VENV_NAME>
    ```

    e.g.: `python3 -m venv venv`

3. Activate the environment (for bash/zsh, more [here](https://docs.python.org/3/library/venv.html#how-venvs-work))
center

4. Deactivate the environment after usage

    ```sh
    deactivate
    ```

## Usage

Install required packages

```sh
pip install -r packages.txt
```

If you using Linux and get the "externally-managed-environment" error you have to install the used dependencies with your package manager (or try a different soluition with venvs or pipx).  
E.g. on Arch Linux:

```sh
sudo pacman -S python-discogs-client python-retrying
```

Execute the main script

```sh
python main.py
```

or

```sh
python3 main.py
```

or once `chmod +x main.py` and then `./main.py`

- Input:
  - [Discogs Token](https://www.discogs.com/de/settings/developers)
  - Name of the CSV file

- Output:
  - CSV file of all your tracks from your whole collection with following data (separated with semicolons)

## Columns

Name | Comment | Implementation status
:-|:-:|:-:
ID|Format: Discogs id_track positon|✔️
CatalogNo|Label code|✔️
ReleaseYear||✔️
Decade||✔️
Album||✔️
AlbumArtist| " & " separated for multiple artists|✔️
TrackArtist| " & " separated for multiple artists|✔️
Label||✔️
Genre||✔️
Subgenre|(Styles) Underscore separated|✔️
Title||✔️
Duration|Format: Seconds.Milliseconds|✔️
Format|RPM, LP, ... (underscore separated)| ✔️
Date downloaded/created|Format: yyyy-mm-dd|✔️
Date added|not included|✖️
