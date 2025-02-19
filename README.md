# Steganography Tool (GUI-Based)

## Description
This Python-based steganography tool allows users to **hide secret messages inside images** and **retrieve hidden messages** using a **Tkinter graphical interface**. The tool utilizes **LSB (Least Significant Bit) steganography** via the `stegano` library.

## Features
✅ **Graphical User Interface (GUI)** using Tkinter  
✅ **Select an image** from your system  
✅ **Hide a secret message** inside the image  
✅ **Extract a hidden message** from an image  
✅ **Save the encoded image** with hidden data  
✅ **Supports PNG, JPG, and JPEG formats**  
✅ **Error handling and alerts**  

## Prerequisites
Ensure you have Python **3.x** installed. You can check your Python version with:
```bash
python --version
```

## Installation
### Step 1: Clone or Download the Repository
Clone this repository using Git or download the script manually.
```bash
git clone https://github.com/pb2106/stegnography.git
cd steganography
```

### Step 2: Install Required Dependencies
Run the following command to install the necessary Python modules:
```bash
pip install pillow stegano
```

## How to Run
Execute the following command in your terminal or command prompt:
```bash
python stego.py
```

## Usage
### 1. **Select an Image**
- Click **"Select Image"** and choose a PNG, JPG, or JPEG file.

### 2. **Encrypt a Message**
- Enter your **secret message** in the text field.
- Click **"Encrypt & Save"** to hide the message inside the image.
- Choose a location to **save the encoded image**.

### 3. **Decrypt a Message**
- Select an **image with a hidden message**.
- Click **"Decrypt Message"** to reveal the hidden text.

## Supported Formats
- PNG
- JPG
- JPEG

## Troubleshooting
- **No image selected?** Ensure you have chosen an image before encrypting/decrypting.
- **No message found?** Make sure the image actually contains a hidden message.
- **Error while saving?** Ensure you have the correct file permissions.
