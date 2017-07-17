'''
    Variable for filters that can cause some problems
'''

filterString = {}


# android.provider.Telephony
filterString['android.provider.Telephony.SMS_RECEIVED'] = "\t[+] Want to get if you have a new SMS_RECEIVED"
filterString['android.provider.Telephony.SMS_DELIVER'] = "\t[+] Have you SMS_DELIVER? The app knows the app knows it too"
filterString['android.provider.Telephony.SIM_FULL'] = "\t[+] Trump and this app know that your SIM_FULL"


# android.intent.action
filterString['android.intent.action.ANSWER'] = "\t[+] This APP can handle your incoming calls with ANSWER"
filterString['android.intent.action.ALL_APPS'] = "\t[+] Can list ALL_APPS, for example AV engines =)"
filterString['android.intent.action.BOOT_COMPLETED'] = "\t[+] When BOOT_COMPLETED this app can start"
filterString['android.intent.action.PHONE_STATE'] = "\t[+] This APP check PHONE_STATE, maybe when receive Calls...?"
filterString['android.intent.action.SCREEN_OFF'] = "\t[+] This APP knows when SCREEN_OFF"
filterString['android.intent.action.SCREEN_ON'] = "\t[+] This APP knows when SCREEN_ON"
filterString['android.intent.action.USER_PRESENT'] = "\t[+] USER_PRESENT... Interesting to knows when you are there"
filterString['android.intent.action.TIME_TICK'] = "\t[+] Frenetic TIME_TICK,tock,Frenetic tick,tick,tock..."
filterString['android.intent.action.TIMEZONE_CHANGED'] = "\t[+] When TIMEZONE_CHANGED you know¿?"
filterString['android.intent.action.PACKAGE_INSTALL'] = "\t[+] This will remember app when you PACKAGE_INSTALL"
filterString['android.intent.action.PACKAGE_ADDED'] = "\t[+] When PACKAGE_ADDED app can knows it"
filterString['android.intent.action.PACKAGE_REPLACED'] = "\t[+] Look if it's antivirus or malware,it knows PACKAGE_REPLACED"
filterString['android.intent.action.MY_PACKAGE_REPLACED'] = "\t[+] okay MY_PACKAGE_REPLACED... I don't know what it is"
filterString['android.intent.action.PACKAGE_REMOVED'] = "\t[+] PACKAGE_REMOVED why the h... needs to know this?"
filterString['android.intent.action.PACKAGE_FULLY_REMOVED'] = "\t[+] PACKAGE_FULLY_REMOVED intent-filter is present"
filterString['android.intent.action.PACKAGE_CHANGED'] = "\t[+] PACKAGE_RESTARTED intent-filter is present"
filterString['android.intent.action.PACKAGE_RESTARTED'] = "\t[+] PACKAGE_RESTARTED intent-filter is present"
filterString['android.intent.action.PACKAGE_DATA_CLEARED'] = "\t[+] PACKAGE_DATA_CLEARED intent-filter is present"
filterString['android.intent.action.PACKAGE_FIRST_LAUNCH'] = "\t[+] It looks that It will know when PACKAGE_FIRST_LAUNCH"
filterString['android.intent.action.PACKAGE_NEEDS_VERIFICATION'] = "\t[+] PACKAGE_NEEDS_VERIFICATION intent-filter is present"
filterString['android.intent.action.PACKAGE_VERIFIED'] = "\t[+] PACKAGE_VERIFIED intent-filter is present"
filterString['android.intent.action.UID_REMOVED'] = "\t[+] UID_REMOVED intent-filter is present"
filterString['android.intent.action.QUERY_PACKAGE_RESTART'] = "\t[+] QUERY_PACKAGE_RESTART intent-filter is present"
filterString['android.intent.action.CONFIGURATION_CHANGED'] = "\t[+] CONFIGURATION_CHANGED intent-filter is present"
filterString['android.intent.action.LOCALE_CHANGED'] = "\t[+] LOCALE_CHANGED intent-filter is present"
filterString['android.intent.action.BATTERY_CHANGED'] = "\t[+] This APP knows when BATTERY_CHANGED"
filterString['android.intent.action.BATTERY_LOW'] = "\t[+] This APP could acts different when BATTERY_LOW"
filterString['android.intent.action.BATTERY_OKAY'] = "\t[+] Interesing, this APP knows when BATTERY_OKAY"
filterString['android.intent.action.ACTION_POWER_CONNECTED'] = "\t[+] This APP will know when ACTION_POWER_CONNECTED"
filterString['android.intent.action.ACTION_POWER_DISCONNECTED'] = "\t[+] This APP knows when ACTION_POWER_DISCONNECTED"
filterString['android.intent.action.ACTION_SHUTDOWN'] = "\t[+] ACTION_SHUTDOWN intent-filter is present"
filterString['android.intent.action.DEVICE_STORAGE_LOW'] = "\t[+] APP knows if DEVICE_STORAGE_LOW"
filterString['android.intent.action.DEVICE_STORAGE_OK'] = "\t[+] APP knows if DEVICE_STORAGE_OK"
filterString['android.intent.action.DEVICE_STORAGE_FULL'] = "\t[+] APP knows if DEVICE_STORAGE_FULL"
filterString['android.intent.action.DEVICE_STORAGE_NOT_FULL'] = "\t[+] APP knows if DEVICE_STORAGE_NOT_FULL"
filterString['android.intent.action.NEW_OUTGOING_CALL'] = "\t[+] APP knows when you have a NEW_OUTGOING_CALL"
filterString['android.intent.action.REBOOT'] = "\t[+] APP knows when you REBOOT"
filterString['android.intent.action.DOCK_EVENT'] = "\t[+] DOCK_EVENT intent-filter is present"
filterString['android.intent.action.MASTER_CLEAR_NOTIFICATION'] = "\t[+] MASTER_CLEAR_NOTIFICATION intent-filter is present"
filterString['android.intent.action.USER_ADDED'] = "\t[+] APP knows when USER_ADDED"
filterString['android.intent.action.USER_REMOVED'] = "\t[+] APP knows when USER_REMOVED"
filterString['android.intent.action.USER_STOPPED'] = "\t[+] APP knows when USER_STOPPED"
filterString['android.intent.action.USER_BACKGROUND'] = "\t[+] APP knows when USER_BACKGROUND"
filterString['android.intent.action.USER_FOREGROUND'] = "\t[+] APP knows when USER_FOREGROUND"
filterString['android.intent.action.USER_SWITCHED'] = "\t[+] APP knows when USER_SWITCHED"
filterString['android.intent.action.HEADSET_PLUG'] = "\t[+] APP knows when HEADSET_PLUG"
filterString['android.intent.action.ANALOG_AUDIO_DOCK_PLUG'] = "\t[+] APP knows when ANALOG_AUDIO_DOCK_PLUG"
filterString['android.intent.action.HDMI_AUDIO_PLUG'] = "\t[+] APP knows when HDMI_AUDIO_PLUG"
filterString['android.intent.action.USB_AUDIO_ACCESSORY_PLUG'] = "\t[+] APP knows when USB_AUDIO_ACCESSORY_PLUG"
filterString['android.intent.action.USB_AUDIO_DEVICE_PLUG'] = "\t[+] APP knows when USB_AUDIO_DEVICE_PLUG"
filterString['android.intent.action.CLEAR_DNS_CACHE'] = "\t[+] CLEAR_DNS_CACHE intent-filter is present"
filterString['android.intent.action.PROXY_CHANGE'] = "\t[+] PROXY_CHANGE intent-filter is present"
filterString['android.intent.action.DREAMING_STARTED'] = "\t[+] DREAMING_STARTED intent-filter is present"
filterString['android.intent.action.DREAMING_STOPPED'] = "\t[+] DREAMING_STOPPED intent-filter is present"
filterString['android.intent.action.ANY_DATA_STATE'] = "\t[+] ANY_DATA_STATE intent-filter is present"

