import hashlib

# This code uses the hashlib module in Python to generate the SHA-512 hash digest of the concatenated data.
# The open function is used to read the contents of the two image files, and the read method is used to read the contents
# of the file into memory as bytes. The contents of the two files are then concatenated using the b''.join method and the
# resulting combined data is passed to the update method of a SHA-512 hash object to generate the hash digest.
# The hexdigest method is then used to get the hexadecimal representation of the hash digest, which is returned from the function.


def generate_sha512_digest(images):
    # Concatenate the contents of the image files
    combined_data = b''.join([open(image, 'rb').read() for image in images])

    # Generate the SHA-512 hash digest of the concatenated data
    sha512 = hashlib.sha512()
    sha512.update(combined_data)
    return sha512.hexdigest()


# Example usage
images = ['image2.png', 'image2.png', 'image3.png']
print("\n\n" + "HASH FUNCTION " + generate_sha512_digest(images) + "\n\n")

