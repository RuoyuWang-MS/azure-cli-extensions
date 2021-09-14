# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from knack.util import CLIError
from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer, record_only)

# pylint: disable=line-too-long
# pylint: disable=too-many-lines

TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


@record_only()
class CustomDomainTests(ScenarioTest):

    def test_bind_cert_to_domain(self):
        self.kwargs.update({
            'cert': 'test-cert',
            'keyVaultUri': 'https://integration-test-prod.vault.azure.net/',
            'KeyVaultCertName': 'cli-unittest',
            'domain': 'cli.asc-test.net',
            'app': 'test-app',
            'serviceName': 'cli-unittest',
            'rg': 'cli'
        })

        self.cmd('spring-cloud certificate add --name {cert} --vault-uri {keyVaultUri} --vault-certificate-name {KeyVaultCertName} -g {rg} -s {serviceName}', checks=[
            self.check('name', '{cert}')
        ])

        self.cmd('spring-cloud certificate show --name {cert} -g {rg} -s {serviceName}', checks=[
            self.check('name', '{cert}')
        ])

        result = self.cmd('spring-cloud certificate list -g {rg} -s {serviceName}').get_output_in_json()
        self.assertTrue(len(result) > 0)

        self.cmd('spring-cloud app custom-domain bind --domain-name {domain} --app {app} -g {rg} -s {serviceName}', checks=[
            self.check('name', '{domain}')
        ])

        self.cmd('spring-cloud app custom-domain show --domain-name {domain} --app {app} -g {rg} -s {serviceName}', checks=[
            self.check('name', '{domain}'),
            self.check('properties.appName', '{app}')
        ])

        result = self.cmd('spring-cloud app custom-domain list --app {app} -g {rg} -s {serviceName}').get_output_in_json()
        self.assertTrue(len(result) > 0)

        self.cmd('spring-cloud app custom-domain update --domain-name {domain} --certificate {cert} --app {app} -g {rg} -s {serviceName}', checks=[
            self.check('name', '{domain}'),
            self.check('properties.appName', '{app}'),
            self.check('properties.certName', '{cert}')
        ])

        self.cmd('spring-cloud app custom-domain unbind --domain-name {domain} --app {app} -g {rg} -s {serviceName}')
        self.cmd('spring-cloud app custom-domain show --domain-name {domain} --app {app} -g {rg} -s {serviceName}', expect_failure=True)

        self.cmd('spring-cloud certificate remove --name {cert} -g {rg} -s {serviceName}')
        self.cmd('spring-cloud certificate show --name {cert} -g {rg} -s {serviceName}', expect_failure=True)


@record_only()
class AppDeployTests(ScenarioTest):
    @ResourceGroupPreparer()
    def test_app_source_code_deploy(self):
        source_app_path = os.path.abspath(os.path.join(os.path.abspath(__file__), '../test-apps/echo-app'))
        self.kwargs.update({
            'app': 'source-code-app',
            'serviceName': self.create_random_name(prefix='source-code-deploy', length=24),
            'path': '"{}"'.format(source_app_path)
        })
        print(self.kwargs['path'])
        self.cmd('az spring-cloud create -g {rg} -n {serviceName}', checks=[
            self.check('name', '{serviceName}'),
            self.check('properties.provisioningState', 'Succeeded')
        ])
        self.cmd('az spring-cloud app create -g {rg} -n {app} -s {serviceName}', checks=[
            self.check('name', '{app}'),
            self.check('properties.provisioningState', 'Succeeded')
        ])
        self.cmd('az spring-cloud app deploy -g {rg} -n {app} -s {serviceName} --source-path {path} --verbose --debug', checks=[
            self.check('name', 'default'),
            self.check('properties.provisioningState', 'Succeeded')
        ])
