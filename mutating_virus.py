"""
MUTATING VIRUS DEMO - Educational Purpose Only
A safe demonstration of file mutation, steganography, and self-replication
"""

import os
import sys
import base64
import hashlib
import subprocess
import ctypes
import time
from PIL import Image
import numpy as np

# ==============================
# STEGANOGRAPHY ENGINE
# ==============================

def hide_data_in_image(image_path, data, output_path=None):
    """Embed data into image using LSB steganography"""
    try:
        if os.path.exists(image_path):
            img = Image.open(image_path)
        else:
            # Create a dummy image if none exists
            arr = np.random.randint(0, 256, (300, 300, 3), dtype=np.uint8)
            img = Image.fromarray(arr)
        
        # Encode data to binary with markers
        b64_data = base64.b64encode(data).decode('utf-8')
        binary = ''.join(format(ord(c), '08b') for c in b64_data)
        binary = '01011001' + binary + '1111111111111110'  # start + end markers
        
        # Flatten pixels
        pixels = np.array(img).flatten()
        if len(binary) > len(pixels):
            raise ValueError("Data too large for this image")
        
        # Embed bits
        for i, bit in enumerate(binary):
            pixels[i] = (pixels[i] & 0xFE) | int(bit)
        
        # Save image
        out_path = output_path if output_path else image_path
        new_img = Image.fromarray(pixels.reshape(np.array(img).shape).astype('uint8'))
        new_img.save(out_path)
        return out_path
    except Exception as e:
        print(f"[ERROR] hide_data_in_image: {e}")
        return None

def extract_data_from_image(image_path):
    """Extract hidden data from image"""
    try:
        img = Image.open(image_path)
        pixels = np.array(img).flatten()
        
        # Extract LSBs
        binary = ''.join(str(p & 1) for p in pixels)
        
        # Find markers
        start = '01011001'
        start_pos = binary.find(start)
        if start_pos == -1:
            return None
        
        end = '1111111111111110'
        end_pos = binary.find(end, start_pos + len(start))
        if end_pos == -1:
            return None
        
        # Get data bits
        data_bits = binary[start_pos + len(start):end_pos]
        byte_data = bytes(int(data_bits[i:i+8], 2) 
                          for i in range(0, len(data_bits), 8))
        
        return base64.b64decode(byte_data)
    except Exception as e:
        print(f"[ERROR] extract_data_from_image: {e}")
        return None

# ==============================
# MAIN VIRUS LOGIC
# ==============================

