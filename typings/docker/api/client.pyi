"""This type stub file was generated by pyright."""
# pylint: disable=C,E,W,R
from __future__ import annotations

import requests
from docker.api.build import BuildApiMixin
from docker.api.config import ConfigApiMixin
from docker.api.container import ContainerApiMixin
from docker.api.daemon import DaemonApiMixin
from docker.api.exec_api import ExecApiMixin
from docker.api.image import ImageApiMixin
from docker.api.network import NetworkApiMixin
from docker.api.plugin import PluginApiMixin
from docker.api.secret import SecretApiMixin
from docker.api.service import ServiceApiMixin
from docker.api.swarm import SwarmApiMixin
from docker.api.volume import VolumeApiMixin

class APIClient(
    requests.Session,
    BuildApiMixin,
    ConfigApiMixin,
    ContainerApiMixin,
    DaemonApiMixin,
    ExecApiMixin,
    ImageApiMixin,
    NetworkApiMixin,
    PluginApiMixin,
    SecretApiMixin,
    ServiceApiMixin,
    SwarmApiMixin,
    VolumeApiMixin,
):
    __attrs__ = ...
    def __init__(
        self,
        base_url=...,
        version=...,
        timeout=...,
        tls=...,
        user_agent=...,
        num_pools=...,
        credstore_env=...,
        use_ssh_client=...,
        max_pool_size=...,
    ) -> None: ...
    def get_adapter(self, url): ...
    @property
    def api_version(self): ...
    def reload_config(self, dockercfg_path=...): ...