# android.os
filterString['android.os.UpdateLock.UPDATE_LOCK_CHANGED'] = "\t[+] UPDATE_LOCK_CHANGED intent-filter is present"

# android.server
filterString['com.android.server.WifiManager.action.START_SCAN'] = "\t[+] START_SCAN intent-filter is present"
filterString['com.android.server.WifiManager.action.DELAYED_DRIVER_STOP'] = "\t[+] DELAYED_DRIVER_STOP intent-filter is present"


# android.app.action 
filterString['android.app.action.ENTER_CAR_MODE'] = "\t[+] ENTER_CAR_MODE intent-filter is present"
filterString['android.app.action.EXIT_CAR_MODE'] = "\t[+] EXIT_CAR_MODE intent-filter is present"
filterString['android.app.action.ENTER_DESK_MODE'] = "\t[+] ENTER_DESK_MODE intent-filter is present"
filterString['android.app.action.EXIT_DESK_MODE'] = "\t[+] EXIT_DESK_MODE intent-filter is present"

# android.net.conn
filterString['android.net.conn.CONNECTIVITY_CHANGE'] ='\t[+] This APP can knows when CONNECTIVITY_CHANGE'
filterString['android.net.conn.CONNECTIVITY_CHANGE_IMMEDIATE'] ='\t[+] This APP can knows when CONNECTIVITY_CHANGE_IMMEDIATE'
filterString['android.net.conn.DATA_ACTIVITY_CHANGE'] ='\t[+] This APP can knows when DATA_ACTIVITY_CHANGE'
filterString['android.net.conn.BACKGROUND_DATA_SETTING_CHANGED'] ='\t[+] This APP can knows when BACKGROUND_DATA_SETTING_CHANGED'
filterString['android.net.conn.CAPTIVE_PORTAL_TEST_COMPLETED'] ='\t[+] This APP can knows when CAPTIVE_PORTAL_TEST_COMPLETED'
filterString['android.net.wifi.WIFI_STATE_CHANGED'] ='\t[+] This APP can knows when WIFI_STATE_CHANGED'
filterString['android.net.wifi.WIFI_AP_STATE_CHANGED'] ='\t[+] This APP can knows when WIFI_AP_STATE_CHANGED'
filterString['android.net.wifi.WIFI_SCAN_AVAILABLE'] ='\t[+] This APP can knows when WIFI_SCAN_AVAILABLE'
filterString['android.net.wifi.SCAN_RESULTS'] ='\t[+] SCAN_RESULTS wifi intent-filter is present'
filterString['android.net.wifi.RSSI_CHANGED'] ='\t[+] RSSI_CHANGED wifi intent-filter is present'
filterString['android.net.wifi.STATE_CHANGE'] ='\t[+] STATE_CHANGE wifi intent-filter is present'
filterString['android.net.wifi.SCAN_RESULTS'] ='\t[+] CAN_RESULTS wifi intent-filter is present'
filterString['android.net.wifi.LINK_CONFIGURATION_CHANGED'] ='\t[+] LINK_CONFIGURATION_CHANGED wifi intent-filter is present'
filterString['android.net.wifi.CONFIGURED_NETWORKS_CHANGE'] ='\t[+] CONFIGURED_NETWORKS_CHANGE wifi intent-filter is present'
filterString['android.net.wifi.supplicant.CONNECTION_CHANGE'] ='\t[+] CONNECTION_CHANGE wifi intent-filter is present'
filterString['android.net.wifi.supplicant.STATE_CHANGE'] = '\t[+] STATE_CHANGE wifi supplicant intent-filter is present'
filterString['android.net.wifi.p2p.STATE_CHANGED'] = '\t[+] STATE_CHANGED wifi p2p intent-filter is present'

