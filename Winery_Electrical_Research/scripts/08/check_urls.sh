#!/bin/bash
u="$1"
ua='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36'
r=$(curl -s -o /dev/null -L --max-time 25 -A "$ua" -r 0-2047 -w '%{http_code}|%{url_effective}' "$u" 2>/dev/null)
code=${r%%|*}
if [ "$code" = "000" ]; then r=$(curl -sk -o /dev/null -L --max-time 25 -A "$ua" -r 0-2047 -w '%{http_code}|%{url_effective}' "$u" 2>/dev/null); code="${r%%|*}"; [ "$code" != "000" ] && code="$code(ssl)"; fi
printf '%s\t%s\t%s\n' "$u" "$code" "${r#*|}"
