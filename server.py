import socket
import threading
import json
from search import Search

HOST = "0.0.0.0"
PORT = 65432

def handle_client(conn, addr):
    print(f"[+] Connected by {addr}")
    try:
        with conn:
            fileobj = conn.makefile("r")
            req_line = fileobj.readline()
            if not req_line:
                return

            try:
                req = json.loads(req_line)
            except json.JSONDecodeError:
                conn.sendall((json.dumps({"status": "error", "message": "Invalid JSON request"}) + "\n").encode())
                return

            filename = req.get("filename")
            word = req.get("word")
            if not filename or not word:
                conn.sendall((json.dumps({"status": "error", "message": "Missing filename or word"}) + "\n").encode())
                return

            try:
                search_obj = Search(filename)
                result = search_obj.getLines(word)
                # convert tuples to lists for JSON
                result_json = [result[0]] + [list(item) for item in result[1:]]
                conn.sendall((json.dumps({"status": "ok", "result": result_json}) + "\n").encode("utf-8"))
            except Exception as e:
                conn.sendall((json.dumps({"status": "error", "message": str(e)}) + "\n").encode("utf-8"))

    except Exception as e:
        print(f"[!] Error handling {addr}: {e}")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    main()
