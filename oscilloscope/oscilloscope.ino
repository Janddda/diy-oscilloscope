const int READ_RESOLUTION = 12; 
int channel = A0; 
int value = 0; 

class Sample {
  public:
  unsigned int value;
  unsigned int timeStamp;
};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(230400);  
  //analogReference(DEFAULT); 
  analogReadResolution(READ_RESOLUTION); 
}

void loop() {
  // put your main code here, to run repeatedly: 
  Sample sample = Sample();
  sample.value = analogRead(channel);
  sample.timeStamp = micros(); 
//  Serial.print("Value:");
//  Serial.print(sample.value);
//  Serial.print(",TimeStamp: ");
  Serial.print(sample.value);
  Serial.print(",");
  Serial.println(sample.timeStamp);
  //delay(2);
}
