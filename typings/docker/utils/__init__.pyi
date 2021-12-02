"""This type stub file was generated by pyright."""
# pylint: disable=C,E,W,R
from __future__ import annotations

from docker.utils.build import create_archive, exclude_paths, mkbuildcontext, tar
from docker.utils.decorators import check_resource, minimum_version, update_headers
from docker.utils.utils import (
    compare_version,
    convert_filters,
    convert_port_bindings,
    convert_service_networks,
    convert_volume_binds,
    create_host_config,
    create_ipam_config,
    create_ipam_pool,
    datetime_to_timestamp,
    decode_json_header,
    format_environment,
    format_extra_hosts,
    kwargs_from_env,
    normalize_links,
    parse_bytes,
    parse_devices,
    parse_env_file,
    parse_host,
    parse_repository_tag,
    split_command,
    version_gte,
    version_lt,
)

__all__ = [
    "check_resource",
    "compare_version",
    "convert_filters",
    "convert_port_bindings",
    "convert_service_networks",
    "convert_volume_binds",
    "create_archive",
    "create_host_config",
    "create_ipam_config",
    "create_ipam_pool",
    "datetime_to_timestamp",
    "decode_json_header",
    "exclude_paths",
    "format_environment",
    "format_extra_hosts",
    "kwargs_from_env",
    "minimum_version",
    "mkbuildcontext",
    "normalize_links",
    "parse_bytes",
    "parse_devices",
    "parse_env_file",
    "parse_host",
    "parse_repository_tag",
    "split_command",
    "tar",
    "update_headers",
    "version_gte",
    "version_lt",
]
