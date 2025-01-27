'''
Ong, Edward T.
Sese, Jacob Mark C.
Takushi, Brannon Y.
CYB - 201
Finals Project
24/10/2024
'''

class Luggage:
    def __init__(self, id, destination):
        self.id = id
        self.destination = destination

    def __str__(self):
        return f"Luggage ID: {self.id}, Destination: {self.destination}"


class LuggageSortingSystem:
    def __init__(self):
        self.queue = []
        self.valid_destinations = {
            "Asia": ["Japan", "China", "India", "Thailand", "Singapore", "Philippines"],
            "North America": ["USA", "Canada", "Mexico", "Cuba", "Jamaica"],
            "Europe": ["UK", "France", "Germany", "Italy", "Spain"]
        }

    def add_luggage(self, luggage):
        continent, country = luggage.destination.split(": ")
        if continent not in self.valid_destinations:
            print(f"Error: Invalid continent '{continent}'.")
            return
        
        if country not in self.valid_destinations[continent]:
            print(f"Error: Invalid country '{country}' for continent '{continent}'. Please choose from: {', '.join(self.valid_destinations[continent])}")
            return

        self.queue.append(luggage)
        print("===========================================================")
        print(f"Added: {luggage}")
        print("===========================================================")

    def remove_luggage(self):
        if self.queue:
            removed_luggage = self.queue.pop(0)
            print(f"\nRemoved: {removed_luggage}")
        else:
            print("\nNo luggage to remove.")

    def view_luggage(self):
        if not self.queue:
            print("\nNo luggage in the queue.")
        else:
            print("===========================================================")
            print("Current Luggage Queue:")
            for luggage in self.queue:
                print(luggage)
            print("===========================================================")

    def real_time_tracking(self):
        if not self.queue:
            print("\nNo luggage to track.")
        else:
            print("===========================================================")
            print("Tracking Luggage:")
            for luggage in self.queue:
                print(f"Tracking: {luggage.id} to {luggage.destination}")
            print("===========================================================")

    def reroute_luggage(self, luggage_id, new_destination):
        for luggage in self.queue:
            if luggage.id == luggage_id:
                luggage.destination = new_destination
                print(f"\nLuggage ID {luggage_id} has been rerouted to {new_destination}.")
                return
        
        print(f"\nError: Luggage ID {luggage_id} not found.")

    def show_countries(self, continent_name):
        if continent_name in self.valid_destinations:
            print("===========================================================")
            print(f"Countries in {continent_name}:")
            for country in self.valid_destinations[continent_name]:
                print(f"- {country}")
        else:
            print("\nInvalid continent.")


def main():
    lss = LuggageSortingSystem()
    
    while True:
        print("\n===========================================================")
        print("Luggage Sorting System (LSS) Airport:")
        print("===========================================================")
        print("1. Choose a Continent and Add Luggage")
        print("2. Remove Luggage")
        print("3. View Luggage")
        print("4. Real-time Tracking")
        print("5. Reroute Luggage")
        print("6. Exit")
        print("===========================================================")
        
        choice = input("Choose an option from(1-6): ")
        
        if choice == '1':
            print("===========================================================")
            print("Choose a continent:")
            for index, continent in enumerate(lss.valid_destinations.keys(), start=1):
                print(f"{index}. {continent}")

            # Continent selection validation
            while True:
                try:
                    print("===========================================================")
                    continent_choice = int(input("Enter the number of your choice: "))
                    if 1 <= continent_choice <= len(lss.valid_destinations):
                        continent_name = list(lss.valid_destinations.keys())[continent_choice - 1]
                        lss.show_countries(continent_name)
                        break
                    else:
                        print("===========================================================")
                        print("Invalid choice. Please select a valid continent number.")
                except ValueError:
                    print("===========================================================")
                    print("Invalid input. Please enter a number.")

            while True:
                print("===========================================================")
                country_choice = input(f"Enter the name of the country you want to add in {continent_name}: ")
                print("===========================================================")
                
                # Check if the chosen country is valid for the selected continent
                if country_choice in lss.valid_destinations[continent_name]:
                    luggage_id = input("Enter Luggage ID: ")
                    destination = f"{continent_name}: {country_choice}"
                    luggage = Luggage(luggage_id, destination)
                    lss.add_luggage(luggage)
                    break  # Exit loop if the country is valid
                else:
                    # If invalid country, loop back to country selection
                    print(f"Invalid country '{country_choice}' for continent '{continent_name}'.")
                    print("===========================================================")
                    print(f"Please choose from the list: ")
                    for country in lss.valid_destinations[continent_name]:
                        print(f"- {country}")
                    print("Let's try again.")

        elif choice == '2':
            lss.remove_luggage()
        
        elif choice == '3':
            lss.view_luggage()
        
        elif choice == '4':
            lss.real_time_tracking()
        
        elif choice == '5':
            if not lss.queue:
                print("\nNo luggage to reroute.")
            else:
                print("\nLuggage List:")
                for index, luggage in enumerate(lss.queue, start=1):
                    print(f"{index}. {luggage}")
                
                while True:
                    try:
                        print("===========================================================")
                        print("Choose a number for reroute:")
                        luggage_num = int(input("Enter number "))
                        if 1 <= luggage_num <= len(lss.queue):
                            selected_luggage = lss.queue[luggage_num - 1]
                            new_destination = input("Enter New Destination (Continent: Country): ")
                            lss.reroute_luggage(selected_luggage.id, new_destination)
                            print("===========================================================")
                            break
                        else:
                            print("===========================================================")
                            print(f"Invalid number. Please select a number between 1 and {len(lss.queue)}.")
                            print("===========================================================")
                    except ValueError:
                        print("===========================================================")
                        print("Invalid input. Please enter a valid number.")
                        print("===========================================================")

        elif choice == '6':
            print("===========================================================")
            print("Exiting the system.")
            print("===========================================================")
            break

        else:
            print("===========================================================")
            print("Invalid choice. Please select a valid option.")
            print("===========================================================")

if __name__ == "__main__":
    main()



