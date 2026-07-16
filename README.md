# 🐍 Python Mutating Virus Demonstration

**⚠️ EDUCATIONAL PURPOSE ONLY - COMPLETELY SAFE DEMONSTRATION**

[![YouTube](https://img.shields.io/badge/YouTube-Watch%20Video-red)](https://youtu.be/Vm_36JfLl-U)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-blue)](https://discord.gg/rbCmYGg2rd)
[![Twitter](https://img.shields.io/badge/Twitter-Follow-black)](https://x.com/MrHackerCharlie)
[![Website](https://img.shields.io/badge/Website-Visit-green)](https://mrhackercharlie.unaux.com)
[![Python](https://img.shields.io/badge/Python-3.9%2B-yellow)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-red)](LICENSE)

---

## 📌 **WARNING & DISCLAIMER**

> **THIS REPOSITORY IS FOR EDUCATIONAL PURPOSES ONLY**

The code in this repository demonstrates file mutation, steganography, and self-replication techniques used in malware. This is a **SAFE, CONTROLLED DEMONSTRATION** meant to teach cybersecurity concepts.

- ✅ All operations are isolated to the current folder
- ✅ No system files are modified
- ✅ No network activity occurs
- ✅ No malicious intent or functionality

**Using these techniques for illegal purposes is strictly prohibited.**
**Always get proper authorization before testing security concepts.**

---

## 🔥 **VIDEO DEMONSTRATION**

Watch the full demonstration on YouTube:

[![Watch the video](https://img.youtube.com/vi/Vm_36JfLl-U/0.jpg)](https://youtube.com/watch?v=Vm_36JfLl-U)

---

## 📚 **WHAT IS THIS?**

This repository contains **THREE** Python virus demonstrations that show:

1. **SHA-256 Mutation** - File changes its hash every time it runs
2. **Multi-Node Replication** - Virus creates copies and hides in images
3. **Windows Steganography** - Virus hides in images, deletes itself, and recovers

Each demonstration builds on the previous one, showing increasingly sophisticated techniques.

---

## 🧬 **THE THREE VIRUSES**

---

### VIRUS 1: SHA-256 Mutation (Kali Linux)

**File:** `virus_1_sha256_mutation/mutating_hash.py`

**Description:**
The simplest demonstration. A Python script that changes its own SHA-256 hash every time it's executed. This shows how file mutation works at the most basic level.

**Features:**
- Self-modifying code
- SHA-256 hash changes on every run
- Signature evasion demonstration
- Safe and isolated operation

**How It Works:**
1. Script reads itself
2. Adds random data at the end
3. Saves itself with new content
4. SHA-256 hash changes completely
5. Original code still works

**Run:**
```bash
python mutating_hash.py
sha256sum mutating_hash.py  # Check hash change
```

---

### VIRUS 2: Multi-Node Replication (Kali Linux)

**File:** `virus_2_multi_node/multi_node_virus.py`

**Description:**
A more advanced demonstration. The virus creates 3 copies of itself (nodes), each hiding inside images and generating recovery engines. Even if you delete the originals, the images hold the virus.

**Features:**
- Self-replication (3 nodes)
- Image steganography (LSB)
- Recovery engine generation
- Persistence after deletion
- Multi-node redundancy

**How It Works:**
1. Virus creates 3 folders (Node_01, Node_02, Node_03)
2. Copies itself into each folder
3. Creates a recovery engine in each node
4. Images hold hidden virus data
5. Recovery engines extract the virus

**Run:**
```bash
python multi_node_virus.py
python node_01/recovery_engine.py  # Recover from Node 1
```

---

### VIRUS 3: Windows Steganography (Windows 11)

**File:** `virus_3_windows_steganography/mutating_virus.py`

**Description:**
The most advanced demonstration. A Windows-based virus that embeds itself into images, deletes the original, and creates a recovery engine. Each recovery produces a file with a NEW SHA-256 hash.

**Features:**
- LSB steganography (hides in images)
- Self-deletion after embedding
- Recovery engine creation
- SHA-256 hash mutation on recovery
- Works with or without existing images
- Notepad demonstration

**How It Works:**
1. Virus finds or creates an image
2. Embeds itself using LSB steganography
3. Creates a recovery engine (different file)
4. Asks for confirmation
5. Deletes itself
6. Recovery engine extracts the virus
7. New file has DIFFERENT SHA-256 hash

**Run:**
```bash
# Install dependencies
pip install -r requirements.txt

# Run the virus
python mutating_virus.py

# After self-deletion, run recovery
python recovery_engine.py
```

---

## 🛠️ **TECHNICAL OVERVIEW**

### Steganography Engine (LSB)

The LSB (Least Significant Bit) steganography technique hides data in the lowest bits of image pixels:

```python
# Hide data in image
binary_data = encode_to_binary(data)
for i, bit in enumerate(binary_data):
    pixels[i] = (pixels[i] & 0xFE) | int(bit)

# Extract data from image
binary_data = ''.join(str(pixel & 1) for pixel in pixels)
data = decode_from_binary(binary_data)
```

### SHA-256 Mutation

The virus modifies itself to change its hash:

```python
# Read current script
with open(__file__, 'rb') as f:
    content = f.read()

# Add random data
random_data = os.urandom(16)
new_content = content + random_data

# Save (hash changes!)
with open(__file__, 'wb') as f:
    f.write(new_content)
```

### Self-Replication & Recovery

The virus creates copies and recovery mechanisms:

```python
# Create nodes
for i in range(3):
    create_node(i)
    copy_virus_to_node(i)
    create_recovery_engine(i)
    embed_in_image(i)

# Self-destruct
delete_original()
```

---

## 📦 **INSTALLATION**

### Prerequisites

```bash
# Python 3.9+ required
python --version

# Install dependencies
pip install -r requirements.txt
```

### Clone Repository

```bash
git clone [https://github.com/YOUR_USERNAME/Python-Mutating-Virus-Demo.git](https://github.com/YOUR_USERNAME/Python-Mutating-Virus-Demo.git)
cd Python-Mutating-Virus-Demo
```

### Dependencies

**requirements.txt:**
```
pillow==10.1.0
numpy==1.24.3
```

---

## 🚀 **USAGE GUIDE**

### Virus 1: SHA-256 Mutation

```bash
cd virus_1_sha256_mutation
python mutating_hash.py
```

### Virus 2: Multi-Node Replication

```bash
cd virus_2_multi_node
python multi_node_virus.py
```

### Virus 3: Windows Steganography

```bash
cd virus_3_windows_steganography
python mutating_virus.py
```

---

## 📊 **COMPARISON TABLE**

| Feature | Virus 1 | Virus 2 | Virus 3 |
|---------|---------|---------|---------|
| SHA-256 Mutation | ✅ | ✅ | ✅ |
| Self-Replication | ❌ | ✅ | ✅ |
| Image Steganography | ❌ | ✅ | ✅ |
| Self-Deletion | ❌ | ✅ | ✅ |
| Recovery Engine | ❌ | ✅ | ✅ |
| Multi-Node | ❌ | ✅ | ❌ |
| Windows Support | ❌ | ❌ | ✅ |
| No-Image Support | ❌ | ❌ | ✅ |

---

## 🔒 **SAFETY FEATURES**

All viruses include built-in safety measures:

- ✅ Isolated to current directory
- ✅ No system file modification
- ✅ No registry changes
- ✅ No network activity
- ✅ No data exfiltration
- ✅ User confirmation required
- ✅ Educational warnings displayed
- ✅ Cleanup possible by deleting folder

---

## 📖 **LEARNING RESOURCES**

### Understanding the Concepts

- [LSB Steganography](https://en.wikipedia.org/wiki/Steganography)
- [SHA-256 Hash Function](https://en.wikipedia.org/wiki/SHA-256)
- [File Mutation Techniques](https://en.wikipedia.org/wiki/Polymorphic_code)
- [Python PIL Documentation](https://pillow.readthedocs.io/)

### Cybersecurity Education

- [OWASP Security Guidelines](https://owasp.org/)
- [Ethical Hacking Certification](https://www.eccouncil.org/ethical-hacking/)
- [Kali Linux Documentation](https://www.kali.org/docs/)

---

## 🤝 **CONTRIBUTING**

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

**Guidelines:**
- Keep educational focus
- Maintain safety features
- Add clear documentation
- Test all code before submitting

---

## 📜 **LICENSE**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 💬 **COMMUNITY & SUPPORT**

Join our community to discuss this project and cybersecurity topics:

🐍 **Discord Server:** [https://discord.gg/rbCmYGg2rd](https://discord.gg/rbCmYGg2rd)

🐍 **Follow on X (Twitter):** [https://x.com/MrHackerCharlie](https://x.com/MrHackerCharlie)

🐍 **Visit Website:** [https://mrhackercharlie.unaux.com](https://mrhackercharlie.unaux.com)

---

## 📺 **WATCH THE VIDEO**

[![Watch the video](https://img.youtube.com/vi/YOUR_VIDEO_ID/0.jpg)](https://youtube.com/watch?v=YOUR_VIDEO_ID)

---

## ⭐ **STAR THIS REPO**

If you found this educational or interesting, please **star** the repository!

[![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/Python-Mutating-Virus-Demo)](https://github.com/YOUR_USERNAME/Python-Mutating-Virus-Demo/stargazers)

---

## ⚠️ **FINAL WARNING**

> **THIS REPOSITORY IS FOR EDUCATIONAL PURPOSES ONLY**

- ✅ Use this to learn about cybersecurity
- ✅ Use this to understand how malware works
- ✅ Use this to protect against attacks
- ❌ DO NOT use for illegal activities
- ❌ DO NOT use on systems without authorization
- ❌ DO NOT distribute as actual malware

**Remember: With great power comes great responsibility.**

---

## 📧 **CONTACT**

For business inquiries, collaborations, or questions:

- Discord: [https://discord.gg/rbCmYGg2rd](https://discord.gg/rbCmYGg2rd)
- Twitter: [@MrHackerCharlie](https://x.com/MrHackerCharlie)
- Website: [mrhackercharlie.unaux.com](https://mrhackercharlie.unaux.com)

---

**Made with ❤️ for the cybersecurity community**

**#Python #Virus #Cybersecurity #EthicalHacking #KaliLinux #Windows #Steganography**
