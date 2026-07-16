import os
import shutil
import random
import string

# --- THE LAB CONFIGURATION ---
LAB_DIR = "safe_lab_environment"
NODE_COUNT = 3

def setup_safe_sandbox():
    """Creates a completely isolated directory for the visual demonstration."""
    if not os.path.exists(LAB_DIR):
        os.makedirs(LAB_DIR)
        print(f"[+] Initialized isolated simulation sandbox: {LAB_DIR}/")

def generate_dynamic_token():
    """Generates a randomized string representing an encrypted deployment key."""
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(16))

def deploy_nodes():
    """Safely simulates self-replication by duplicating the core module into isolated folders."""
    current_script = __file__
    
    print("\n[!] Triggering automated network expansion...")
    
    for i in range(1, NODE_COUNT + 1):
        node_folder = os.path.join(LAB_DIR, f"node_endpoint_0{i}")
        
        # Create the sub-directories visually on screen
        if not os.path.exists(node_folder):
            os.makedirs(node_folder)
            
        # 1. Safely clone this script into the destination node folder
        destination_script = os.path.join(node_folder, f"engine_0{i}.py")
        shutil.copy2(current_script, destination_script)
        print(f" -> Synchronized Core Engine to: {destination_script}")
        
        # 2. Generate a 'visual infection marker' - a safe metadata token file
        token_file = os.path.join(node_folder, "session_token.dat")
        token_data = generate_dynamic_token()
        with open(token_file, "w") as f:
            f.write(f"CLUSTER_AUTH_SIGNATURE={token_data}\nSTATUS=ACTIVE\n")
        print(f"    ↳ Dropped Deployment Token: {token_data}")

    # 3. Create a central master control log sheet
    log_manifest = os.path.join(LAB_DIR, "master_manifest.txt")
    with open(log_manifest, "w") as f:
        f.write("=== CLUSTER DEPLOYMENT MANIFEST ===\n")
        f.write(f"Status: Total Control Established\nActive Endpoints: {NODE_COUNT}\n")
    print(f"\n[+] Master manifest file generated successfully: {log_manifest}")

if __name__ == "__main__":
    print("=== CENTRAL REPLICATING CONTROLLER INITIALIZED ===")
    
    # 1. Prepare the simulation sandbox
    setup_safe_sandbox()
    
    # 2. Execute the visual duplication routine
    deploy_nodes()
    
    print("\n[=== MISSION METRICS COMPLETED ===]")
