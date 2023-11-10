# Bugcrowd Spider 🕷️🕸️

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Description

This Python script extracts information about Bugcrowd programs, their targets, and reward ranges. It utilizes inferred Bugcrowd's API to fetch program data and generate a JSON file with the extracted information, without the need of scraping them by using any overloaded headless machinery.

## Features

- Program name extraction
- Program URL extraction
- Target group information extraction
- Reward range extraction (prices are in $)

## Configuration

- No additional configuration is required.

## Usage

```bash
python3 bugcrowd-spider.py
```

## Sample output
```json
{
    "programs": [
        {
            "name": "Rec Room Video Games",
            "url": "https://bugcrowd.com/recroom-og",
            "rewards": [
                {
                    "1": {
                        "min": 2100.0,
                        "max": 2500.0
                    },
                    "2": {
                        "min": 1000.0,
                        "max": 1250.0
                    },
                    "3": {
                        "min": 450.0,
                        "max": 600.0
                    },
                    "4": {
                        "min": 150.0,
                        "max": 200.0
                    }
                }
            ]
        },
        {
            "name": "Atlassian",
            "url": "https://bugcrowd.com/atlassian",
            "rewards": [
                // ... (Programs with multiple reward sets)
            ]
        },
        // ... (Additional programs)
    ]
}
```

## Contributing

Feel free to contribute to this project. Fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.