# android.nfc 
filterString['android.nfc.action.LLCP_LINK_STATE_CHANGED'] = '\t[+] LLCP_LINK_STATE_CHANGED intent-filter is present'
filterString['com.android.nfc_extras.action.RF_FIELD_ON_DETECTED'] = '\t[+] RF_FIELD_ON_DETECTED intent-filter is present'
filterString['com.android.nfc_extras.action.RF_FIELD_OFF_DETECTED'] = '\t[+] RF_FIELD_OFF_DETECTED intent-filter is present'
filterString['com.android.nfc_extras.action.AID_SELECTED'] = '\t[+] AID_SELECTED intent-filter is present'
filterString['android.nfc.action.TRANSACTION_DETECTED'] = '\t[+] TRANSACTION_DETECTED intent-filter is present'



# android.appwidget.action
filterString['android.appwidget.action.APPWIDGET_UPDATE_OPTIONS'] = "\t[+] APPWIDGET_UPDATE_OPTIONS intent-filter is present"
filterString['android.appwidget.action.APPWIDGET_DELETED'] = "\t[+] APPWIDGET_DELETED intent-filter is present"
filterString['android.appwidget.action.APPWIDGET_DISABLED'] = "\t[+] APPWIDGET_DISABLED intent-filter is present"
filterString['android.appwidget.action.APPWIDGET_ENABLED'] = "\t[+] APPWIDGET_ENABLED intent-filter is present"

