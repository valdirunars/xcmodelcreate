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

```bash
xcmodelcreate "{ \"SomeNewObject\": { \"some_property\": \"String\", \"timestamp\": \"Date\" } }" Kraken "Sources/Models" "Sources/Models"
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

- The second input represents the project name with path included e.g. path/to/the/project_name

- The third input represents the path to the folder where the files should be added

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

## Fun fact: You can create dropdown menus in markdown (at least on GitHub)

<details>
<summary>How do I drop?</summary>
<details>
<summary>I'll tell you how</summary>
... like it's hot

```markdown
<details>
<summary>Outer Arrow</summary>
<details>
<summary>Inner Arrow</summary>
Drop it like it's hot
</details>
</details>
```
</details>
</details>
