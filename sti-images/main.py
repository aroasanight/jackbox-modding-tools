import shutil
import os
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image

filelist = [
"Airplane.jpg",
"ApplePicking.jpg",
"ArtMuseum.jpg",
"AvocadoToast.jpg",
"BBQ.jpg",
"BabyAnnouncement.jpg",
"Barn.jpg",
"Baseball.jpg",
"Basketball.jpg",
"Bat.jpg",
"BathroomStall.jpg",
"Beach.jpg",
"Bear.jpg",
"Bicycle.jpg",
"BirthdayParty.jpg",
"Bonfire.jpg",
"BookStore.jpg",
"Boxing.jpg",
"BubbleBath.jpg",
"Cabin.jpg",
"Camping.jpg",
"Cat.jpg",
"Chimpanzee.jpg",
"Chinese.jpg",
"CoffeeShop.jpg",
"CompactCar.jpg",
"ConcertStage.jpg",
"Condo.jpg",
"CondoInterior.jpg",
"Convertible.jpg",
"DMV.jpg",
"Dentist.jpg",
"Desert.jpg",
"Dog.jpg",
"Dolphin.jpg",
"Elephant.jpg",
"EngagementRing.jpg",
"FarmHouse.jpg",
"FeetOnBeach.jpg",
"Ferret.jpg",
"Field.jpg",
"Fireworks.jpg",
"Football.jpg",
"Forest.jpg",
"Funeral.jpg",
"GasStation.jpg",
"Giraffe.jpg",
"Goldfish.jpg",
"Gorilla.jpg",
"Graduation.jpg",
"Guacamole.jpg",
"Gym.jpg",
"Gyro.jpg",
"Hamburger.jpg",
"Hockey.jpg",
"HomeRepair.jpg",
"Horse.jpg",
"HorseRace.jpg",
"HotAirBalloon.jpg",
"HotDogs.jpg",
"HouseParty.jpg",
"IceCream.jpg",
"Igloo.jpg",
"Indian.jpg",
"Island.jpg",
"Jeep.jpg",
"Jungle.jpg",
"Kite.jpg",
"Kittens.jpg",
"Laundromat.jpg",
"Lion.jpg",
"London.jpg",
"Mansion.jpg",
"MeatSkewer.jpg",
"Meditation.jpg",
"Mexican.jpg",
"Minivan.jpg",
"Moose.jpg",
"Motel.jpg",
"Motorcycle.jpg",
"Mountains.jpg",
"MovieTheater.jpg",
"Moving.jpg",
"Museum.jpg",
"Nascar.jpg",
"NewYorkCity.jpg",
"Office.jpg",
"Orangutan.jpg",
"Parade.jpg",
"Paris.jpg",
"Park.jpg",
"ParkingTicket.jpg",
"PickupTruck.jpg",
"Pig.jpg",
"Pizza.jpg",
"PoolParty.jpg",
"PostOffice.jpg",
"Puppies.jpg",
"Rabbit.jpg",
"Rainstorm.jpg",
"RollerCoaster.jpg",
"Rollerblades.jpg",
"RomanticGetaway.jpg",
"Russia.jpg",
"Sailboat.jpg",
"Salad.jpg",
"Salmon.jpg",
"SanFrancisco.jpg",
"Segway.jpg",
"SemiTruck.jpg",
"ShootingStar.jpg",
"Skyscraper.jpg",
"Snake.jpg",
"Soccer.jpg",
"Spider.jpg",
"StationWagon.jpg",
"Statue.jpg",
"Steak.jpg",
"SubwayCar.jpg",
"Suitcase.jpg",
"Sunset.jpg",
"Tennis.jpg",
"Traffic.jpg",
"Train.jpg",
"VR.jpg",
"Vegas.jpg",
"Volleyball.jpg",
"Voting.jpg",
"Wedding.jpg",
"Wrestling.jpg",
"WritingDesk.jpg"
]

def browse_input_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        input_folder_entry.delete(0, tk.END)
        input_folder_entry.insert(0, folder_selected)

def browse_output_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        output_folder_entry.delete(0, tk.END)
        output_folder_entry.insert(0, folder_selected)

def browse_output_lq_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        output_lq_folder_entry.delete(0, tk.END)
        output_lq_folder_entry.insert(0, folder_selected)

def convert_image_to_jpg(image_path, output_path, quality=100):
    """Converts an image to .jpg format and saves it to the output path."""
    with Image.open(image_path) as img:
        rgb_img = img.convert('RGB')  # Convert to RGB (required for saving as JPG)
        rgb_img.save(output_path, 'JPEG', quality=quality)

