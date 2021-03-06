# Copyright 2014, 2015 OpenMarket Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ._base import Config


class VoipConfig(Config):

    def read_config(self, config):
        self.turn_uris = config.get("turn_uris", [])
        self.turn_shared_secret = config["turn_shared_secret"]
        self.turn_user_lifetime = self.parse_duration(config["turn_user_lifetime"])

    def default_config(self, config_dir_path, server_name):
        return """\
        ## Turn ##

        # The public URIs of the TURN server to give to clients
        turn_uris: []

        # The shared secret used to compute passwords for the TURN server
        turn_shared_secret: "YOUR_SHARED_SECRET"

        # How long generated TURN credentials last
        turn_user_lifetime: "1h"
        """
