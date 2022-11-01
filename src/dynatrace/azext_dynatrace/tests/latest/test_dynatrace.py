# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

import unittest
from azure.cli.testsdk import *
from .credential_replacer import ExpressRoutePortLOAContentReplacer


class DynatraceScenario(ScenarioTest):

    def __init__(self, method_name):
        super().__init__(method_name, recording_processors=[
            ExpressRoutePortLOAContentReplacer()
        ])

    @ResourceGroupPreparer(name_prefix='cli_test_dynatrace_monitor', location='eastus2euap')
    def test_dynatrace_monitor(self, resource_group):
        self.kwargs.update({
            'monitor': self.create_random_name('monitor', 15),
        })

        self.cmd('dynatrace monitor create -g {rg} -n {monitor} --user-info {{first-name:Alice,last-name:Bobab,email-address:agarwald@microsoft.com,phone-number:1234567890,country:US}} --plan-data {{usage-type:committed,billing-cycle:Monthly,plan-details:azureportalintegration_privatepreview@TIDhjdtn7tfnxcy,effective-date:2022-08-20}} --environment {{single-sign-on:{{aad-domains:[\'abc\']}}}}')
        self.cmd('dynatrace monitor show -g {rg} -n {monitor}', checks=[
            self.check('name', '{monitor}'),
            self.check('resourceGroup', '{rg}'),
            self.check('dynatraceEnvironmentProperties.singleSignOnProperties.aadDomains[0]', 'abc'),
            self.check('dynatraceEnvironmentProperties.singleSignOnProperties.provisioningState', 'Accepted'),
            self.check('dynatraceEnvironmentProperties.singleSignOnProperties.singleSignOnState', 'Initial'),
            self.check('marketplaceSubscriptionStatus', 'Active'),
            self.check('monitoringStatus', 'Enabled'),
            self.check('planData.billingCycle', 'Monthly'),
            self.check('planData.planDetails', 'azureportalintegration_privatepreview@TIDhjdtn7tfnxcy'),
            self.check('planData.usageType', 'committed'),
            self.check('userInfo.country', 'US'),
            self.check('userInfo.emailAddress', 'agarwald@microsoft.com'),
            self.check('userInfo.firstName', 'Alice'),
            self.check('userInfo.lastName', 'Bobab'),
            self.check('userInfo.phoneNumber', '1234567890')
        ])
        self.cmd('dynatrace monitor update -g {rg} -n {monitor} --tags {{env:dev}}', checks=[
            self.check('name', '{monitor}'),
            self.check('resourceGroup', '{rg}'),
            self.check('tags', {'env': 'dev'})
        ])
        self.cmd('dynatrace monitor list -g {rg}', checks=[
            self.check('[0].name', '{monitor}'),
            self.check('[0].resourceGroup', '{rg}'),
            self.check('[0].dynatraceEnvironmentProperties.singleSignOnProperties.aadDomains[0]', 'abc'),
            self.check('[0].dynatraceEnvironmentProperties.singleSignOnProperties.provisioningState', 'Accepted'),
            self.check('[0].dynatraceEnvironmentProperties.singleSignOnProperties.singleSignOnState', 'Initial'),
            self.check('[0].marketplaceSubscriptionStatus', 'Active'),
            self.check('[0].monitoringStatus', 'Enabled'),
            self.check('[0].planData.billingCycle', 'Monthly'),
            self.check('[0].planData.planDetails', 'azureportalintegration_privatepreview@TIDhjdtn7tfnxcy'),
            self.check('[0].planData.usageType', 'committed'),
            self.check('[0].userInfo.country', 'US'),
            self.check('[0].userInfo.emailAddress', 'agarwald@microsoft.com'),
            self.check('[0].userInfo.firstName', 'Alice'),
            self.check('[0].userInfo.lastName', 'Bobab'),
            self.check('[0].userInfo.phoneNumber', '1234567890'),
        ])
        self.cmd('dynatrace monitor list-app-service -g {rg} --monitor-name {monitor}')
        self.cmd('dynatrace monitor list-host -g {rg} --monitor-name {monitor}')
        self.cmd('dynatrace monitor list-monitored-resource -g {rg} --monitor-name {monitor}')
        self.cmd('dynatrace monitor list-linkable-environment -g {rg} --monitor-name {monitor} --user-principal agarwald@microsoft.com --region eastus2euap --tenant-id be9927fa-821c-4178-9dae-e520c4beca74')
        self.cmd('dynatrace monitor get-sso-detail -g {rg} --monitor-name {monitor} --user-principal agarwald@microsoft.com', checks=[
            self.check('adminUsers[0]', 'agarwald@microsoft.com')
        ])
        self.cmd('dynatrace monitor get-vm-host-payload -g {rg} --monitor-name {monitor}', checks=[
            self.exists('environmentId'),
            self.exists('ingestionKey')
        ])
        self.cmd('dynatrace monitor delete -n {monitor} -g {rg} -y')

    @ResourceGroupPreparer(name_prefix='cli_test_dynatrace_monitor_single_sign_on_configurations', location='eastus2euap')
    def test_dynatrace_monitor_single_sign_on_configurations(self, resource_group):
        self.kwargs.update({
            'monitor': self.create_random_name('monitor', 15),
        })
        self.cmd('dynatrace monitor create -g {rg} -n {monitor} --user-info {{first-name:Alice,last-name:Bobab,email-address:agarwald@microsoft.com,phone-number:1234567890,country:US}} --plan-data {{usage-type:committed,billing-cycle:Monthly,plan-details:azureportalintegration_privatepreview@TIDhjdtn7tfnxcy,effective-date:2022-08-20}} --environment {{single-sign-on:{{aad-domains:[\'abc\']}}}}')
        self.cmd('dynatrace monitor sso-config create -g {rg} --monitor-name {monitor} -n default --aad-domains [\'mpliftrdt20210811outlook.onmicrosoft.com\'] --single-sign-on-url "https://www.dynatrace.io"', checks=[
            self.check('aadDomains[0]', 'mpliftrdt20210811outlook.onmicrosoft.com'),
            self.check('singleSignOnUrl', 'https://www.dynatrace.io')
        ])
        self.cmd('dynatrace monitor sso-config show -g {rg} --monitor-name {monitor} -n default', checks=[
            self.check('aadDomains[0]', 'mpliftrdt20210811outlook.onmicrosoft.com'),
            self.check('singleSignOnUrl', 'https://www.dynatrace.io')
        ])
        self.cmd('dynatrace monitor sso-config list -g {rg} --monitor-name {monitor}', checks=[
            self.check('[0].aadDomains[0]', 'mpliftrdt20210811outlook.onmicrosoft.com'),
            self.check('[0].singleSignOnUrl', 'https://www.dynatrace.io')
        ])

    @ResourceGroupPreparer(name_prefix='cli_test_dynatrace_monitor_tag_rule', location='eastus2euap')
    def test_dynatrace_monitor_tag_rule(self, resource_group):
        self.kwargs.update({
            'monitor': self.create_random_name('monitor', 15),
        })

        self.cmd('dynatrace monitor create -g {rg} -n {monitor} --user-info {{first-name:Alice,last-name:Bobab,email-address:agarwald@microsoft.com,phone-number:1234567890,country:US}} --plan-data {{usage-type:committed,billing-cycle:Monthly,plan-details:azureportalintegration_privatepreview@TIDhjdtn7tfnxcy,effective-date:2022-08-20}} --environment {{single-sign-on:{{aad-domains:[\'abc\']}}}} ')
        self.cmd('dynatrace monitor tag-rule create -g {rg} --monitor-name {monitor} -n default --log-rules {{send-aad-logs:enabled,send-subscription-logs:enabled,send-activity-logs:enabled,filtering-tags:[{{name:env,value:prod,action:include}},{{name:env,value:dev,action:exclude}}]}} --metric-rules {{filtering-tags:[{{name:env,value:prod,action:include}}]}}', checks=[
            self.check('name', 'default'),
            self.check('resourceGroup', '{rg}'),
            self.check('logRules.filteringTags[0].action', 'Include'),
            self.check('logRules.filteringTags[0].name', 'env'),
            self.check('logRules.filteringTags[0].value', 'prod'),
            self.check('logRules.filteringTags[1].action', 'Exclude'),
            self.check('logRules.filteringTags[1].name', 'env'),
            self.check('logRules.filteringTags[1].value', 'dev'),
            self.check('logRules.sendAadLogs', 'Enabled'),
            self.check('logRules.sendActivityLogs', 'Enabled'),
            self.check('logRules.sendSubscriptionLogs', 'Enabled'),
            self.check('metricRules.filteringTags[0].action', 'Include'),
            self.check('metricRules.filteringTags[0].name', 'env'),
            self.check('metricRules.filteringTags[0].value', 'prod')
        ])
        self.cmd('dynatrace monitor tag-rule update -g {rg} --monitor-name {monitor} -n default', checks=[
            self.check('name', 'default'),
            self.check('resourceGroup', '{rg}'),
            self.check('logRules.filteringTags[0].action', 'Include'),
            self.check('logRules.filteringTags[0].name', 'env'),
            self.check('logRules.filteringTags[0].value', 'prod'),
            self.check('logRules.filteringTags[1].action', 'Exclude'),
            self.check('logRules.filteringTags[1].name', 'env'),
            self.check('logRules.filteringTags[1].value', 'dev'),
            self.check('logRules.sendAadLogs', 'Enabled'),
            self.check('logRules.sendActivityLogs', 'Enabled'),
            self.check('logRules.sendSubscriptionLogs', 'Enabled'),
            self.check('metricRules.filteringTags[0].action', 'Include'),
            self.check('metricRules.filteringTags[0].name', 'env'),
            self.check('metricRules.filteringTags[0].value', 'prod')
        ])
        self.cmd('dynatrace monitor tag-rule show -g {rg} --monitor-name {monitor} -n default', checks=[
            self.check('name', 'default'),
            self.check('resourceGroup', '{rg}'),
            self.check('logRules.filteringTags[0].action', 'Include'),
            self.check('logRules.filteringTags[0].name', 'env'),
            self.check('logRules.filteringTags[0].value', 'prod'),
            self.check('logRules.filteringTags[1].action', 'Exclude'),
            self.check('logRules.filteringTags[1].name', 'env'),
            self.check('logRules.filteringTags[1].value', 'dev'),
            self.check('logRules.sendAadLogs', 'Enabled'),
            self.check('logRules.sendActivityLogs', 'Enabled'),
            self.check('logRules.sendSubscriptionLogs', 'Enabled'),
            self.check('metricRules.filteringTags[0].action', 'Include'),
            self.check('metricRules.filteringTags[0].name', 'env'),
            self.check('metricRules.filteringTags[0].value', 'prod')
        ])
        self.cmd('dynatrace monitor tag-rule list -g {rg} --monitor-name {monitor}', checks=[
            self.check('[0].name', 'default'),
            self.check('[0].resourceGroup', '{rg}'),
            self.check('[0].logRules.filteringTags[0].action', 'Include'),
            self.check('[0].logRules.filteringTags[0].name', 'env'),
            self.check('[0].logRules.filteringTags[0].value', 'prod'),
            self.check('[0].logRules.filteringTags[1].action', 'Exclude'),
            self.check('[0].logRules.filteringTags[1].name', 'env'),
            self.check('[0].logRules.filteringTags[1].value', 'dev'),
            self.check('[0].logRules.sendAadLogs', 'Enabled'),
            self.check('[0].logRules.sendActivityLogs', 'Enabled'),
            self.check('[0].logRules.sendSubscriptionLogs', 'Enabled'),
            self.check('[0].metricRules.filteringTags[0].action', 'Include'),
            self.check('[0].metricRules.filteringTags[0].name', 'env'),
            self.check('[0].metricRules.filteringTags[0].value', 'prod')
        ])
        self.cmd('dynatrace monitor tag-rule delete -g {rg} --monitor-name {monitor} -n default -y')