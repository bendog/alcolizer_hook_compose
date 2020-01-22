#!/bin/bash
LOG_ID=$1
LOOKUP_ID=1315988
LOOKUP_TABLE=machine_log_wm4
./hook_compose_v1.py '{"url": "'${TEST_URL}'", "headers": {"Authorization": "'${TEST_AUTH}'"}, "table_name": "'${LOOKUP_TABLE}'", "table_id": '${LOOKUP_ID}', "hook_log_id": '${LOG_ID}' }'
