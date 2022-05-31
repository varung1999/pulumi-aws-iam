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
    /// The different policies to attach to the role.
    /// </summary>
    public sealed class EKSRolePoliciesArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Amazon Managed Service for Prometheus IAM policy.
        /// </summary>
        [Input("amazonManagedServicePrometheus")]
        public Input<Inputs.EKSAmazonManagedServicePrometheusPolicyArgs>? AmazonManagedServicePrometheus { get; set; }

        /// <summary>
        /// The Appmesh policies.
        /// </summary>
        [Input("appmesh")]
        public Input<Inputs.EKSAppmeshPolicyArgs>? Appmesh { get; set; }

        /// <summary>
        /// The Cert Manager IAM policy.
        /// </summary>
        [Input("certManager")]
        public Input<Inputs.EKSCertManagerPolicyArgs>? CertManager { get; set; }

        /// <summary>
        /// The Cluster Autoscaler IAM policy.
        /// </summary>
        [Input("clusterAutoScaling")]
        public Input<Inputs.EKSClusterAutoscalerPolicyArgs>? ClusterAutoScaling { get; set; }

        /// <summary>
        /// The EBS CSI IAM policy.
        /// </summary>
        [Input("ebsCsi")]
        public Input<Inputs.EKSEBSCSIPolicyArgs>? EbsCsi { get; set; }

        /// <summary>
        /// The EFS CSI IAM policy.
        /// </summary>
        [Input("efsCsi")]
        public Input<Inputs.EKSEFSCSIPolicyArgs>? EfsCsi { get; set; }

        /// <summary>
        /// The External DNS IAM policy.
        /// </summary>
        [Input("externalDns")]
        public Input<Inputs.EKSExternalDNSPolicyArgs>? ExternalDns { get; set; }

        /// <summary>
        /// The External Secrets policy.
        /// </summary>
        [Input("externalSecrets")]
        public Input<Inputs.EKSExternalSecretsPolicyArgs>? ExternalSecrets { get; set; }

        /// <summary>
        /// The FSx for Lustre CSI Driver IAM policy.
        /// </summary>
        [Input("fsxLustreCsi")]
        public Input<Inputs.FSxLustreCSIPolicyArgs>? FsxLustreCsi { get; set; }

        /// <summary>
        /// The Karpenter Controller policy.
        /// </summary>
        [Input("karpenterController")]
        public Input<Inputs.EKSKarpenterControllerPolicyArgs>? KarpenterController { get; set; }

        /// <summary>
        /// The Load Balancer policy.
        /// </summary>
        [Input("loadBalancer")]
        public Input<Inputs.EKSLoadBalancerPolicyArgs>? LoadBalancer { get; set; }

        /// <summary>
        /// The Node Termination Handler policy to the role.
        /// </summary>
        [Input("nodeTerminationHandler")]
        public Input<Inputs.EKSNodeTerminationHandlerPolicyArgs>? NodeTerminationHandler { get; set; }

        /// <summary>
        /// The Velero IAM policy.
        /// </summary>
        [Input("velero")]
        public Input<Inputs.EKSVeleroPolicyArgs>? Velero { get; set; }

        /// <summary>
        /// The VPC CNI IAM policy to the role.
        /// </summary>
        [Input("vpnCni")]
        public Input<Inputs.EKSVPNCNIPolicyArgs>? VpnCni { get; set; }

        public EKSRolePoliciesArgs()
        {
        }
    }
}