# CTF Description:
# "we got this corrupted hash password from a Pcap file with a note (password = sha-1(hash-result)).
# HASH:77be5d24ed2e3e590045e1d6o7e84i50d2799c19f48ede46804a8734e287df120f"

# I observe that this hash looks like hex format, but it has two characters 'i' and 'o' which are not found in hexadecimal.
# Removing these two characters from the string, I confirm that this is a 64-character long string, the length of a Sha256 hash.

str = "77be5d24ed2e3e590045e1d67e8450d2799c19f48ede46804a8734e287df120f"
print(len(str)) #64

# I google "77be5d24ed2e3e590045e1d67e8450d2799c19f48ede46804a8734e287df120f" and get the Sha256 digest unhashed: "s3cr3tpassword" but sadly this is not the flag.
# https://md5hashing.net/hash/sha256/77be5d24ed2e3e590045e1d67e8450d2799c19f48ede46804a8734e287df120f

# Per the description I hash the string "s3cr3tpassword"

# Sha1 encoding
import hashlib
new_sha1 = hashlib.sha1()
new_sha1.update("s3cr3tpassword".encode())
print(new_sha1.hexdigest())

# Our flag is 83874343435092cb681c0d558a84bfeb389c32ed
