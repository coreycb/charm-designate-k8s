<!--
Avoid using this README file for information that is maintained or published elsewhere, e.g.:

* metadata.yaml > published on Charmhub
* documentation > published on (or linked to from) Charmhub
* detailed contribution guide > documentation or CONTRIBUTING.md

Use links instead.
-->

# designate-k8s

Charmhub package name: operator-template
More information: https://charmhub.io/designate-k8s

Describe your charm in one or two sentences.

juju deploy ./designate-k8s_ubuntu-22.04-amd64.charm --resource designate-api-image=kolla/ubuntu-binary-designate-api:yoga designate
juju relate designate mysql
juju relate designate keystone
juju relate designate rabbitmq
juju relate designate:ingress-internal traefik:ingress
juju relate designate:ingress-public traefik:ingress

## Other resources

<!-- If your charm is documented somewhere else other than Charmhub, provide a link separately. -->

- [Read more](https://example.com)

- [Contributing](CONTRIBUTING.md) <!-- or link to other contribution documentation -->

- See the [Juju SDK documentation](https://juju.is/docs/sdk) for more information about developing and improving charms.
