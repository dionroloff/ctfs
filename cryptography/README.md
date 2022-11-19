# CyberTalents Cryptography CTF Write-ups

The following are write-ups for cryptography-based capture the flag challenges hosted by [CyberTalents](https://cybertalents.com/challenges/cryptography).

For terminal commands I'm using Kali Linux and when needed, Python 3.10.5. Some of these CTFs were overly simple (Google is the best source of cracked hashes), others were more complicated and required researching man pages and python docs.

### Challenges:

- [Hide Data]()
- [Hash3rror]()
- [RSA101]()


## Hide Data
__(Easy, 50 Points)__

>I used to hide my data with a classic cypher, can you get the flag hidden inside? gur synt vf 2w68lsudym Vg vf cerggl rnfl gb frr gur synt ohg pna lbh frr vg v gbbx arneyl 1 zvahgr gb rapbqr guvf jvgu EBG13 tbbq yhpx va fbyivat gung

The hint looks like a rotational cipher; I try ROT13 and get the flag.

```
$ echo 'gur synt vf 2w68lsudym Vg vf cerggl rnfl gb frr gur synt ohg pna lbh frr vg v gbbx arneyl 1 zvahgr gb rapbqr guvf jvgu EBG13 tbbq yhpx va fbyivat gung' | rot13

the flag is 2j68yfhqlz It is pretty easy to see the flag but can you see it i took nearly 1 minute to encode this with ROT13 good luck in solving that
```
`2j68yfhqlz`is indeed the flag.

## Hash3rror

__(Easy, 50 Points)__

>we got this corrupted hash password from a Pcap file with a note (password = sha-1(hash-result)).
>HASH:77be5d24ed2e3e590045e1d6o7e84i50d2799c19f48ede46804a8734e287df120f

I notice that this hash looks like hex encoding, but it has two characters 'i' and 'o' which are not found in hexadecimal (0-9 and A-F only). Removing these two characters from the string, I confirm that this is a 64-character long string, the length of a Sha256 hash:

```
str = "77be5d24ed2e3e590045e1d67e8450d2799c19f48ede46804a8734e287df120f"
print(len(str))
# 64
```

I literally google "77be5d24ed2e3e590045e1d67e8450d2799c19f48ede46804a8734e287df120f" and get the reversed Sha256 hash: `s3cr3tpassword` but sadly this is not the flag.

Re-reading the description I hash the string "s3cr3tpassword"

```
import hashlib
sha1 = hashlib.sha1()
sha1.update("s3cr3tpassword".encode())
print(sha1.hexdigest())
```
The flag is `83874343435092cb681c0d558a84bfeb389c32ed`

## RSA101
__(Basic, 25 Points)__

>we received a message from our agent but we don't know how to use our key to read the message

Opening the challenge there’s a link to a zip download. Unzipping, there are two files: a ciphertext and key.pem (RSA private key). I use openssl to decrypt the ciphertext:

```
$ unzip RSA101.zip 
Archive:  RSA101.zip
 extracting: cipher                  
  inflating: key.pem

$ openssl pkeyutl -decrypt -in cipher -out plain -inkey key.pem

$ cat plain 
flag{RSA_nice_try}
```














