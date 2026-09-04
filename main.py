import sys
from modules.data_loader import load_data
from modules.stats_calculator import calculate_team_stats
from modules.ml_predictor import train_and_predict

def display_menu():
    
    print("\n" + "="*45)
    print("--- CRICKET PLAYER PERFORMANCE PREDICTOR ---")
    print("="*45)
    print("1. Load & View T20 Data")
    print("2. Calculate Franchise Statistics")
    print("3. Predict Player Performance (ML Model)")
    print("4. Exit")
    print("="*45)

def main():
    df = None
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            print("\n[INFO] Loading data...")
            df = load_data()
        elif choice == '2':
            calculate_team_stats(df)
        elif choice == '3':
            train_and_predict(df)
        elif choice == '4':
            print("\nExiting the predictor. Goodbye!")
            sys.exit()
        else:
            print("\n[ERROR] Invalid choice. Please select from 1 to 4.")

if __name__ == "__main__":
    main()