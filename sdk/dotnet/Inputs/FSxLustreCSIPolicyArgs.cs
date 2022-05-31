// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsIam.Inputs
{

    /// <summary>
    /// The FSx for Lustre CSI Driver IAM policy to the role.
    /// </summary>
    public sealed class FSxLustreCSIPolicyArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Determines whether to attach the FSx for Lustre CSI Driver IAM policy to the role.
        /// </summary>
        [Input("attach", required: true)]
        public Input<bool> Attach { get; set; } = null!;

        [Input("serviceRoleArns")]
        private InputList<string>? _serviceRoleArns;

        /// <summary>
        /// Service role ARNs to allow FSx for Lustre CSI create and manage FSX for Lustre service linked roles. If not provided,
        /// the default ARN "arn:aws:iam::*:role/aws-service-role/s3.data-source.lustre.fsx.amazonaws.com/*" will be applied.
        /// </summary>
        public InputList<string> ServiceRoleArns
        {
            get => _serviceRoleArns ?? (_serviceRoleArns = new InputList<string>());
            set => _serviceRoleArns = value;
        }

        public FSxLustreCSIPolicyArgs()
        {
        }
    }
}