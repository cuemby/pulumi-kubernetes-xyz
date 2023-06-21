package main

import (
	"fmt"
	xyz "github.com/cuemby/pulumi-kubernetes-xyz/sdk/go/kubernetes-xyz"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		name := fmt.Sprintf("%s-%s", ctx.Project(), ctx.Stack())

		_, err := xyz.NewXyz(ctx, name, &xyz.XyzArgs{
			HelmOptions: &xyz.ReleaseArgs{},
		})
		if err != nil {
			return err
		}

		return nil
	})
}
