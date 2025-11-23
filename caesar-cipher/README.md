# Caesar Cipher

Classic encryption & decryption tool – one of the most famous ciphers in history!
"hello" → shift 5 → "mjqqt"
text### Features
- Encrypts and decrypts messages
- Works with any shift number (1–25)
- Preserves spaces, numbers, and symbols
- Smart shift wrapping (`% 26`)
- Input validation (no crashes!)
- Restart option with clean loop
- Beautiful ASCII logo

### Example
```
Type 'encode' to encrypt, 'decode' to decrypt: encode
Type your message: hello world!
Type the shift number: 5
The encoded text is: mjqqt btwqi!
```
```
How to Run
python main.py
```
```
Files
main.py – core logic
art.py – logo

Pure Python • No dependencies • Clean & commented code
