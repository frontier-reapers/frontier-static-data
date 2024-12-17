## EVE Frontier Static Data

### Requirements

- pipx - `sudo apt install pipx && pipx ensurepath`
- poetry - `pipx install poetry`

### Usage

You will need to create a new venv to run the commands, the easiest way to do this is to install the Requirements and then open a `poetry shell`:

```
git clone https://github.com/frontier-reapers/frontier-static-data.git
cd frontier-static-data
poetry install
poetry shell
```

> [!NOTE]
> The examples below assume Windows Subsystem for Linix (WSL) is in use so the `C:` drive is mounted on `/mnt/c`. If using a Mac or Windows adjust the paths for your operating system. i.e. `"C:\CCP\EVE Frontier\ResFiles\"`.

## Commands

### `get_resfile.py`

Finds a ResFile in the CCP static data.

- `--root`: root of the game client's ResFiles directory, i.e. `/mnt/c/CCP/Project\ Awakening/ResFiles`
- `--file`: name of the resource you are looking for, normally of the format `res:{dir}/{file}.{ext}`

#### Examples

##### Find the Star Map

```
poetry run ./static_data/get_resfile.py --root /mnt/c/CCP/Project\ Awakening/ResFiles --file res:/staticdata/starmapcache.pickle
```

```
Searching for res:/staticdata/starmapcache.pickle in 2
found res:/staticdata/starmapcache.pickle located at 2e/2edadfca55978bdf_fb6b6396f7c1a2fcbb7267a0fba56269 in 56/5610a6eb8b5a4975_1a78826bc07a6e1c4814141ad484df52
```

### `export_starmap.py`

Exports the `starmapcache.pickle` to a file.

- `--root`: root of the game clients ResFiles directory, i.e. /mnt/c/CCP/Project\ Awakening/ResFiles
- `--format`: currently only `json` is supported
- `--output`: filename to write the data to

#### Examples

```
poetry run ./static_data/export_starmap.py --root /mnt/c/CCP/EVE\ Frontier/ResFiles/ --output ./starmap.json
```
