# kpnrouter
router with ssh/ssl hhtp/ssh tunnel capabality

please install first xderm by ryan fauzi 


opkg update
opkg install bash python screen redsocks curl openssh-client
wget https://rureka.com/files/sshpass/sshpass_1.06-Rureka.com_aarch64_cortex-a53.ipk
wget https://rureka.com/files/sshpass/sshpass_1.06-Rureka.com_mips_mips32.ipk
wget https://rureka.com/files/sshpass/sshpass_1.06-Rureka.com_mipsel_24kc.ipk

opkg install *.ipk
opkg install python screen redsocks coreutils-timeout openssl-util curl ncat openssh-client bash wget libustream-openssl
