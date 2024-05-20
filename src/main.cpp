#include <Arduino.h>
// defines pins numbers//*/
// defines pins numbers
const int trigPin = 27;
const int echoPin = 26;
const int motorPin = 32;
// defines variables
long duration;
int distance;

// Set LED_BUILTIN if it is not defined by Arduino framework
# ifndef LED_BUILTIN
# define LED_BUILTIN 2
# endif


void setup() {
    pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
    pinMode(echoPin, INPUT); // Sets the echoPin as an Input
    Serial.begin(9600); // Starts the serial communication
    pinMode(LED_BUILTIN, OUTPUT);
    pinMode(motorPin, OUTPUT); // Sets the motorPin as an Output
}
void loop() {
    // Clears the trigPin
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    // Sets the trigPin on HIGH state for 10 micro seconds
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    // Reads the echoPin, returns the sound wave travel time in microseconds
    duration = pulseIn(echoPin, HIGH);
    // Calculating the distance
    distance = duration * 0.034 / 2;
    // Prints the distance on the Serial Monitor
    if (distance < 50) {
        digitalWrite(LED_BUILTIN, HIGH);
        digitalWrite(motorPin, LOW);
    } else {
        digitalWrite(LED_BUILTIN, LOW);
        digitalWrite(motorPin, HIGH);
    }
    Serial.print("Distance: ");
    Serial.println(distance);
}