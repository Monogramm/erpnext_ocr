#!/usr/bin/sh

echo "Waiting to ensure everything is fully ready for the tests..."
sleep 60

echo "Checking content of sites directory..."
ls -al "${FRAPPE_WD}/sites/"

# FIXME We couldn't be here if those files did not existed... so why are they not?!
#if [ ! -f "${FRAPPE_WD}/sites/apps.txt" ] \
#    || [ ! -f "${FRAPPE_WD}/sites/.docker-app-init" ] \
#    || [ ! -f "${FRAPPE_WD}/sites/currentsite.txt" ] \
#    || [ ! -f "${FRAPPE_WD}/sites/.docker-site-init" ] \
#    || [ ! -f "${FRAPPE_WD}/sites/.docker-init" ]; then
#    echo 'Apps and site are not initalized!'
#    exit 1
#fi

echo "Checking main containers are reachable..."
if [ ! sudo ping -c 10 -q erpnext_db ]; then
    echo 'Database container is not responding!'
    exit 4
fi

if [ ! sudo ping -c 10 -q erpnext_app ]; then
    echo 'App container is not responding!'
    exit 8
fi

if [ ! sudo ping -c 10 -q erpnext_web ]; then
    echo 'Web container is not responding!'
    exit 16
fi

## https://frappe.io/docs/user/en/testing
## https://frappe.io/docs/user/en/guides/automated-testing/unit-testing
echo "Executing custom app tests..."
bench run-tests --profile --app erpnext_ocr
## TODO Test result of tests

# Success
echo 'Docker test successful'
exit 0
