"""Sensor platform for thermostat_with_presets."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription

from .const import DOMAIN
from .coordinator import ThermostatWithPresetsDataUpdateCoordinator
from .entity import ThermostatWithPresetsEntity

ENTITY_DESCRIPTIONS = (
    SensorEntityDescription(
        key="thermostat_with_presets",
        name="Integration Sensor",
        icon="mdi:format-quote-close",
    ),
)


async def async_setup_entry(hass, entry, async_add_devices):
    """Set up the sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices(
        ThermostatWithPresetsSensor(
            coordinator=coordinator,
            entity_description=entity_description,
        )
        for entity_description in ENTITY_DESCRIPTIONS
    )


class ThermostatWithPresetsSensor(ThermostatWithPresetsEntity, SensorEntity):
    """thermostat_with_presets Sensor class."""

    def __init__(
        self,
        coordinator: ThermostatWithPresetsDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
    ) -> None:
        """Initialize the sensor class."""
        super().__init__(coordinator)
        self.entity_description = entity_description

    @property
    def native_value(self) -> str:
        """Return the native value of the sensor."""
        return self.coordinator.data.get("body")
