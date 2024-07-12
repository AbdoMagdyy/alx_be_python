from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_datetime = datetime.now()
    # Format the current date and time
    current_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    # Print the current date and time
    print(f"Current date and time: {current_date}")

def calculate_future_date():
    # Prompt the user to enter a number of days
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    # Get the current date
    current_date = datetime.now().date()
    # Calculate the future date by adding the specified number of days
    future_date = current_date + timedelta(days=number_of_days)
    # Format the future date
    future_date_str = future_date.strftime("%Y-%m-%d")
    # Print the future date
    print(f"Future date: {future_date_str}")

# Main function to call the above functions
def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
