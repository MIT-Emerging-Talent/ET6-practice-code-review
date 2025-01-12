# Traffic Light System Simulation

This project simulates a traffic light system using LEDs (Arduino version)
and a console-based simulation (Python version).
The program follows a basic traffic light sequence:

- Red light: ON for 5 seconds
- Green light: ON for 5 seconds
- Yellow light: ON for 2 seconds

## Features

- **Arduino Implementation**: Controls physical LEDs connected to an Arduino board.
- **Python Simulation**: Simulates the traffic light system in the console.
- **Customizable Timing**: Light durations can be adjusted.

---

## Setup Instructions

### Arduino Implementation

1. **Hardware Requirements**:
   - Arduino board
   - Red, Yellow, and Green LEDs
   - Resistors (220 ohms recommended)
   - Breadboard and jumper wires

2. **Circuit Diagram**:
   - Connect the Red LED to pin **13** with a resistor.
   - Connect the Yellow LED to pin **12** with a resistor.
   - Connect the Green LED to pin **11** with a resistor.
   - Connect all LED ground ends to **GND**.

3. **Upload Code**:
   - Copy the Arduino code (see `traffic_light.ino`) into the Arduino IDE.
   - Connect your board and upload the code.

### Python Simulation

1. **Requirements**:
   - Python 3.x
   - No external libraries required

2. **Run the Code**:
   - Save the Python script as `traffic_light.py`.
   - Run the script in your terminal using:

     ```bash
     python traffic_light.py
     ```

---

## Testing

### Test Cases

1. **Arduino Testing**:
   - Verify each LED lights up at the correct time (Red → Green → Yellow).
   - Test light durations by measuring the time each light stays on.

2. **Python Testing**:
   - Ensure the console outputs match the sequence and timing.
   - Modify the `time.sleep()` values to confirm timing adjustments work.

### Test Results

| Test Scenario                          | Expected Behavior
|----------------------------------------|--------------------------------------
| Arduino lights up Red → Green → Yellow | Correct sequence followed
| Timing for each light                  | Red: 5s, Green: 5s, Yellow: 2s
| Python simulation sequence             | Console shows correct light sequence
| Console simulation timing              | Red: 5s, Green: 5s, Yellow: 2s

## Future Improvements

- Add a pedestrian crossing button.
- Integrate a real-time clock for dynamic timing.
- Add sound effects (buzzer) during the Yellow light phase.
