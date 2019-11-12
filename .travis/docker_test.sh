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

FRAPPE_APP_TO_TEST=erpnext_ocr

################################################################################
# Automated Unit tests
# https://docs.docker.com/docker-hub/builds/automated-testing/
# https://frappe.io/docs/user/en/testing
################################################################################

################################################################################
# Frappe Unit tests
# https://frappe.io/docs/user/en/guides/automated-testing/unit-testing

echo "Executing ${FRAPPE_APP_TO_TEST} app tests..."
bench run-tests --profile --app ${FRAPPE_APP_TO_TEST}

## TODO Test result of tests

################################################################################

################################################################################
# QUnit (JS) Unit tests
# https://frappe.io/docs/user/en/guides/automated-testing/qunit-testing

echo "Executing ${FRAPPE_APP_TO_TEST} app UI tests..."
if [[ "${VERSION}" = "10" ]] || [[ "${VERSION}" = "11" ]]; then
    bench run-ui-tests --app ${FRAPPE_APP_TO_TEST}
else
    bench run-ui-tests ${FRAPPE_APP_TO_TEST}
fi

## TODO Test result of UI tests

################################################################################

# Success
echo 'Docker test successful'
#echo 'Check the following logs for details:'
#tail -n 100 logs/*.log
exit 0
