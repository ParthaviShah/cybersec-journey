# OverTheWire: Bandit — Progress Log

Practicing Linux fundamentals through OverTheWire's Bandit wargame.
Each level requires finding a password hidden somewhere on the system
using basic Linux commands. Passwords are not included here — only
the technique and reasoning used to solve each level.

## Level 0 → 1
**Command:** `cat readme`
The password was sitting in a plainly named file in the home directory.

## Level 1 → 2
**Command:** `cat ./-`
The filename was literally `-`, which looks like a command flag.
Prefixing it with `./` tells the shell "this is a file in the current
directory," not an option being passed to `cat`.

## Level 2 → 3
**Command:** `cat -- "--spaces in this filename--"`
The filename itself contained spaces and leading dashes. Wrapping it
in quotes treats it as one single filename instead of multiple
arguments; the `--` tells `cat` to stop interpreting further dashes
as flags.

## Level 3 → 4
**Commands:** `ls -a`, then `cat ...Hiding-From-You`
A filename starting with `.` is hidden by default in Linux. The `-a`
flag on `ls` reveals hidden files too.

## Level 4 → 5
**Command:** `file ./*`
Several decoy files existed in the folder. `file` checks the actual
type of each one (not just the name), which quickly revealed which
single file was human-readable ASCII text — that was the target.

## Level 5 → 6
**Commands:** `find . -type f -size 1033c ! -executable`, then `file ./maybehere07/.file2`
Narrowed down one specific file among many nested folders by exact
size (1033 bytes), file type, and by excluding executables.

## Level 6 → 7
**Command:** `find / -user bandit7 -group bandit6 -size 33c 2>/dev/null`
Searched the entire filesystem for a file matching a specific owner,
group, and size. Redirecting errors to `/dev/null` hides the
"permission denied" noise from folders the user can't access,
leaving a clean result.

## Level 7 → 8
**Concept:** `grep` searches for lines matching a pattern.
**Command:** `grep "keyword" data.txt`
The password was one line among thousands in a large file, located
next to a specific keyword used as a marker.

## Level 8 → 9
**Concept:** `sort` arranges lines; `uniq` identifies duplicates;
`uniq -u` shows only lines that appear exactly once.
**Command:** `sort data.txt | uniq -u`
The password was the single line in the file with no duplicate.
Sorting first groups identical lines together so `uniq -u` can
correctly isolate the one unique line.

## Level 9 → 10
**Command:** `strings data.txt | grep "="`
The file contained mostly binary/non-printable data. `strings`
extracts only human-readable text from it; piping that into `grep`
then filtered for the line containing an `=` sign, which marked the
password.

## Level 10 → 11
**Command:** `base64 -d data.txt`
The password was stored in base64-encoded form. The `-d` flag
decodes it back into readable plain text.
