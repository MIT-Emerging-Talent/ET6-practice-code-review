# BMI Calculator

## What Is This?

This is a simple Python program that calculates your Body Mass Index (BMI). It  
works with both metric (kg/m²) and imperial (lbs/in²) units. It tells you if  
you’re underweight, normal weight, overweight, or obese.  

---

## How It Works  

The program uses these formulas:  

### Metric (kg and meters)

BMI = Weight (kg) / Height (m)²

### Imperial (lbs and inches)

BMI = (Weight (lbs) × 703) / Height (in)²

### BMI Categories  

- **Underweight**: BMI < 18.5  
- **Normal weight**: 18.5 ≤ BMI < 24.9  
- **Overweight**: 25 ≤ BMI < 29.9  
- **Obesity**: BMI ≥ 30  

---

## What’s Included?  

- **BMI Calculator**: You can enter your weight, height, and unit system.  
- **BMI Category**: The program shows which category you fall into.  
- **Unit Tests**: Tests ensure the program works as expected.  

---

## How To Use It  

### 1. Set It Up  

1. Make sure you have Python 3.7 or higher installed.  
2. Download the project:  

   ```bash
   git clone https://github.com/your-username/bmi-calculator.git
   cd bmi-calculator

3. Move into the project directory:

   ```bash
   cd bmi-calculator

## Run the Program

   Run the program by typing this in the terminal:

  python bmi_calculator.py

### 3. Run Tests

To test the program, use the appropriate command for testing

   python -m unittest discover tests

### Key Features

- **Works with Metric and Imperial Units**: You can choose between kg/m²  
  or lbs/in².
- **User-Friendly**: Easy-to-follow instructions and error messages.
- **Accurate**: Displays BMI category based on your results.

## Contributing

- Use branch names like `feature/<description>` or `bugfix/<description>`.
- Make sure all tests pass before submitting a pull request.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
