import phonenumbers
from phonenumbers import carrier, geocoder, timezone

def validate_phone_number(phone_number, region=None):
    """
    Validate a phone number for any country.

    :param phone_number: Phone number in international format or national format with region.
    :param region: Optional country code (e.g., "US" for the United States).
    :return: Dictionary containing validation status, formatted number, location, carrier, and timezone.
    """
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number, region)
        
        # Check if the number is valid
        if not phonenumbers.is_valid_number(parsed_number):
            return {"valid": False, "message": "Invalid phone number"}
        
        # Get phone number details
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        country = geocoder.description_for_number(parsed_number, "en")
        sim_provider = carrier.name_for_number(parsed_number, "en")
        timezones = timezone.time_zones_for_number(parsed_number)

        return {
            "valid": True,
            "formatted_number": formatted_number,
            "country": country,
            "carrier": sim_provider if sim_provider else "Unknown",
            "timezones": timezones
        }
    
    except phonenumbers.NumberParseException:
        return {"valid": False, "message": "Invalid phone number format"}


