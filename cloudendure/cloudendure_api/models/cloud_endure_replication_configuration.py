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


class CloudEndureReplicationConfiguration:
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
        "volume_encryption_key": "str",
        "replication_tags": "list[object]",
        "subnet_host_project": "str",
        "replication_server_type": "str",
        "compute_location_id": "str",
        "cloud_credentials": "str",
        "subnet_id": "str",
        "logical_location_id": "str",
        "bandwidth_throttling": "int",
        "storage_location_id": "str",
        "use_dedicated_server": "bool",
        "zone": "str",
        "replicator_security_group_i_ds": "list[str]",
        "use_private_ip": "bool",
        "region": "str",
        "id": "str",
        "proxy_url": "str",
        "volume_encryption_allowed": "bool",
        "archiving_enabled": "bool",
        "object_storage_location": "str",
    }

    attribute_map = {
        "volume_encryption_key": "volumeEncryptionKey",
        "replication_tags": "replicationTags",
        "subnet_host_project": "subnetHostProject",
        "replication_server_type": "replicationServerType",
        "compute_location_id": "computeLocationId",
        "cloud_credentials": "cloudCredentials",
        "subnet_id": "subnetId",
        "logical_location_id": "logicalLocationId",
        "bandwidth_throttling": "bandwidthThrottling",
        "storage_location_id": "storageLocationId",
        "use_dedicated_server": "useDedicatedServer",
        "zone": "zone",
        "replicator_security_group_i_ds": "replicatorSecurityGroupIDs",
        "use_private_ip": "usePrivateIp",
        "region": "region",
        "id": "id",
        "proxy_url": "proxyUrl",
        "volume_encryption_allowed": "volumeEncryptionAllowed",
        "archiving_enabled": "archivingEnabled",
        "object_storage_location": "objectStorageLocation",
    }

    def __init__(
        self,
        volume_encryption_key=None,
        replication_tags=None,
        subnet_host_project=None,
        replication_server_type=None,
        compute_location_id=None,
        cloud_credentials=None,
        subnet_id=None,
        logical_location_id=None,
        bandwidth_throttling=None,
        storage_location_id=None,
        use_dedicated_server=None,
        zone=None,
        replicator_security_group_i_ds=None,
        use_private_ip=None,
        region=None,
        id=None,
        proxy_url=None,
        volume_encryption_allowed=None,
        archiving_enabled=None,
        object_storage_location=None,
    ):  # noqa: E501
        """CloudEndureReplicationConfiguration - a model defined in Swagger"""  # noqa: E501
        self._volume_encryption_key = None
        self._replication_tags = None
        self._subnet_host_project = None
        self._replication_server_type = None
        self._compute_location_id = None
        self._cloud_credentials = None
        self._subnet_id = None
        self._logical_location_id = None
        self._bandwidth_throttling = None
        self._storage_location_id = None
        self._use_dedicated_server = None
        self._zone = None
        self._replicator_security_group_i_ds = None
        self._use_private_ip = None
        self._region = None
        self._id = None
        self._proxy_url = None
        self._volume_encryption_allowed = None
        self._archiving_enabled = None
        self._object_storage_location = None
        self.discriminator = None
        if volume_encryption_key is not None:
            self.volume_encryption_key = volume_encryption_key
        if replication_tags is not None:
            self.replication_tags = replication_tags
        if subnet_host_project is not None:
            self.subnet_host_project = subnet_host_project
        if replication_server_type is not None:
            self.replication_server_type = replication_server_type
        if compute_location_id is not None:
            self.compute_location_id = compute_location_id
        if cloud_credentials is not None:
            self.cloud_credentials = cloud_credentials
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if logical_location_id is not None:
            self.logical_location_id = logical_location_id
        if bandwidth_throttling is not None:
            self.bandwidth_throttling = bandwidth_throttling
        if storage_location_id is not None:
            self.storage_location_id = storage_location_id
        if use_dedicated_server is not None:
            self.use_dedicated_server = use_dedicated_server
        if zone is not None:
            self.zone = zone
        if replicator_security_group_i_ds is not None:
            self.replicator_security_group_i_ds = replicator_security_group_i_ds
        if use_private_ip is not None:
            self.use_private_ip = use_private_ip
        if region is not None:
            self.region = region
        if id is not None:
            self.id = id
        if proxy_url is not None:
            self.proxy_url = proxy_url
        if volume_encryption_allowed is not None:
            self.volume_encryption_allowed = volume_encryption_allowed
        if archiving_enabled is not None:
            self.archiving_enabled = archiving_enabled
        if object_storage_location is not None:
            self.object_storage_location = object_storage_location

    @property
    def volume_encryption_key(self):
        """Gets the volume_encryption_key of this CloudEndureReplicationConfiguration.  # noqa: E501

        AWS only. ARN to private key for Volume Encryption. Possible values can be fetched from the Region object.  # noqa: E501

        :return: The volume_encryption_key of this CloudEndureReplicationConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._volume_encryption_key

    @volume_encryption_key.setter
    def volume_encryption_key(self, volume_encryption_key):
        """Sets the volume_encryption_key of this CloudEndureReplicationConfiguration.

        AWS only. ARN to private key for Volume Encryption. Possible values can be fetched from the Region object.  # noqa: E501

        :param volume_encryption_key: The volume_encryption_key of this CloudEndureReplicationConfiguration.  # noqa: E501
        :type: str
        """

        self._volume_encryption_key = volume_encryption_key

    @property
    def replication_tags(self):
        """Gets the replication_tags of this CloudEndureReplicationConfiguration.  # noqa: E501

        AWS only. Tags that will be applied to every cloud resource created in the CloudEndure Staging Area.  # noqa: E501

        :return: The replication_tags of this CloudEndureReplicationConfiguration.  # noqa: E501
        :rtype: list[object]
        """
        return self._replication_tags

    @replication_tags.setter
    def replication_tags(self, replication_tags):
        """Sets the replication_tags of this CloudEndureReplicationConfiguration.

        AWS only. Tags that will be applied to every cloud resource created in the CloudEndure Staging Area.  # noqa: E501

        :param replication_tags: The replication_tags of this CloudEndureReplicationConfiguration.  # noqa: E501
        :type: list[object]
        """

        self._replication_tags = replication_tags

    @property
    def subnet_host_project(self):
        """Gets the subnet_host_project of this CloudEndureReplicationConfiguration.  # noqa: E501

        GCP only. Host project of cross project network subnet.  # noqa: E501

        :return: The subnet_host_project of this CloudEndureReplicationConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._subnet_host_project

    @subnet_host_project.setter
    def subnet_host_project(self, subnet_host_project):
        """Sets the subnet_host_project of this CloudEndureReplicationConfiguration.

        GCP only. Host project of cross project network subnet.  # noqa: E501

        :param subnet_host_project: The subnet_host_project of this CloudEndureReplicationConfiguration.  # noqa: E501
        :type: str
        """

        self._subnet_host_project = subnet_host_project

    @property
    def replication_server_type(self):
        """Gets the replication_server_type of this CloudEndureReplicationConfiguration.  # noqa: E501


        :return: The replication_server_type of this CloudEndureReplicationConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._replication_server_type

    @replication_server_type.setter
    def replication_server_type(self, replication_server_type):
        """Sets the replication_server_type of this CloudEndureReplicationConfiguration.


        :param replication_server_type: The replication_server_type of this CloudEndureReplicationConfiguration.  # noqa: E501
        :type: str
        """

        self._replication_server_type = replication_server_type

    @property
    def compute_location_id(self):
        """Gets the compute_location_id of this CloudEndureReplicationConfiguration.  # noqa: E501

        todo  vcenter only  # noqa: E501

        :return: The compute_location_id of this CloudEndureReplicationConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._compute_location_id

    @compute_location_id.setter
    def compute_location_id(self, compute_location_id):
        """Sets the compute_location_id of this CloudEndureReplicationConfiguration.

        todo  vcenter only  # noqa: E501

        :param compute_location_id: The compute_location_id of this CloudEndureReplicationConfiguration.  # noqa: E501
        :type: str
        """

        self._compute_location_id = compute_location_id

    @property
    def cloud_credentials(self):
        """Gets the cloud_credentials of this CloudEndureReplicationConfiguration.  # noqa: E501

        The ID for the cloudCredentials object containing the credentials to be used for accessing the target cloud.  # noqa: E501

        :return: The cloud_credentials of this CloudEndureReplicationConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._cloud_credentials

    @cloud_credentials.setter
    def cloud_credentials(self, cloud_credentials):
        """Sets the cloud_credentials of this CloudEndureReplicationConfiguration.

        The ID for the cloudCredentials object containing the credentials to be used for accessing the target cloud.  # noqa: E501

        :param cloud_credentials: The cloud_credentials of this CloudEndureReplicationConfiguration.  # noqa: E501
        :type: str
        """

        self._cloud_credentials = cloud_credentials

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CloudEndureReplicationConfiguration.  # noqa: E501

        Subnet where replication servers will be created. Possible values can be fetched from the Region object.  # noqa: E501

        :return: The subnet_id of this CloudEndureReplicationConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CloudEndureReplicationConfiguration.

        Subnet where replication servers will be created. Possible values can be fetched from the Region object.  # noqa: E501

        :param subnet_id: The subnet_id of this CloudEndureReplicationConfiguration.  # noqa: E501
        :type: str
        """

        self._subnet_id = subnet_id

    @property
    def logical_location_id(self):
        """Gets the logical_location_id of this CloudEndureReplicationConfiguration.  # noqa: E501

        vcenter = vmFolder  # noqa: E501

        :return: The logical_location_id of this CloudEndureReplicationConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._logical_location_id

    @logical_location_id.setter
    def logical_location_id(self, logical_location_id):
        """Sets the logical_location_id of this CloudEndureReplicationConfiguration.

        vcenter = vmFolder  # noqa: E501

        :param logical_location_id: The logical_location_id of this CloudEndureReplicationConfiguration.  # noqa: E501
        :type: str
        """

        self._logical_location_id = logical_location_id

    @property
    def bandwidth_throttling(self):
        """Gets the bandwidth_throttling of this CloudEndureReplicationConfiguration.  # noqa: E501

        Mbps to use for Data Replication (zero means no throttling).  # noqa: E501

        :return: The bandwidth_throttling of this CloudEndureReplicationConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth_throttling

    @bandwidth_throttling.setter
    def bandwidth_throttling(self, bandwidth_throttling):
        """Sets the bandwidth_throttling of this CloudEndureReplicationConfiguration.

        Mbps to use for Data Replication (zero means no throttling).  # noqa: E501

        :param bandwidth_throttling: The bandwidth_throttling of this CloudEndureReplicationConfiguration.  # noqa: E501
        :type: int
        """

        self._bandwidth_throttling = bandwidth_throttling

    @property
    def storage_location_id(self):
        """Gets the storage_location_id of this CloudEndureReplicationConfiguration.  # noqa: E501

        @todo backend creates cloudendure bla bla storage account upon need (empty string).   # noqa: E501

        :return: The storage_location_id of this CloudEndureReplicationConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._storage_location_id

    @storage_location_id.setter
    def storage_location_id(self, storage_location_id):
        """Sets the storage_location_id of this CloudEndureReplicationConfiguration.

        @todo backend creates cloudendure bla bla storage account upon need (empty string).   # noqa: E501

        :param storage_location_id: The storage_location_id of this CloudEndureReplicationConfiguration.  # noqa: E501
        :type: str
        """

        self._storage_location_id = storage_location_id

    @property
    def use_dedicated_server(self):
        """Gets the use_dedicated_server of this CloudEndureReplicationConfiguration.  # noqa: E501


        :return: The use_dedicated_server of this CloudEndureReplicationConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._use_dedicated_server

    @use_dedicated_server.setter
    def use_dedicated_server(self, use_dedicated_server):
        """Sets the use_dedicated_server of this CloudEndureReplicationConfiguration.


        :param use_dedicated_server: The use_dedicated_server of this CloudEndureReplicationConfiguration.  # noqa: E501
        :type: bool
        """

        self._use_dedicated_server = use_dedicated_server

    @property
    def zone(self):
        """Gets the zone of this CloudEndureReplicationConfiguration.  # noqa: E501

        Relevant for GCP and Azure ARM. The Zone to replicate into.  # noqa: E501

        :return: The zone of this CloudEndureReplicationConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this CloudEndureReplicationConfiguration.

        Relevant for GCP and Azure ARM. The Zone to replicate into.  # noqa: E501

        :param zone: The zone of this CloudEndureReplicationConfiguration.  # noqa: E501
        :type: str
        """

        self._zone = zone

    @property
    def replicator_security_group_i_ds(self):
        """Gets the replicator_security_group_i_ds of this CloudEndureReplicationConfiguration.  # noqa: E501

        AWS only. The security groups that will be applied to the replication servers. Possible values can be fetched from the Region object.  # noqa: E501

        :return: The replicator_security_group_i_ds of this CloudEndureReplicationConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._replicator_security_group_i_ds

    @replicator_security_group_i_ds.setter
    def replicator_security_group_i_ds(self, replicator_security_group_i_ds):
        """Sets the replicator_security_group_i_ds of this CloudEndureReplicationConfiguration.

        AWS only. The security groups that will be applied to the replication servers. Possible values can be fetched from the Region object.  # noqa: E501

        :param replicator_security_group_i_ds: The replicator_security_group_i_ds of this CloudEndureReplicationConfiguration.  # noqa: E501
        :type: list[str]
        """

        self._replicator_security_group_i_ds = replicator_security_group_i_ds

    @property
    def use_private_ip(self):
        """Gets the use_private_ip of this CloudEndureReplicationConfiguration.  # noqa: E501

        Should the CloudEndure agent access the replication server using its private IP address.  # noqa: E501

        :return: The use_private_ip of this CloudEndureReplicationConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._use_private_ip

    @use_private_ip.setter
    def use_private_ip(self, use_private_ip):
        """Sets the use_private_ip of this CloudEndureReplicationConfiguration.

        Should the CloudEndure agent access the replication server using its private IP address.  # noqa: E501

        :param use_private_ip: The use_private_ip of this CloudEndureReplicationConfiguration.  # noqa: E501
        :type: bool
        """

        self._use_private_ip = use_private_ip

    @property
    def region(self):
        """Gets the region of this CloudEndureReplicationConfiguration.  # noqa: E501


        :return: The region of this CloudEndureReplicationConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CloudEndureReplicationConfiguration.


        :param region: The region of this CloudEndureReplicationConfiguration.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def id(self):
        """Gets the id of this CloudEndureReplicationConfiguration.  # noqa: E501


        :return: The id of this CloudEndureReplicationConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CloudEndureReplicationConfiguration.


        :param id: The id of this CloudEndureReplicationConfiguration.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def proxy_url(self):
        """Gets the proxy_url of this CloudEndureReplicationConfiguration.  # noqa: E501

        The full URI for a proxy (schema, username, password, domain, port) if required for the CloudEndure agent.  # noqa: E501

        :return: The proxy_url of this CloudEndureReplicationConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._proxy_url

    @proxy_url.setter
    def proxy_url(self, proxy_url):
        """Sets the proxy_url of this CloudEndureReplicationConfiguration.

        The full URI for a proxy (schema, username, password, domain, port) if required for the CloudEndure agent.  # noqa: E501

        :param proxy_url: The proxy_url of this CloudEndureReplicationConfiguration.  # noqa: E501
        :type: str
        """

        self._proxy_url = proxy_url

    @property
    def volume_encryption_allowed(self):
        """Gets the volume_encryption_allowed of this CloudEndureReplicationConfiguration.  # noqa: E501

        todo  # noqa: E501

        :return: The volume_encryption_allowed of this CloudEndureReplicationConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._volume_encryption_allowed

    @volume_encryption_allowed.setter
    def volume_encryption_allowed(self, volume_encryption_allowed):
        """Sets the volume_encryption_allowed of this CloudEndureReplicationConfiguration.

        todo  # noqa: E501

        :param volume_encryption_allowed: The volume_encryption_allowed of this CloudEndureReplicationConfiguration.  # noqa: E501
        :type: bool
        """

        self._volume_encryption_allowed = volume_encryption_allowed

    @property
    def archiving_enabled(self):
        """Gets the archiving_enabled of this CloudEndureReplicationConfiguration.  # noqa: E501


        :return: The archiving_enabled of this CloudEndureReplicationConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._archiving_enabled

    @archiving_enabled.setter
    def archiving_enabled(self, archiving_enabled):
        """Sets the archiving_enabled of this CloudEndureReplicationConfiguration.


        :param archiving_enabled: The archiving_enabled of this CloudEndureReplicationConfiguration.  # noqa: E501
        :type: bool
        """

        self._archiving_enabled = archiving_enabled

    @property
    def object_storage_location(self):
        """Gets the object_storage_location of this CloudEndureReplicationConfiguration.  # noqa: E501

        bucket in aws   # noqa: E501

        :return: The object_storage_location of this CloudEndureReplicationConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._object_storage_location

    @object_storage_location.setter
    def object_storage_location(self, object_storage_location):
        """Sets the object_storage_location of this CloudEndureReplicationConfiguration.

        bucket in aws   # noqa: E501

        :param object_storage_location: The object_storage_location of this CloudEndureReplicationConfiguration.  # noqa: E501
        :type: str
        """

        self._object_storage_location = object_storage_location

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
        if issubclass(CloudEndureReplicationConfiguration, dict):
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
        if not isinstance(other, CloudEndureReplicationConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
