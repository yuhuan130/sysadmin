#!/usr/bin/env python
# new <name> <number> -> adds an entry
# list -> display whole without order, if empty display phonebook is empty
# remove <name> -> remove everything related to given name
# clear -> deletes whole
# lookup <name> -> displays phone numbers associated with give name
#!/usr/bin/env python
import sys
import os

PHONEBOOK_ENTRIES = "python_phonebook_entries"


def main():
    if len(sys.argv) < 2:
        exit(1)

    elif sys.argv[1] == "new":
        # YOUR CODE HERE #
      	with open(PHONEBOOK_ENTRIES, 'a') as f:
            f.write(" ".join(sys.argv[2:]) + '\n') 
    elif sys.argv[1] == "list":
        pass
        if not os.path.isfile(PHONEBOOK_ENTRIES) or os.path.getsize(
            PHONEBOOK_ENTRIES
        ) == 0:
            print("phonebook is empty")
        else:
            # YOUR CODE HERE #
            with open(PHONEBOOK_ENTRIES, 'r') as f:
                for line in f:
                    print(line, end='')

    elif sys.argv[1] == "lookup":
        # YOUR CODE HERE #
        pass

    elif sys.argv[1] == "remove":
        name = " ".join(sys.argv[2:])
        # YOUR CODE HERE #
        exit(1)

    elif sys.argv[1] == "clear":
        if os.path.isfile(PHONEBOOK_ENTRIES):
            os.remove(PHONEBOOK_ENTRIES)
        exit(1)

    else:
        name = " ".join(sys.argv[1:])
        with open(PHONEBOOK_ENTRIES, "r") as f:
            lookup = "".join(
                filter(lambda line: name in line, f.readlines())
            )
            # YOUR CODE HERE #
        exit(1)


if __name__ == "__main__":
    main()
