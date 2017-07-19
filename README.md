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
xcmodelcreate "{ \"SomeNewObject\": { \"some_property\": \"String\", \"timestamp\": \"Date\" } }" "path/to/xcprojectname" "path/to/models_folder"
```

This generates a model:

```swift
import Foundation

struct SomeNewObject: DictionaryRepresentable {
	public let timestamp: Date
	public let some_property: String

	enum CodingKeys: String {
		case timestamp
		case some_property
	}

	public init(timestamp: Date, some_property: String) {
		self.timestamp = timestamp
		self.some_property = some_property
	}

	public init?(dic: [String: Any]) {
		guard let param0 = dic[CodingKeys.timestamp.rawValue] as? TimeInterval else { return nil }
		self.timestamp = Date(timeIntervalSince1970: param0)

		guard let param1 = dic[CodingKeys.some_property.rawValue] as? String else { return nil }
		self.some_property = param1
	}

	public func asDictionary() -> [String: Any] {
		return [
			CodingKeys.timestamp.rawValue: self.timestamp.timeIntervalSince1970,
			CodingKeys.some_property.rawValue: self.some_property
		]
	}
}
```

Conforming to the protocol:

```swift
protocol DictionaryRepresentable {
  init?(dic: [String: Any])
  func asDictionary() -> [String: Any]
}
```

<details>
<summary>How do I dropdown?</summary>
<details>
<summary>How do I dropdown?</summary>
This is how you dropdown.
</details>

</details>
