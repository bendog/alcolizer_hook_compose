#!/bin/bash
LOG_ID=$1
./hook_compose_v1.py '{"url": "https://uat.riw.net.au/Sync/serviceApi/Breathalyser/RecordBreathalyserResult", "headers": {"Host": "uat.riw.net.au", "Authorization": "123"}, "table_name": "machine_log_wm4", "table_id": 3129266, "hook_log_id": '${LOG_ID}' }'
