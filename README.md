# 📤 AnonUp by DamClover

A simple Python tool to upload files anonymously to **anonfile.la** easily via CLI.

### 📦 Requirements

- **Python 3.6+**
- **Internet connection**

---

### 🔧 Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/damclover/anonup
cd anonup
```

#### 2. Make it Global (Linux Only)

If you want to use `anonup` anywhere on your system:

```bash
sudo chmod +x install.sh
./install.sh
```

✅ Now you can just type `anonup file.txt` from any terminal!

*(Make sure `/usr/local/bin` is in your PATH, which it usually is by default.)*

---

### 🚀 Usage

```bash
anonup file.txt
```

Using anonymousfiles.org:
```bash
anonup file.txt -s 2
```

Using Tor Proxys (enable on your system first):
```bash
anonup file.txt --tor
anonup file.txt -s 2 --tor
```

or if running manually:

```bash
python3 anonup.py file.txt
```

#### 🔹 Show Help:

```bash
anonup -h
```

It will display all usage options and examples.

---

### 📥 Example Output

```bash
┌──(root㉿Master)-[/usr/local/bin]
└─# anonup file.txt -s 2 --tor

[+] Uploaded in anonymousfiles.org using Tor Proxy
[+] Link: https://anonymousfiles.org/files/D10g0D3VL0u
```

---

## 🧑‍💻 Author

DamClover (damclover@proton.me)  
**For educational and ethical testing purposes only.**
