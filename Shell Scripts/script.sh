#!/bin/bash

RED='\033[0;31m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'
CLEAR='\033[0m'

echo -e "${YELLOW}-----SYSTEM INFO-----${CLEAR}"
echo -e "${GREEN}Your OS Release Version Is: ${CLEAR}"
   cat /etc/os-release | grep 'VERSION=' --color=never

echo -e "${GREEN}Your KERNEL Version Is: ${CLEAR}"
   uname -r

echo -e "${GREEN}Your Virtual Memory Size Is: ${CLEAR}"
   cat /proc/meminfo | grep 'VmallocTotal:' --color=never

echo -e "${RED}-----END-----${CLEAR}"