# android.backup.intent 
filterString['android.backup.intent.RUN'] = "\t[+] RUN backup intent-filter is present"
filterString['android.backup.intent.CLEAR'] = "\t[+] CLEAR backup intent-filter is present"
filterString['android.backup.intent.INIT'] = "\t[+] INIT backup intent-filter is present"

# android.bluetooth.adapter.action
filterString['android.bluetooth.adapter.action.STATE_CHANGED'] = "\t[+] STATE_CHANGED bluetooth adapter intent-filter is present"
filterString['android.bluetooth.adapter.action.SCAN_MODE_CHANGED'] = "\t[+] SCAN_MODE_CHANGED bluetooth adapter intent-filter is present"
filterString['android.bluetooth.adapter.action.DISCOVERY_STARTED'] = "\t[+] DISCOVERY_STARTED bluetooth adapter intent-filter is present"
filterString['android.bluetooth.adapter.action.DISCOVERY_FINISHED'] = "\t[+] DISCOVERY_FINISHED bluetooth adapter intent-filter is present"
filterString['android.bluetooth.adapter.action.LOCAL_NAME_CHANGED'] = "\t[+] LOCAL_NAME_CHANGED bluetooth adapter intent-filter is present"
filterString['android.bluetooth.adapter.action.CONNECTION_STATE_CHANGED'] = "\t[+] CONNECTION_STATE_CHANGED bluetooth adapter intent-filter is present"
filterString['android.bluetooth.device.action.FOUND'] = "\t[+] FOUND bluetooth device intent-filter is present"
filterString['android.bluetooth.device.action.DISAPPEARED'] = "\t[+] DISAPPEARED bluetooth device intent-filter is present"
filterString['android.bluetooth.device.action.CLASS_CHANGED'] = "\t[+] CLASS_CHANGED bluetooth device intent-filter is present"
filterString['android.bluetooth.device.action.ACL_CONNECTED'] = "\t[+] ACL_CONNECTED bluetooth device intent-filter is present"
filterString['android.bluetooth.device.action.ACL_DISCONNECT_REQUESTED'] = "\t[+] ACL_DISCONNECT_REQUESTED bluetooth device intent-filter is present"
filterString['android.bluetooth.device.action.ACL_DISCONNECTED'] = "\t[+] ACL_DISCONNECTED bluetooth device intent-filter is present"
filterString['android.bluetooth.device.action.NAME_CHANGED'] = "\t[+] NAME_CHANGED bluetooth device intent-filter is present"
filterString['android.bluetooth.device.action.BOND_STATE_CHANGED'] = "\t[+] BOND_STATE_CHANGED bluetooth device intent-filter is present"
filterString['android.bluetooth.device.action.NAME_FAILED'] = "\t[+] NAME_FAILED bluetooth device intent-filter is present"
filterString['android.bluetooth.device.action.PAIRING_REQUEST'] = "\t[+] PAIRING_REQUEST bluetooth device intent-filter is present"
filterString['android.bluetooth.device.action.PAIRING_CANCEL'] = "\t[+] PAIRING_CANCEL bluetooth device intent-filter is present"
filterString['android.bluetooth.device.action.CONNECTION_ACCESS_REPLY'] = "\t[+] CONNECTION_ACCESS_REPLY bluetooth device intent-filter is present"
filterString['android.bluetooth.headset.profile.action.AUDIO_STATE_CHANGED'] = "\t[+] AUDIO_STATE_CHANGED bluetooth headset intent-filter is present"
filterString['android.bluetooth.a2dp.profile.action.CONNECTION_STATE_CHANGED'] = "\t[+] CONNECTION_STATE_CHANGED bluetooth a2dp intent-filter is present"
filterString['android.bluetooth.input.profile.action.CONNECTION_STATE_CHANGED'] = "\t[+] CONNECTION_STATE_CHANGED bluetooth input intent-filter is present"
filterString['android.bluetooth.pan.profile.action.CONNECTION_STATE_CHANGED'] = "\t[+] CONNECTION_STATE_CHANGED bluetooth pan intent-filter is present"

