def celsius_fahrenheit(temp_c):
    return (temp_c*9/5)+32

def main():
    temp_c = float(input("Insira a temperatura em °C:"))
    temp_f = celsius_fahrenheit(temp_c)
    print(f"\n{temp_c}°C equivalem a {temp_f}°F\n")
    
main()