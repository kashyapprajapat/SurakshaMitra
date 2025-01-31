import os

def validate_file_upload(file_path, allowed_extensions=None, max_size_mb=None):
    """
    Validate an uploaded file based on developer-provided file types and size.

    :param file_path: Path to the uploaded file.
    :param allowed_extensions: List of allowed file extensions (e.g., ["pdf", "jpg", "png"]).
    :param max_size_mb: Maximum file size in MB.
    :return: Dictionary with validation result.
    """
    
    if not os.path.exists(file_path):
        return {"valid": False, "message": "File does not exist"}

    # Extract file extension
    file_extension = file_path.split(".")[-1].lower()

    # Validate file type (if provided by the developer)
    if allowed_extensions is not None:
        if file_extension not in allowed_extensions:
            return {"valid": False, "message": f"Invalid file type. Allowed: {', '.join(allowed_extensions)}"}

    # Validate file size (if provided by the developer)
    if max_size_mb is not None:
        file_size = os.path.getsize(file_path) / (1024 * 1024)  # Convert to MB
        if file_size > max_size_mb:
            return {"valid": False, "message": f"File size exceeds {max_size_mb}MB limit"}

    return {"valid": True, "message": "Valid file"}
