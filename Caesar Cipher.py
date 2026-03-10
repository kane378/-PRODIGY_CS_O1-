import string

def transform_text(original_text, key, task='encrypt'):
    alphabet = string.ascii_lowercase
    transformed_message = []
    
    # If decrypting, we just flip the key to move backwards
    if task == 'decrypt':
        key = -key
        
    for character in original_text:
        if character.lower() in alphabet:
            # Find the current position
            current_idx = alphabet.find(character.lower())
            # Calculate new position with wrap-around
            new_idx = (current_idx + key) % 26
            # Get the new letter
            new_char = alphabet[new_idx]
            transformed_message.append(new_char.upper() if character.isupper() else new_char)
        else:
            transformed_message.append(character)
            
    return "".join(transformed_message)

print("--- Simple Text Scrambler ---")
user_input = input("Message: ")
user_key = int(input("Shift Value: "))
user_action = input("Type 'encrypt' or 'decrypt': ").strip().lower()

result = transform_text(user_input, user_key, user_action)
print(f"\nResulting Text: {result}")