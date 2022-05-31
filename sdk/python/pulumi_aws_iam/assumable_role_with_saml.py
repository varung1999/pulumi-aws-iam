# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from ._inputs import *

__all__ = ['AssumableRoleWithSAMLArgs', 'AssumableRoleWithSAML']

@pulumi.input_type
class AssumableRoleWithSAMLArgs:
    def __init__(__self__, *,
                 aws_saml_endpoint: Optional[pulumi.Input[str]] = None,
                 force_detach_policies: Optional[pulumi.Input[bool]] = None,
                 max_session_duration: Optional[pulumi.Input[int]] = None,
                 provider_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role: Optional[pulumi.Input['RoleArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a AssumableRoleWithSAML resource.
        :param pulumi.Input[str] aws_saml_endpoint: AWS SAML Endpoint.
        :param pulumi.Input[bool] force_detach_policies: Whether policies should be detached from this role when destroying.
        :param pulumi.Input[int] max_session_duration: Maximum CLI/API session duration in seconds between 3600 and 43200.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] provider_ids: List of SAML Provider IDs.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to add.
        """
        if aws_saml_endpoint is None:
            aws_saml_endpoint = 'https://signin.aws.amazon.com/saml'
        if aws_saml_endpoint is not None:
            pulumi.set(__self__, "aws_saml_endpoint", aws_saml_endpoint)
        if force_detach_policies is None:
            force_detach_policies = False
        if force_detach_policies is not None:
            pulumi.set(__self__, "force_detach_policies", force_detach_policies)
        if max_session_duration is None:
            max_session_duration = 3600
        if max_session_duration is not None:
            pulumi.set(__self__, "max_session_duration", max_session_duration)
        if provider_ids is not None:
            pulumi.set(__self__, "provider_ids", provider_ids)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="awsSamlEndpoint")
    def aws_saml_endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        AWS SAML Endpoint.
        """
        return pulumi.get(self, "aws_saml_endpoint")

    @aws_saml_endpoint.setter
    def aws_saml_endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aws_saml_endpoint", value)

    @property
    @pulumi.getter(name="forceDetachPolicies")
    def force_detach_policies(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether policies should be detached from this role when destroying.
        """
        return pulumi.get(self, "force_detach_policies")

    @force_detach_policies.setter
    def force_detach_policies(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force_detach_policies", value)

    @property
    @pulumi.getter(name="maxSessionDuration")
    def max_session_duration(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum CLI/API session duration in seconds between 3600 and 43200.
        """
        return pulumi.get(self, "max_session_duration")

    @max_session_duration.setter
    def max_session_duration(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_session_duration", value)

    @property
    @pulumi.getter(name="providerIds")
    def provider_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of SAML Provider IDs.
        """
        return pulumi.get(self, "provider_ids")

    @provider_ids.setter
    def provider_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "provider_ids", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input['RoleArgs']]:
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input['RoleArgs']]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to add.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class AssumableRoleWithSAML(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_saml_endpoint: Optional[pulumi.Input[str]] = None,
                 force_detach_policies: Optional[pulumi.Input[bool]] = None,
                 max_session_duration: Optional[pulumi.Input[int]] = None,
                 provider_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role: Optional[pulumi.Input[pulumi.InputType['RoleArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Create a AssumableRoleWithSAML resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] aws_saml_endpoint: AWS SAML Endpoint.
        :param pulumi.Input[bool] force_detach_policies: Whether policies should be detached from this role when destroying.
        :param pulumi.Input[int] max_session_duration: Maximum CLI/API session duration in seconds between 3600 and 43200.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] provider_ids: List of SAML Provider IDs.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to add.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[AssumableRoleWithSAMLArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a AssumableRoleWithSAML resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param AssumableRoleWithSAMLArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AssumableRoleWithSAMLArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_saml_endpoint: Optional[pulumi.Input[str]] = None,
                 force_detach_policies: Optional[pulumi.Input[bool]] = None,
                 max_session_duration: Optional[pulumi.Input[int]] = None,
                 provider_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role: Optional[pulumi.Input[pulumi.InputType['RoleArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AssumableRoleWithSAMLArgs.__new__(AssumableRoleWithSAMLArgs)

            if aws_saml_endpoint is None:
                aws_saml_endpoint = 'https://signin.aws.amazon.com/saml'
            __props__.__dict__["aws_saml_endpoint"] = aws_saml_endpoint
            if force_detach_policies is None:
                force_detach_policies = False
            __props__.__dict__["force_detach_policies"] = force_detach_policies
            if max_session_duration is None:
                max_session_duration = 3600
            __props__.__dict__["max_session_duration"] = max_session_duration
            __props__.__dict__["provider_ids"] = provider_ids
            __props__.__dict__["role"] = role
            __props__.__dict__["tags"] = tags
            __props__.__dict__["role_arn"] = None
            __props__.__dict__["role_name"] = None
            __props__.__dict__["role_path"] = None
            __props__.__dict__["role_unique_id"] = None
        super(AssumableRoleWithSAML, __self__).__init__(
            'aws-iam:index:AssumableRoleWithSAML',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[str]:
        """
        ARN of IAM role.
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter(name="roleName")
    def role_name(self) -> pulumi.Output[str]:
        """
        Name of IAM role.
        """
        return pulumi.get(self, "role_name")

    @property
    @pulumi.getter(name="rolePath")
    def role_path(self) -> pulumi.Output[str]:
        """
        Path of IAM role.
        """
        return pulumi.get(self, "role_path")

    @property
    @pulumi.getter(name="roleUniqueId")
    def role_unique_id(self) -> pulumi.Output[str]:
        """
        Unique ID of IAM role.
        """
        return pulumi.get(self, "role_unique_id")
