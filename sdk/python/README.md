# Pulumi Kubernetes Xyz Component

This repo contains the Pulumi Kubernetes Xyz component for Kubernetes. BRIEF DESCRIPTION OF THE 
ADDON.

This component wraps [Kubernetes Xyz Helm Chart](https://url),
and offers a Pulumi-friendly and strongly-typed way to manage Kubernetes Xyz installations.

For examples of usage, see [the official documentation](https://url),
or refer to [the examples](/examples) in this repo.

## To Use

To use this component, first install the Pulumi Package:

Afterwards, import the library and instantiate it within your Pulumi program:

## Configuration

This component supports all of the configuration options of the [official Helm chart](
https://url_to_the_values.yaml), except that these are strongly typed so you will get IDE support and static error checking.

The Helm deployment uses reasonable defaults, including the chart name and repo URL, however,
if you need to override them, you may do so using the `helmOptions` parameter. Refer to
[the API docs for the `kubernetes:helm/v3:Release` Pulumi type](
https://www.pulumi.com/docs/reference/pkg/kubernetes/helm/v3/release/#inputs) for a full set of choices.

For complete details, refer to the Pulumi Package details within the Pulumi Registry.