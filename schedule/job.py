import json
import psutil
import socket
from datetime import datetime
from cellxgene_gateway.backend_cache import BackendCache
from gateway import MQTT_CLIENT, MQTT_TOPIC


class Cache:
    cache = BackendCache()


def publish_machine_status(cache):
    # print('job_start')
    ip = get_ip()
    available_memory = get_available_memory()
    cache_list = [
                {
                    "dataset": entry.key.file_path,
                    "annotation_file": entry.key.annotation_file_path,
                    "source_name": entry.source_name,
                    "launchtime": entry.launchtime,
                    "last_access": entry.timestamp,
                    "status": entry.status.value,
                }
                for entry in cache.entry_list
            ]
    # print(type(ip), ip, type(available_memory), available_memory)
    send_message = {
        "ip": ip,
        "available_memory": available_memory,
        "entry_list": cache_list,
        "server_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    print('send-message:', send_message)
    MQTT_CLIENT.publish(MQTT_TOPIC, json.dumps(send_message).encode('utf-8'))


def get_available_memory():
    total_memory = psutil.virtual_memory()
    available_memory = total_memory.available / (1024 * 1024 * 1024)
    return round(available_memory, 2)


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


if __name__ == "__main__":
    # get_ip()
    # get_available_memory()
    publish_machine_status()
