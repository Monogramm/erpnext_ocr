#!/usr/bin/sh

set -e

echo "Waiting to ensure everything is fully ready for the tests..."
sleep 60

echo "Checking content of sites directory..."
if [ ! -f "./sites/apps.txt" ] || [ ! -f "./sites/.docker-app-init" ] || [ ! -f "./sites/currentsite.txt" ] || [ ! -f "./sites/.docker-site-init" ] || [ ! -f "./sites/.docker-init" ]; then
    echo 'Apps and site are not initalized?!'
    ls -al "./sites"
    exit 1
fi

echo "Checking main containers are reachable..."
if ! sudo ping -c 10 -q erpnext_db ; then
    echo 'Database container is not responding!'
    echo 'Check the following logs for details:'
    tail -n 100 logs/*.log
    exit 2
fi

if ! sudo ping -c 10 -q erpnext_app ; then
    echo 'App container is not responding!'
    echo 'Check the following logs for details:'
    tail -n 100 logs/*.log
    exit 4
fi

if ! sudo ping -c 10 -q erpnext_web ; then
    echo 'Web container is not responding!'
    echo 'Check the following logs for details:'
    tail -n 100 logs/*.log
    exit 8
fi

# https://docs.docker.com/docker-hub/builds/automated-testing/
# https://frappe.io/docs/user/en/testing
# https://frappe.io/docs/user/en/guides/automated-testing/unit-testing
echo "Executing erpnext_ocr app tests..."
bench run-tests --profile --app erpnext_ocr
## TODO Test result of tests

# Success
echo 'Docker test successful'
#echo 'Check the following logs for details:'
#tail -n 100 logs/*.log
exit 0
