// Code generated by Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package kubernetesxyz

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Automates the management and issuance of TLS certificates from various issuing sources within Kubernetes
type Xyz struct {
	pulumi.ResourceState

	// Detailed information about the status of the underlying Helm deployment.
	Status ReleaseStatusOutput `pulumi:"status"`
}

// NewXyz registers a new resource with the given unique name, arguments, and options.
func NewXyz(ctx *pulumi.Context,
	name string, args *XyzArgs, opts ...pulumi.ResourceOption) (*Xyz, error) {
	if args == nil {
		args = &XyzArgs{}
	}

	var resource Xyz
	err := ctx.RegisterRemoteComponentResource("kubernetes-xyz:index:Xyz", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

type xyzArgs struct {
	Global *XyzGlobal `pulumi:"global"`
	// HelmOptions is an escape hatch that lets the end user control any aspect of the Helm deployment. This exposes the entirety of the underlying Helm Release component args.
	HelmOptions *Release `pulumi:"helmOptions"`
	InstallCRDs *bool    `pulumi:"installCRDs"`
}

// The set of arguments for constructing a Xyz resource.
type XyzArgs struct {
	Global XyzGlobalPtrInput
	// HelmOptions is an escape hatch that lets the end user control any aspect of the Helm deployment. This exposes the entirety of the underlying Helm Release component args.
	HelmOptions ReleasePtrInput
	InstallCRDs pulumi.BoolPtrInput
}

func (XyzArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*xyzArgs)(nil)).Elem()
}

type XyzInput interface {
	pulumi.Input

	ToXyzOutput() XyzOutput
	ToXyzOutputWithContext(ctx context.Context) XyzOutput
}

func (*Xyz) ElementType() reflect.Type {
	return reflect.TypeOf((**Xyz)(nil)).Elem()
}

func (i *Xyz) ToXyzOutput() XyzOutput {
	return i.ToXyzOutputWithContext(context.Background())
}

func (i *Xyz) ToXyzOutputWithContext(ctx context.Context) XyzOutput {
	return pulumi.ToOutputWithContext(ctx, i).(XyzOutput)
}

// XyzArrayInput is an input type that accepts XyzArray and XyzArrayOutput values.
// You can construct a concrete instance of `XyzArrayInput` via:
//
//	XyzArray{ XyzArgs{...} }
type XyzArrayInput interface {
	pulumi.Input

	ToXyzArrayOutput() XyzArrayOutput
	ToXyzArrayOutputWithContext(context.Context) XyzArrayOutput
}

type XyzArray []XyzInput

func (XyzArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Xyz)(nil)).Elem()
}

func (i XyzArray) ToXyzArrayOutput() XyzArrayOutput {
	return i.ToXyzArrayOutputWithContext(context.Background())
}

func (i XyzArray) ToXyzArrayOutputWithContext(ctx context.Context) XyzArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(XyzArrayOutput)
}

// XyzMapInput is an input type that accepts XyzMap and XyzMapOutput values.
// You can construct a concrete instance of `XyzMapInput` via:
//
//	XyzMap{ "key": XyzArgs{...} }
type XyzMapInput interface {
	pulumi.Input

	ToXyzMapOutput() XyzMapOutput
	ToXyzMapOutputWithContext(context.Context) XyzMapOutput
}

type XyzMap map[string]XyzInput

func (XyzMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Xyz)(nil)).Elem()
}

func (i XyzMap) ToXyzMapOutput() XyzMapOutput {
	return i.ToXyzMapOutputWithContext(context.Background())
}

func (i XyzMap) ToXyzMapOutputWithContext(ctx context.Context) XyzMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(XyzMapOutput)
}

type XyzOutput struct{ *pulumi.OutputState }

func (XyzOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Xyz)(nil)).Elem()
}

func (o XyzOutput) ToXyzOutput() XyzOutput {
	return o
}

func (o XyzOutput) ToXyzOutputWithContext(ctx context.Context) XyzOutput {
	return o
}

// Detailed information about the status of the underlying Helm deployment.
func (o XyzOutput) Status() ReleaseStatusOutput {
	return o.ApplyT(func(v *Xyz) ReleaseStatusOutput { return v.Status }).(ReleaseStatusOutput)
}

type XyzArrayOutput struct{ *pulumi.OutputState }

func (XyzArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Xyz)(nil)).Elem()
}

func (o XyzArrayOutput) ToXyzArrayOutput() XyzArrayOutput {
	return o
}

func (o XyzArrayOutput) ToXyzArrayOutputWithContext(ctx context.Context) XyzArrayOutput {
	return o
}

func (o XyzArrayOutput) Index(i pulumi.IntInput) XyzOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Xyz {
		return vs[0].([]*Xyz)[vs[1].(int)]
	}).(XyzOutput)
}

type XyzMapOutput struct{ *pulumi.OutputState }

func (XyzMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Xyz)(nil)).Elem()
}

func (o XyzMapOutput) ToXyzMapOutput() XyzMapOutput {
	return o
}

func (o XyzMapOutput) ToXyzMapOutputWithContext(ctx context.Context) XyzMapOutput {
	return o
}

func (o XyzMapOutput) MapIndex(k pulumi.StringInput) XyzOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Xyz {
		return vs[0].(map[string]*Xyz)[vs[1].(string)]
	}).(XyzOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*XyzInput)(nil)).Elem(), &Xyz{})
	pulumi.RegisterInputType(reflect.TypeOf((*XyzArrayInput)(nil)).Elem(), XyzArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*XyzMapInput)(nil)).Elem(), XyzMap{})
	pulumi.RegisterOutputType(XyzOutput{})
	pulumi.RegisterOutputType(XyzArrayOutput{})
	pulumi.RegisterOutputType(XyzMapOutput{})
}