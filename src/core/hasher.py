import hashlib
import pathlib

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
    #print(results)
    return results

def hash_directories(directory_path, algorithms=None, recursive=True):
    """
        Calculate hashes for all files in a directory

        Args:
            directory_path (str): path to the direcory
            algorithms (list, optional): list of hash algorithms to use
            recursive (bool, optional): whether to process subdirectories. defaults to True

        Returns:
            dict: Nested dictionary mapping file paths to their hash results
    """
    if algorithms is None: 
        algorithms = ['md5', 'sha1', 'sha256']

    directory_path = pathlib.Path(directory_path)
    results = {}

    # Determine which files to process
    if recursive:
        # Get all files in directory and subdirectories
        files = [f for f in directory_path.glob('**/*') if f.is_file()]
    else:
        # Get only files in the furrent directory
        files = [f for f in directory_path.glob('*') if f.is_file()]

    
    # Calculate hashes for each file
    for file_path in files:
        try:
            # Use relative path as the key
            rel_path = file_path.relative_to(directory_path)
            results[str(rel_path)] = calculate_file_hashes(file_path, algorithms)
          
        except Exception as e:
            results[str(file_path.relative_to(directory_path))] = f"Error: {str(e)}"
    
   #for r in results:
      #  print(r)

    print(results["tips"])
    return results



if __name__ == "__main__":
    #sha256Hash()
   # calculate_file_hashes("/home/lc/Desktop/tips", None)
   hash_directories("/home/lc/Desktop/", None, False)
