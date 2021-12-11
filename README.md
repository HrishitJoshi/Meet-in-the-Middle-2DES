# Meet-in-the-Middle-2DES
Meet in the middle attacks on 2DES encryption

Here we are doing Meet in the middle attack where we have a 2DES encryption scheme with only a 3 byte key to save computer resources as this is only a demonstration.

In the function DDES_encrypt we have hardcoded the 2 keys for 2DES encryption and it takes in the value m which will be the bytearray of the message being encrypted.

We have hardcoded the keys as 200 and 220 for first and second DES implementation respectively.

We convert that into bytes and generate a key by the built in function DesKey and encrypt the message.

We have the message to be m = b"any long message" and m_1= b"abc deffg djcwij"

Then we have the MitM function that takes in 2 pairs plain text and cipher text and returns 0 and prints out the two keys.

First for loop populates the mid array for all the middle values for all the keys. Then we have another loops which tell us when a key is matching the array and return the corresponding key values.
