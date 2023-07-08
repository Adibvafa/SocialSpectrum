import webbrowser
import os

# Search for Google Chrome and open the best matching app
webbrowser.open("https://www.google.com/chrome/")

# Search for AI in Google Images
search_term = "ai"
webbrowser.open(f"https://www.google.com/search?q={search_term}&tbm=isch")

# Save the first image file as a.png in the desktop directory
first_image = webbrowser.get_images(search_term)[0]
os.system(f"wget {first_image} -O 'C:\\Users\\<username>\Desktop\\a.png'")