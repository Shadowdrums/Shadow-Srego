# Shadow-Srego
embed python code into images and execute the code from an image

# Python Script Steganography Tool

This is a command-line tool for embedding and executing Python scripts hidden within image files using steganography techniques. It allows you to encode a Python script into an image, execute the script from within an encoded image, and optionally delete the image after execution.

## Features

- **Embed Python Script into an Image**: Hide a compiled Python script (`.pyc` bytecode) within the pixels of an image.
- **Execute Embedded Code**: Extract and execute the embedded Python bytecode from an image.
- **Self-destruct Option**: Execute the embedded code and delete the image and temporary bytecode file afterward.

## Requirements

- Python 3.x
- The following Python packages:
  - `Pillow`
  - `bitarray`

You can install the required packages using pip:

```bash
pip install Pillow bitarray
```

## Usage
Run the script from the command line:
```sh
python stego_tool.py
```

## Menu Options
Embed Python Script into an Image:

- Select a Python script (.py file) and an image (.png file).
The script will compile the Python code to bytecode (.pyc) and embed it into the selected image.
You will be prompted to enter the output file name for the encoded image.
Execute Embedded Code from an Image:

- Select an image file (.png) that contains embedded Python bytecode.
The script will extract the bytecode, execute it, and display the result.
Execute and Delete Image with Embedded Code:

- Select an image file (.png) that contains embedded Python bytecode.
The script will extract and execute the bytecode, then delete both the image file and the temporary bytecode file.

```Exit: Exit the tool.```

## Example Workflow
Embed a Python Script:

Place a .py script in the same directory as the tool.
- Run the tool and select option 1.
Choose the script and an image file (.png) to hide the script in.
Specify an output file name for the encoded image.
Execute Embedded Script:

### Run the tool and select option 2.
- Choose the encoded image file.
The tool will execute the embedded script.
Execute and Delete:

### Run the tool and select option 3.
- Choose the encoded image file.
The tool will execute the embedded script and delete the image.
How It Works


## Embedding:

The Python script is compiled into bytecode (.pyc).
The bytecode is converted into a bit array.
The bit array is then embedded into the least significant bit of the image pixels.
Decoding:

The embedded bit array is extracted from the image pixels.
The bit array is converted back into bytecode.
The bytecode is then executed.


## Limitations
The image must be large enough to contain the bytecode. If the bytecode is too large for the image, the tool will raise an error.
The tool currently supports .png images.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request.

Original framework is by DJ Stomp 

[DJ Stomp Zone GitHub](https://github.com/DJStompZone)


## Acknowledgments
The Pillow library for image manipulation.
The bitarray library for handling binary data.


# Disclaimer
This tool is for educational purposes only. Use it responsibly and do not use it for any malicious activity.
