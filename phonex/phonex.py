import sys
import time
import random
import webbrowser
import urllib.parse
import phonenumbers
from phonenumbers import NumberParseException, PhoneNumberFormat

def strip_spaces_and_dashes(number_str: str) -> str:
    """
    Remove all spaces, dashes, and other punctuation from the string,
    but keep plus sign if present.
    """
    return "".join(ch for ch in number_str if ch.isalnum() or ch == '+')

def sanitize_phone_number(raw_input: str) -> str:
    """
    Normalize the phone number by stripping spaces and dashes.
    """
    sanitized_input = strip_spaces_and_dashes(raw_input)
    return normalize_double_zero(sanitized_input)

def normalize_double_zero(number_str: str) -> str:
    """
    Convert phone numbers starting with '00' to start with '+'.
    """
    if number_str.startswith('00'):
        return '+' + number_str[2:]
    return number_str

def is_valid_phone_number(phone_number: str, default_region: str = "US") -> bool:
    try:
        parsed_number = phonenumbers.parse(phone_number, default_region)
        return phonenumbers.is_valid_number(parsed_number)
    except NumberParseException:
        return False

def generate_phone_number_variants(raw_input: str, default_region: str = "US") -> list:
    """
    Generate multiple variants of a phone number for Google Dork search.
    """
    phone_number = sanitize_phone_number(raw_input.strip())

    if not (phone_number.startswith('+') or phone_number.startswith('00')):
        print("Error: Phone number must begin with '+' or '00' to indicate an international prefix.")
        sys.exit(1)

    if not is_valid_phone_number(phone_number):
        print(f"Error: '{phone_number}' is not a valid phone number.")
        sys.exit(1)

    parsed_number = phonenumbers.parse(phone_number, None)
    
    variants = set()
    e164_fmt = phonenumbers.format_number(parsed_number, PhoneNumberFormat.E164)
    variants.add(e164_fmt)

    intl_fmt = phonenumbers.format_number(parsed_number, PhoneNumberFormat.INTERNATIONAL)
    variants.add(intl_fmt)

    nat_fmt = phonenumbers.format_number(parsed_number, PhoneNumberFormat.NATIONAL)
    variants.add(nat_fmt)

    if e164_fmt.startswith('+'):
        double_zero_ns = "00" + e164_fmt[1:]
        variants.add(double_zero_ns)

        double_zero_spaced = "00" + intl_fmt[1:]
        variants.add(double_zero_spaced)

    final_variants = set()
    for var in variants:
        final_variants.add(var)
        final_variants.add(strip_spaces_and_dashes(var))

    return sorted(final_variants)

def open_google_dork_query_in_browser(phone_number: str):
    variants = generate_phone_number_variants(phone_number)

    for variant in variants:
        query = f'+"{variant}"'
        encoded_query = urllib.parse.quote(query)
        google_url = f"https://www.google.com/search?q={encoded_query}"
        print(f"Opening Google search results for: {variant}")  # Ensure this uses the sanitized number
        time.sleep(random.uniform(1, 3))
        webbrowser.open(google_url)


def print_usage():
    print("Usage: phonex <phone_number>")
    print("       phonex -h  (show this help message)")

def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    if sys.argv[1] in ('-h', '--help'):
        print_usage()
        sys.exit(0)

    phone_number = sys.argv[1]
    sanitized_number = sanitize_phone_number(phone_number)
    print(f"Sanitized number (DEBUG): {sanitized_number}")  # Add this
    open_google_dork_query_in_browser(sanitized_number)



if __name__ == "__main__":
    main()

