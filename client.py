import socket
import json
import sys
import os

HOST = "127.0.0.1"
PORT = 65432

def main():
    filename = input("Enter filename (txt/pdf): ").strip()

    # Local existence check
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    word = input("Enter word or regex pattern: ").strip()
    request = {"filename": filename, "word": word}

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall((json.dumps(request) + "\n").encode("utf-8"))

        response = s.recv(8192).decode("utf-8").strip()
        if not response:
            print("Error: No response from server")
            return

        try:
            response_data = json.loads(response)
        except json.JSONDecodeError:
            print("Error: Invalid JSON response:", response)
            return

        # ✅ Standardized: always check status
        if response_data.get("status") == "error":
            print(f"Error: {response_data.get('message')}")
            return

        if response_data.get("status") == "ok":
            results = response_data["result"]
            pattern = results[0]
            matches = results[1:]

            print(f"\nSearch results for '{pattern}' in {filename}:\n")
            if not matches:
                print("No matches found.")
            else:
                for line_no, line_text in matches:
                    print(f"{line_no}: {line_text}")

if __name__ == "__main__":
    main()
