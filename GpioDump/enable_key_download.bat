adb wait-for-device
adb shell setprop service.user.test 1
adb wait-for-device
adb shell setenforce 0
adb wait-for-device
adb remount
adb shell "echo 0xd0 > /sys/kernel/debug/spmi/spmi-0/address"
adb shell "echo 0xa5 > /sys/kernel/debug/spmi/spmi-0/data"
adb shell "echo 0x844 > /sys/kernel/debug/spmi/spmi-0/address"
adb shell "echo 1 > /sys/kernel/debug/spmi/spmi-0/count"
adb shell "echo 0x0 > /sys/kernel/debug/spmi/spmi-0/data"
adb shell "echo 0x845 > /sys/kernel/debug/spmi/spmi-0/address"
adb shell "echo 0x0 > /sys/kernel/debug/spmi/spmi-0/data"
adb shell "echo 0x846 > /sys/kernel/debug/spmi/spmi-0/address"
adb shell "echo 0x1 > /sys/kernel/debug/spmi/spmi-0/data"
adb shell "echo 0x847 > /sys/kernel/debug/spmi/spmi-0/address"
adb shell "echo 0x80 > /sys/kernel/debug/spmi/spmi-0/data"
adb shell sync
pause