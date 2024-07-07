import binascii
from collections import Counter

# Chaîne hexadécimale encodée du défi
hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

# Fonction pour convertir l'hexadécimal en octets
def hex_to_bytes(hex_str):
    return binascii.unhexlify(hex_str)

# Fonction pour effectuer le XOR avec un byte unique
def single_byte_xor(byte_array, key):
    return bytes([b ^ key for b in byte_array])

# Fonction de notation basée sur la fréquence des lettres anglaises courantes
def score_text(text):
    frequency = Counter(text)
    score = sum(frequency[char] for char in b'ETAOIN SHRDLUetaoin shrdlu')
    return score

# Fonction pour trouver la meilleure clé XOR d'un byte unique
def find_best_xor_key(byte_array):
    best_score = 0
    best_text = ""
    best_key = None
    
    for key in range(256):
        decrypted_text = single_byte_xor(byte_array, key)
        try:
            decrypted_text.decode('ascii')  # Ne considérer que les sorties ASCII valides
        except UnicodeDecodeError:
            continue
        
        current_score = score_text(decrypted_text)
        if current_score > best_score:
            best_score = current_score
            best_text = decrypted_text
            best_key = key
    
    return best_key, best_text

# Convertir l'hexadécimal en octets
byte_array = hex_to_bytes(hex_string)

# Trouver la meilleure clé et le texte en clair correspondant
best_key, best_text = find_best_xor_key(byte_array)

# Afficher les résultats
print(f"Meilleure Clé : {best_key} (caractère : {chr(best_key)})")
print("Message Déchiffré :", best_text.decode('ascii'))
