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
or you can use the requirements.txt
```bash
pip install requirements.txt
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

## MIT License

Copyright (c) 2024 Shadowdrums

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request.

Original framework is by DJ Stomp 

[DJ Stomp Zone GitHub](https://github.com/DJStompZone)


## Acknowledgments
- The Pillow library for image manipulation.

- The bitarray library for handling binary data.


# Disclaimer

## Intended Use and Purpose

This software is intended solely for educational purposes and as a tool for experimentation with steganography techniques in Python programming. The creators of this software do not endorse or condone the use of this tool for any illegal or unethical activities, including but not limited to unauthorized data embedding, data exfiltration, or any form of malicious software distribution.

## Responsibility of the User

By using this software, you agree that you are solely responsible for any actions you take with it. You are expected to use this software in a manner that is lawful, ethical, and compliant with all applicable local, national, and international laws and regulations. Misuse of this software for activities such as unauthorized access to data, distribution of malicious code, or any other harmful actions is strictly prohibited and could result in legal consequences.

## No Warranty

This software is provided "as is" without any guarantees or warranties of any kind, express or implied. The authors make no representations or warranties regarding the accuracy, completeness, reliability, or suitability of the software for any particular purpose. Use of this software is at your own risk.

## Limitation of Liability

In no event shall the authors, contributors, or copyright holders be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this software, even if advised of the possibility of such damage.

## Compliance with Laws

It is the responsibility of the user to ensure that their use of this software complies with all applicable laws, regulations, and policies. The authors do not assume any responsibility for the user's legal compliance and shall not be held liable for any legal issues that may arise from the use of this software.

## Amendments

The authors reserve the right to make changes to this disclaimer at any time. It is the responsibility of the user to review this disclaimer periodically for updates. Continued use of the software after any such changes shall constitute the user's acceptance of these changes.

