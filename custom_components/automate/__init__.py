"""The Automate Pulse Hub v2 integration."""

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers import device_registry

from .const import DOMAIN
from .hub import PulseHub

PLATFORMS = ["cover", "sensor"]


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the Automate Pulse Hub v2 component."""
    hass.data.setdefault(DOMAIN, {})
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Automate Pulse Hub v2 from a config entry."""
    hub = PulseHub(hass, entry)

    if not await hub.async_setup():
        return False

    # Extract hub ID from config entry title. Title has a fixed known format
    # (see PulseHub.title) e.g., "1234567" from "1234567 (192.168.1.199)"
    # Can't use the aiopulse2 API to get the ID, as it is not available until
    # the hub is connected to HA.
    hub_id = entry.title.split(" ")[0]

    # Register the hub in the device registry to avoid via_device warning
    dev_registry = device_registry.async_get(hass)
    dev_registry.async_get_or_create(
        config_entry_id=entry.entry_id,
        identifiers={("automate", hub_id)},
        manufacturer="Automate",
        model="Pulse V2 Hub",
        name=f"Pulse V2 Hub ({hub.host})",
    )

    hass.data[DOMAIN][entry.entry_id] = hub

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    hub = hass.data[DOMAIN][entry.entry_id]

    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    if not await hub.async_reset():
        return False

    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
