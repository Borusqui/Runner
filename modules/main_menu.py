import time

# Assume these functions are defined elsewhere
def colony_menu(space_agency):
    print("Inside colony_menu")
    # Placeholder for actual logic

def astronaut_menu(space_agency):
    print("Inside astronaut_menu")
    # Placeholder for actual logic

def research_menu(space_agency):
    print("Inside research_menu")
    # Placeholder for actual logic

def print_status(space_agency):
    space_agency.get_status()

def next_month(space_agency):
    print("Have you finished buying, building, researching, and hiring this month? (y/n)")
    choice = input("Enter your choice (y/n): ")
    if choice == "y":
        print("Time flies...")
        time.sleep(3)
        space_agency.next_month()
        quest_manager.check_for_quests()
    else:
        pass  # Do nothing if user chooses not to proceed

def save_and_exit():
    print("Unable to save game at this point of development\n"
          "Are you sure you want to leave? y/n")
    choice = input("Enter your choice (y/n): ")
    if choice.lower() == "y":
        return True  # Signal to break out of the loop
    else:
        print("Thank god!")
        return False  # Continue the loop


def main_menu():
    options = {
        1: colony_menu,
        2: astronaut_menu,
        3: research_menu,
        4: print_status,
        5: next_month,
        6: save_and_exit
    }

    while True:
        print(f"-------------------- MONTH {space_agency.months} --------------------")
        print("Main Menu: \n"
              "What would you like to do?")
        print("1. Build/Check Colonies")
        print("2. Hire/Fire & Check Astronauts")
        print("3. Enter the Research Panel")
        print("4. Check status")
        print("5. Next Month")
        print("6. Save & Exit Game")
        try:
            choice = int(input("Enter your choice (1-6): "))
            if choice in options:
                if choice == 5:
                    options[choice](space_agency)  # Handle special case for option 5
                elif choice == 6:
                    if options[choice]():  # Execute function and check return value
                        break  # Exit loop if save_and_exit returns True
                else:
                    options[choice](space_agency)  # Call the selected menu function
            else:
                print("Enter a number between 1 and 6")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Example usage assuming space_agency and quest_manager are defined elsewhere
space_agency = {'months': 1}  # Placeholder for demonstration
quest_manager = {}  # Placeholder for demonstration

main_menu()
