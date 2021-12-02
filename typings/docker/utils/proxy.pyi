"""This type stub file was generated by pyright."""
# pylint: disable=C,E,W,R
from __future__ import annotations

class ProxyConfig(dict):
    @property
    def http(self): ...
    @property
    def https(self): ...
    @property
    def ftp(self): ...
    @property
    def no_proxy(self): ...
    @staticmethod
    def from_dict(config): ...
    def get_environment(self): ...
    def inject_proxy_environment(self, environment): ...
    def __str__(self) -> str: ...
