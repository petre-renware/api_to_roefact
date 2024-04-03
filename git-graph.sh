
while IFS=+ read -r graph hash time branch message;do

  # Count needed amount of white spaces and create them
  whitespaces=$((9-$(sed -nl1000 'l' <<< "$graph" | grep -Eo '\\\\|\||\/|\ |\*|_' | wc -l)))
  whitespaces=$(seq -s' ' $whitespaces|tr -d '[:digit:]')

  # Show hashes besides the tree ...
  #graph_all="$graph_all$graph$(printf '%7s' "$hash")$whitespaces \n"

  # ... or in an own column
  graph_all="$graph_all$graph$whitespaces\n"
  hash_all="$hash_all$(printf '%7s' "$hash")  \n"

  # Format all other columns
  time_all="$time_all$(printf '%12s' "$time") \n"
  branch_all="$branch_all$(printf '%15s' "$branch")\n"
  message_all="$message_all$message\n"
done < <(git log --all --graph --decorate=short --color --pretty=format:'+%C(bold 214)%<(7,trunc)%h%C(reset)+%C(dim white)%>(12,trunc)%cr%C(reset)+%C(214)%>(15,trunc)%d%C(reset)+%C(white)%s%C(reset)' && echo);

# Paste the columns together and show the table-like output
paste -d' ' <(echo -e "$time_all") <(echo -e "$branch_all") <(echo -e "$graph_all") <(echo -e "$hash_all") <(echo -e "$message_all")
