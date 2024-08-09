import importlib
import subprocess
import sys
from importlib import util
import base64
import os
import py_compile
import tempfile
from PIL import Image
from bitarray import bitarray


LOCAL_DIR = os.getcwd()


class StegoEncoder:
    def __init__(self, image_path: str):
        self.image = Image.open(image_path)
        self.pixels = list(self.image.getdata())

    @staticmethod
    def compile_code(code: str, do_raise=True) -> bytes:
        bytecode = b''
        temp_script_file = ".temp.py"
        temp_bytecode = ".temp.pyc"
        with open(temp_script_file, "w") as fp:
            fp.write(code)
        out_file = py_compile.compile(file=temp_script_file, cfile=temp_bytecode, doraise=do_raise)
        with open(out_file, "rb") as f:
            bytecode = f.read()
        os.unlink(temp_script_file)
        os.unlink(temp_bytecode)
        return bytecode

    @staticmethod
    def bytecode_to_bits(bytecode: bytes) -> bitarray:
        end_marker = b'!END!'
        bytecode += end_marker
        encoded_bytecode = base64.b64encode(bytecode)
        bit_array = bitarray()
        bit_array.frombytes(encoded_bytecode)
        return bit_array

    def embed_bytecode(self, bytecode: bytes, output_path: str):
        bit_array = self.bytecode_to_bits(bytecode)
        flat_pixels = [channel for pixel in self.pixels for channel in pixel[:3]]

        if len(bit_array) > len(flat_pixels):
            raise ValueError("Image size is too small to hold the bytecode.")

        for i, bit in enumerate(bit_array):
            flat_pixels[i] = (flat_pixels[i] & 0xFE) | bit

        new_pixels = [tuple(flat_pixels[i:i + 3]) + (255,) for i in range(0, len(flat_pixels), 3)]

        encoded_image = Image.new(self.image.mode, self.image.size)
        encoded_image.putdata(new_pixels)
        encoded_image.save(output_path)


class StegoDecoder:
    def __init__(self, image_path: str):
        self.image = Image.open(image_path)
        self.pixels = list(self.image.getdata())

    @staticmethod
    def bits_to_bytecode(bit_array: bitarray) -> bytes:
        if len(bit_array) % 8 != 0:
            bit_array = bit_array[:-(len(bit_array) % 8)]
        encoded_bytecode = bit_array.tobytes()
        bytecode = base64.b64decode(encoded_bytecode)
        unique_sequence = b'\x01\xFE\x01\x59\x01'
        bytecode = bytecode.replace(unique_sequence, b'\x00')
        return bytecode

    def extract_bytecode_to_pyc(self) -> str:
        flat_pixels = [channel for pixel in self.pixels for channel in pixel[:3]]
        extracted_bits = bitarray()
        for pixel in flat_pixels:
            extracted_bits.append(pixel & 1)

        bytecode = self.bits_to_bytecode(extracted_bits)
        temp_bytecode_file = "./_temp_bytecode.pyc"
        with open(temp_bytecode_file, "wb") as fp:
            fp.write(bytecode)
        return temp_bytecode_file

    def execute_bytecode(self, delete_after_execution=False):
        bytecode_pyc_file = self.extract_bytecode_to_pyc()
        spec = importlib.util.spec_from_file_location('tempcode', bytecode_pyc_file)
        extracted_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(extracted_module)
        if delete_after_execution:
            os.remove(bytecode_pyc_file)
        return extracted_module


def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(f"Output: {result.stdout}")
        print(f"Error: {result.stderr}")
        sys.exit(result.returncode)
    return result.stdout.strip()


def select_file(prompt, file_extension=None):
    files = [f for f in os.listdir('.') if os.path.isfile(f) and (file_extension is None or f.endswith(file_extension))]
    for i, file in enumerate(files, 1):
        print(f"{i}. {file}")
    file_index = int(input(f"{prompt} [1-{len(files)}]: ")) - 1
    return files[file_index]


def interactive_menu():
    while True:
        print("\nMenu:")
        print("1. Embed Python script into an image")
        print("2. Execute embedded code from an image")
        print("3. Execute and delete image with embedded code")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            source_file = select_file("Select a Python script to embed", ".py")
            image_file = select_file("Select an image file", ".png")
            output_file = input("Enter the name for the output image file (e.g., output.png): ")

            encoder = StegoEncoder(image_file)
            try:
                with tempfile.NamedTemporaryFile(delete=False, suffix='.pyc') as temp_file:
                    temp_file.close()
                    py_compile.compile(source_file, cfile=temp_file.name, doraise=True)
                    with open(temp_file.name, 'rb') as f:
                        bytecode = f.read()
                    os.remove(temp_file.name)
                encoder.embed_bytecode(bytecode, output_file)
                print(f"Successfully embedded {source_file} into {output_file}")
            except py_compile.PyCompileError as e:
                print(f"Error compiling {source_file}: {e}")
            except Exception as e:
                print(f"An error occurred during encoding: {e}")

        elif choice == '2':
            image_file = select_file("Select an image file to decode and execute", ".png")
            decoder = StegoDecoder(image_file)
            try:
                decoder.execute_bytecode()
                print(f"Executed bytecode from {image_file}")
            except Exception as e:
                print(f"An error occurred during decoding: {e}")

        elif choice == '3':
            image_file = select_file("Select an image file to decode, execute, and delete", ".png")
            decoder = StegoDecoder(image_file)
            try:
                decoder.execute_bytecode(delete_after_execution=True)
                os.remove(image_file)
                print(f"Executed bytecode from {image_file} and deleted the image.")
            except Exception as e:
                print(f"An error occurred during decoding: {e}")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    interactive_menu()
