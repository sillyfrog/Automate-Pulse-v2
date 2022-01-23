# Rollease Acmeda Automate Pulse Hub v2 integration for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)

The Automate Pulse 2 Hub by Rollease Acmeda integration allows you to control and monitor covers via your Automate Pulse v2 Hub (see the [acmeda](/integrations/acmeda) integration for the v1 hub). The integration uses an [API](https://pypi.org/project/aiopulse2/) to directly communicate with hubs on the local network, rather than connecting via the cloud. [See this integration](https://www.home-assistant.io/integrations/acmeda/) if you have a v1 hub.

Devices are represented as a cover for monitoring and control as well as a sensor for monitoring battery level and signal strength.

# Installation

This integration is designed to be added as a custom [HACS](https://hacs.xyz/) repository. Start with [installing HACS](https://hacs.xyz/docs/installation/prerequisites).

Once HACS is installed, go to HACS in the sidebar, in the top right click on the 3 dots, select Custom repositories, then enter `https://github.com/sillyfrog/Automate-Pulse-v2` for the repository URL, and select "Integration" for the Category, and click Add.

Close the window and then click "Explore & Add Repositories" in the bottom right.

Search for and select the "Rollease Acmeda Automate Pulse Hub v2" integration, then click "Install this repository in HACS" and click "Install".

Once installed, restart Home Assistant (not strictly required as this uses a Config Flow, but it's good practice).

Once HA is back up, go to Configuration > Integrations > Add integration, and select "Automate Pulse Hub v2".

This will prompt for the IP address of the hub and register the covers with Home Assistant. All devices are automatically discovered on the hub and you will have the opportunity to select the area each device is located.

Once registration is complete, you should see a `cover` and a `sensor` entity for the battery for each device. Additionally there is a disabled sensors for the signal strength. The integration automatically manages the addition/update/removal of any devices connected on the hub at startup, including device names unless manually specified in Home Assistant.

## Caveats

If the IP address for the hub changes, you will need to re-register it with Home Assistant again. To avoid this, set up a DHCP reservation on your router for your hub so that it always has the same IP address.

The integration has the following limitations:

- covers with position as well as tilt are not yet supported (I'm not sure if such a product exists).
- the integration doesn't make use of rooms and scenes configured in the hub, use the equivalent functionality in Home Assistant instead.
- when adding new covers, you may need to restart Home Assistant to see the full details _after_ updating the name in the *Pulse 2* app.
