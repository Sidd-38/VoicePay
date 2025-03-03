from blockchain import bc
from encryption import get_or_create_keys, encrypt_message

def process_transaction(input_text):
    """Parse input, encrypt sender/receiver, and add transaction to blockchain"""
    words = input_text.split()
    sender, amount, receiver = words[0], words[2], words[-1]

    # Generate or get existing keys
    sender_keys = get_or_create_keys(sender)
    receiver_keys = get_or_create_keys(receiver)

    # Encrypt sender and receiver names
    encrypted_sender = encrypt_message(sender, receiver_keys[0])  # Encrypted with receiver's public key
    encrypted_receiver = encrypt_message(receiver, sender_keys[0])  # Encrypted with sender's public key

    # Transaction Data
    transaction_data = {
        "sender": encrypted_sender,
        "receiver": encrypted_receiver,
        "amount": amount
    }

    # Add to Blockchain
    bc.add_block(transaction_data)
    print(f"Transaction added: {transaction_data}")

# Run Example
if __name__ == "__main__":
    user_input = input("Enter transaction (e.g., 'RAM pays 1000 to SHYAM'): ")
    process_transaction(user_input)
