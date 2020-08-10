from swapper import swappable_setting

from openwisp_notifications.base.models import (
    AbstractNotification,
    AbstractNotificationSetting,
)


class Notification(AbstractNotification):
    class Meta(AbstractNotification.Meta):
        abstract = False
        app_label = 'openwisp_notifications'
        swappable = swappable_setting('openwisp_notifications', 'Notification')


class NotificationSetting(AbstractNotificationSetting):
    class Meta(AbstractNotificationSetting.Meta):
        abstract = False
        swappable = swappable_setting('openwisp_notifications', 'NotificationSetting')
