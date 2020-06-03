import json
import threading

global_lock = threading.Lock()

class data_handler():
    @staticmethod
    def load(file):
        try:
            with open(f"data/{file}.json", 'r') as f:
                return json.load(f)
        except:
            return None

    @staticmethod
    def dump(data, file):
        try:
            while global_lock.locked():
                continue

            global_lock.acquire()
            with open(f"data/{file}.json", 'w') as f:
                json.dump(data, f, indent = 4)
        except:
            raise
        finally:
            global_lock.release()
