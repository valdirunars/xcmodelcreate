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

- `xcmodelcreate raw`

- `xcmodelcreate init`

- `xcmodelcreate all`


#### `xcmodelcreate raw`

```bash
xcmodelcreate raw "{ \"SomeNewObject\": { \"some_property\": \"String\", \"timestamp\": \"Date\" } }" "Sources/Models" "Sources/Models"
```

- Here the first input is the JSON for the object:

	```JSON
	{
		"SomeNewObject": {
			"some_property": "String",
			"timestamp": "Date"
		}
	}
	```

- The second input represents the path to the folder where the files should be added

- Finally the fourth input represents the group path within the object

This generates the model:

```swift
import Foundation

struct SomeNewObject: DictionaryRepresentable {
	let timestamp: Date
	let some_property: String

	enum CodingKeys: String {
		case timestamp
		case some_property
	}
}
```

##### Options

- `-a` Add to current models

	- NOTE: Current project must be initialized see: `xcmodelcreate init`

#### Initialization
```bash
xcmodelcreate init
```

This method sets up everything needed for maintaining the model structure
