# HomeAssistant - PlayStation 4 Custom Component

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)
[![Maintainer](https://img.shields.io/badge/MAINTAINER-%40fleXible-red?style=flat)](https://github.com/fleXible)

This is a custom component fixes a bug in the built-in [Playstation 4](https://www.home-assistant.io/integrations/ps4/) integration. Toggling the power is not working.

* Fix broken power toggle feature used in Lovelace Mediaplayer-UI with runtime patch

## Installation

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=Felix+Franz&repository=https%3A%2F%2Fgithub.com%2FfleXible%2Fha-ps4-custom&category=Integration)

## Configuration

To load and activate the fix, add the following to your `configuration.yaml` file:

```yaml
# Example configuration.yaml entry
ps4_custom:
```

 Because this is a runtime patch, the device administration is not changed.
 For further documentation, consult the official HomeAssistant [PlayStation 4](https://www.home-assistant.io/integrations/ps4/) pages.

***
