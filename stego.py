import tkinter as tk
from tkinter import filedialog, messagebox
from stegano.lsb import hide, reveal
from PIL import Image, ImageTk

class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Steganography Tool")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Title Label
        tk.Label(root, text="Image Steganography", font=("Arial", 16, "bold")).pack(pady=10)

        # Image Selection Button
        self.btn_select = tk.Button(root, text="Select Image", command=self.select_image, font=("Arial", 12))
        self.btn_select.pack(pady=5)

        # Display Image
        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

        # Message Entry
        self.message_entry = tk.Entry(root, width=50, font=("Arial", 12))
        self.message_entry.pack(pady=5)
        self.message_entry.insert(0, "Enter secret message...")

        # Encrypt & Decrypt Buttons
        self.btn_encrypt = tk.Button(root, text="Encrypt & Save", command=self.encrypt_message, font=("Arial", 12))
        self.btn_encrypt.pack(pady=5)
        
        self.btn_decrypt = tk.Button(root, text="Decrypt Message", command=self.decrypt_message, font=("Arial", 12))
        self.btn_decrypt.pack(pady=5)

        # Selected Image Path
        self.image_path = None

    def select_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("PNG Images", "*.png"), ("JPG Images", "*.jpg"), ("JPEG Images", "*.jpeg")])
        if self.image_path:
            img = Image.open(self.image_path)
            img = img.resize((200, 200))
            img_tk = ImageTk.PhotoImage(img)
            self.image_label.config(image=img_tk)
            self.image_label.image = img_tk  # Prevent garbage collection

    def encrypt_message(self):
        if not self.image_path:
            messagebox.showerror("Error", "No image selected!")
            return

        message = self.message_entry.get().strip()
        if not message or message == "Enter secret message...":
            messagebox.showerror("Error", "Enter a valid secret message!")
            return
        
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Images", "*.png")])
        if not save_path:
            return

        try:
            secret_image = hide(self.image_path, message)
            secret_image.save(save_path)
            messagebox.showinfo("Success", f"Message hidden successfully in {save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {e}")

    def decrypt_message(self):
        if not self.image_path:
            messagebox.showerror("Error", "No image selected!")
            return

        try:
            hidden_message = reveal(self.image_path)
            if hidden_message:
                messagebox.showinfo("Hidden Message", f"Secret Message: {hidden_message}")
            else:
                messagebox.showerror("Error", "No hidden message found!")
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SteganographyApp(root)
    root.mainloop()
