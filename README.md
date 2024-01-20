# Squarespace Image Extractor

Squarespace Image Extractor is a desktop application designed to help users download all image assets from a Squarespace website via an XML file. The application provides a simple and intuitive graphical user interface (GUI) that allows users to select an XML file, choose a destination folder, and download the images with ease.

## Features

- Easy-to-use GUI for selecting XML files and destination folders.
- Ability to download all image assets listed in an XML file from a Squarespace website.
- Support for `.jpg` and `.png` image formats.
- Real-time feedback on the download progress.
- Modern and clean interface with a 16:9 aspect ratio.

## Prerequisites

Before running the Squarespace Image Extractor, ensure that you have the following installed:

- Python 3.6 or higher
- `beautifulsoup4` library
- `requests` library
- `lxml` library

You can install the required Python libraries using `pip`:

bash pip3 install beautifulsoup4 requests lxml

## Usage

1. Clone the repository or download the source code to your local machine.
2. Run the application by executing the script with Python:
Replit

bash python3 squarespace_image_extractor.py

3. Use the "Browse local XML File" button to select the XML file containing the image URLs.
4. Use the "Select destination folder" button to choose where the downloaded images should be saved.
5. Click "Start download" to begin the download process. The status will be updated in the application window.
6. Once the download is complete, the images will be available in the chosen destination folder.

## Contributing

Contributions to Squarespace Image Extractor are welcome. Please feel free to submit pull requests, open issues, or suggest new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
