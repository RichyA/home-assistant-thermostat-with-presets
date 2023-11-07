# Thermostat with Presets

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

![Project Maintenance][maintenance-shield]

_Custom component to provide Presets on a thermostat integration that doesn't natively support them._

Note: This project is mainly for personal use. It meets my requirements and I'm unlikely to invest too much time in broadening the scope.

**This integration will set up the following platforms.**

Platform | Description
-- | --
`climate` | Provides instances of the thermostat with added functionality for presets.

## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
1. If you do not have a `custom_components` directory (folder) there, you need to create it.
1. In the `custom_components` directory (folder) create a new folder called `thermostat_with_presets`.
1. Download _all_ the files from the `custom_components/thermostat_with_presets/` directory (folder) in this repository.
1. Place the files you downloaded in the new directory (folder) you created.
1. Restart Home Assistant
1. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Thermostat with Presets"

## Configuration is done in the UI

<!---->

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

***

[thermostat_with_presets]: https://github.com/RichyA/home-assistant-thermostat-with-presets
[commits-shield]: https://img.shields.io/github/commit-activity/y/RichyA/home-assistant-thermostat-with-presets?style=for-the-badge
[commits]: https://github.com/RichyA/home-assistant-thermostat-with-presets/commits/main
[license-shield]: https://img.shields.io/github/license/RichyA/home-assistant-thermostat-with-presets.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-Richard%20Archer%20%40RichyA-blue?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/RichyA/home-assistant-thermostat-with-presets?style=for-the-badge
[releases]: https://github.com/RichyA/home-assistant-thermostat-with-presets/releases
