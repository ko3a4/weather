
---

### 🌦 **weather.py**
```python
import random

conditions = ["Sunny", "Cloudy", "Rainy", "Windy", "Snowy", "Stormy"]
temperatures = range(-10, 36)

def simulate_weather():
    condition = random.choice(conditions)
    temperature = random.choice(temperatures)
    print(f"Today's weather: {condition}, {temperature}°C")

if __name__ == "__main__":
    simulate_weather()
