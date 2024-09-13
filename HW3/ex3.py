class Temperature:
    def __init__(self, celsius=0.0):
        self._celsius = celsius

    @property
    def celsius(self): #отримати температуру в цельсіях
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9
    

temp = Temperature(25)

print(f"Temperature in Celsius: {temp.celsius}°C")
print(f"Temperature in Fahrenheit: {temp.fahrenheit}°F")
    
temp.fahrenheit = 100
print(f"Updated Temperature in Celsius: {temp.celsius}°C")  
print(f"Updated Temperature in Fahrenheit: {temp.fahrenheit}°F") 