int BAUD = 9600; // our baud  rate for Serial 
int LED = 13; // led pin on most arduino boards
int delay_time = 1000;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(BAUD);
  pinMode(LED, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0){
    delay_time = Serial.parseInt(); 
    Serial.read(); // flushes out any extra bytes in buffer
    
    Serial.println("Changing delay time.");
  }
  digitalWrite(LED, HIGH);
  delay(delay_time);
  digitalWrite(LED, LOW);
  delay(delay_time);
}
