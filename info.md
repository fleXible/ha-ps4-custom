[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)
[![](https://img.shields.io/badge/MAINTAINER-%40fleXible-red?style=flat)](https://github.com/fleXible)

# HomeAssistant - PlayStation 4 Custom Component

This is a custom component fixes a bug in the built-in [Playstation 4](https://www.home-assistant.io/integrations/ps4/) integration. Toggling the power is not working.

* Fix broken power toggle feature used in Lovelace Mediaplayer-UI with runtime patch

## Configuration

To load and activate the fix, add the following to your `configuration.yaml` file:

```yaml
# Example configuration.yaml entry
ps4_custom:
```

 Because this is a runtime patch, the device administration is not changed. 
 For further documentation, consult the official HomeAssistant [PlayStation 4](https://www.home-assistant.io/integrations/ps4/) pages.

***
