#!/bin/sh
setfacl -R -b ${1}
chown -R root ${1}
chgrp -R wheel ${1}
setfacl -R -m everyone@:full_set::allow ${1}
setfacl -R -m group@:full_set::allow ${1}
setfacl -R -m owner@:full_set::allow ${1}
setfacl -R -m group:usuários_do_domínio:full_set::allow ${1}

