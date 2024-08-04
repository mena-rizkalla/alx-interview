# UTF-8 Validation
his project contains a Python function `validUTF8` that determines if a given dataset represents a valid UTF-8 encoding.

## UTF-8 Encoding

UTF-8 is a variable-width character encoding used for electronic communication. Each character in UTF-8 can be represented by 1 to 4 bytes. The structure of the bytes is as follows:

1. **1-byte character**:
   - Bits: `0xxxxxxx`
2. **2-byte character**:
   - Bits: `110xxxxx 10xxxxxx`
3. **3-byte character**:
   - Bits: `1110xxxx 10xxxxxx 10xxxxxx`
4. **4-byte character**:
   - Bits: `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx`

The first byte in a multi-byte sequence indicates the number of bytes in the character. Each subsequent byte must start with the bits `10`.

### Code

```python
def validUTF8(data) -> bool:
    x = 128
    y = 64
    n = 0

    if len(data) == 1 and (data[0] & x) == 0:
        return True

    if len(data) == 1 and (data[0] & x) != 0:
        return False
    for i in range(len(data)):
        if n == 0:
            if (data[i] & x) == 0:
                continue
            while((data[i] & x) != 0):
                data[i] = data[i] << 1
                n = n + 1
            if n == 1 or n >= 5:
                return False
            n = n-1
        else:
            if((data[i] & x) == 0 or (data[i] & y) != 0):
                return False
            n = n - 1
    return n == 0

### How it works
 Iterates through the input array: Processes each integer as a byte.
 Checks byte type: Determines the number of bytes in the current UTF-8 character based on the leading bits of the byte.
 Validates subsequent bytes: Ensures that the following bytes adhere to the UTF-8 encoding rules for continuation bytes.
 Returns result: Indicates whether the entire input is a valid UTF-8 encoding.



