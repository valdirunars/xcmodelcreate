<img src="https://travis-ci.org/valdirunars/xcmodelcreate.svg?branch=master"/>

# xcmodelcreate

## How to install
```bash
git clone https://github.com/valdirunars/xcmodelcreate
pip install pbxproj
pip install ./xcmodelcreate
sudo rm -r xcmodelcreate
```

## Usage

### Commands

- `xcmodelcreate init`

- `xcmodelcreate all`

#### Initialization

```bash
xcmodelcreate init
```

This method sets up everything needed for maintaining the model structure

After running this command, check out the generated private folder `.xcmodelcreate`

#### `xcmodelcreate all`
To run this command xcmodelcreate must have been initialized using `xcmodelcreate init`

```bash
xcmodelcreate all
```

The command generates all models specified in the `./.xcmodelcreate/models.json` and based on the configuration specified `./.xcmodelcreate/config.json`
