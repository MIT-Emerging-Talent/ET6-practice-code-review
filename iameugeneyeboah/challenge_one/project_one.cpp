// Define LED pins
const int redLight = 13;   // Red LED connected to pin 13
const int yellowLight = 12; // Yellow LED connected to pin 12
const int greenLight = 11;  // Green LED connected to pin 11

void setup() {
  // Set all LED pins as outputs
  pinMode(redLight, OUTPUT);
  pinMode(yellowLight, OUTPUT);
  pinMode(greenLight, OUTPUT);
}

void loop() {
  // Turn on Red Light
  digitalWrite(redLight, HIGH);
  digitalWrite(yellowLight, LOW);
  digitalWrite(greenLight, LOW);
  delay(5000); // Wait for 5 seconds

  // Turn on Green Light
  digitalWrite(redLight, LOW);
  digitalWrite(yellowLight, LOW);
  digitalWrite(greenLight, HIGH);
  delay(5000); // Wait for 5 seconds

  // Turn on Yellow Light
  digitalWrite(redLight, LOW);
  digitalWrite(yellowLight, HIGH);
  digitalWrite(greenLight, LOW);
  delay(2000); // Wait for 2 seconds
}
