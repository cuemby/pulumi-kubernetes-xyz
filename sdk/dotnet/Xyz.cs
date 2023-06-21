// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Cuemby.Xyz
{
    /// <summary>
    /// Automates the management and issuance of TLS certificates from various issuing sources within Kubernetes
    /// </summary>
    [XyzResourceType("kubernetes-xyz:index:Xyz")]
    public partial class Xyz : global::Pulumi.ComponentResource
    {
        /// <summary>
        /// Detailed information about the status of the underlying Helm deployment.
        /// </summary>
        [Output("status")]
        public Output<Outputs.ReleaseStatus> Status { get; private set; } = null!;


        /// <summary>
        /// Create a Xyz resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Xyz(string name, XyzArgs? args = null, ComponentResourceOptions? options = null)
            : base("kubernetes-xyz:index:Xyz", name, args ?? new XyzArgs(), MakeResourceOptions(options, ""), remote: true)
        {
        }

        private static ComponentResourceOptions MakeResourceOptions(ComponentResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new ComponentResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = ComponentResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
    }

    public sealed class XyzArgs : global::Pulumi.ResourceArgs
    {
        [Input("global")]
        public Input<Inputs.XyzGlobalArgs>? Global { get; set; }

        /// <summary>
        /// HelmOptions is an escape hatch that lets the end user control any aspect of the Helm deployment. This exposes the entirety of the underlying Helm Release component args.
        /// </summary>
        [Input("helmOptions")]
        public Input<Inputs.ReleaseArgs>? HelmOptions { get; set; }

        [Input("installCRDs")]
        public Input<bool>? InstallCRDs { get; set; }

        public XyzArgs()
        {
        }
        public static new XyzArgs Empty => new XyzArgs();
    }
}