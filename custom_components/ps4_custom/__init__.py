"""The ps4_custom component."""
import logging

from homeassistant.components.ps4.media_player import PS4Device
from homeassistant.const import (
    STATE_OFF,
    STATE_STANDBY
)

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass, config):
    """Set up the PS4 Component."""
    def async_toggle(self):
        """Toggle the power on the media player.

        This method must be run in the event loop and returns a coroutine.
        """
        _LOGGER.debug("PS4Device.async_toggle() called on device=%s", self.entity_id)
        if hasattr(self, "toggle"):
            # pylint: disable=no-member
            return self.hass.async_add_job(self.toggle)

        if self.state in [STATE_OFF, STATE_STANDBY]:
            return self.async_turn_on()
        return self.async_turn_off()

    PS4Device.async_toggle = async_toggle
    _LOGGER.debug("Patched class=PS4Device, method=async_toggle sucessfully.")

    return True
