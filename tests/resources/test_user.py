from unittest.mock import MagicMock

import requests
import pytest
from pydantic import ValidationError

from threecxapi.resources.exceptions.users_exceptions import UserCreateError
from threecxapi.resources.users import ListUserParameters, UserProperties
from threecxapi.components.parameters import ListParameters
from threecxapi.resources.users import UsersResource
from threecxapi.tcx_api_connection import ThreeCXApiConnection
from threecxapi.components.schemas.pbx import User
import threecxapi.exceptions as TCX_Exceptions


class TestListUserParameters:

    def test_inherits_from_parameters(self):
        assert issubclass(ListUserParameters, ListParameters)

    def test_valid_empty_parameters(self):
        test_list_user_parameters = ListUserParameters()
        assert isinstance(test_list_user_parameters, ListUserParameters)

    def test_valid_select(self):
        select = list(UserProperties)
        params = ListUserParameters(select=select)
        assert isinstance(params, ListUserParameters)

    def test_invalid_select(self):
        select = list(UserProperties)
        select.append("INVALID_VALUE")
        with pytest.raises(ValidationError):
            ListUserParameters(select=select)

    def test_valid_expand(self):
        expand = "test"
        params = ListUserParameters(expand=expand)
        assert isinstance(params, ListUserParameters)

    def test_invalid_expand(self):
        expand = 3
        with pytest.raises(ValidationError):
            ListUserParameters(expand=expand)

    def test_valid_top(self):
        test_params = ListUserParameters(top=1, skip=1)
        assert test_params.top == 1

    def test_invalid_top(self):
        with pytest.raises(ValidationError):
            test_params = ListUserParameters(top=-1)

        test_params = ListUserParameters(top=1)
        with pytest.raises(ValidationError):
            test_params.top = -1

    def test_valid_skip(self):
        test_params = ListUserParameters(skip=1)
        assert test_params.skip == 1

    def test_invalid_skip(self):
        with pytest.raises(ValidationError):
            test_params = ListUserParameters(skip=-1)

        test_params = ListUserParameters(skip=1)
        with pytest.raises(ValidationError):
            test_params.skip = -1


class TestUsersResource:
    @pytest.fixture
    def mock_tcx_api_connection(self):
        return MagicMock(spec=ThreeCXApiConnection)

    @pytest.fixture
    def mock_list_user_parameters(self):
        return MagicMock(spec=ListUserParameters)

    @pytest.fixture
    def user_resource(self, mock_tcx_api_connection):
        return UsersResource(api=mock_tcx_api_connection)

    @pytest.fixture
    def user(self):
        user = User(
            Id=123,
            FirstName="TestFirstName",
            LastName="TestLastName",
            Number="123"
        )
        yield user

    @pytest.fixture
    def user2(self):
        user = User(
            Id=456,
            FirstName="TestFirstName2",
            LastName="TestLastName2",
            Number="456"
        )
        yield user

    def test_endpoint(self, user_resource):
        assert user_resource.endpoint == "Users"

    def test_create_user_success(self, user_resource):
        user_dict = {
            "Id": 123,
            "FirstName": "TestFirstName",
            "LastName": "TestLastName",
            "Number": "123"
        }
        user_resource.create_user(user_dict)
        user_resource.api.post.assert_called_once_with(user_resource.endpoint, user_dict)

    def test_create_user_failure(self, user_resource, user):  
        mock_response = MagicMock(spec=requests.models.Response)
        mock_response.status_code = 418
        user_resource.api.post.side_effect = requests.HTTPError("An Error Occured", response=mock_response)
        user_dict = user.model_dump()

        with pytest.raises(UserCreateError):
            user_resource.create_user(user_dict)

    def test_list_user_with_single_result(self, mock_list_user_parameters, user_resource, user):
        api_response = {"value": [user.model_dump()]}
        user_resource.api.get.return_value = MagicMock(json=MagicMock(return_value=api_response))
        expected_user = User.model_construct(**user.model_dump())

        users = user_resource.list_user(mock_list_user_parameters)

        assert len(users) == 1
        assert users[0].model_dump() == expected_user.model_dump()
        user_resource.api.get.assert_called_once_with("Users", mock_list_user_parameters)

    def test_list_user_with_multiple_results(self, mock_list_user_parameters, user_resource, user):
        # Mocking the API response
        api_response = {"value": [user.model_dump(), user.model_dump()]}
        user_resource.api.get.return_value = MagicMock(json=MagicMock(return_value=api_response))

        # Calling the method under test
        params = ListUserParameters()
        users = user_resource.list_user(params)

        # Assertions
        assert len(users) == 2
        assert users[1].Id == 2
        assert users[1].FirstName == "TestFirstName2"
        assert users[1].LastName == "TestLastName2"

        # Asserting that the API was called with the correct parameters
        user_resource.api.get.assert_called_once_with("Users", params)

    def test_list_user_failure(self, user_resource):
        # Mocking the API response to simulate an error
        user_resource.api.get.side_effect = requests.HTTPError

        # Calling the method under test
        params = ListUserParameters()
        with pytest.raises(TCX_Exceptions.UserListError):
            users = user_resource.list_user(params)

        # Asserting that the API was called with the correct parameters
        user_resource.api.get.assert_called_once_with("Users", params)

    def test_get_user_success(self, user_resource, user):
        id = 1
        mock_response = MagicMock()
        mock_response.json.return_value = user.model_dump()
        user_resource.api.get.return_value = mock_response

        params = ListUserParameters()
        user = user_resource.get_user(id=id, params=params)

        assert isinstance(user, User)
        assert user.FirstName == "TestFirstName"
        assert user.LastName == "TestLastName"

        user_resource.api.get.assert_called_once_with(
            endpoint=f"Users({id})", params=params
        )

    def test_get_user_failure(self, user_resource):
        id = 1
        user_resource.api.get.side_effect = requests.HTTPError

        params = ListUserParameters()
        with pytest.raises(TCX_Exceptions.UserGetError):
            user = user_resource.get_user(id=id, params=params)

        user_resource.api.get.assert_called_once_with(
            endpoint=f"Users({id})", params=params
        )

    def test_update_user_success(self, user_resource):
        ...

    def test_update_user_failure(self, user_resource):
        ...

    def test_delete_user(self, user_resource):
        ...

    def test_get_hotdesks_by_assigned_user_number(self, user_resource):
        ...
    
    def test_clear_hotdesk_assignment(self, user_resource):
        ...
    
    def test_has_duplicate_email(self, user_resource):
        ...
    
    def test_get_user_id(self, user_resource):
        ...
    
    def test_get_new_user(self):
        ...