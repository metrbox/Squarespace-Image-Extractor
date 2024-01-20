import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import requests
import os

window = tk.Tk()
window.title('Squarespace Image Extractor by @MetrBox')
window.geometry("640x360")
window.config(background="#ffffff")


xmlfile = ''
folder_selected = ''


def browseFiles():
    global xmlfile, labeltext
    xmlfile = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("XML files", "*.xml"), ("all files", "*.*")))
    print(f"Selected XML file: {xmlfile}")  
    if xmlfile:
        if folder_selected == '':
            labeltext.set("XML file has been selected. Please select destination folder")
        else:
            labeltext.set("XML file and destination folder have been selected. Ready to start download")
    else:
        labeltext.set("No XML file selected. Please select an XML file.")


def extract_hyperlinks_from_xml(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    html_content = ""
    for elem in root.iter():
        if elem.text and 'http' in elem.text:
            html_content += elem.text
    soup = BeautifulSoup(html_content, 'lxml')
    img_tags = soup.find_all('img', {'src': True})
    images = [img['src'] for img in img_tags if 'images.squarespace-cdn.com' in img['src']]
    return images


def download_links(links, folder_selected):
    for link in links:
        try:
            response = requests.get(link)
            response.raise_for_status()
            filename = os.path.basename(link)
            file_path = os.path.join(folder_selected, filename)
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded {filename}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download {link}: {e}")


def download(): 
    global labeltext
    print("Download function triggered.")  # Debug print
    if xmlfile == '':
        labeltext.set("Please select XML file")
        print("No XML file selected.")  # Debug print
    elif folder_selected == '':
        labeltext.set("Please select destination folder")
        print("No destination folder selected.")  # Debug print
    else:
        labeltext.set("Downloading images. Please wait...")
        print("Downloading images...")  # Debug print
        links = extract_hyperlinks_from_xml(xmlfile)
        if not links:
            labeltext.set("No images found to download.")
            print("No images found in the XML file.")  # Debug print
        else:
            download_links(links, folder_selected)
            labeltext.set("Finished downloading all images")
            print("Finished downloading all images.")  # Debug print


def destination():
    global folder_selected, labeltext
    folder_selected = filedialog.askdirectory()
    print(f"Selected destination folder: {folder_selected}")  # Debug print
    if not xmlfile:
        labeltext.set("Destination folder has been selected. Please select XML file.")
    else:
        labeltext.set("XML file and destination folder have been selected. Ready to start download.")


def close_app():
    window.destroy()


style = ttk.Style()
style.configure('TButton', font=('Arial', 10), padding=6)
style.map('TButton', foreground=[('active', 'blue')], background=[('active', 'lightgrey')])


frame = ttk.Frame(window, padding="10")
frame.grid(sticky=(tk.W, tk.E, tk.N, tk.S))
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)


button_explore = ttk.Button(frame, text="Browse local XML File", command=browseFiles)
button_destination = ttk.Button(frame, text="Select destination folder", command=destination)
button_download = ttk.Button(frame, text="Start download", command=download)
button_exit = ttk.Button(frame, text="Exit", command=close_app)
labeltext = tk.StringVar()
labeltext.set("Select XML file and destination folder")
label = tk.Label(frame, textvariable=labeltext, font=('Arial', 12), background="#f0f0f0", foreground="#333")


button_explore.grid(row=0, column=0, padx=5, pady=5, sticky='ew')
button_destination.grid(row=1, column=0, padx=5, pady=5, sticky='ew')
button_download.grid(row=2, column=0, padx=5, pady=5, sticky='ew')
button_exit.grid(row=3, column=0, padx=5, pady=5, sticky='ew')
label.grid(row=4, column=0, padx=5, pady=5, sticky='ew')


window.mainloop()
