# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'KubernetesXyzGlobalArgs',
    'ReleaseArgs',
    'RepositoryOptsArgs',
]

@pulumi.input_type
class KubernetesXyzGlobalArgs:
    def __init__(__self__):
        pass


@pulumi.input_type
class ReleaseArgs:
    def __init__(__self__, *,
                 atomic: Optional[pulumi.Input[bool]] = None,
                 chart: Optional[pulumi.Input[str]] = None,
                 cleanup_on_fail: Optional[pulumi.Input[bool]] = None,
                 create_namespace: Optional[pulumi.Input[bool]] = None,
                 dependency_update: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 devel: Optional[pulumi.Input[bool]] = None,
                 disable_crd_hooks: Optional[pulumi.Input[bool]] = None,
                 disable_openapi_validation: Optional[pulumi.Input[bool]] = None,
                 disable_webhooks: Optional[pulumi.Input[bool]] = None,
                 force_update: Optional[pulumi.Input[bool]] = None,
                 keyring: Optional[pulumi.Input[str]] = None,
                 lint: Optional[pulumi.Input[bool]] = None,
                 manifest: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 max_history: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 postrender: Optional[pulumi.Input[str]] = None,
                 recreate_pods: Optional[pulumi.Input[bool]] = None,
                 render_subchart_notes: Optional[pulumi.Input[bool]] = None,
                 replace: Optional[pulumi.Input[bool]] = None,
                 repository_opts: Optional[pulumi.Input['RepositoryOptsArgs']] = None,
                 reset_values: Optional[pulumi.Input[bool]] = None,
                 resource_names: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]] = None,
                 reuse_values: Optional[pulumi.Input[bool]] = None,
                 skip_await: Optional[pulumi.Input[bool]] = None,
                 skip_crds: Optional[pulumi.Input[bool]] = None,
                 timeout: Optional[pulumi.Input[int]] = None,
                 value_yaml_files: Optional[pulumi.Input[Sequence[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]]]] = None,
                 values: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 verify: Optional[pulumi.Input[bool]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 wait_for_jobs: Optional[pulumi.Input[bool]] = None):
        """
        A Release is an instance of a chart running in a Kubernetes cluster.
        A Chart is a Helm package. It contains all of the resource definitions necessary to run an application, tool, or service inside of a Kubernetes cluster.
        Note - Helm Release is currently in BETA and may change. Use in production environment is discouraged.
        :param pulumi.Input[bool] atomic: If set, installation process purges chart on fail. `skipAwait` will be disabled automatically if atomic is used.
        :param pulumi.Input[str] chart: Chart name to be installed. A path may be used.
        :param pulumi.Input[bool] cleanup_on_fail: Allow deletion of new resources created in this upgrade when upgrade fails.
        :param pulumi.Input[bool] create_namespace: Create the namespace if it does not exist.
        :param pulumi.Input[bool] dependency_update: Run helm dependency update before installing the chart.
        :param pulumi.Input[str] description: Add a custom description
        :param pulumi.Input[bool] devel: Use chart development versions, too. Equivalent to version '>0.0.0-0'. If `version` is set, this is ignored.
        :param pulumi.Input[bool] disable_crd_hooks: Prevent CRD hooks from, running, but run other hooks.  See helm install --no-crd-hook
        :param pulumi.Input[bool] disable_openapi_validation: If set, the installation process will not validate rendered templates against the Kubernetes OpenAPI Schema
        :param pulumi.Input[bool] disable_webhooks: Prevent hooks from running.
        :param pulumi.Input[bool] force_update: Force resource update through delete/recreate if needed.
        :param pulumi.Input[str] keyring: Location of public keys used for verification. Used only if `verify` is true
        :param pulumi.Input[bool] lint: Run helm lint when planning.
        :param pulumi.Input[Mapping[str, Any]] manifest: The rendered manifests as JSON. Not yet supported.
        :param pulumi.Input[int] max_history: Limit the maximum number of revisions saved per release. Use 0 for no limit.
        :param pulumi.Input[str] name: Release name.
        :param pulumi.Input[str] namespace: Namespace to install the release into.
        :param pulumi.Input[str] postrender: Postrender command to run.
        :param pulumi.Input[bool] recreate_pods: Perform pods restart during upgrade/rollback.
        :param pulumi.Input[bool] render_subchart_notes: If set, render subchart notes along with the parent.
        :param pulumi.Input[bool] replace: Re-use the given name, even if that name is already used. This is unsafe in production
        :param pulumi.Input['RepositoryOptsArgs'] repository_opts: Specification defining the Helm chart repository to use.
        :param pulumi.Input[bool] reset_values: When upgrading, reset the values to the ones built into the chart.
        :param pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]] resource_names: Names of resources created by the release grouped by "kind/version".
        :param pulumi.Input[bool] reuse_values: When upgrading, reuse the last release's values and merge in any overrides. If 'resetValues' is specified, this is ignored
        :param pulumi.Input[bool] skip_await: By default, the provider waits until all resources are in a ready state before marking the release as successful. Setting this to true will skip such await logic.
        :param pulumi.Input[bool] skip_crds: If set, no CRDs will be installed. By default, CRDs are installed if not already present.
        :param pulumi.Input[int] timeout: Time in seconds to wait for any individual kubernetes operation.
        :param pulumi.Input[Sequence[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]]] value_yaml_files: List of assets (raw yaml files). Content is read and merged with values. Not yet supported.
        :param pulumi.Input[Mapping[str, Any]] values: Custom values set for the release.
        :param pulumi.Input[bool] verify: Verify the package before installing it.
        :param pulumi.Input[str] version: Specify the exact chart version to install. If this is not specified, the latest version is installed.
        :param pulumi.Input[bool] wait_for_jobs: Will wait until all Jobs have been completed before marking the release as successful. This is ignored if `skipAwait` is enabled.
        """
        if atomic is not None:
            pulumi.set(__self__, "atomic", atomic)
        if chart is not None:
            pulumi.set(__self__, "chart", chart)
        if cleanup_on_fail is not None:
            pulumi.set(__self__, "cleanup_on_fail", cleanup_on_fail)
        if create_namespace is not None:
            pulumi.set(__self__, "create_namespace", create_namespace)
        if dependency_update is not None:
            pulumi.set(__self__, "dependency_update", dependency_update)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if devel is not None:
            pulumi.set(__self__, "devel", devel)
        if disable_crd_hooks is not None:
            pulumi.set(__self__, "disable_crd_hooks", disable_crd_hooks)
        if disable_openapi_validation is not None:
            pulumi.set(__self__, "disable_openapi_validation", disable_openapi_validation)
        if disable_webhooks is not None:
            pulumi.set(__self__, "disable_webhooks", disable_webhooks)
        if force_update is not None:
            pulumi.set(__self__, "force_update", force_update)
        if keyring is not None:
            pulumi.set(__self__, "keyring", keyring)
        if lint is not None:
            pulumi.set(__self__, "lint", lint)
        if manifest is not None:
            pulumi.set(__self__, "manifest", manifest)
        if max_history is not None:
            pulumi.set(__self__, "max_history", max_history)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)
        if postrender is not None:
            pulumi.set(__self__, "postrender", postrender)
        if recreate_pods is not None:
            pulumi.set(__self__, "recreate_pods", recreate_pods)
        if render_subchart_notes is not None:
            pulumi.set(__self__, "render_subchart_notes", render_subchart_notes)
        if replace is not None:
            pulumi.set(__self__, "replace", replace)
        if repository_opts is not None:
            pulumi.set(__self__, "repository_opts", repository_opts)
        if reset_values is not None:
            pulumi.set(__self__, "reset_values", reset_values)
        if resource_names is not None:
            pulumi.set(__self__, "resource_names", resource_names)
        if reuse_values is not None:
            pulumi.set(__self__, "reuse_values", reuse_values)
        if skip_await is not None:
            pulumi.set(__self__, "skip_await", skip_await)
        if skip_crds is not None:
            pulumi.set(__self__, "skip_crds", skip_crds)
        if timeout is not None:
            pulumi.set(__self__, "timeout", timeout)
        if value_yaml_files is not None:
            pulumi.set(__self__, "value_yaml_files", value_yaml_files)
        if values is not None:
            pulumi.set(__self__, "values", values)
        if verify is not None:
            pulumi.set(__self__, "verify", verify)
        if version is not None:
            pulumi.set(__self__, "version", version)
        if wait_for_jobs is not None:
            pulumi.set(__self__, "wait_for_jobs", wait_for_jobs)

    @property
    @pulumi.getter
    def atomic(self) -> Optional[pulumi.Input[bool]]:
        """
        If set, installation process purges chart on fail. `skipAwait` will be disabled automatically if atomic is used.
        """
        return pulumi.get(self, "atomic")

    @atomic.setter
    def atomic(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "atomic", value)

    @property
    @pulumi.getter
    def chart(self) -> Optional[pulumi.Input[str]]:
        """
        Chart name to be installed. A path may be used.
        """
        return pulumi.get(self, "chart")

    @chart.setter
    def chart(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "chart", value)

    @property
    @pulumi.getter(name="cleanupOnFail")
    def cleanup_on_fail(self) -> Optional[pulumi.Input[bool]]:
        """
        Allow deletion of new resources created in this upgrade when upgrade fails.
        """
        return pulumi.get(self, "cleanup_on_fail")

    @cleanup_on_fail.setter
    def cleanup_on_fail(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "cleanup_on_fail", value)

    @property
    @pulumi.getter(name="createNamespace")
    def create_namespace(self) -> Optional[pulumi.Input[bool]]:
        """
        Create the namespace if it does not exist.
        """
        return pulumi.get(self, "create_namespace")

    @create_namespace.setter
    def create_namespace(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "create_namespace", value)

    @property
    @pulumi.getter(name="dependencyUpdate")
    def dependency_update(self) -> Optional[pulumi.Input[bool]]:
        """
        Run helm dependency update before installing the chart.
        """
        return pulumi.get(self, "dependency_update")

    @dependency_update.setter
    def dependency_update(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "dependency_update", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Add a custom description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def devel(self) -> Optional[pulumi.Input[bool]]:
        """
        Use chart development versions, too. Equivalent to version '>0.0.0-0'. If `version` is set, this is ignored.
        """
        return pulumi.get(self, "devel")

    @devel.setter
    def devel(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "devel", value)

    @property
    @pulumi.getter(name="disableCRDHooks")
    def disable_crd_hooks(self) -> Optional[pulumi.Input[bool]]:
        """
        Prevent CRD hooks from, running, but run other hooks.  See helm install --no-crd-hook
        """
        return pulumi.get(self, "disable_crd_hooks")

    @disable_crd_hooks.setter
    def disable_crd_hooks(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_crd_hooks", value)

    @property
    @pulumi.getter(name="disableOpenapiValidation")
    def disable_openapi_validation(self) -> Optional[pulumi.Input[bool]]:
        """
        If set, the installation process will not validate rendered templates against the Kubernetes OpenAPI Schema
        """
        return pulumi.get(self, "disable_openapi_validation")

    @disable_openapi_validation.setter
    def disable_openapi_validation(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_openapi_validation", value)

    @property
    @pulumi.getter(name="disableWebhooks")
    def disable_webhooks(self) -> Optional[pulumi.Input[bool]]:
        """
        Prevent hooks from running.
        """
        return pulumi.get(self, "disable_webhooks")

    @disable_webhooks.setter
    def disable_webhooks(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_webhooks", value)

    @property
    @pulumi.getter(name="forceUpdate")
    def force_update(self) -> Optional[pulumi.Input[bool]]:
        """
        Force resource update through delete/recreate if needed.
        """
        return pulumi.get(self, "force_update")

    @force_update.setter
    def force_update(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force_update", value)

    @property
    @pulumi.getter
    def keyring(self) -> Optional[pulumi.Input[str]]:
        """
        Location of public keys used for verification. Used only if `verify` is true
        """
        return pulumi.get(self, "keyring")

    @keyring.setter
    def keyring(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "keyring", value)

    @property
    @pulumi.getter
    def lint(self) -> Optional[pulumi.Input[bool]]:
        """
        Run helm lint when planning.
        """
        return pulumi.get(self, "lint")

    @lint.setter
    def lint(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "lint", value)

    @property
    @pulumi.getter
    def manifest(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        The rendered manifests as JSON. Not yet supported.
        """
        return pulumi.get(self, "manifest")

    @manifest.setter
    def manifest(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "manifest", value)

    @property
    @pulumi.getter(name="maxHistory")
    def max_history(self) -> Optional[pulumi.Input[int]]:
        """
        Limit the maximum number of revisions saved per release. Use 0 for no limit.
        """
        return pulumi.get(self, "max_history")

    @max_history.setter
    def max_history(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_history", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Release name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        Namespace to install the release into.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter
    def postrender(self) -> Optional[pulumi.Input[str]]:
        """
        Postrender command to run.
        """
        return pulumi.get(self, "postrender")

    @postrender.setter
    def postrender(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "postrender", value)

    @property
    @pulumi.getter(name="recreatePods")
    def recreate_pods(self) -> Optional[pulumi.Input[bool]]:
        """
        Perform pods restart during upgrade/rollback.
        """
        return pulumi.get(self, "recreate_pods")

    @recreate_pods.setter
    def recreate_pods(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "recreate_pods", value)

    @property
    @pulumi.getter(name="renderSubchartNotes")
    def render_subchart_notes(self) -> Optional[pulumi.Input[bool]]:
        """
        If set, render subchart notes along with the parent.
        """
        return pulumi.get(self, "render_subchart_notes")

    @render_subchart_notes.setter
    def render_subchart_notes(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "render_subchart_notes", value)

    @property
    @pulumi.getter
    def replace(self) -> Optional[pulumi.Input[bool]]:
        """
        Re-use the given name, even if that name is already used. This is unsafe in production
        """
        return pulumi.get(self, "replace")

    @replace.setter
    def replace(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "replace", value)

    @property
    @pulumi.getter(name="repositoryOpts")
    def repository_opts(self) -> Optional[pulumi.Input['RepositoryOptsArgs']]:
        """
        Specification defining the Helm chart repository to use.
        """
        return pulumi.get(self, "repository_opts")

    @repository_opts.setter
    def repository_opts(self, value: Optional[pulumi.Input['RepositoryOptsArgs']]):
        pulumi.set(self, "repository_opts", value)

    @property
    @pulumi.getter(name="resetValues")
    def reset_values(self) -> Optional[pulumi.Input[bool]]:
        """
        When upgrading, reset the values to the ones built into the chart.
        """
        return pulumi.get(self, "reset_values")

    @reset_values.setter
    def reset_values(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "reset_values", value)

    @property
    @pulumi.getter(name="resourceNames")
    def resource_names(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]]:
        """
        Names of resources created by the release grouped by "kind/version".
        """
        return pulumi.get(self, "resource_names")

    @resource_names.setter
    def resource_names(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]]):
        pulumi.set(self, "resource_names", value)

    @property
    @pulumi.getter(name="reuseValues")
    def reuse_values(self) -> Optional[pulumi.Input[bool]]:
        """
        When upgrading, reuse the last release's values and merge in any overrides. If 'resetValues' is specified, this is ignored
        """
        return pulumi.get(self, "reuse_values")

    @reuse_values.setter
    def reuse_values(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "reuse_values", value)

    @property
    @pulumi.getter(name="skipAwait")
    def skip_await(self) -> Optional[pulumi.Input[bool]]:
        """
        By default, the provider waits until all resources are in a ready state before marking the release as successful. Setting this to true will skip such await logic.
        """
        return pulumi.get(self, "skip_await")

    @skip_await.setter
    def skip_await(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "skip_await", value)

    @property
    @pulumi.getter(name="skipCrds")
    def skip_crds(self) -> Optional[pulumi.Input[bool]]:
        """
        If set, no CRDs will be installed. By default, CRDs are installed if not already present.
        """
        return pulumi.get(self, "skip_crds")

    @skip_crds.setter
    def skip_crds(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "skip_crds", value)

    @property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[int]]:
        """
        Time in seconds to wait for any individual kubernetes operation.
        """
        return pulumi.get(self, "timeout")

    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "timeout", value)

    @property
    @pulumi.getter(name="valueYamlFiles")
    def value_yaml_files(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]]]]:
        """
        List of assets (raw yaml files). Content is read and merged with values. Not yet supported.
        """
        return pulumi.get(self, "value_yaml_files")

    @value_yaml_files.setter
    def value_yaml_files(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]]]]):
        pulumi.set(self, "value_yaml_files", value)

    @property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Custom values set for the release.
        """
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def verify(self) -> Optional[pulumi.Input[bool]]:
        """
        Verify the package before installing it.
        """
        return pulumi.get(self, "verify")

    @verify.setter
    def verify(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "verify", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        Specify the exact chart version to install. If this is not specified, the latest version is installed.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)

    @property
    @pulumi.getter(name="waitForJobs")
    def wait_for_jobs(self) -> Optional[pulumi.Input[bool]]:
        """
        Will wait until all Jobs have been completed before marking the release as successful. This is ignored if `skipAwait` is enabled.
        """
        return pulumi.get(self, "wait_for_jobs")

    @wait_for_jobs.setter
    def wait_for_jobs(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "wait_for_jobs", value)


@pulumi.input_type
class RepositoryOptsArgs:
    def __init__(__self__, *,
                 ca_file: Optional[pulumi.Input[str]] = None,
                 cert_file: Optional[pulumi.Input[str]] = None,
                 key_file: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 repo: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        """
        Specification defining the Helm chart repository to use.
        :param pulumi.Input[str] ca_file: The Repository's CA File
        :param pulumi.Input[str] cert_file: The repository's cert file
        :param pulumi.Input[str] key_file: The repository's cert key file
        :param pulumi.Input[str] password: Password for HTTP basic authentication
        :param pulumi.Input[str] repo: Repository where to locate the requested chart. If is a URL the chart is installed without installing the repository.
        :param pulumi.Input[str] username: Username for HTTP basic authentication
        """
        if ca_file is not None:
            pulumi.set(__self__, "ca_file", ca_file)
        if cert_file is not None:
            pulumi.set(__self__, "cert_file", cert_file)
        if key_file is not None:
            pulumi.set(__self__, "key_file", key_file)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if repo is not None:
            pulumi.set(__self__, "repo", repo)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="caFile")
    def ca_file(self) -> Optional[pulumi.Input[str]]:
        """
        The Repository's CA File
        """
        return pulumi.get(self, "ca_file")

    @ca_file.setter
    def ca_file(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ca_file", value)

    @property
    @pulumi.getter(name="certFile")
    def cert_file(self) -> Optional[pulumi.Input[str]]:
        """
        The repository's cert file
        """
        return pulumi.get(self, "cert_file")

    @cert_file.setter
    def cert_file(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cert_file", value)

    @property
    @pulumi.getter(name="keyFile")
    def key_file(self) -> Optional[pulumi.Input[str]]:
        """
        The repository's cert key file
        """
        return pulumi.get(self, "key_file")

    @key_file.setter
    def key_file(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_file", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        Password for HTTP basic authentication
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def repo(self) -> Optional[pulumi.Input[str]]:
        """
        Repository where to locate the requested chart. If is a URL the chart is installed without installing the repository.
        """
        return pulumi.get(self, "repo")

    @repo.setter
    def repo(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repo", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        """
        Username for HTTP basic authentication
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)

