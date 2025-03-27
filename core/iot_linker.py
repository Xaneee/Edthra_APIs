def simulate_device_action(device: str, action: str):
    if device.lower() == "lamp" and action.lower() == "on":
        return "🟡 Lamp is now ON"
    elif device.lower() == "lamp" and action.lower() == "off":
        return "⚫ Lamp is now OFF"
    else:
        return f"Device '{device}' does not support action '{action}'."