def get_jpg_filename(filename):
    """Convert .png or .jpeg filenames to .jpg."""
    # Replace .jpeg or .png with .jpg
    return os.path.splitext(filename)[0] + ".jpg"

def replace_images():
    # Get the folder paths from the user inputs
    input_dir = input_folder_entry.get()
    output_dir = output_folder_entry.get()
    output_lq_dir = output_lq_folder_entry.get()

    # Check if directories exist
    if not os.path.exists(input_dir) or not os.path.exists(output_dir) or not os.path.exists(output_lq_dir):
        messagebox.showerror("Error", "One or more directories do not exist.")
        return

    try:
        # Remove existing images in output directories
        output_images = os.listdir(output_dir)
        output_images_lq = os.listdir(output_lq_dir)

        for file in output_images:
            os.remove(os.path.join(output_dir, file))
        for file in output_images_lq:
            os.remove(os.path.join(output_lq_dir, file))

        # Get all input images with supported formats
        input_images = [file for file in os.listdir(input_dir) if file.lower().endswith(('.jpg', '.jpeg', '.png'))]

        if not input_images:
            messagebox.showerror("Error", "No supported image files found in the input directory.")
            return

        input_photo_index = 0

        # Replace images
        for line in filelist:
            line = line.strip()
            random_image = input_images[input_photo_index]
            input_photo_index += 1
            if input_photo_index >= len(input_images):
                input_photo_index = 0

            output_image = line
            output_image_lq = line[:-4] + "-thumb.jpg"

            input_image_path = os.path.join(input_dir, random_image)

            # Convert to JPG if necessary and update the filename correctly
            if random_image.lower().endswith(('.jpeg', '.png')):
                converted_image_name = get_jpg_filename(random_image)
                converted_image_path = os.path.join(input_dir, converted_image_name)
                convert_image_to_jpg(input_image_path, converted_image_path)
                input_image_path = converted_image_path

            # Copy converted image to the full-quality output folder
            shutil.copy(input_image_path, os.path.join(output_dir, output_image))

            # Convert and save a lower-quality version for the low-quality folder
            low_quality_image_path = os.path.join(output_lq_dir, output_image_lq)
            convert_image_to_jpg(input_image_path, low_quality_image_path, quality=5)  # 25 is 1/4 of the default 100 quality

        messagebox.showinfo("Success", "Images replaced successfully.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main tkinter window
window = tk.Tk()
window.title("Survive The Internet - Photosharing Image Modder")

# Labels and text entry for folder paths with Browse buttons
input_folder_label = tk.Label(window, text="Input Images Folder:")
input_folder_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
input_folder_entry = tk.Entry(window, width=50)
input_folder_entry.insert(0, "~/Documents/sti-images/input_images")
input_folder_entry.grid(row=0, column=1, padx=10, pady=5)
input_browse_button = tk.Button(window, text="Browse", command=browse_input_folder)
input_browse_button.grid(row=0, column=2, padx=5, pady=5)

output_folder_label = tk.Label(window, text="Output Images Folder:")
output_folder_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
output_folder_entry = tk.Entry(window, width=50)
output_folder_entry.insert(0, "~/Library/Application Support/Steam/steamapps/common/The Jackbox Party Pack 4/The Jackbox Party Pack 4.app/Contents/Resources/macos/games/SurviveTheInternet/content/STIPhoto")
output_folder_entry.grid(row=1, column=1, padx=10, pady=5)
output_browse_button = tk.Button(window, text="Browse", command=browse_output_folder)
output_browse_button.grid(row=1, column=2, padx=5, pady=5)

output_lq_folder_label = tk.Label(window, text="Thumbnail Output Folder:")
output_lq_folder_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
output_lq_folder_entry = tk.Entry(window, width=50)
output_lq_folder_entry.insert(0, "~/Library/Application Support/Steam/steamapps/common/The Jackbox Party Pack 4/The Jackbox Party Pack 4.app/Contents/Resources/macos/games/SurviveTheInternet/content/STIPhoto/Thumbnails")
output_lq_folder_entry.grid(row=2, column=1, padx=10, pady=5)
output_lq_browse_button = tk.Button(window, text="Browse", command=browse_output_lq_folder)
output_lq_browse_button.grid(row=2, column=2, padx=5, pady=5)

# Go button
go_button = tk.Button(window, text="Go", command=replace_images)
go_button.grid(row=3, column=0, columnspan=3, pady=10)

# Start the tkinter main loop
window.mainloop()