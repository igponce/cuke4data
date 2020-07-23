#!/bin/bash
#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# Launch postgres via docker
# Hardcoded (default) credentials are:

# See docker configuration on: https://hub.docker.com/_/postgres

# Postgres root user
POSTGRES_USER='cukeuser'

# Postgres root passwd
POSTGRES_PASSWORD='cuke4data'

# Database name
POSGRES_DB='cukedb'

# Where to place postgres files (/tmp since this is for a test)
PGDATA='/tmp/pgdata'

docker run --name 'Postgres-cuke4data' \
   --rm \
   -e POSTGRES_USER=$POSTGRES_USER \
   -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
   -e POSTGRES_DB=$POSTGRES_DB \
   -e PGDATA=$PGDATA \
   -d postgres:12.3     
