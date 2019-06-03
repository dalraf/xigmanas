#!/bin/sh
find ${1} -type f  -exec setfacl -m everyone@:full_set::allow {} \;
find ${1} -type f  -exec setfacl -m group@:full_set::allow {} \;
find ${1} -type f  -exec setfacl -m owner@:full_set::allow {} \;
find ${1} -type f -exec setfacl -m group:usuários_do_domínio:full_set::allow {} \;
find ${1} -type d -exec setfacl -m everyone@:full_set:fd:allow {} \;
find ${1} -type d -exec setfacl -m group@:full_set:fd:allow {} \;
find ${1} -type d -exec setfacl -m owner@:full_set:fd:allow {} \;
find ${1} -type d -exec setfacl -m group:usuários_do_domínio:full_set:fd:allow {} \;