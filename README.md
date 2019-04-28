Paper Trail
===========
Utilities to help with filing digital documents

Scan Files (coming soon)
------------------------
Use the `scan` command to scan the current directory for any file name violations.

```
$ scan
> Scanned 1234 file(s), found 123 potential issue(s)
> Invalid Date(s)
> ---------------
> 1. ACME Inc. - Invoice.pdf
> 2. 2019-01-1 ACME Inc. - Invoice.pdf
> 3. 2019-1-01 ACME Inc. - Invoice.pdf
> 4. 2019-01 ACME Inc. - Invoice.pdf
> 5. 2019-13-01 ACME Inc. - Invoice.pdf
> 6. 2019-01-32 ACME Inc. - Invoice.pdf
> 
> Missing Entity or Subject
> -------------------------
> 1. 2019-01-01 Invoice.pdf
> 2. 2019-01-01 ACME Inc. - .pdf
> 3. 2019-01-01 - Invoice.pdf
>
> CAPS on Extension
> -----------------
> 1. 2019-01-01 ACME Inc. - Invoice.PDF
> 2. 2019-01-01 ACME Inc. - Invoice.Pdf
``` 

Backlog
-------
1. Pad short dates (shadow mode)
1. Execute mode
1. Trimming whitespace
1. Lowercase file extensions
1. Reverse names containing comma
1. Find and replace (exact match)
1. Find and replace (regex)
1. List suspect files
1. List potential duplicates
1. Interactive mode
