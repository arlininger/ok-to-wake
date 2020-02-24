# ok-to-wake
A python-based library for making an "Ok to wake" style alarm clock from a raspberry pi.

## What is an ok-to-wake clock
As any parent knows, kids don't always stay in bed until it is time to get up. A traditional alarm clock is not always reasonable as you won't necessairly want to wake them at the appointed time either. There are a variety of commercial products on the market with the feature that they turn on a light with a soft glow when children are permitted to get out of bed. Unfortunately, the market for them is small enough that they are expensive and have generally poor engineering. This project is aimed at duplicating that behavior with quality off-the-shelf hardware while allowing for significant customizablity.

## Basic design
At it's core, this project is nothing more than chaging LED colors based on a schedule. Eventual upgrade may include a configuration file, logic for running as a service, or even a web interface (when hell freezes over).

## Hardware

| Item | Link |
| ---- | ---- |
| Raspberry Pi ZeroWH | https://smile.amazon.com/dp/B07CMVDHWB/ref=cm_sw_em_r_mt_dp_U_poZuEb546QE5G |
| LED Bar | https://smile.amazon.com/dp/B01J7Y332Q/ref=cm_sw_em_r_mt_dp_U_0mZuEbVDB30VQ |

Technically any Raspberry Pi of recent vintage (I think since the 2) will do. The linked Pi kit has a case with sutable screw holes for mounting wherever desired as well as the required power supply. It is a convenient kit with most of the required parts and not much extra.

The LED Bar is the Pimoroni Blinkt! module. While the code is aimed specifically at that LED set, it can be fairly easily modified to support a variety of other LED modules.