# android hardware
filterString['android.hardware.display.action.WIFI_DISPLAY_STATUS_CHANGED'] = '\t[+] WIFI_DISPLAY_STATUS_CHANGED hardware display intent-filter is present'
filterString['android.hardware.usb.action.USB_STATE'] = '\t[+] USB_STATE hardware usb intent-filter is present'
filterString['android.hardware.usb.action.USB_ACCESSORY_ATTACHED'] = '\t[+] USB_ACCESSORY_ATTACHED hardware usb intent-filter is present'
filterString['android.hardware.usb.action.USB_DEVICE_ATTACHED'] = '\t[+] USB_DEVICE_ATTACHED hardware usb intent-filter is present'
filterString['android.hardware.usb.action.USB_DEVICE_DETACHED'] = '\t[+] USB_DEVICE_DETACHED hardware usb intent-filter is present'
filterString['android.hardware.usb.action.USB_DEVICE_ATTACHED'] = '\t[+] USB_DEVICE_ATTACHED hardware usb intent-filter is present'



#TODO Add this filters
# 'android.net.wifi.p2p.DISCOVERY_STATE_CHANGE','android.net.wifi.p2p.THIS_DEVICE_CHANGED','android.net.wifi.p2p.PEERS_CHANGED','android.net.wifi.p2p.CONNECTION_STATE_CHANGE','android.net.wifi.p2p.PERSISTENT_GROUPS_CHANGED','android.net.conn.TETHER_STATE_CHANGED','android.net.conn.INET_CONDITION_ACTION','android.intent.action.EXTERNAL_APPLICATIONS_AVAILABLE','android.intent.action.EXTERNAL_APPLICATIONS_UNAVAILABLE','android.intent.action.AIRPLANE_MODE','android.intent.action.ADVANCED_SETTINGS','android.intent.action.BUGREPORT_FINISHED','android.intent.action.ACTION_IDLE_MAINTENANCE_START','android.intent.action.ACTION_IDLE_MAINTENANCE_END','android.intent.action.SERVICE_STATE','android.intent.action.RADIO_TECHNOLOGY','android.intent.action.EMERGENCY_CALLBACK_MODE_CHANGED','android.intent.action.SIG_STR','android.intent.action.ANY_DATA_STATE','android.intent.action.DATA_CONNECTION_FAILED','android.intent.action.SIM_STATE_CHANGED','android.intent.action.NETWORK_SET_TIME','android.intent.action.NETWORK_SET_TIMEZONE','android.intent.action.ACTION_SHOW_NOTICE_ECM_BLOCK_OTHERS','android.intent.action.ACTION_MDN_STATE_CHANGED','android.provider.Telephony.SPN_STRINGS_UPDATED','android.provider.Telephony.SIM_FULL','com.android.internal.telephony.data-restart-trysetup','com.android.internal.telephony.data-stall'
