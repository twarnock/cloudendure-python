# coding: utf-8

"""
    CloudEndure API documentation

    © 2017 CloudEndure All rights reserved  # General Request authentication in CloudEndure's API is done using session cookies. A session cookie is returned upon successful execution of the \"login\" method. This value must then be provided within the request headers of all subsequent API requests.  ## Errors Some errors are not specifically written in every method since they may always return. Those are: 1) 401 (Unauthorized) - for unauthenticated requests. 2) 405 (Method Not Allowed) - for using a method that is not supported (POST instead of GET). 3) 403 (Forbidden) - request is authenticated, but the user is not allowed to access. 4) 422 (Unprocessable Entity) - for invalid input.  ## Formats All strings with date-time format are according to RFC3339.  All strings with \"duration\" format are according to ISO8601. For example, a full day duration can be specified with \"PNNNND\".   # noqa: E501

    OpenAPI spec version: 5
    Contact: https://bit.ly/2T54hSc
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

from cloudendure.cloudendure_api.models.cloud_endure_saml_settings import (
    CloudEndureSamlSettings,
)  # noqa: F401,E501


class CloudEndureAccount:
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        "invite_token_expiry_minutes": "int",
        "allow_archiving_default_value": "bool",
        "per_account_user_pool": "bool",
        "is_gcp_self_service": "bool",
        "is_dr_trial": "bool",
        "is_arm_self_service": "bool",
        "is_aws_self_service": "bool",
        "saml_settings": "CloudEndureSamlSettings",
        "is_right_sizing_enabled": "bool",
        "default_license_type": "str",
        "max_projects_allowed": "int",
        "ce_admin_properties": "object",
        "owner_id": "str",
        "is_med_one": "bool",
        "id": "str",
    }

    attribute_map = {
        "invite_token_expiry_minutes": "inviteTokenExpiryMinutes",
        "allow_archiving_default_value": "allowArchivingDefaultValue",
        "per_account_user_pool": "perAccountUserPool",
        "is_gcp_self_service": "isGcpSelfService",
        "is_dr_trial": "isDrTrial",
        "is_arm_self_service": "isArmSelfService",
        "is_aws_self_service": "isAwsSelfService",
        "saml_settings": "samlSettings",
        "is_right_sizing_enabled": "isRightSizingEnabled",
        "default_license_type": "defaultLicenseType",
        "max_projects_allowed": "maxProjectsAllowed",
        "ce_admin_properties": "ceAdminProperties",
        "owner_id": "ownerId",
        "is_med_one": "isMedOne",
        "id": "id",
    }

    def __init__(
        self,
        invite_token_expiry_minutes=None,
        allow_archiving_default_value=None,
        per_account_user_pool=None,
        is_gcp_self_service=None,
        is_dr_trial=None,
        is_arm_self_service=None,
        is_aws_self_service=None,
        saml_settings=None,
        is_right_sizing_enabled=None,
        default_license_type=None,
        max_projects_allowed=None,
        ce_admin_properties=None,
        owner_id=None,
        is_med_one=None,
        id=None,
    ):  # noqa: E501
        """CloudEndureAccount - a model defined in Swagger"""  # noqa: E501
        self._invite_token_expiry_minutes = None
        self._allow_archiving_default_value = None
        self._per_account_user_pool = None
        self._is_gcp_self_service = None
        self._is_dr_trial = None
        self._is_arm_self_service = None
        self._is_aws_self_service = None
        self._saml_settings = None
        self._is_right_sizing_enabled = None
        self._default_license_type = None
        self._max_projects_allowed = None
        self._ce_admin_properties = None
        self._owner_id = None
        self._is_med_one = None
        self._id = None
        self.discriminator = None
        if invite_token_expiry_minutes is not None:
            self.invite_token_expiry_minutes = invite_token_expiry_minutes
        if allow_archiving_default_value is not None:
            self.allow_archiving_default_value = allow_archiving_default_value
        if per_account_user_pool is not None:
            self.per_account_user_pool = per_account_user_pool
        if is_gcp_self_service is not None:
            self.is_gcp_self_service = is_gcp_self_service
        if is_dr_trial is not None:
            self.is_dr_trial = is_dr_trial
        if is_arm_self_service is not None:
            self.is_arm_self_service = is_arm_self_service
        if is_aws_self_service is not None:
            self.is_aws_self_service = is_aws_self_service
        if saml_settings is not None:
            self.saml_settings = saml_settings
        if is_right_sizing_enabled is not None:
            self.is_right_sizing_enabled = is_right_sizing_enabled
        if default_license_type is not None:
            self.default_license_type = default_license_type
        if max_projects_allowed is not None:
            self.max_projects_allowed = max_projects_allowed
        if ce_admin_properties is not None:
            self.ce_admin_properties = ce_admin_properties
        if owner_id is not None:
            self.owner_id = owner_id
        if is_med_one is not None:
            self.is_med_one = is_med_one
        if id is not None:
            self.id = id

    @property
    def invite_token_expiry_minutes(self):
        """Gets the invite_token_expiry_minutes of this CloudEndureAccount.  # noqa: E501


        :return: The invite_token_expiry_minutes of this CloudEndureAccount.  # noqa: E501
        :rtype: int
        """
        return self._invite_token_expiry_minutes

    @invite_token_expiry_minutes.setter
    def invite_token_expiry_minutes(self, invite_token_expiry_minutes):
        """Sets the invite_token_expiry_minutes of this CloudEndureAccount.


        :param invite_token_expiry_minutes: The invite_token_expiry_minutes of this CloudEndureAccount.  # noqa: E501
        :type: int
        """

        self._invite_token_expiry_minutes = invite_token_expiry_minutes

    @property
    def allow_archiving_default_value(self):
        """Gets the allow_archiving_default_value of this CloudEndureAccount.  # noqa: E501


        :return: The allow_archiving_default_value of this CloudEndureAccount.  # noqa: E501
        :rtype: bool
        """
        return self._allow_archiving_default_value

    @allow_archiving_default_value.setter
    def allow_archiving_default_value(self, allow_archiving_default_value):
        """Sets the allow_archiving_default_value of this CloudEndureAccount.


        :param allow_archiving_default_value: The allow_archiving_default_value of this CloudEndureAccount.  # noqa: E501
        :type: bool
        """

        self._allow_archiving_default_value = allow_archiving_default_value

    @property
    def per_account_user_pool(self):
        """Gets the per_account_user_pool of this CloudEndureAccount.  # noqa: E501


        :return: The per_account_user_pool of this CloudEndureAccount.  # noqa: E501
        :rtype: bool
        """
        return self._per_account_user_pool

    @per_account_user_pool.setter
    def per_account_user_pool(self, per_account_user_pool):
        """Sets the per_account_user_pool of this CloudEndureAccount.


        :param per_account_user_pool: The per_account_user_pool of this CloudEndureAccount.  # noqa: E501
        :type: bool
        """

        self._per_account_user_pool = per_account_user_pool

    @property
    def is_gcp_self_service(self):
        """Gets the is_gcp_self_service of this CloudEndureAccount.  # noqa: E501


        :return: The is_gcp_self_service of this CloudEndureAccount.  # noqa: E501
        :rtype: bool
        """
        return self._is_gcp_self_service

    @is_gcp_self_service.setter
    def is_gcp_self_service(self, is_gcp_self_service):
        """Sets the is_gcp_self_service of this CloudEndureAccount.


        :param is_gcp_self_service: The is_gcp_self_service of this CloudEndureAccount.  # noqa: E501
        :type: bool
        """

        self._is_gcp_self_service = is_gcp_self_service

    @property
    def is_dr_trial(self):
        """Gets the is_dr_trial of this CloudEndureAccount.  # noqa: E501


        :return: The is_dr_trial of this CloudEndureAccount.  # noqa: E501
        :rtype: bool
        """
        return self._is_dr_trial

    @is_dr_trial.setter
    def is_dr_trial(self, is_dr_trial):
        """Sets the is_dr_trial of this CloudEndureAccount.


        :param is_dr_trial: The is_dr_trial of this CloudEndureAccount.  # noqa: E501
        :type: bool
        """

        self._is_dr_trial = is_dr_trial

    @property
    def is_arm_self_service(self):
        """Gets the is_arm_self_service of this CloudEndureAccount.  # noqa: E501


        :return: The is_arm_self_service of this CloudEndureAccount.  # noqa: E501
        :rtype: bool
        """
        return self._is_arm_self_service

    @is_arm_self_service.setter
    def is_arm_self_service(self, is_arm_self_service):
        """Sets the is_arm_self_service of this CloudEndureAccount.


        :param is_arm_self_service: The is_arm_self_service of this CloudEndureAccount.  # noqa: E501
        :type: bool
        """

        self._is_arm_self_service = is_arm_self_service

    @property
    def is_aws_self_service(self):
        """Gets the is_aws_self_service of this CloudEndureAccount.  # noqa: E501


        :return: The is_aws_self_service of this CloudEndureAccount.  # noqa: E501
        :rtype: bool
        """
        return self._is_aws_self_service

    @is_aws_self_service.setter
    def is_aws_self_service(self, is_aws_self_service):
        """Sets the is_aws_self_service of this CloudEndureAccount.


        :param is_aws_self_service: The is_aws_self_service of this CloudEndureAccount.  # noqa: E501
        :type: bool
        """

        self._is_aws_self_service = is_aws_self_service

    @property
    def saml_settings(self):
        """Gets the saml_settings of this CloudEndureAccount.  # noqa: E501


        :return: The saml_settings of this CloudEndureAccount.  # noqa: E501
        :rtype: CloudEndureSamlSettings
        """
        return self._saml_settings

    @saml_settings.setter
    def saml_settings(self, saml_settings):
        """Sets the saml_settings of this CloudEndureAccount.


        :param saml_settings: The saml_settings of this CloudEndureAccount.  # noqa: E501
        :type: CloudEndureSamlSettings
        """

        self._saml_settings = saml_settings

    @property
    def is_right_sizing_enabled(self):
        """Gets the is_right_sizing_enabled of this CloudEndureAccount.  # noqa: E501


        :return: The is_right_sizing_enabled of this CloudEndureAccount.  # noqa: E501
        :rtype: bool
        """
        return self._is_right_sizing_enabled

    @is_right_sizing_enabled.setter
    def is_right_sizing_enabled(self, is_right_sizing_enabled):
        """Sets the is_right_sizing_enabled of this CloudEndureAccount.


        :param is_right_sizing_enabled: The is_right_sizing_enabled of this CloudEndureAccount.  # noqa: E501
        :type: bool
        """

        self._is_right_sizing_enabled = is_right_sizing_enabled

    @property
    def default_license_type(self):
        """Gets the default_license_type of this CloudEndureAccount.  # noqa: E501


        :return: The default_license_type of this CloudEndureAccount.  # noqa: E501
        :rtype: str
        """
        return self._default_license_type

    @default_license_type.setter
    def default_license_type(self, default_license_type):
        """Sets the default_license_type of this CloudEndureAccount.


        :param default_license_type: The default_license_type of this CloudEndureAccount.  # noqa: E501
        :type: str
        """
        allowed_values = ["MIGRATION", "DR", "DR_TRIAL", "BACKUP"]  # noqa: E501
        if default_license_type not in allowed_values:
            raise ValueError(
                "Invalid value for `default_license_type` ({0}), must be one of {1}".format(  # noqa: E501
                    default_license_type, allowed_values
                )
            )

        self._default_license_type = default_license_type

    @property
    def max_projects_allowed(self):
        """Gets the max_projects_allowed of this CloudEndureAccount.  # noqa: E501


        :return: The max_projects_allowed of this CloudEndureAccount.  # noqa: E501
        :rtype: int
        """
        return self._max_projects_allowed

    @max_projects_allowed.setter
    def max_projects_allowed(self, max_projects_allowed):
        """Sets the max_projects_allowed of this CloudEndureAccount.


        :param max_projects_allowed: The max_projects_allowed of this CloudEndureAccount.  # noqa: E501
        :type: int
        """

        self._max_projects_allowed = max_projects_allowed

    @property
    def ce_admin_properties(self):
        """Gets the ce_admin_properties of this CloudEndureAccount.  # noqa: E501

        For internal use.  # noqa: E501

        :return: The ce_admin_properties of this CloudEndureAccount.  # noqa: E501
        :rtype: object
        """
        return self._ce_admin_properties

    @ce_admin_properties.setter
    def ce_admin_properties(self, ce_admin_properties):
        """Sets the ce_admin_properties of this CloudEndureAccount.

        For internal use.  # noqa: E501

        :param ce_admin_properties: The ce_admin_properties of this CloudEndureAccount.  # noqa: E501
        :type: object
        """

        self._ce_admin_properties = ce_admin_properties

    @property
    def owner_id(self):
        """Gets the owner_id of this CloudEndureAccount.  # noqa: E501

        Account Owner (a User)  # noqa: E501

        :return: The owner_id of this CloudEndureAccount.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this CloudEndureAccount.

        Account Owner (a User)  # noqa: E501

        :param owner_id: The owner_id of this CloudEndureAccount.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

    @property
    def is_med_one(self):
        """Gets the is_med_one of this CloudEndureAccount.  # noqa: E501


        :return: The is_med_one of this CloudEndureAccount.  # noqa: E501
        :rtype: bool
        """
        return self._is_med_one

    @is_med_one.setter
    def is_med_one(self, is_med_one):
        """Sets the is_med_one of this CloudEndureAccount.


        :param is_med_one: The is_med_one of this CloudEndureAccount.  # noqa: E501
        :type: bool
        """

        self._is_med_one = is_med_one

    @property
    def id(self):
        """Gets the id of this CloudEndureAccount.  # noqa: E501

        UUID of the account  # noqa: E501

        :return: The id of this CloudEndureAccount.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CloudEndureAccount.

        UUID of the account  # noqa: E501

        :param id: The id of this CloudEndureAccount.  # noqa: E501
        :type: str
        """

        self._id = id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(CloudEndureAccount, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CloudEndureAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
