# Basic Secure Login System

A basic secure login and registration system implemented in Python using XOR-based key derivation and SHA hashing for authentication.

## Features

- **User Registration**: Allows new users to register with a username and password.
- **Secure Authentication**: Uses SHA-1 and SHA-256 hashing for secure login verification.
- **XOR Encryption**: Encrypts and decrypts stored user data using an XOR-based method.
- **Data Protection**: User data is stored securely in hashed directories with encrypted content.

## Requirements

- **Python 3.x**
- **OS Module** (built-in)
- **Hashlib Module** (built-in)
- **Time Module** (built-in)

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/Secure-Login-System.git
   cd Secure-Login-System
   ```

2. Run the script:
   ```bash
   python main.py
   ```

## Project Structure

- **`main.py`**: The main script containing the login and registration logic.
- **Login System**: Checks the username and password, decrypts stored data, and verifies access.
- **Registration System**: Hashes and encrypts user credentials before storing them securely.
- **XOR-Based Key Derivation**: Uses XOR operations to generate encryption keys from user credentials.

## Customization

You can modify various parameters in the script:

- **Password and Username Processing** (Handles length adjustments and XOR transformations.)
- **Encryption Mechanism** (Currently uses SHA-1 for user validation and SHA-256 for encryption.)
- **Storage Format** (User data is stored in directories named after hashed credentials.)

## Security Details

- **XOR Encryption**: Each character of the username and password is XOR-ed to generate a unique key.
- **SHA-1 Hashing**: Used to create unique directory names for storing encrypted user data.
- **SHA-256 Key Derivation**: The key derived from XOR operations is hashed with SHA-256 for decryption.
- **Data Verification**: The system ensures integrity by checking stored authentication markers.

## License

This project is licensed under the Mozilla Public License 2.0 (MPL-2.0).

### Additional Note on Commercial Use
**Commercial use of this software or any derived works is prohibited without prior written permission from the original author.** For commercial licensing inquiries, please contact loan.tremoulet.breton@gmail.com.


