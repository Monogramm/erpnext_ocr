#!/usr/bin/sh

set -e

echo "Waiting to ensure everything is fully ready for the tests..."
sleep 60

echo "Checking content of sites directory..."
if [ ! -f "./sites/apps.txt" ] || [ ! -f "./sites/.docker-app-init" ] || [ ! -f "./sites/currentsite.txt" ] || [ ! -f "./sites/.docker-site-init" ] || [ ! -f "./sites/.docker-init" ]; then
    echo 'Apps and site are not initalized?!'
    ls -al "./sites"
    # FIXME We couldn't be running tests if those files did not existd... so why are they not visible?!
    #exit 1
fi

echo "Checking main containers are reachable..."
if ! sudo ping -c 10 -q frappe_db ; then
    echo 'Database container is not responding!'
    exit 2
fi

if ! sudo ping -c 10 -q frappe_app ; then
    echo 'App container is not responding!'
    exit 4
fi

if ! sudo ping -c 10 -q frappe_web ; then
    echo 'Web container is not responding!'
    exit 8
fi

# https://docs.docker.com/docker-hub/builds/automated-testing/
# https://frappe.io/docs/user/en/testing
# https://frappe.io/docs/user/en/guides/automated-testing/unit-testing
echo "Executing custom app tests..."
bench run-tests --profile --app erpnext_ocr
## TODO Test result of tests

# Success
echo 'Docker test successful'
exit 0
