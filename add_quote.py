import json

def load_data():
    with open('db.json', 'r') as file:
        data = json.load(file)
    return data 

def write_data(data):
    with open('db.json', 'w') as file:
        json.dump(data, file, indent=2)

if __name__ == "__main__":
    database = load_data()

    print("Enter asked Input type ('exit' to stop it)\n")
    while True:
        quote = input("Enter the new quote: ")
        if quote.lower() == 'exit':break
        
        animeName = input("Enter the anime name: ")
        if animeName.lower() == 'exit': break

        image = input("Enter the image or quote URL: ")
        if image.lower() == 'exit': break

        new_entry = {"quote": quote, "animeName": animeName, "image": image}
        database["quotes"].append(new_entry)
        print("New entry added to the databases successfully!")

    write_data(database)
    print("New entries added successfully!")
