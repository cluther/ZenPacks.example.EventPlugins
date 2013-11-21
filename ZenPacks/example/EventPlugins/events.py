# Map of collector name to datacenter name.
DATACENTER_MAP = {
    'localhost': 'datacenter1',
    'collector1-1': 'datacenter1',
    'collector1-2': 'datacenter1',
    'collector2-1': 'datacenter2',
    'collector2-2': 'datacenter2',
    }


class DatacenterPlugin(object):
    def apply(self, eventProxy, dmd):
        # Determine what collector the event came from.
        collector = getattr(eventProxy, 'monitor', 'unknown')

        # Lookup the datacenter in which that collector is deployed.
        datacenter = DATACENTER_MAP.get(collector, 'unknown')

        # Set the "datacenter" property on the event.
        eventProxy.datacenter = datacenter
