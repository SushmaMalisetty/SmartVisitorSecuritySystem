import os
import shutil

dataset_path = "dataset"

if not os.path.exists(dataset_path):
    print("Dataset folder does not exist")
    exit()

print("\nAvailable persons:")
persons = os.listdir(dataset_path)

if not persons:
    print("No datasets found")
    exit()

for i, person in enumerate(persons, start=1):
    print(f"{i}. {person}")

choice = input("\nEnter person name to delete (or type ALL to delete everything): ")

if choice.upper() == "ALL":
    confirm = input("Are you sure you want to delete ALL datasets? (yes/no): ")
    if confirm.lower() == "yes":
        shutil.rmtree(dataset_path)
        os.mkdir(dataset_path)
        print("All datasets deleted successfully")
    else:
        print("Operation cancelled")

else:
    person_folder = os.path.join(dataset_path, choice)
    if os.path.exists(person_folder):
        shutil.rmtree(person_folder)
        print(f"Dataset for '{choice}' deleted successfully")
    else:
        print("Person not found")
