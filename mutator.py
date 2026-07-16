import os
import random
import string

# --- THE CONFIGURATION ---
SECURE_PAYLOAD = "print('=== SYSTEM OPERATIONAL: ACCESS CONFIRMED ===')"

def generate_random_padding():
    """Generates a random string comment to force the file's hash signature to change completely."""
    length = random.randint(10, 30)
    random_str = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    return f"\n# Signature Padding: {random_str}\n"

def mutate_self():
    file_path = __file__
    
    # 1. Read the current contents of this exact file
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    # 2. Find where the template ends and truncate everything after it
    # We split the string search token so the loop doesn't match itself!
    marker_token = "# --- " + "END OF CORE ENGINE" + " ---"
    
    clean_lines = []
    for line in lines:
        clean_lines.append(line)
        if marker_token in line:
            break
            
    # 3. Generate a brand new, unique padding signature
    new_padding = generate_random_padding()
    
    # 4. Overwrite itself on disk with the new signature
    with open(file_path, 'w') as f:
        f.writelines(clean_lines)
        f.write(new_padding)

if __name__ == "__main__":
    # Execute our operational message
    exec(SECURE_PAYLOAD)
    
    # Trigger the mutation engine
    mutate_self()
    print("[+] Mutation complete. Signature rewritten.")

# --- END OF CORE ENGINE ---

# Signature Padding: hxv4PdksyVp564TVR32x5kCe
