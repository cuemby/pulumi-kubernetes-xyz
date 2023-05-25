// Copyright 2021, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package provider

import (
	helmbase "github.com/pulumi/pulumi-go-helmbase"
	helmv3 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/helm/v3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

const (
	ChartName = "chartname"
	RepoUrl   = "https://repourl"
)

type KubernetesXyz struct {
	pulumi.ResourceState
	Status helmv3.ReleaseStatusOutput `pulumi:"status" pschema:"out"`
}

func (c *KubernetesXyz) SetOutputs(out helmv3.ReleaseStatusOutput) { c.Status = out }
func (c *KubernetesXyz) Type() string                              { return ComponentName }
func (c *KubernetesXyz) DefaultChartName() string                  { return ChartName }
func (c *KubernetesXyz) DefaultRepoURL() string                    { return RepoUrl }

// KubernetesXyzArgs contains the set of arguments for creating a KubernetesXyz component resource.
type KubernetesXyzArgs struct {
	Global      *KubernetesXyzGlobal `pulumi:"global"`
	InstallCRDs *bool                `pulumi:"installCRDs"`
	// HelmOptions is an escape hatch that lets the end user control any aspect of the
	// Helm deployment. This exposes the entirety of the underlying Helm KubernetesXyz component args.
	HelmOptions *helmbase.ReleaseType `pulumi:"helmOptions" pschema:"ref=#/types/pulumi-xyz:index:Release" json:"-"`
}

func (args *KubernetesXyzArgs) R() **helmbase.ReleaseType { return &args.HelmOptions }

type KubernetesXyzGlobal struct{}
