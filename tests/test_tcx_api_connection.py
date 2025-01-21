import pytest
import requests
from unittest.mock import patch, MagicMock, PropertyMock
from threecxapi.tcx_api_connection import TCX_API_Connection, AuthenticationToken
from threecxapi.exceptions import APIAuthenticationError
from threecxapi.components.parameters import QueryParameters
from threecxapi.exceptions import APIAuthenticationError


class TestTCX_API_Connection:

    @pytest.fixture
    def mock_response(self):
        # Mock a basic response object from requests
        response = MagicMock(spec=requests.Response)
        response.status_code = 200
        response.text = '{"key": "value"}'
        return response

    @pytest.fixture
    def api_connection(self, mock_response):
        # Get a TCX_API_Connection object with a mocked _make_request method
        with patch.object(TCX_API_Connection, "_make_request", return_value=MagicMock(spec=requests.Response)):
            api_connection = TCX_API_Connection(server_url="https://example.com")
            yield api_connection

    def test_api_url(self, api_connection):
        assert api_connection.api_url == "https://example.com/xapi/v1"

    def test_token_getter(self, api_connection):
        token = AuthenticationToken(**{
            "token_type": "Bearer",
            "expires_in": 3600,
            "access_token": "access",
            "refresh_token": "refresh"
            })
        api_connection._token = token
        assert api_connection.token == token

    def test_token_setter(self, api_connection):
        token = {"token_type": "Bearer", "expires_in": 3600, "access_token": "access", "refresh_token": "refresh"}
        api_connection.token = token
        assert api_connection._token == AuthenticationToken(**token)

    @patch("threecxapi.tcx_api_connection.requests.Session")
    def test_init(self, mock_requests_session):
        mock_session = MagicMock()
        mock_requests_session.return_value = mock_session

        api_connection = TCX_API_Connection(server_url="https://example.com")

        assert api_connection.server_url == "https://example.com"
        assert api_connection.api_path == "/xapi/v1"
        assert api_connection.session == mock_session
        assert api_connection.token_expiry_time == 0
        assert api_connection._token is None

    def test_get_api_endpoint_url(self, api_connection):
        assert api_connection.get_api_endpoint_url("endpoint") == "https://example.com/xapi/v1/endpoint"

    def test_get_with_params(self, api_connection, mock_response):
        api_connection._make_request.return_value = mock_response
        api_connection = TCX_API_Connection(server_url="https://example.com")
        return_data = {"key": "value"}
        query_params = MagicMock(model_dump=MagicMock(return_value=return_data))  # Mocking the QueryParameters class
        endpoint = "/test-endpoint"

        result = api_connection.get(endpoint, params=query_params)

        api_connection._make_request.assert_called_once_with(
            "get", endpoint, params=return_data
        )
        query_params.model_dump.assert_called_once_with(exclude_none=True, by_alias=True)
        assert result == mock_response

    def test_get_without_params(mself, api_connection, mock_response):
        api_connection._make_request.return_value = mock_response
        api_connection = TCX_API_Connection(server_url="https://example.com")
        endpoint = "/test-endpoint"

        result = api_connection.get(endpoint)

        api_connection._make_request.assert_called_once_with(
            "get", endpoint, params=None
        )
        assert result == mock_response

    def test_post(self, api_connection, mock_response):
        data = {"key": "value"}
        api_connection._make_request.return_value = mock_response

        response = api_connection.post("endpoint", data)

        api_connection._make_request.assert_called_once_with("post", "endpoint", json=data)
        assert response == mock_response

    def test_patch(self, api_connection, mock_response):
        data = {"key": "value"}
        api_connection._make_request.return_value = mock_response

        response = api_connection.patch("endpoint", data)

        api_connection._make_request.assert_called_once_with("patch", "endpoint", json=data)
        assert response == mock_response

    def test_delete(self, api_connection, mock_response):
        data = 1
        api_connection._make_request.return_value = mock_response

        response = api_connection.delete("endpoint", data)

        api_connection._make_request.assert_called_once_with("delete", "endpoint", params=data)
        assert response == mock_response

    @patch('threecxapi.tcx_api_connection.requests.Session')
    def test_authenticate_success(self, mock_session_class):
        # Patch token again in the test to track setter calls
        with patch.object(TCX_API_Connection, 'token', new_callable=PropertyMock) as mock_token:
            token = {"Token": {"token_type": "Bearer", "expires_in": 3600, "access_token": "access", "refresh_token": "refresh"}}
            mock_response = MagicMock()
            mock_response.json.return_value = token
            api_connection = TCX_API_Connection(server_url="https://example.com")
            api_connection.session.post.return_value = mock_response

            # Call the method that sets self.token
            api_connection.authenticate("username", "password")

            # Assert the setter was called with the correct token value
            mock_token.mock_calls
            mock_token.assert_called_with(token["Token"])

    @patch("requests.Session.post")
    def test_authenticate_failure(self, mock_post, api_connection):
        with pytest.raises(APIAuthenticationError) as e:
            mock_response = MagicMock(spec=requests.models.Response)
            mock_response.status_code = 418
            mock_response.raise_for_status.side_effect = requests.HTTPError(response=mock_response)
            api_connection = TCX_API_Connection(server_url="https://example.com")
            api_connection.session.post.return_value = mock_response

            # Call the method that sets self.token
            api_connection.authenticate("username", "password")
        assert e.value.status_code == 418
        assert str(e) == "blah" # Not done yet


    @patch("requests.Session.post")
    def test_refresh_access_token(self, mock_post, api_connection):
        api_connection._token = AuthenticationToken("Bearer", 3600, "access", "refresh")
        mock_response = MagicMock()
        mock_response.json.return_value = {"token_type": "Bearer", "expires_in": 3600, "access_token": "new_access", "refresh_token": "new_refresh"}
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        api_connection._refresh_access_token()

        assert api_connection.token.access_token == "new_access"
        assert api_connection.token.refresh_token == "new_refresh"
