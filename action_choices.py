#import json
#import cPickle as pickle
#import os
#ACTION_LIST_STORE_JSON = 'fcu_action_list.json'
#ACTION_LIST_STORE_PICKLE = 'fcu_action_list.p'

def get_ows_action_choices():
    return ["DescribeVpcEndpointServices", "CreateSnapshot", "CreateSubnet", "DeleteNetworkInterface", "ModifySnapshotAttribute", "CreateVpc", "CreateInternetGateway", "CreateVpnConnectionRoute", "ModifyInstanceKeypair", "DisassociateRouteTable", "CreateTags", "DescribeSecurityGroups", "DescribeKeyPairs", "CreateDhcpOptions", "DescribeNetworkInterfaces", "ReleaseAddress", "DescribeInstanceStatus", "DescribeReservedInstances", "StopInstances", "DescribeQuotas", "DeleteSecurityGroup", "RevokeSecurityGroupIngress", "DeleteRouteTable", "DescribeInstanceTypes", "DeleteVpnConnectionRoute", "DescribeImages", "DescribeReservedInstancesOfferings", "CreateCustomerGateway", "DisassociateAddress", "ModifyNetworkInterfaceAttribute", "DescribePrefixLists", "DescribeSnapshotExportTasks", "DescribeVpnGateways", "PurchaseReservedInstancesOffering", "StartInstances", "CopyImage", "DetachNetworkInterface", "DetachVolume", "CreateImage", "AssignPrivateIpAddresses", "DeregisterImage", "DeleteVolume", "DescribeSubnets", "DeleteVpnConnection", "DisableVgwRoutePropagation", "CreateVpnConnection", "CreateRoute", "DeleteSubnet", "ModifyInstanceAttribute", "DeleteSnapshot", "DescribeInstanceAttribute", "CreateRouteTable", "DescribeSnapshotAttribute", "AssociateAddress", "DescribeInstances", "EnableVgwRoutePropagation", "DeleteVpcPeeringConnection", "DescribeVpcPeeringConnections", "RegisterImage", "CreateVpcPeeringConnection", "DescribeVolumes", "AttachVolume", "DescribeSnapshots", "DescribeImageAttribute", "CreateNatGateway", "DescribeImageExportTasks", "DescribeVpcs", "CreateSnapshotExportTask", "ModifyVpcAttribute", "DeleteDhcpOptions", "AssociateDhcpOptions", "RunInstances", "DescribeRegions", "DeleteRoute", "AcceptVpcPeeringConnection", "DescribeDhcpOptions", "DeleteCustomerGateway", "ImportKeyPair", "AuthorizeSecurityGroupEgress", "DescribeAvailabilityZones", "GetProductTypes", "DetachVpnGateway", "DescribeSpotFleetRequestHistory", "DescribeAddresses", "DeleteVpcEndpoints", "DescribeVpnConnections", "AttachNetworkInterface", "AllocateAddress", "ReplaceRoute", "CreateNetworkInterface", "CancelExportTask", "DescribeTags", "ReplaceRouteTableAssociation", "CreateImageExportTask", "DeleteInternetGateway", "DescribeNatGateways", "GetProductType", "DeleteVpnGateway", "RevokeSecurityGroupEgress", "ModifyImageAttribute", "DescribeVpcAttribute", "UnassignPrivateIpAddresses", "DeleteKeyPair", "RejectVpcPeeringConnection", "CreateVpnGateway", "GetConsoleOutput", "AssociateRouteTable", "DescribeCustomerGateways", "CopySnapshot", "DeleteNatGateway", "AttachVpnGateway", "CreateVolume", "ModifyVpcEndpoint", "DescribeVpcEndpoints", "AttachInternetGateway", "CreateSecurityGroup", "DescribeInternetGateways", "DescribeRouteTables", "DescribeProductTypes", "GetPasswordData", "DeleteVpc", "DeleteTags", "RebootInstances", "CreateKeyPair", "DetachInternetGateway", "AuthorizeSecurityGroupIngress", "CreateVpcEndpoint", "TerminateInstances"]
#    action_list = []
#    if os.path.exists(ACTION_LIST_STORE_PICKLE):
#        with open(ACTION_LIST_STORE_PICKLE, 'r') as f:
#            action_list = pickle.load(f)
#            return action_list
#    else:
#        with open(ACTION_LIST_STORE_JSON, 'w+') as f:
#            action_list = json.load(f)
#            json.dump([action.split('=')[1] for action in action_list])
#        with open(ACTION_LIST_STORE_PICKLE, 'w+') as f:
#            pickle.dump([action.split('=')[1] for action in action_list], f)
#    return [action.split('=')[1] for action in action_list]
