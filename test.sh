#!/bin/bash
LOG_ID=$1
./hook_compose_v1.py '{"url": "'${TEST_URL}'", "headers": {"Authorization": "'${TEST_AUTH}'"}, "table_name": "machine_log_wm4", "table_id": 3129266, "hook_log_id": '${LOG_ID}' }'
