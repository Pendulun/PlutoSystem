def validate_non_empty_string(value: str) -> None:
    if not value.strip():
        raise ValueError("String attribute cannot be empty")
