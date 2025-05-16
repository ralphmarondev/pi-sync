# Raspberry PI

## Implementing mobile control, dashboard, fingerprint and key switch actions

### 1. Run the files

```bash
sh run_cutie.sh
```

## For admin only

### 1. GUI for registering fingerprint

```bash
python3 register_fingerprint_for_admin.py
```

## I2C LCD pinout to RPI5 GPIO Connection

- GND [Ground] -> pin6 [GND]
- VCC [Power] -> pin 2 or 4 [5V]
- SDA [Data] -> pin 3 [GPIO 2 / SDA]
- SCL [Clock] -> pin 5 [GPIO 3 / SCL]
