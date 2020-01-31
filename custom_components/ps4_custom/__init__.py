"""The ps4_custom component."""
import logging

from homeassistant.components.homekit.type_media_players import TelevisionMediaPlayer, MediaPlayer
from homeassistant.components.ps4.media_player import PS4Device
from homeassistant.const import (
    STATE_OFF,
    STATE_STANDBY,
)
from homeassistant.core import State

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass, config):
    """Set up the PS4 Component."""
    def async_toggle(self):
        """Toggle the power on the media player.

        This method must be run in the event loop and returns a coroutine.
        """
        _LOGGER.debug("%s: PS4Device.async_toggle() state=%s", self.entity_id, self.state)
        if hasattr(self, "toggle"):
            # pylint: disable=no-member
            return self.hass.async_add_job(self.toggle)

        if self.state in [STATE_OFF, STATE_STANDBY]:
            return self.async_turn_on()
        return self.async_turn_off()

    PS4Device.async_toggle = async_toggle
    _LOGGER.debug("Patched class=PS4Device, method=async_toggle sucessfully.")

    def update_state_MediaPlayer_wrapper(func):
        def update_state_MediaPlayer(self, new_state):
            # fix STATE_STANDBY beeing regarded as STATE_ON
            if new_state.state == STATE_STANDBY:
                fixed_state_dict = new_state.as_dict()
                fixed_state_dict.update({"state": STATE_OFF})
                _LOGGER.debug("%s: Adjusting state=%s to new_state=off (%s %s)",
                              self.entity_id,
                              new_state.state,
                              self.hass.states.get(self.entity_id).state,
                              fixed_state_dict)
                new_state = State.from_dict(fixed_state_dict)

            # call original update_state() method
            func(self, new_state)

        return update_state_MediaPlayer

    MediaPlayer.update_state = update_state_MediaPlayer_wrapper(MediaPlayer.update_state)
    _LOGGER.debug("Patched class=MediaPlayer, method=update_state sucessfully.")
    TelevisionMediaPlayer.update_state = update_state_MediaPlayer_wrapper(TelevisionMediaPlayer.update_state)
    _LOGGER.debug("Patched class=TelevisionMediaPlayer, method=update_state sucessfully.")

    return True
