```
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒  ▒   ▒▒▒   ▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒   ▒   ▒▒▒▒▒▒   ▒▒▒▒▒   ▒▒▒   
▓  ▓▓   ▓▓     ▓▓▓▓▓   ▓▓   ▓▓▓   ▓▓   ▓▓  ▓▓▓   ▓▓▓▓  ▓   ▓
▓  ▓▓▓   ▓   ▓▓  ▓▓   ▓▓▓▓   ▓▓   ▓▓   ▓         ▓▓▓▓▓  ▓▓▓▓
▓   ▓   ▓▓  ▓▓▓   ▓▓   ▓▓   ▓▓▓   ▓▓   ▓  ▓▓▓▓▓▓▓▓▓▓  ▓▓   ▓
█   ██████  ███   ████   █████    ██   ███     ████   ███   
█   ████████████████████████████████████████████████████████ 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~v1.1-alpha
```

A Python utility for searching phone numbers in international format across the web. Ideal for
compliance checks, data validation, or open-source intelligence.

---

## FEATURES

   **Phone Number Search**  
   Efficiently sanitizes and queries the web for specified phone numbers by generating
   multiple string variants. Generates multiple phone number formats: E.164, international (+), double-zero (00),
   and local formats—with or without spacing/dashes.

   **Error Handling**  
   - If no prefix is provided, an error message will indicate that a prefix is required.
   - If the phone number is invalid, an error message will state that the number is not valid.

---

## INSTALLATION

```bash
pipx install git+https://github.com/forria64/phonex.git#egg=phonex
```

---

## USAGE

Run the tool by providing a phone number with international prefix '+' or '00':

```bash
phonex +491701234567
phonex 00491701234567
```

### Help Option
To display usage information:
```bash
phonex -h
```

