for repositorie in $(bat $1); do
	gh repo delete --yes $repositorie
done
