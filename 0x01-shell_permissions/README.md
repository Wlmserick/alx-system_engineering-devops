1. `cd`: Change directory.
2. `ls`: List directory contents.
3. `pwd`: Print working directory.
4. `cat`: Concatenate and display files.
5. `touch`: Create an empty file.
6. `cp`: Copy files and directories.
7. `mv`: Move or rename files and directories.
8. `rm`: Remove files and directories.
9. `mkdir`: Create a new directory.
10. `rmdir`: Remove an empty directory.
11. `cut`: Cut out sections of a file.
12. `gzip`: Compress or decompress files using gzip.
13. `gunzip`: Decompress files compressed with gzip.
14. `find`: Find files and directories matching a pattern.
15. `grep`: Search for a pattern in a file.
16. `awk`: Pattern scanning and processing language.
17. `journalctl`: Displays the system journal.
18. `dmesg`: Displays the kernel ring buffer.
19. `crontab`: Schedules recurring tasks.
20. `at`: Schedules a one-time task.
21. `service`: Manages system services.
22. `systemctl`: Controls system services in systemd-based distributions.
23. `traceroute`: Traces the network path to a remote host.
24. `bzip2`: Compresses files using the bzip2 algorithm.
25. `unzip`: Extracts files from a ZIP archive.
26. `tar`: Create, extract, and list archives.
27. `ping`: Send ICMP echo requests to a remote host.
28. `ssh`: Securely connect to a remote host.
29. `scp`: Securely copy files to and from a remote host.
30. `wget`: Download files from the internet.
31. `curl`: Transfer data from or to a server.
32. `man`: Display the manual page for a command.
33. `info`: Display the Info documentation for a command.
34. `which`: Locate the binary for a command.
35. `whereis`: Locate the binary, source, and man page for a command.
36. `type`: Display the type of a command.
37. `alias`: List or define aliases.
38. `unalias`: Remove an alias.
39. `export`: Set or display environment variables.
40. `unset`: Unset an environment variable.
41. `history`: List previously entered commands.
42. `jobs`: List running jobs.
43. `fg`: Bring a job to the foreground.
44. `bg`: Send a job to the background.
45. `kill`: Send a signal to a process.
46. `pkill`: Kill all processes matching a pattern.
47. `top`: Display real-time information about running processes.
48. `htop`: A more interactive version of top.
49. `free`: Display the amount of free and used memory.
50. `df`: Display the amount of free and used disk space.
51. `du`: Display the disk usage of a file or directory.
52. `mount`: List or mount filesystems.
53. `umount`: Unmount a filesystem.
54. `fdisk`: Create, delete, and modify partitions.
55. `mkfs`: Create a filesystem.
56. `mount`: Mount a filesystem.
57. `umount`: Unmount a filesystem.
58. `parted`: Create, delete, and resize partitions.
59. `mkswap`: Create a swap partition.
60. `swapon`: Enable a swap partition.
61. `swapoff`: Disable a swap partition.
62. `mkfs.ext4`: Create an ext4 filesystem.
63. `mkfs.xfs`: Create an xfs filesystem.
64. `mkfs.btrfs`: Create a btrfs filesystem.
65. `mkfs.ntfs`: Create an ntfs filesystem.
66. `mkfs.fat`: Create a fat filesystem.
67. `mkfs.vfat`: Create a vfat filesystem.
68. `mount.ext4`: Mount an ext4 filesystem.
69. `mount.xfs`: Mount an xfs filesystem.
70. `mount.btrfs`: Mount a btrfs filesystem.
* **chmod** - Changes the permissions of a file or directory.
* **sudo** - Runs a command as another user.
* **su** - Switches to another user account.
* **chown** - Changes the ownership of a file or directory.
* **chgrp** - Changes the group of a file or directory.
* **id** - Prints the user ID and group ID of the current user.
* **groups** - Prints the groups that the current user belongs to.
* **whoami** - Prints the username of the current user.
* **adduser** - Creates a new user account.
useradd - Creates a new user account (alias for adduser).
addgroup - Creates a new group.
Command	Description
chmod	Changes the permissions of a file or directory.
ls -l	Lists the permissions of all files and directories in a directory.
chown	Changes the owner of a file or directory.
chgrp	Changes the group of a file or directory.
umask	Sets the default permissions for newly created files and directories.
Permission Symbols	Description
r	Read permission
w	Write permission
x	Execute permission
--	No permission
Symbolic Notation	Description
u	Owner
g	Group
o	Others
a	All users
=	Set permission
+	Add permission
-	Remove permission
Examples

To give the owner of the file myfile read, write, and execute permissions, you would use the following command:
chmod 700 myfile
To give the group of the file myfile read and write permissions, you would use the following command:
chmod 640 myfile
To give everyone read permissions to the file myfile, you would use the following command:
chmod 444 myfile
To change the owner of the file myfile to the user alice, you would use the following command:
chown alice myfile
To change the group of the file myfile to the group developers, you would use the following command:
chgrp developers myfile
To set the default permissions for newly created files and directories to 644, you would use the following command:
umask 022

Permission	 Symbol	Owner	Group	Others
Read	r	4	4	4
Write	w	2	2	2
Execute	x	1	1	1
Read and write	rw	6	6	6
Read and execute	r-x	5	5	5
Write and execute	-wx	3	3	3
No permissions	---	0	0	0
