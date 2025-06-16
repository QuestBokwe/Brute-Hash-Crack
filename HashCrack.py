import hashlib
import itertools
import string

def crack_hash(hash_to_crack, algorithm='md5'):
    """Brute force password by trying all combinations of letters and numbers."""
    charset = string.ascii_lowercase + string.digits
    
    for length in range(1, 5): 
        for candidate in itertools.product(charset, repeat=length):
            password = ''.join(candidate)

            if algorithm == 'md5':
                hashed = hashlib.md5(password.encode()).hexdigest()
            elif algorithm == 'sha256':
                hashed = hashlib.sha256(password.encode()).hexdigest()
            else:
                print("Unknown algorithm.")
                return None

            if hashed == hash_to_crack:
                return password
    
    return None

if __name__ == "__main__":
    hash_to_crack = input("Enter hash to crack: ")
    algorithm = input("Enter algorithm (md5 or sha256): ")
    password = crack_hash(hash_to_crack, algorithm)

    if password:
        print(f"[+] Password found: {password}")
    else:
        print("[-] Password not found.")
