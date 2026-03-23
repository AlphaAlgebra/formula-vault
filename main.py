import formulas

def main():
    print("--- ALPHALGEBRA FORMULA VAULT v1.0 ---")
    print("Available: slope | midpoint | distance | quit")
    
    while True:
        # Standardize input by removing whitespace and lowercasing
        choice = input("\nSelect a formula: ").strip().lower()
        
        if choice == 'quit':
            print("Session terminated.")
            break
            
        if choice in ['slope', 'midpoint', 'distance']:
            try:
                x1 = float(input("Enter x1: "))
                y1 = float(input("Enter y1: "))
                x2 = float(input("Enter x2: "))
                y2 = float(input("Enter y2: "))
                
                if choice == 'slope':
                    result = formulas.calculate_slope(x1, y1, x2, y2)
                    print(f"Result (m): {result}")
                elif choice == 'midpoint':
                    result = formulas.calculate_midpoint(x1, y1, x2, y2)
                    print(f"Result (xm, ym): {result}")
                elif choice == 'distance':
                    result = formulas.calculate_distance(x1, y1, x2, y2)
                    print(f"Result (d): {result}")
            except ValueError:
                print("Error: Numeric input required.")
        else:
            print(f"Error: '{choice}' is not recognized.")

if __name__ == "__main__":
    main()
