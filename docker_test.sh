#!/usr/bin/sh

echo "Checking content of sites directory..."
ls -al "${FRAPPE_WD}/sites/"

if [ ! -f "${FRAPPE_WD}/sites/apps.txt" ] || [ ! -f "${FRAPPE_WD}/sites/.docker-app-init" ]; then
    echo 'Apps were not installed in time!'
    exit 1
fi

if [ ! -f "${FRAPPE_WD}/sites/currentsite.txt" ] || [ ! -f "${FRAPPE_WD}/sites/.docker-site-init" ]; then
    echo 'Site was not installed in time!'
    exit 2
fi

echo "Checking main containers are reachable..."
if [ ! sudo ping -c 10 -q erpnext_db ]; then
    echo 'ERPNext database container is not responding!'
    exit 4
fi

if [ ! sudo ping -c 10 -q erpnext_app ]; then
    echo 'ERPNext app container is not responding!'
    exit 8
fi

if [ ! sudo ping -c 10 -q erpnext_web ]; then
    echo 'ERPNext web container is not responding!'
    exit 16
fi

## https://frappe.io/docs/user/en/testing
## https://frappe.io/docs/user/en/guides/automated-testing/unit-testing
echo "Executing custom app tests..."
bench run-tests --profile --app erpnext_ocr
## TODO Test result of tests

# Success
echo 'Frappe docker test successful'
exit 0
