import hashlib

def calculate_file_hashes(file_path, algorithms=None):
    
    """ Calculate multiple hash digests for a file

    Args: file_path(str): path to the file
    algorithms (list, optional): list of hash algorithms to use
        Defaults to ['md5', 'sha1', 'sha256']
    """

    if algorithms is None:
        algorithms = ['md5', 'sha1', 'sha256']

    hash_objects = {}
    for algorithm in algorithms:
        if hasattr(hashlib, algorithm):
            hash_objects[algorithm] = getattr(hashlib, algorithm)()
        else: 
            print(f"Warning: Algorithm {algorithm} is not available in hashlib")
        
    # Read file in chunks to handle large files efficiently
    with open(file_path, 'rb') as f:
        chunk = f.read(8192)
        while chunk:
                # update all hash objects with the chunk
                for hash_obj in hash_objects.values():
                    hash_obj.update(chunk)
                chunk = f.read(8192)
    
    results = {algorithm: hash_obj.hexdigest() for algorithm, hash_obj in hash_objects.items()}
    print(results)
    return results


def sha256Hash():
    h = hashlib.new("SHA256")
    message = "Hello world!"
    h.update(message.encode())

    msg_hash = h.hexdigest()
    print(msg_hash)

    h = hashlib.sha256()
    message = "Hello world!"
    h.update(message.encode())

    msg_hash = h.hexdigest()
    print(msg_hash)


if __name__ == "__main__":
    #sha256Hash()
    calculate_file_hashes("/home/lc/Desktop/tips", None)
