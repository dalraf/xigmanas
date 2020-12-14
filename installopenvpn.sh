#/bin/sh
pkg install openvpn screen
sysrc openvpn_enable="YES"
sysrc openvpn_if="tun"
sysrc openvpn_configfile=${1}
sysrc openvpn_dir=${2}
service openvpn start; 