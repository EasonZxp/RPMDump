Usage
hansei.py [-h] --elf rpm.elf --output <OutPut Path> dumpfile <dump path>

Dump path should contain rpm_code_ram.bin rpm_data_ram.bin rpm_msg_ram.bin

Example
python hansei.py –elf rpm.elf -o . dumpfile <dump path containing rpm_code_ram.bin rpm_data_ram.bin rpm_msg_ram.bin>

Output
rpm-summary.txt – Contains general information about the health of the RPM, including the Core dump state and different fault information.

rpm-log.txt – The postprocessed “RPM external log”.

npa-dump.txt – The standard NPA dump format, though without the (inaccurate)timestamps.

ee-status.txt – Contains information about the subsystems (and their cores) that areactive or sleeping.

reqs_by_master/* – A folder that contains a file for each execution environment, detailing all the current requests that EE has in place with the RPM.

reqs_by_resource/* – A folder structure containing a folder for each of the resource

“types” registered with the RPM server, and under that folder, a file containing all of the requests to each resource of that type.