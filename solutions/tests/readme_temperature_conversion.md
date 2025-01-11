# Temperature Conversion

A Python project to convert temperatures from Celsius to Fahrenheit. Includes a
function and unit tests.

---

## Features

- Convert Celsius to Fahrenheit.
- Unit tests for valid and invalid inputs.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MIT-Emerging-Talent/ET6-foundations-group-11.git
   ```

2. Navigate to the project directory:

   ```bash
   cd ET6-foundations-group-11/solutions/tests
   ```

---

## Usage

Import the function and use it in your code:

```python
from temperature_conversion import celsius_to_fahrenheit

result = celsius_to_fahrenheit(25)
print(f"25°C is equal to {result}°F")
```

---

## Running Tests

Run the unit tests:

```bash
python test_temperature_conversion.py
```

For detailed output, use:

```bash
python -m unittest test_temperature_conversion.py -v
```

---

## Contributing

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Commit your changes:

   ```bash
   git commit -m "Add your feature"
   ```

4. Push your changes:

   ```bash
   git push origin feature/your-feature-name
   ```

5. Open a pull request.

---

## License

MIT License. See [LICENSE](LICENSE) for details.
