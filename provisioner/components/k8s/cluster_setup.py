#!/usr/bin/env python3

# Copyright (c) 2022 Seagate Technology LLC and/or its Affiliates

# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
# For any questions about this software or licensing, please email
# opensource@seagate.com or cortx-questions@seagate.com.

import ansible_runner
import logging

inventory_path = "/opt/halo/install_depot/cortx-halo/provisioner/components/k8s/setup_playbook/inventory.yaml"
playbook_path = "/opt/halo/install_depot/cortx-halo/provisioner/components/k8s/setup_playbook/cluster_setup_playbook.yml"

class Runner:

    @staticmethod
    def run (playbook, ini):
        rc = ansible_runner.run(playbook = playbook_path, inventory = inventory_path)
        return rc


def setup():
    try:
        return(Runner.run(playbook_path, inventory_path))
    except Exception as e:
        logging.exception(f'{e}')


if __name__ == "__main__":
    setup()
