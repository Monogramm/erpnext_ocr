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

################################################################################
# Automated Unit tests
# https://docs.docker.com/docker-hub/builds/automated-testing/
# https://frappe.io/docs/user/en/testing
################################################################################

FRAPPE_APP_TO_TEST=erpnext_ocr

################################################################################
# Frappe Unit tests
# https://frappe.io/docs/user/en/guides/automated-testing/unit-testing

#bench run-tests --help
echo "Executing Unit Tests of '${FRAPPE_APP_TO_TEST}' app..."
bench run-tests \
    --app ${FRAPPE_APP_TO_TEST}

# FIXME Frappe 11+ / Python 3.7 issue when generating --junit-xml-output "${FRAPPE_APP_TO_TEST}_unit_tests.xml"
# Traceback (most recent call last):
#   File "/usr/local/lib/python3.7/runpy.py", line 193, in _run_module_as_main
#     "__main__", mod_spec)
#   File "/usr/local/lib/python3.7/runpy.py", line 85, in _run_code
#     exec(code, run_globals)
#   File "/home/frappe/frappe-bench/apps/frappe/frappe/utils/bench_helper.py", line 97, in <module>
#     main()
#   File "/home/frappe/frappe-bench/apps/frappe/frappe/utils/bench_helper.py", line 18, in main
#     click.Group(commands=commands)(prog_name='bench')
#   File "/home/frappe/frappe-bench/env/lib/python3.7/site-packages/click/core.py", line 764, in __call__
#     return self.main(*args, **kwargs)
#   File "/home/frappe/frappe-bench/env/lib/python3.7/site-packages/click/core.py", line 717, in main
#     rv = self.invoke(ctx)
#   File "/home/frappe/frappe-bench/env/lib/python3.7/site-packages/click/core.py", line 1137, in invoke
#     return _process_result(sub_ctx.command.invoke(sub_ctx))
#   File "/home/frappe/frappe-bench/env/lib/python3.7/site-packages/click/core.py", line 1137, in invoke
#     return _process_result(sub_ctx.command.invoke(sub_ctx))
#   File "/home/frappe/frappe-bench/env/lib/python3.7/site-packages/click/core.py", line 956, in invoke
#     return ctx.invoke(self.callback, **ctx.params)
#   File "/home/frappe/frappe-bench/env/lib/python3.7/site-packages/click/core.py", line 555, in invoke
#     return callback(*args, **kwargs)
#   File "/home/frappe/frappe-bench/env/lib/python3.7/site-packages/click/decorators.py", line 17, in new_func
#     return f(get_current_context(), *args, **kwargs)
#   File "/home/frappe/frappe-bench/apps/frappe/frappe/commands/__init__.py", line 25, in _func
#     ret = f(frappe._dict(ctx.obj), *args, **kwargs)
#   File "/home/frappe/frappe-bench/apps/frappe/frappe/commands/utils.py", line 419, in run_tests
#     ui_tests = ui_tests, doctype_list_path = doctype_list_path, failfast=failfast)
#   File "/home/frappe/frappe-bench/apps/frappe/frappe/test_runner.py", line 70, in main
#     ret = run_all_tests(app, verbose, profile, ui_tests, failfast=failfast)
#   File "/home/frappe/frappe-bench/apps/frappe/frappe/test_runner.py", line 118, in run_all_tests
#     out = unittest_runner(verbosity=1+(verbose and 1 or 0), failfast=failfast).run(test_suite)
#   File "/home/frappe/frappe-bench/env/lib/python3.7/site-packages/xmlrunner/runner.py", line 116, in run
#     result.generate_reports(self)
#   File "/home/frappe/frappe-bench/env/lib/python3.7/site-packages/xmlrunner/result.py", line 657, in generate_reports
#     test_runner.output.write(xml_content)
# TypeError: write() argument must be str, not bytes
#    --junit-xml-output "${FRAPPE_APP_TO_TEST}_unit_tests.xml"

## TODO Check result of tests
#cat "${FRAPPE_APP_TO_TEST}_unit_tests.xml"


################################################################################
# QUnit (JS) Unit tests
# https://frappe.io/docs/user/en/guides/automated-testing/qunit-testing

#bench run-ui-tests --help
#echo "Executing UI Tests of '${FRAPPE_APP_TO_TEST}' app..."
#bench run-tests \
#    --app ${FRAPPE_APP_TO_TEST} \
#    --ui-tests \
#    --junit-xml-output "${FRAPPE_APP_TO_TEST}_ui_tests.xml"

#if [ "${TEST_VERSION}" = "10" ] || [ "${TEST_VERSION}" = "11" ]; then
#    bench run-ui-tests --app ${FRAPPE_APP_TO_TEST}
#else
#    bench run-ui-tests ${FRAPPE_APP_TO_TEST}
#fi

## TODO Check result of UI tests
#cat "${FRAPPE_APP_TO_TEST}_ui_tests.xml"


################################################################################
# Success
echo 'Docker test successful'
#echo 'Check the following logs for details:'
#tail -n 100 logs/*.log
exit 0
