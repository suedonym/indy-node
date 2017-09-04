from plenum.server.notifier_plugin_manager import PluginManager, notifierPluginTriggerEvents
from stp_core.common.log import getlogger

logger = getlogger()


NOTIFIER_PLUGIN_TRIGGER_EVENTS = {
    **notifierPluginTriggerEvents,
    'node_self_upgrade_scheduled': 'NodeUpgradeScheduled',
    'node_self_upgrade_complete': 'NodeUpgradeComplete',
    'node_self_upgrade_fail': 'NodeUpgradeFail',
    'pool_upgrade_cancel': 'PoolUpgradeCancel',
}


class PluginManagerNode(PluginManager):
    __instance = None

    def __new__(cls):
        if PluginManagerNode.__instance is None:
            PluginManagerNode.__instance = object.__new__(cls)
        return PluginManagerNode.__instance

    def __init__(self):
        super().__init__()
        self.topics = NOTIFIER_PLUGIN_TRIGGER_EVENTS

    def send_node_self_upgrade_scheduled(
            self, message='Node uprgade has been scheduled'):
        return self._sendMessage(self.topics['node_upgrade_scheduled'], message)

    def send_node_self_upgrade_complete(
            self, message='Node has successfully upgraded.'):
        return self._sendMessage(self.topics['node_upgrade_complete'], message)

    def send_node_self_upgrade_fail(
            self, message='Node upgrade has failed. Please take action.'):
        return self._sendMessage(self.topics['node_upgrade_fail'], message)

    def send_pool_upgrade_cancel(
            self, message='Pool upgrade has been cancelled. Please take action.'):
        return self._sendMessage(self.topics['pool_upgrade_cancel'], message)
