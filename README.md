## EVE Frontier Static Data

### Requirements

- pipx - `sudo apt install pipx && pipx ensurepath`
- poetry - `pipx install poetry`

## Commands

### `get_resfile.py`

Finds a ResFile in the CCP static data.

- `--root`: root of the game client's ResFiles directory, i.e. `/mnt/c/CCP/Project\ Awakening/ResFiles`
- `--file`: name of the resource you are looking for, normally of the format `res:{dir}/{file}.{ext}`

#### Examples

##### Find the Star Map

```
./get_resfile.py --root /mnt/c/CCP/Project\ Awakening/ResFiles --file res:/staticdata/starmapcache.pickle
```

```
Searching for res:/staticdata/starmapcache.pickle in 2
found res:/staticdata/starmapcache.pickle located at 2e/2edadfca55978bdf_fb6b6396f7c1a2fcbb7267a0fba56269 in 56/5610a6eb8b5a4975_1a78826bc07a6e1c4814141ad484df52
```

