"""The ps4_custom component."""
import logging

from homeassistant.components.ps4.media_player import PS4Device
from homeassistant.const import STATE_OFF

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass, config):
    """Set up the PS4 Component."""
    def state_standby(self):
        """Set states for state standby."""
        self.reset_title()
        self._state = STATE_OFF

    PS4Device.state_standby = state_standby
    _LOGGER.debug("Patched class=PS4Device, method=state_standby sucessfully.")

    return True
