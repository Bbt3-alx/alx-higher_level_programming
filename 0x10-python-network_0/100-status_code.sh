#!/usr/bin/env bash
curl -s -o /dev/null -w "%{http_code}\n" $1
