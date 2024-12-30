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
    1) Enforce that 'raw_input' starts with '+' or '00'. Otherwise, reject.
    2) Parse with libphonenumbers:
       - First try no region
       - Then fallback to 'default_region' if invalid
    3) If valid, generate base formats:
       - E.164
       - INTERNATIONAL
       - NATIONAL (local)
       - "00" version from E.164 (no spaces)
       - "00" spaced version from INTERNATIONAL
    4) For each of those base formats, also create a "no-spaces" variant.
    5) Return them all sorted.
    """

    # 1) Reject if number does not start with '+' or '00'
    if not (raw_input.startswith('+') or raw_input.startswith('00')):
        print("Error: Phone number must begin with '+' or '00' to indicate an international prefix.")
        sys.exit(1)

    # Normalize '00' to '+'
    phone_number = normalize_double_zero(raw_input.strip())

    if not is_valid_phone_number(phone_number):
        print(f"Error: '{phone_number}' is not a valid phone number.")
        sys.exit(1)

    parsed_number = phonenumbers.parse(phone_number, None)
    
    # 3) Build base variants
    variants = set()
    e164_fmt = phonenumbers.format_number(parsed_number, PhoneNumberFormat.E164)
    variants.add(e164_fmt)

    intl_fmt = phonenumbers.format_number(parsed_number, PhoneNumberFormat.INTERNATIONAL)
    variants.add(intl_fmt)

    nat_fmt = phonenumbers.format_number(parsed_number, PhoneNumberFormat.NATIONAL)
    variants.add(nat_fmt)

    # 3a) "00" variants:
    if e164_fmt.startswith('+'):
        double_zero_ns = "00" + e164_fmt[1:]
        variants.add(double_zero_ns)

        double_zero_spaced = "00" + intl_fmt[1:]
        variants.add(double_zero_spaced)

    # 4) For each variant, also create a "no-spaces" version
    final_variants = set()
    for var in variants:
        final_variants.add(var)
        final_variants.add(strip_spaces_and_dashes(var))

    return sorted(final_variants)

def open_google_dork_query_in_browser(phone_number: str):
    """
    Generate phone number variants, then for each variant, construct a Google exact-match query
    and open it in the browser (with a slight random delay).
    """
    variants = generate_phone_number_variants(phone_number)

    for variant in variants:
        query = f'+"{variant}"'
        encoded_query = urllib.parse.quote(query)
        google_url = f"https://www.google.com/search?q={encoded_query}"

        time.sleep(random.uniform(1, 3))  # random delay
        print(f"Opening Google search results for: {variant}")
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
    open_google_dork_query_in_browser(phone_number)

if __name__ == "__main__":
    main()

