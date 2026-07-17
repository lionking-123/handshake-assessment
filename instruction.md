# Access log summary report

An Apache-style access log is available at `/app/access.log` in your working
directory. Analyze the traffic and produce a short JSON summary report.

Write your report to `/app/report.json` as a single JSON object with exactly
these fields:

- `total_requests` (integer): the number of request lines in the log.
- `unique_ips` (integer): the number of distinct client IP addresses (the first
  whitespace-separated field of each line).
- `top_path` (string): the request path (the path portion of the request line,
  e.g. `/index.html`) that appears most frequently across all requests.

## Success criteria

1. A file exists at `/app/report.json` and contains a single valid JSON object.
2. `total_requests` equals the total number of request lines in `/app/access.log`.
3. `unique_ips` equals the number of distinct client IP addresses in the log.
4. `top_path` equals the most frequently requested path in the log.
