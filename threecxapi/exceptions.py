import json
from requests import HTTPError
from threecxapi.components.schemas.ODataErrors import ErrorDetails, MainError, ODataError


class APIError(Exception):
    """Base class for API-related errors."""

    def __init__(self, e: HTTPError, message: str = ""):
        super().__init__(message)
        self._http_error = e
        self.message = message
        self.api_error_message = ""
        self._parse_http_error()

    def _parse_http_error(self):
        """Parses the HTTPError and sets the api_error_message."""
        if not hasattr(self._http_error, "response") or not self._http_error.response:
            self.api_error_message = f"HTTP Error: {self._http_error}"
            return

        response_text = self._http_error.response.text or {}
        if response_text:
            try:
                error_response = json.loads(response_text)
                odata_error = ODataError(**error_response)
                self.api_error_message = self._format_main_error(odata_error.error)
            except (json.JSONDecodeError, ValueError) as ex:
                self.api_error_message = f"Failed to parse error response: {ex}"
        else:
            self.api_error_message = f"HTTP Error: {self._http_error.response.reason}"

    def _format_main_error(self, main_error: MainError) -> str:
        """Formats the MainError into a readable string."""
        message = f"{f'[{main_error.code}] ' if main_error.code else ''}{main_error.message or 'Unknown error'}"
        if main_error.details:
            for detail in main_error.details:
                message += "\n" + self._format_error_details(detail)
        return message

    def _format_error_details(self, detail: ErrorDetails) -> str:
        """Formats individual error details into a readable string."""
        return f"[{detail.code}] {detail.message}{f' {detail.target}' if detail.target else ''}"

    def __str__(self) -> str:
        """Returns a string representation of the error."""
        return f"{self.message} {self.api_error_message}"


class APIAuthenticationError(Exception):
    """Exception raised for authentication failures.

    Attributes:
        original_exception (HTTPError): The original HTTPError instance.
        status_code (int): The HTTP response status code.
        error_message (str): The error message from the original exception.
    """
    def __init__(self, original_exception: HTTPError):
        self.original_exception = original_exception

    @property
    def status_code(self):
        try:
            return self.original_exception.response.status_code
        except AttributeError:
            return None

    @property
    def error_message(self):
        return str(self.original_exception)

    def __str__(self):
        return f"Authentication Failure. ({self.status_code}) {self.error_message}"


class APIAuthenticationTokenRefreshError(APIAuthenticationError):
    # def __init__(self, original_exception: HTTPError):
    #     super().__init__(self, original_exception=original_exception)
    def __str__(self):
        return f"Failed to refresh authentication token. ({self.status_code}) {self.error_message}"