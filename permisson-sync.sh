#!/bin/sh
setfacl -R -b ${1}
chown -R root ${1}
chgrp -R wheel ${1}
setfacl -R -m owner@:rwxpDdaARWcCo-:fd----I:allow ${1}
setfacl -R -m group@:rwxpDdaARWcCo-:fd----I:allow ${1}
setfacl -R -m user:syncthing:rwxpDdaARWcCo-:fdi----:allow ${1}
setfacl -m everyone@:r-x---a-R-c---:-------:allow ${1}
setfacl -R -m everyone@:rwxpDdaARWcCo-:fdi----:allow ${1}/

