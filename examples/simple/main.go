package main

import (
	xyz "github.com/cuemby/pulumi-kubernetes-xyz/sdk/go/kubernetes-xyz"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		_, err := xyz.NewKubernetesXyz(ctx, "simple", &xyz.KubernetesXyzArgs{
			HelmOptions: &xyz.ReleaseArgs{},
			InstallCRDs: pulumi.Bool(true),
		})
		if err != nil {
			return err
		}

		return nil
	})
}