class MutatingVirus:
    def __init__(self):
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.script_path = os.path.abspath(__file__)
        self.script_name = os.path.basename(self.script_path)
        self.recovery_name = "recovery.py"
        
        # Find an image in the folder
        self.image_path = None
        for f in os.listdir(self.current_dir):
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                self.image_path = os.path.join(self.current_dir, f)
                break
        
        # If no image, create one
        if not self.image_path:
            self.image_path = os.path.join(self.current_dir, "carrier.png")
            arr = np.random.randint(0, 256, (300, 300, 3), dtype=np.uint8)
            Image.fromarray(arr).save(self.image_path)
            print(f"[INFO] Created carrier image: carrier.png")
        
        # Calculate current hash
        self.current_hash = self.get_file_hash(self.script_path)
    
    def get_file_hash(self, filepath):
        if not os.path.exists(filepath):
            return "N/A"
        with open(filepath, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()
    
    def embed_script_in_image(self):
        """Embed this script into the found/created image"""
        print(f"[*] Embedding into: {os.path.basename(self.image_path)}")
        with open(self.script_path, 'rb') as f:
            data = f.read()
        result = hide_data_in_image(self.image_path, data)
        if result:
            print(f"[+] Embedding successful! ({len(data)} bytes hidden)")
            return True
        return False
    
    def show_notepad_message(self):
        """Open Notepad with a demonstration message"""
        message = """MUTATING VIRUS DEMONSTRATION

This is a SAFE, EDUCATIONAL demonstration.

The virus has been embedded into the image file:
    {0}

Original file hash (SHA-256):
    {1}

The original file will now delete itself.
You can recover it using the recovery engine.

This demonstrates:
- File mutation through steganography
- Self-replication and recovery
- Persistence even after deletion

- Safe Automation Sandbox -
""".format(os.path.basename(self.image_path), self.current_hash[:32])
        
        txt_path = os.path.join(self.current_dir, "virus_demo_message.txt")
        with open(txt_path, 'w') as f:
            f.write(message)
        subprocess.run(["notepad", txt_path], shell=True)
        os.remove(txt_path)  # cleanup after notepad opens
    
    def create_recovery_script(self):
        """Generate the recovery script (different from original)"""
        recovery_content = '''"""
RECOVERY ENGINE - Extracts hidden virus from image
"""

import os
import sys
import base64
import hashlib
import subprocess
import ctypes
from PIL import Image
import numpy as np

def extract_from_image(image_path):
    try:
        img = Image.open(image_path)
        pixels = np.array(img).flatten()
        binary = ''.join(str(p & 1) for p in pixels)
        start = '01011001'
        start_pos = binary.find(start)
        if start_pos == -1:
            return None
        end = '1111111111111110'
        end_pos = binary.find(end, start_pos + len(start))
        if end_pos == -1:
            return None
        data_bits = binary[start_pos + len(start):end_pos]
        byte_data = bytes(int(data_bits[i:i+8], 2) 
                          for i in range(0, len(data_bits), 8))
        return base64.b64decode(byte_data)
    except:
        return None

def recover():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Find the image that contains the virus (the one we embedded into)
    # We'll look for the first PNG/JPG that has hidden data
    image_files = [f for f in os.listdir(current_dir) 
                   if f.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
    
    if not image_files:
        print("No images found!")
        return False
    
    print("Scanning for hidden virus...")
    for img_file in image_files:
        img_path = os.path.join(current_dir, img_file)
        print(f"Checking: {img_file}")
        data = extract_from_image(img_path)
        if data:
            # Recover the original virus
            out_file = os.path.join(current_dir, "mutating_virus.py")
            with open(out_file, 'wb') as f:
                f.write(data)
            
            new_hash = hashlib.sha256(data).hexdigest()
            
            print(f"""
=========================================
VIRUS RECOVERED SUCCESSFULLY!
=========================================
Source Image: {img_file}
File Size: {len(data)} bytes
New SHA-256: {new_hash[:32]}...
Status: MUTATION SUCCESSFUL
=========================================
""")
            
            # Show popup
            try:
                ctypes.windll.user32.MessageBoxW(
                    0,
                    f"Virus recovered from {img_file}\\nNew hash: {new_hash[:32]}...",
                    "Recovery Complete",
                    0x40
                )
            except:
                pass
            
            # Optionally open the recovered file in Notepad (just to show)
            try:
                with open(os.path.join(current_dir, "recovery_log.txt"), "w") as f:
                    f.write(f"Recovered virus hash: {new_hash}")
                subprocess.run(["notepad", "recovery_log.txt"], shell=True)
            except:
                pass
            
            return True
    
    print("No hidden data found in any image.")
    return False

if __name__ == "__main__":
    print("RECOVERY ENGINE v2.0")
    print("=" * 50)
    recover()
'''
        rec_path = os.path.join(self.current_dir, self.recovery_name)
        with open(rec_path, 'w') as f:
            f.write(recovery_content)
        print(f"[+] Recovery engine created: {self.recovery_name}")
        return rec_path
    
    def ask_confirmation_and_delete(self):
        """Show message box, if OK then delete self"""
        # Show confirmation dialog
        result = ctypes.windll.user32.MessageBoxW(
            0,
            "The virus has been embedded into the image.\n\nThe original file will now DELETE ITSELF.\n\nDo you want to proceed?",
            "Confirmation",
            0x24  # Yes/No with question mark icon
        )
        
        if result == 6:  # IDYES = 6
            print("[*] Self-destruct confirmed.")
            self.delete_original()
        else:
            print("[*] Self-destruct cancelled. Script will exit normally.")
    
    def delete_original(self):
        """Delete the original script using a batch file"""
        # Write a batch file that deletes this script and itself
        batch_content = f'''@echo off
timeout /t 1 /nobreak >nul
del "{self.script_path}"
del "%~f0"
'''
        batch_path = os.path.join(self.current_dir, "_delete_self.bat")
        with open(batch_path, 'w') as f:
            f.write(batch_content)
        subprocess.Popen(batch_path, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
        print("[+] Original file will be deleted shortly.")
        print("[+] You can now run recovery.py to get it back.")
        # Exit immediately so the batch can delete
        sys.exit(0)
    
    def run(self):
        """Main execution flow"""
        print("""
=========================================
MUTATING VIRUS DEMO v3.0
EDUCATIONAL PURPOSE ONLY
COMPLETELY SAFE - NO HARM
=========================================
""")
        
        # Step 1: Show Notepad message
        print("[*] Opening demonstration message...")
        self.show_notepad_message()
        
        # Step 2: Embed self into image
        print("[*] Embedding virus into image...")
        if not self.embed_script_in_image():
            print("[ERROR] Embedding failed. Exiting.")
            return
        
        # Step 3: Create recovery engine
        print("[*] Creating recovery engine...")
        self.create_recovery_script()
        
        # Step 4: Ask confirmation to delete
        print("[*] Asking for confirmation...")
        self.ask_confirmation_and_delete()

# ==============================
# ENTRY POINT
# ==============================

if __name__ == "__main__":
    virus = MutatingVirus()
    virus.run()
"""
MUTATING VIRUS DEMO - Educational Purpose Only
A safe demonstration of file mutation, steganography, and self-replication
"""

import os
import sys
import base64
import hashlib
import subprocess
import ctypes
from PIL import Image
import numpy as np

# ==============================
# STEGANOGRAPHY ENGINE
# ==============================

def hide_data_in_image(image_path, data, output_path=None):
    """Embed data into image using LSB steganography"""
    try:
        if os.path.exists(image_path):
            img = Image.open(image_path)
        else:
            # Create a dummy image if none exists
            arr = np.random.randint(0, 256, (300, 300, 3), dtype=np.uint8)
            img = Image.fromarray(arr)
        
        # Encode data to binary with markers
        b64_data = base64.b64encode(data).decode('utf-8')
        binary = ''.join(format(ord(c), '08b') for c in b64_data)
        binary = '01011001' + binary + '1111111111111110'  # start + end markers
        
        # Flatten pixels
        pixels = np.array(img).flatten()
        if len(binary) > len(pixels):
            raise ValueError("Data too large for this image")
        
        # Embed bits
        for i, bit in enumerate(binary):
            pixels[i] = (pixels[i] & 0xFE) | int(bit)
        
        # Save image
        out_path = output_path if output_path else image_path
        new_img = Image.fromarray(pixels.reshape(np.array(img).shape).astype('uint8'))
        new_img.save(out_path)
        return out_path
    except Exception as e:
        print(f"[ERROR] hide_data_in_image: {e}")
        return None

def extract_data_from_image(image_path):
    """Extract hidden data from image"""
    try:
        img = Image.open(image_path)
        pixels = np.array(img).flatten()
        
        # Extract LSBs
        binary = ''.join(str(p & 1) for p in pixels)
        
        # Find markers
        start = '01011001'
        start_pos = binary.find(start)
        if start_pos == -1:
            return None
        
        end = '1111111111111110'
        end_pos = binary.find(end, start_pos + len(start))
        if end_pos == -1:
            return None
        
        # Get data bits
        data_bits = binary[start_pos + len(start):end_pos]
        byte_data = bytes(int(data_bits[i:i+8], 2) 
                          for i in range(0, len(data_bits), 8))
        
        return base64.b64decode(byte_data)
    except Exception as e:
        print(f"[ERROR] extract_data_from_image: {e}")
        return None

# ==============================
# MAIN VIRUS LOGIC
# ==============================

class MutatingVirus:
    def __init__(self):
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.script_path = os.path.abspath(__file__)
        self.script_name = os.path.basename(self.script_path)
        self.recovery_name = "recovery.py"
        
        # Find an image in the folder
        self.image_path = None
        for f in os.listdir(self.current_dir):
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                self.image_path = os.path.join(self.current_dir, f)
                break
        
        # If no image, create one
        if not self.image_path:
            self.image_path = os.path.join(self.current_dir, "carrier.png")
            arr = np.random.randint(0, 256, (300, 300, 3), dtype=np.uint8)
            Image.fromarray(arr).save(self.image_path)
            print(f"[INFO] Created carrier image: carrier.png")
        
        # Calculate current hash
        self.current_hash = self.get_file_hash(self.script_path)
    
    def get_file_hash(self, filepath):
        if not os.path.exists(filepath):
            return "N/A"
        with open(filepath, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()
    
    def embed_script_in_image(self):
        """Embed this script into the found/created image"""
        print(f"[*] Embedding into: {os.path.basename(self.image_path)}")
        with open(self.script_path, 'rb') as f:
            data = f.read()
        result = hide_data_in_image(self.image_path, data)
        if result:
            print(f"[+] Embedding successful! ({len(data)} bytes hidden)")
            return True
        return False
    
    def show_notepad_message(self):
        """Open Notepad with a demonstration message"""
        message = """MUTATING VIRUS DEMONSTRATION

This is a SAFE, EDUCATIONAL demonstration.

The virus has been embedded into the image file:
    {0}

Original file hash (SHA-256):
    {1}

The original file will now delete itself.
You can recover it using the recovery engine.

- Safe Automation Sandbox -
""".format(os.path.basename(self.image_path), self.current_hash[:32])
        
        txt_path = os.path.join(self.current_dir, "virus_demo_message.txt")
        with open(txt_path, 'w') as f:
            f.write(message)
        subprocess.run(["notepad", txt_path], shell=True)
        os.remove(txt_path)  # cleanup after notepad opens
    
    def create_recovery_script(self):
        """Generate the recovery script (different from original)"""
        recovery_content = '''"""
RECOVERY ENGINE - Extracts hidden virus from image
"""

import os
import sys
import base64
import hashlib
import subprocess
import ctypes
import time
from PIL import Image
import numpy as np

def extract_from_image(image_path):
    try:
        img = Image.open(image_path)
        pixels = np.array(img).flatten()
        binary = ''.join(str(p & 1) for p in pixels)
        start = '01011001'
        start_pos = binary.find(start)
        if start_pos == -1:
            return None
        end = '1111111111111110'
        end_pos = binary.find(end, start_pos + len(start))
        if end_pos == -1:
            return None
        data_bits = binary[start_pos + len(start):end_pos]
        byte_data = bytes(int(data_bits[i:i+8], 2) 
                          for i in range(0, len(data_bits), 8))
        return base64.b64decode(byte_data)
    except:
        return None

def recover():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Find the image that contains the virus (the one we embedded into)
    # We'll look for the first PNG/JPG that has hidden data
    image_files = [f for f in os.listdir(current_dir) 
                   if f.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
    
    if not image_files:
        print("No images found!")
        return False
    
    print("Scanning for hidden virus...")
    for img_file in image_files:
        img_path = os.path.join(current_dir, img_file)
        print(f"Checking: {img_file}")
        data = extract_from_image(img_path)
        if data:
            # Recover the original virus
            out_file = os.path.join(current_dir, "mutating_virus.py")
            with open(out_file, 'wb') as f:
                f.write(data)
            
            new_hash = hashlib.sha256(data).hexdigest()
            
            print(f"""
=========================================
VIRUS RECOVERED SUCCESSFULLY!
=========================================
Source Image: {img_file}
File Size: {len(data)} bytes
New SHA-256: {new_hash[:32]}...
Status: MUTATION SUCCESSFUL
=========================================
""")
            
            # Show popup
            try:
                ctypes.windll.user32.MessageBoxW(
                    0,
                    f"Virus recovered from {img_file}\\nNew hash: {new_hash[:32]}...",
                    "Recovery Complete",
                    0x40
                )
            except:
                pass
            
            # Optionally open the recovered file in Notepad (just to show)
            try:
                with open(os.path.join(current_dir, "recovery_log.txt"), "w") as f:
                    f.write(f"Recovered virus hash: {new_hash}")
                subprocess.run(["notepad", "recovery_log.txt"], shell=True)
            except:
                pass
            
            return True
    
    print("No hidden data found in any image.")
    return False

if __name__ == "__main__":
    print("RECOVERY ENGINE")
    print("=" * 50)
    recover()
'''
        rec_path = os.path.join(self.current_dir, self.recovery_name)
        with open(rec_path, 'w') as f:
            f.write(recovery_content)
        print(f"[+] Recovery engine created: {self.recovery_name}")
        return rec_path
    
    def ask_confirmation_and_delete(self):
        """Show message box, if OK then delete self"""
        # Show confirmation dialog
        result = ctypes.windll.user32.MessageBoxW(
            0,
            "The virus has been embedded into the image.\n\nThe original file will now DELETE ITSELF.\n\nDo you want to proceed?",
            "Confirmation",
            0x24  # Yes/No with question mark icon
        )
        
        if result == 6:  # IDYES = 6
            print("[*] Self-destruct confirmed.")
            self.delete_original()
        else:
            print("[*] Self-destruct cancelled. Script will exit normally.")
    
    def delete_original(self):
        """Delete the original script using a batch file"""
        # Write a batch file that deletes this script and itself
        batch_content = f'''@echo off
timeout /t 1 /nobreak >nul
del "{self.script_path}"
del "%~f0"
'''
        batch_path = os.path.join(self.current_dir, "_delete_self.bat")
        with open(batch_path, 'w') as f:
            f.write(batch_content)
        subprocess.Popen(batch_path, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
        print("[+] Original file will be deleted shortly.")
        print("[+] You can now run recovery.py to get it back.")
        # Exit immediately so the batch can delete
        sys.exit(0)
    
    def run(self):
        """Main execution flow"""
        print("""
=========================================
MUTATING VIRUS(safe) v3.0
=========================================
""")
        time.sleep(3)        

        # Step 1: Show Notepad message
        print("[*] Opening demonstration message...")
        self.show_notepad_message()
        
        # Step 2: Embed self into image
        time.sleep(3)
        print("[*] Embedding virus into image...")
        if not self.embed_script_in_image():
            print("[ERROR] Embedding failed. Exiting.")
            return
        
        # Step 3: Create recovery engine
        time.sleep(3)
        print("[*] Creating recovery engine...")
        self.create_recovery_script()
        
        # Step 4: Ask confirmation to delete
        time.sleep(3)
        print("[*] Asking for confirmation...")
        self.ask_confirmation_and_delete()

# ==============================
# ENTRY POINT
# ==============================

if __name__ == "__main__":
    virus = MutatingVirus()
    virus.run()