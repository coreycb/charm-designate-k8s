#!/usr/bin/env python3
"""Designate Operator Charm.

This charm provide Designate services as part of an OpenStack deployment
"""

import logging

from ops.framework import StoredState
from ops.main import main

import ops_sunbeam.charm as sunbeam_charm

logger = logging.getLogger(__name__)


class DesignateOperatorCharm(sunbeam_charm.OSBaseOperatorAPICharm):
    """Charm the service."""

    _state = StoredState()
    service_name = "designate-api"
    wsgi_admin_script = '/usr/bin/designate-api-wsgi'
    wsgi_public_script = '/usr/bin/designate-api-wsgi'

    db_sync_cmds = [
        ['designate-manage', 'database', 'sync']
    ]

    @property
    def service_conf(self) -> str:
        """Service default configuration file."""
        return f"/etc/designate/designate.conf"

    @property
    def service_user(self) -> str:
        """Service user file and directory ownership."""
        return 'designate'

    @property
    def service_group(self) -> str:
        """Service group file and directory ownership."""
        return 'designate'

    @property
    def service_endpoints(self):
        return [
            {
                'service_name': 'designate',
                'type': 'designate',
                'description': "OpenStack Designate API",
                'internal_url': f'{self.internal_url}',
                'public_url': f'{self.public_url}',
                'admin_url': f'{self.admin_url}'}]

    @property
    def default_public_ingress_port(self):
        return 9001


if __name__ == "__main__":
    main(DesignateOperatorCharm)
