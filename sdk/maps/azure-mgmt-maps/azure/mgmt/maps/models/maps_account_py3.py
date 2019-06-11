# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class MapsAccount(Resource):
    """An Azure resource which represents access to a suite of Maps REST APIs.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The fully qualified Maps Account resource identifier.
    :vartype id: str
    :ivar name: The name of the Maps Account, which is unique within a
     Resource Group.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :ivar location: The location of the resource.
    :vartype location: str
    :ivar tags: Gets a list of key value pairs that describe the resource.
     These tags can be used in viewing and grouping this resource (across
     resource groups). A maximum of 15 tags can be provided for a resource.
     Each tag must have a key no greater than 128 characters and value no
     greater than 256 characters.
    :vartype tags: dict[str, str]
    :ivar sku: The SKU of this account.
    :vartype sku: ~azure.mgmt.maps.models.Sku
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'readonly': True},
        'tags': {'readonly': True},
        'sku': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'Sku'},
    }

    def __init__(self, **kwargs) -> None:
        super(MapsAccount, self).__init__(**kwargs)
        self.location = None
        self.tags = None
        self.sku = None