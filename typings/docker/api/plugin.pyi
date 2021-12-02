"""This type stub file was generated by pyright."""
# pylint: disable=C,E,W,R
from __future__ import annotations

from docker import utils

class PluginApiMixin:
    @utils.minimum_version("1.25")
    @utils.check_resource("name")
    def configure_plugin(self, name, options): ...
    @utils.minimum_version("1.25")
    def create_plugin(self, name, plugin_data_dir, gzip=...): ...
    @utils.minimum_version("1.25")
    def disable_plugin(self, name): ...
    @utils.minimum_version("1.25")
    def enable_plugin(self, name, timeout=...): ...
    @utils.minimum_version("1.25")
    def inspect_plugin(self, name): ...
    @utils.minimum_version("1.25")
    def pull_plugin(self, remote, privileges, name=...): ...
    @utils.minimum_version("1.25")
    def plugins(self): ...
    @utils.minimum_version("1.25")
    def plugin_privileges(self, name): ...
    @utils.minimum_version("1.25")
    @utils.check_resource("name")
    def push_plugin(self, name): ...
    @utils.minimum_version("1.25")
    @utils.check_resource("name")
    def remove_plugin(self, name, force=...): ...
    @utils.minimum_version("1.26")
    @utils.check_resource("name")
    def upgrade_plugin(self, name, remote, privileges): ...
