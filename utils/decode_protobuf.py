import binascii
import json
from google.protobuf.wrappers_pb2 import StringValue


def decode_protobuf_string(item : str) -> str:
    try:
        data = json.loads(item)
        hex_value = data.get("value")
        if not hex_value:
            return None

        decoded_bytes = binascii.unhexlify(hex_value)
        sv = StringValue()
        try:
            sv.ParseFromString(decoded_bytes)
            decoded_value = sv.value.strip()
        except Exception:
            decoded_str = decoded_bytes.decode("utf-8", errors="ignore")
            cleaned = ''.join(ch for ch in decoded_str if ch.isprintable())
            decoded_value = cleaned.strip()
        
        # Remove "data" prefix if present
        # The protobuf message may have a field named "data" that prefixes the JSON
        if decoded_value.startswith("data"):
            # Extract the JSON part after "data" prefix
            json_part = decoded_value[4:]  # Remove "data" (4 characters)
            # Validate it's valid JSON by trying to parse it
            try:
                json.loads(json_part)
                return json_part
            except json.JSONDecodeError:
                # If it's not valid JSON, return as is
                return decoded_value
        
        return decoded_value
    except Exception as e:
        return None
        
