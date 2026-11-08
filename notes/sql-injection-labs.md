# PortSwigger SQL Injection Labs

## Lab 1: WHERE clause bypass (hidden data)
Payload: Gifts' OR 1=1--
The category filter's query normally checked category AND released=1.
The payload closed the original quote early, added an always-true
OR condition, then used -- to comment out the rest of the query
(including the released=1 restriction). This revealed hidden/
unreleased products that should never have been shown.

## Lab 2: Login bypass
Payload (username field): ' OR 1=1--
Same technique applied to a login form. The query normally checked
username AND password. By closing the quote and adding an always-true
OR condition, then commenting out the password check entirely with
--, I logged in without knowing any real password.

## Lab 3: UNION attack - Oracle version extraction
Step 1: Used ORDER BY 1, 2, 3... on the category filter to find the
query had exactly 2 columns (ORDER BY 3 caused an error).
Step 2: Tested the UNION technique with placeholder values:
  Tech gifts' UNION SELECT 'a','b' FROM dual--
  (Oracle requires FROM dual when not selecting from a real table)
Step 3: Replaced the placeholder with Oracle's real version-info
column and table:
  Tech gifts' UNION SELECT banner,'b' FROM v$version--
This combined the normal product results with an injected row
containing the database's own internal version string, displayed
disguised as a product name.
