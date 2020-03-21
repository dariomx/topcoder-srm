# Read from the file words.txt and output the word frequency list to stdout.
tr ' ' '\n' < words.txt | sort | uniq -c | awk '{ if ($2 != "") print $2" "$1 }' | sort -rn -k 2