# Copyright 2015 Maxime Terras <maxime.terras@numergy.com>
# Copyright 2015 Pierre Padrixe <pierre.padrixe@gmail.com>
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


from vsd_license import *
from vsd_enterprise import *
from vsd_domain import *
from vsd_subnet import *
from vsd_user import *
from vsd_gateway import *
from vsd_vsp import *
from vsd_vm import *
from vsd_vport import *
from vsd_policy import *
from vsd_dhcp import *
from vsd_metadata import *
from vsd_route import *


def main():
    vsdcli(obj={})

if __name__ == '__main__':
    main()
