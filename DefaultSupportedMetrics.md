对服务器缺省支持如下指标：
```
####  HELP go_gc_duration_seconds A summary of the GC invocation durations.
####  TYPE go_gc_duration_seconds summary
go_gc_duration_seconds{quantile="0"} 0.00011784600000000001
go_gc_duration_seconds{quantile="0.25"} 0.000164017
go_gc_duration_seconds{quantile="0.5"} 0.00029328000000000004
go_gc_duration_seconds{quantile="0.75"} 0.000362152
go_gc_duration_seconds{quantile="1"} 0.012253659
go_gc_duration_seconds_sum 210.532211541
go_gc_duration_seconds_count 378981
####  HELP go_goroutines Number of goroutines that currently exist.
####  TYPE go_goroutines gauge
go_goroutines 15
####  HELP go_memstats_alloc_bytes Number of bytes allocated and still in use.
####  TYPE go_memstats_alloc_bytes gauge
go_memstats_alloc_bytes 3.146832e+06
####  HELP go_memstats_alloc_bytes_total Total number of bytes allocated, even if freed.
####  TYPE go_memstats_alloc_bytes_total counter
go_memstats_alloc_bytes_total 8.5091084536e+11
####  HELP go_memstats_buck_hash_sys_bytes Number of bytes used by the profiling bucket hash table.
####  TYPE go_memstats_buck_hash_sys_bytes gauge
go_memstats_buck_hash_sys_bytes 1.70381e+06
####  HELP go_memstats_frees_total Total number of frees.
####  TYPE go_memstats_frees_total counter
go_memstats_frees_total 8.143564497e+09
####  HELP go_memstats_gc_sys_bytes Number of bytes used for garbage collection system metadata.
####  TYPE go_memstats_gc_sys_bytes gauge
go_memstats_gc_sys_bytes 966656
####  HELP go_memstats_heap_alloc_bytes Number of heap bytes allocated and still in use.
####  TYPE go_memstats_heap_alloc_bytes gauge
go_memstats_heap_alloc_bytes 3.146832e+06
####  HELP go_memstats_heap_idle_bytes Number of heap bytes waiting to be used.
####  TYPE go_memstats_heap_idle_bytes gauge
go_memstats_heap_idle_bytes 4.980736e+06
####  HELP go_memstats_heap_inuse_bytes Number of heap bytes that are in use.
####  TYPE go_memstats_heap_inuse_bytes gauge
go_memstats_heap_inuse_bytes 3.964928e+06
####  HELP go_memstats_heap_objects Number of allocated objects.
####  TYPE go_memstats_heap_objects gauge
go_memstats_heap_objects 28731
####  HELP go_memstats_heap_released_bytes Number of heap bytes released to OS.
####  TYPE go_memstats_heap_released_bytes gauge
go_memstats_heap_released_bytes 0
####  HELP go_memstats_heap_sys_bytes Number of heap bytes obtained from system.
####  TYPE go_memstats_heap_sys_bytes gauge
go_memstats_heap_sys_bytes 8.945664e+06
####  HELP go_memstats_last_gc_time_seconds Number of seconds since 1970 of last garbage collection.
####  TYPE go_memstats_last_gc_time_seconds gauge
go_memstats_last_gc_time_seconds 1.5308755950269077e+09
####  HELP go_memstats_lookups_total Total number of pointer lookups.
####  TYPE go_memstats_lookups_total counter
go_memstats_lookups_total 1.5835538e+07
####  HELP go_memstats_mallocs_total Total number of mallocs.
####  TYPE go_memstats_mallocs_total counter
go_memstats_mallocs_total 8.143593228e+09
####  HELP go_memstats_mcache_inuse_bytes Number of bytes in use by mcache structures.
####  TYPE go_memstats_mcache_inuse_bytes gauge
go_memstats_mcache_inuse_bytes 2400
####  HELP go_memstats_mcache_sys_bytes Number of bytes used for mcache structures obtained from system.
####  TYPE go_memstats_mcache_sys_bytes gauge
go_memstats_mcache_sys_bytes 16384
####  HELP go_memstats_mspan_inuse_bytes Number of bytes in use by mspan structures.
####  TYPE go_memstats_mspan_inuse_bytes gauge
go_memstats_mspan_inuse_bytes 54240
####  HELP go_memstats_mspan_sys_bytes Number of bytes used for mspan structures obtained from system.
####  TYPE go_memstats_mspan_sys_bytes gauge
go_memstats_mspan_sys_bytes 65536
####  HELP go_memstats_next_gc_bytes Number of heap bytes when next garbage collection will take place.
####  TYPE go_memstats_next_gc_bytes gauge
go_memstats_next_gc_bytes 4.194304e+06
####  HELP go_memstats_other_sys_bytes Number of bytes used for other system allocations.
####  TYPE go_memstats_other_sys_bytes gauge
go_memstats_other_sys_bytes 829814
####  HELP go_memstats_stack_inuse_bytes Number of bytes in use by the stack allocator.
####  TYPE go_memstats_stack_inuse_bytes gauge
go_memstats_stack_inuse_bytes 491520
####  HELP go_memstats_stack_sys_bytes Number of bytes obtained from system for stack allocator.
####  TYPE go_memstats_stack_sys_bytes gauge
go_memstats_stack_sys_bytes 491520
####  HELP go_memstats_sys_bytes Number of bytes obtained from system.
####  TYPE go_memstats_sys_bytes gauge
go_memstats_sys_bytes 1.3019384e+07
####  HELP go_threads Number of OS threads created
####  TYPE go_threads gauge
go_threads 9
####  HELP http_request_duration_microseconds The HTTP request latencies in microseconds.
####  TYPE http_request_duration_microseconds summary
http_request_duration_microseconds{handler="prometheus",quantile="0.5"} 12857.504
http_request_duration_microseconds{handler="prometheus",quantile="0.9"} 17768.741
http_request_duration_microseconds{handler="prometheus",quantile="0.99"} 23518.752
http_request_duration_microseconds_sum{handler="prometheus"} 4.79387855833707e+09
http_request_duration_microseconds_count{handler="prometheus"} 376954
####  HELP http_request_size_bytes The HTTP request sizes in bytes.
####  TYPE http_request_size_bytes summary
http_request_size_bytes{handler="prometheus",quantile="0.5"} 283
http_request_size_bytes{handler="prometheus",quantile="0.9"} 283
http_request_size_bytes{handler="prometheus",quantile="0.99"} 283
http_request_size_bytes_sum{handler="prometheus"} 1.06677982e+08
http_request_size_bytes_count{handler="prometheus"} 376954
####  HELP http_requests_total Total number of HTTP requests made.
####  TYPE http_requests_total counter
http_requests_total{code="200",handler="prometheus",method="get"} 376954
####  HELP http_response_size_bytes The HTTP response sizes in bytes.
####  TYPE http_response_size_bytes summary
http_response_size_bytes{handler="prometheus",quantile="0.5"} 10504
http_response_size_bytes{handler="prometheus",quantile="0.9"} 10514
http_response_size_bytes{handler="prometheus",quantile="0.99"} 10522
http_response_size_bytes_sum{handler="prometheus"} 3.938159378e+09
http_response_size_bytes_count{handler="prometheus"} 376954
####  HELP node_boot_time Node boot time, in unixtime.
####  TYPE node_boot_time gauge
node_boot_time 1.524849709e+09
####  HELP node_context_switches Total number of context switches.
####  TYPE node_context_switches counter
node_context_switches 3.67795786e+08
####  HELP node_cpu Seconds the cpus spent in each mode.
####  TYPE node_cpu counter
node_cpu{cpu="cpu0",mode="guest"} 0
node_cpu{cpu="cpu0",mode="idle"} 6.01120145e+06
node_cpu{cpu="cpu0",mode="iowait"} 445.06
node_cpu{cpu="cpu0",mode="irq"} 0
node_cpu{cpu="cpu0",mode="nice"} 0
node_cpu{cpu="cpu0",mode="softirq"} 59.12
node_cpu{cpu="cpu0",mode="steal"} 949.59
node_cpu{cpu="cpu0",mode="system"} 2979.5
node_cpu{cpu="cpu0",mode="user"} 9147.96
node_cpu{cpu="cpu1",mode="guest"} 0
node_cpu{cpu="cpu1",mode="idle"} 5.99737497e+06
node_cpu{cpu="cpu1",mode="iowait"} 768.26
node_cpu{cpu="cpu1",mode="irq"} 0
node_cpu{cpu="cpu1",mode="nice"} 0
node_cpu{cpu="cpu1",mode="softirq"} 438.7
node_cpu{cpu="cpu1",mode="steal"} 2394.77
node_cpu{cpu="cpu1",mode="system"} 5141.25
node_cpu{cpu="cpu1",mode="user"} 14615.95
####  HELP node_disk_bytes_read The total number of bytes read successfully.
####  TYPE node_disk_bytes_read counter
node_disk_bytes_read{device="md0"} 0
node_disk_bytes_read{device="nbd0"} 0
node_disk_bytes_read{device="nbd1"} 0
node_disk_bytes_read{device="nbd10"} 0
node_disk_bytes_read{device="nbd11"} 0
node_disk_bytes_read{device="nbd12"} 0
node_disk_bytes_read{device="nbd13"} 0
node_disk_bytes_read{device="nbd14"} 0
node_disk_bytes_read{device="nbd15"} 0
node_disk_bytes_read{device="nbd2"} 0
node_disk_bytes_read{device="nbd3"} 0
node_disk_bytes_read{device="nbd4"} 0
node_disk_bytes_read{device="nbd5"} 0
node_disk_bytes_read{device="nbd6"} 0
node_disk_bytes_read{device="nbd7"} 0
node_disk_bytes_read{device="nbd8"} 0
node_disk_bytes_read{device="nbd9"} 0
node_disk_bytes_read{device="sda"} 1.62674688e+08
node_disk_bytes_read{device="sdb"} 1.200128e+06
####  HELP node_disk_bytes_written The total number of bytes written successfully.
####  TYPE node_disk_bytes_written counter
node_disk_bytes_written{device="md0"} 0
node_disk_bytes_written{device="nbd0"} 0
node_disk_bytes_written{device="nbd1"} 0
node_disk_bytes_written{device="nbd10"} 0
node_disk_bytes_written{device="nbd11"} 0
node_disk_bytes_written{device="nbd12"} 0
node_disk_bytes_written{device="nbd13"} 0
node_disk_bytes_written{device="nbd14"} 0
node_disk_bytes_written{device="nbd15"} 0
node_disk_bytes_written{device="nbd2"} 0
node_disk_bytes_written{device="nbd3"} 0
node_disk_bytes_written{device="nbd4"} 0
node_disk_bytes_written{device="nbd5"} 0
node_disk_bytes_written{device="nbd6"} 0
node_disk_bytes_written{device="nbd7"} 0
node_disk_bytes_written{device="nbd8"} 0
node_disk_bytes_written{device="nbd9"} 0
node_disk_bytes_written{device="sda"} 4.5874307072e+10
node_disk_bytes_written{device="sdb"} 0
####  HELP node_disk_io_now The number of I/Os currently in progress.
####  TYPE node_disk_io_now gauge
node_disk_io_now{device="md0"} 0
node_disk_io_now{device="nbd0"} 0
node_disk_io_now{device="nbd1"} 0
node_disk_io_now{device="nbd10"} 0
node_disk_io_now{device="nbd11"} 0
node_disk_io_now{device="nbd12"} 0
node_disk_io_now{device="nbd13"} 0
node_disk_io_now{device="nbd14"} 0
node_disk_io_now{device="nbd15"} 0
node_disk_io_now{device="nbd2"} 0
node_disk_io_now{device="nbd3"} 0
node_disk_io_now{device="nbd4"} 0
node_disk_io_now{device="nbd5"} 0
node_disk_io_now{device="nbd6"} 0
node_disk_io_now{device="nbd7"} 0
node_disk_io_now{device="nbd8"} 0
node_disk_io_now{device="nbd9"} 0
node_disk_io_now{device="sda"} 0
node_disk_io_now{device="sdb"} 0
####  HELP node_disk_io_time_ms Total Milliseconds spent doing I/Os.
####  TYPE node_disk_io_time_ms counter
node_disk_io_time_ms{device="md0"} 0
node_disk_io_time_ms{device="nbd0"} 0
node_disk_io_time_ms{device="nbd1"} 0
node_disk_io_time_ms{device="nbd10"} 0
node_disk_io_time_ms{device="nbd11"} 0
node_disk_io_time_ms{device="nbd12"} 0
node_disk_io_time_ms{device="nbd13"} 0
node_disk_io_time_ms{device="nbd14"} 0
node_disk_io_time_ms{device="nbd15"} 0
node_disk_io_time_ms{device="nbd2"} 0
node_disk_io_time_ms{device="nbd3"} 0
node_disk_io_time_ms{device="nbd4"} 0
node_disk_io_time_ms{device="nbd5"} 0
node_disk_io_time_ms{device="nbd6"} 0
node_disk_io_time_ms{device="nbd7"} 0
node_disk_io_time_ms{device="nbd8"} 0
node_disk_io_time_ms{device="nbd9"} 0
node_disk_io_time_ms{device="sda"} 1.354606e+06
node_disk_io_time_ms{device="sdb"} 16
####  HELP node_disk_io_time_weighted The weighted ####  of milliseconds spent doing I/Os. See https://www.kernel.org/doc/Documentation/iostats.txt.
####  TYPE node_disk_io_time_weighted counter
node_disk_io_time_weighted{device="md0"} 0
node_disk_io_time_weighted{device="nbd0"} 0
node_disk_io_time_weighted{device="nbd1"} 0
node_disk_io_time_weighted{device="nbd10"} 0
node_disk_io_time_weighted{device="nbd11"} 0
node_disk_io_time_weighted{device="nbd12"} 0
node_disk_io_time_weighted{device="nbd13"} 0
node_disk_io_time_weighted{device="nbd14"} 0
node_disk_io_time_weighted{device="nbd15"} 0
node_disk_io_time_weighted{device="nbd2"} 0
node_disk_io_time_weighted{device="nbd3"} 0
node_disk_io_time_weighted{device="nbd4"} 0
node_disk_io_time_weighted{device="nbd5"} 0
node_disk_io_time_weighted{device="nbd6"} 0
node_disk_io_time_weighted{device="nbd7"} 0
node_disk_io_time_weighted{device="nbd8"} 0
node_disk_io_time_weighted{device="nbd9"} 0
node_disk_io_time_weighted{device="sda"} 1.796903e+06
node_disk_io_time_weighted{device="sdb"} 40
####  HELP node_disk_read_time_ms The total number of milliseconds spent by all reads.
####  TYPE node_disk_read_time_ms counter
node_disk_read_time_ms{device="md0"} 0
node_disk_read_time_ms{device="nbd0"} 0
node_disk_read_time_ms{device="nbd1"} 0
node_disk_read_time_ms{device="nbd10"} 0
node_disk_read_time_ms{device="nbd11"} 0
node_disk_read_time_ms{device="nbd12"} 0
node_disk_read_time_ms{device="nbd13"} 0
node_disk_read_time_ms{device="nbd14"} 0
node_disk_read_time_ms{device="nbd15"} 0
node_disk_read_time_ms{device="nbd2"} 0
node_disk_read_time_ms{device="nbd3"} 0
node_disk_read_time_ms{device="nbd4"} 0
node_disk_read_time_ms{device="nbd5"} 0
node_disk_read_time_ms{device="nbd6"} 0
node_disk_read_time_ms{device="nbd7"} 0
node_disk_read_time_ms{device="nbd8"} 0
node_disk_read_time_ms{device="nbd9"} 0
node_disk_read_time_ms{device="sda"} 5880
node_disk_read_time_ms{device="sdb"} 40
####  HELP node_disk_reads_completed The total number of reads completed successfully.
####  TYPE node_disk_reads_completed counter
node_disk_reads_completed{device="md0"} 0
node_disk_reads_completed{device="nbd0"} 0
node_disk_reads_completed{device="nbd1"} 0
node_disk_reads_completed{device="nbd10"} 0
node_disk_reads_completed{device="nbd11"} 0
node_disk_reads_completed{device="nbd12"} 0
node_disk_reads_completed{device="nbd13"} 0
node_disk_reads_completed{device="nbd14"} 0
node_disk_reads_completed{device="nbd15"} 0
node_disk_reads_completed{device="nbd2"} 0
node_disk_reads_completed{device="nbd3"} 0
node_disk_reads_completed{device="nbd4"} 0
node_disk_reads_completed{device="nbd5"} 0
node_disk_reads_completed{device="nbd6"} 0
node_disk_reads_completed{device="nbd7"} 0
node_disk_reads_completed{device="nbd8"} 0
node_disk_reads_completed{device="nbd9"} 0
node_disk_reads_completed{device="sda"} 3883
node_disk_reads_completed{device="sdb"} 43
####  HELP node_disk_reads_merged The total number of reads merged. See https://www.kernel.org/doc/Documentation/iostats.txt.
####  TYPE node_disk_reads_merged counter
node_disk_reads_merged{device="md0"} 0
node_disk_reads_merged{device="nbd0"} 0
node_disk_reads_merged{device="nbd1"} 0
node_disk_reads_merged{device="nbd10"} 0
node_disk_reads_merged{device="nbd11"} 0
node_disk_reads_merged{device="nbd12"} 0
node_disk_reads_merged{device="nbd13"} 0
node_disk_reads_merged{device="nbd14"} 0
node_disk_reads_merged{device="nbd15"} 0
node_disk_reads_merged{device="nbd2"} 0
node_disk_reads_merged{device="nbd3"} 0
node_disk_reads_merged{device="nbd4"} 0
node_disk_reads_merged{device="nbd5"} 0
node_disk_reads_merged{device="nbd6"} 0
node_disk_reads_merged{device="nbd7"} 0
node_disk_reads_merged{device="nbd8"} 0
node_disk_reads_merged{device="nbd9"} 0
node_disk_reads_merged{device="sda"} 454
node_disk_reads_merged{device="sdb"} 0
####  HELP node_disk_sectors_read The total number of sectors read successfully.
####  TYPE node_disk_sectors_read counter
node_disk_sectors_read{device="md0"} 0
node_disk_sectors_read{device="nbd0"} 0
node_disk_sectors_read{device="nbd1"} 0
node_disk_sectors_read{device="nbd10"} 0
node_disk_sectors_read{device="nbd11"} 0
node_disk_sectors_read{device="nbd12"} 0
node_disk_sectors_read{device="nbd13"} 0
node_disk_sectors_read{device="nbd14"} 0
node_disk_sectors_read{device="nbd15"} 0
node_disk_sectors_read{device="nbd2"} 0
node_disk_sectors_read{device="nbd3"} 0
node_disk_sectors_read{device="nbd4"} 0
node_disk_sectors_read{device="nbd5"} 0
node_disk_sectors_read{device="nbd6"} 0
node_disk_sectors_read{device="nbd7"} 0
node_disk_sectors_read{device="nbd8"} 0
node_disk_sectors_read{device="nbd9"} 0
node_disk_sectors_read{device="sda"} 317724
node_disk_sectors_read{device="sdb"} 2344
####  HELP node_disk_sectors_written The total number of sectors written successfully.
####  TYPE node_disk_sectors_written counter
node_disk_sectors_written{device="md0"} 0
node_disk_sectors_written{device="nbd0"} 0
node_disk_sectors_written{device="nbd1"} 0
node_disk_sectors_written{device="nbd10"} 0
node_disk_sectors_written{device="nbd11"} 0
node_disk_sectors_written{device="nbd12"} 0
node_disk_sectors_written{device="nbd13"} 0
node_disk_sectors_written{device="nbd14"} 0
node_disk_sectors_written{device="nbd15"} 0
node_disk_sectors_written{device="nbd2"} 0
node_disk_sectors_written{device="nbd3"} 0
node_disk_sectors_written{device="nbd4"} 0
node_disk_sectors_written{device="nbd5"} 0
node_disk_sectors_written{device="nbd6"} 0
node_disk_sectors_written{device="nbd7"} 0
node_disk_sectors_written{device="nbd8"} 0
node_disk_sectors_written{device="nbd9"} 0
node_disk_sectors_written{device="sda"} 8.9598256e+07
node_disk_sectors_written{device="sdb"} 0
####  HELP node_disk_write_time_ms This is the total number of milliseconds spent by all writes.
####  TYPE node_disk_write_time_ms counter
node_disk_write_time_ms{device="md0"} 0
node_disk_write_time_ms{device="nbd0"} 0
node_disk_write_time_ms{device="nbd1"} 0
node_disk_write_time_ms{device="nbd10"} 0
node_disk_write_time_ms{device="nbd11"} 0
node_disk_write_time_ms{device="nbd12"} 0
node_disk_write_time_ms{device="nbd13"} 0
node_disk_write_time_ms{device="nbd14"} 0
node_disk_write_time_ms{device="nbd15"} 0
node_disk_write_time_ms{device="nbd2"} 0
node_disk_write_time_ms{device="nbd3"} 0
node_disk_write_time_ms{device="nbd4"} 0
node_disk_write_time_ms{device="nbd5"} 0
node_disk_write_time_ms{device="nbd6"} 0
node_disk_write_time_ms{device="nbd7"} 0
node_disk_write_time_ms{device="nbd8"} 0
node_disk_write_time_ms{device="nbd9"} 0
node_disk_write_time_ms{device="sda"} 1.79249e+06
node_disk_write_time_ms{device="sdb"} 0
####  HELP node_disk_writes_completed The total number of writes completed successfully.
####  TYPE node_disk_writes_completed counter
node_disk_writes_completed{device="md0"} 0
node_disk_writes_completed{device="nbd0"} 0
node_disk_writes_completed{device="nbd1"} 0
node_disk_writes_completed{device="nbd10"} 0
node_disk_writes_completed{device="nbd11"} 0
node_disk_writes_completed{device="nbd12"} 0
node_disk_writes_completed{device="nbd13"} 0
node_disk_writes_completed{device="nbd14"} 0
node_disk_writes_completed{device="nbd15"} 0
node_disk_writes_completed{device="nbd2"} 0
node_disk_writes_completed{device="nbd3"} 0
node_disk_writes_completed{device="nbd4"} 0
node_disk_writes_completed{device="nbd5"} 0
node_disk_writes_completed{device="nbd6"} 0
node_disk_writes_completed{device="nbd7"} 0
node_disk_writes_completed{device="nbd8"} 0
node_disk_writes_completed{device="nbd9"} 0
node_disk_writes_completed{device="sda"} 2.533356e+06
node_disk_writes_completed{device="sdb"} 0
####  HELP node_disk_writes_merged The number of writes merged. See https://www.kernel.org/doc/Documentation/iostats.txt.
####  TYPE node_disk_writes_merged counter
node_disk_writes_merged{device="md0"} 0
node_disk_writes_merged{device="nbd0"} 0
node_disk_writes_merged{device="nbd1"} 0
node_disk_writes_merged{device="nbd10"} 0
node_disk_writes_merged{device="nbd11"} 0
node_disk_writes_merged{device="nbd12"} 0
node_disk_writes_merged{device="nbd13"} 0
node_disk_writes_merged{device="nbd14"} 0
node_disk_writes_merged{device="nbd15"} 0
node_disk_writes_merged{device="nbd2"} 0
node_disk_writes_merged{device="nbd3"} 0
node_disk_writes_merged{device="nbd4"} 0
node_disk_writes_merged{device="nbd5"} 0
node_disk_writes_merged{device="nbd6"} 0
node_disk_writes_merged{device="nbd7"} 0
node_disk_writes_merged{device="nbd8"} 0
node_disk_writes_merged{device="nbd9"} 0
node_disk_writes_merged{device="sda"} 3.050216e+06
node_disk_writes_merged{device="sdb"} 0
####  HELP node_entropy_available_bits Bits of available entropy.
####  TYPE node_entropy_available_bits gauge
node_entropy_available_bits 2221
####  HELP node_exporter_build_info A metric with a constant '1' value labeled by version, revision, branch, and goversion from which node_exporter was built.
####  TYPE node_exporter_build_info gauge
node_exporter_build_info{branch="master",goversion="go1.7.5",revision="840ba5dcc71a084a3bc63cb6063003c1f94435a6",version="0.14.0"} 1
####  HELP node_filefd_allocated File descriptor statistics: allocated.
####  TYPE node_filefd_allocated gauge
node_filefd_allocated 480
####  HELP node_filefd_maximum File descriptor statistics: maximum.
####  TYPE node_filefd_maximum gauge
node_filefd_maximum 401654
####  HELP node_filesystem_avail Filesystem space available to non-root users in bytes.
####  TYPE node_filesystem_avail gauge
node_filesystem_avail{device="/dev/root",fstype="ext4",mountpoint="/"} 1.8497224704e+10
node_filesystem_avail{device="tmpfs",fstype="tmpfs",mountpoint="/run"} 1.845661696e+09
node_filesystem_avail{device="tmpfs",fstype="tmpfs",mountpoint="/run/lock"} 5.24288e+06
####  HELP node_filesystem_files Filesystem total file nodes.
####  TYPE node_filesystem_files gauge
node_filesystem_files{device="/dev/root",fstype="ext4",mountpoint="/"} 1.228608e+06
node_filesystem_files{device="tmpfs",fstype="tmpfs",mountpoint="/run"} 504217
node_filesystem_files{device="tmpfs",fstype="tmpfs",mountpoint="/run/lock"} 504217
####  HELP node_filesystem_files_free Filesystem total free file nodes.
####  TYPE node_filesystem_files_free gauge
node_filesystem_files_free{device="/dev/root",fstype="ext4",mountpoint="/"} 1.196554e+06
node_filesystem_files_free{device="tmpfs",fstype="tmpfs",mountpoint="/run"} 503026
node_filesystem_files_free{device="tmpfs",fstype="tmpfs",mountpoint="/run/lock"} 504215
####  HELP node_filesystem_free Filesystem free space in bytes.
####  TYPE node_filesystem_free gauge
node_filesystem_free{device="/dev/root",fstype="ext4",mountpoint="/"} 1.9574321152e+10
node_filesystem_free{device="tmpfs",fstype="tmpfs",mountpoint="/run"} 1.845661696e+09
node_filesystem_free{device="tmpfs",fstype="tmpfs",mountpoint="/run/lock"} 5.24288e+06
####  HELP node_filesystem_readonly Filesystem read-only status.
####  TYPE node_filesystem_readonly gauge
node_filesystem_readonly{device="/dev/root",fstype="ext4",mountpoint="/"} 0
node_filesystem_readonly{device="tmpfs",fstype="tmpfs",mountpoint="/run"} 0
node_filesystem_readonly{device="tmpfs",fstype="tmpfs",mountpoint="/run/lock"} 0
####  HELP node_filesystem_size Filesystem size in bytes.
####  TYPE node_filesystem_size gauge
node_filesystem_size{device="/dev/root",fstype="ext4",mountpoint="/"} 2.0873670656e+10
node_filesystem_size{device="tmpfs",fstype="tmpfs",mountpoint="/run"} 2.065272832e+09
node_filesystem_size{device="tmpfs",fstype="tmpfs",mountpoint="/run/lock"} 5.24288e+06
####  HELP node_forks Total number of forks.
####  TYPE node_forks counter
node_forks 732701
####  HELP node_intr Total number of interrupts serviced.
####  TYPE node_intr counter
node_intr 2.49553256e+08
####  HELP node_load1 1m load average.
####  TYPE node_load1 gauge
node_load1 0
####  HELP node_load15 15m load average.
####  TYPE node_load15 gauge
node_load15 0
####  HELP node_load5 5m load average.
####  TYPE node_load5 gauge
node_load5 0
####  HELP node_memory_Active Memory information field Active.
####  TYPE node_memory_Active gauge
node_memory_Active 2.6140672e+08
####  HELP node_memory_Active_anon Memory information field Active_anon.
####  TYPE node_memory_Active_anon gauge
node_memory_Active_anon 1.51113728e+08
####  HELP node_memory_Active_file Memory information field Active_file.
####  TYPE node_memory_Active_file gauge
node_memory_Active_file 1.10292992e+08
####  HELP node_memory_AnonPages Memory information field AnonPages.
####  TYPE node_memory_AnonPages gauge
node_memory_AnonPages 6.8112384e+07
####  HELP node_memory_Bounce Memory information field Bounce.
####  TYPE node_memory_Bounce gauge
node_memory_Bounce 0
####  HELP node_memory_Buffers Memory information field Buffers.
####  TYPE node_memory_Buffers gauge
node_memory_Buffers 2.5665536e+07
####  HELP node_memory_Cached Memory information field Cached.
####  TYPE node_memory_Cached gauge
node_memory_Cached 7.86571264e+08
####  HELP node_memory_CommitLimit Memory information field CommitLimit.
####  TYPE node_memory_CommitLimit gauge
node_memory_CommitLimit 2.333704192e+09
####  HELP node_memory_Committed_AS Memory information field Committed_AS.
####  TYPE node_memory_Committed_AS gauge
node_memory_Committed_AS 4.50797568e+08
####  HELP node_memory_DirectMap1G Memory information field DirectMap1G.
####  TYPE node_memory_DirectMap1G gauge
node_memory_DirectMap1G 3.221225472e+09
####  HELP node_memory_DirectMap2M Memory information field DirectMap2M.
####  TYPE node_memory_DirectMap2M gauge
node_memory_DirectMap2M 3.193962496e+09
####  HELP node_memory_DirectMap4k Memory information field DirectMap4k.
####  TYPE node_memory_DirectMap4k gauge
node_memory_DirectMap4k 2.7123712e+07
####  HELP node_memory_Dirty Memory information field Dirty.
####  TYPE node_memory_Dirty gauge
node_memory_Dirty 28672
####  HELP node_memory_Inactive Memory information field Inactive.
####  TYPE node_memory_Inactive gauge
node_memory_Inactive 6.1898752e+08
####  HELP node_memory_Inactive_anon Memory information field Inactive_anon.
####  TYPE node_memory_Inactive_anon gauge
node_memory_Inactive_anon 1.36650752e+08
####  HELP node_memory_Inactive_file Memory information field Inactive_file.
####  TYPE node_memory_Inactive_file gauge
node_memory_Inactive_file 4.82336768e+08
####  HELP node_memory_KernelStack Memory information field KernelStack.
####  TYPE node_memory_KernelStack gauge
node_memory_KernelStack 1.622016e+06
####  HELP node_memory_Mapped Memory information field Mapped.
####  TYPE node_memory_Mapped gauge
node_memory_Mapped 4.0800256e+07
####  HELP node_memory_MemAvailable Memory information field MemAvailable.
####  TYPE node_memory_MemAvailable gauge
node_memory_MemAvailable 3.691851776e+09
####  HELP node_memory_MemFree Memory information field MemFree.
####  TYPE node_memory_MemFree gauge
node_memory_MemFree 3.12651776e+09
####  HELP node_memory_MemTotal Memory information field MemTotal.
####  TYPE node_memory_MemTotal gauge
node_memory_MemTotal 4.13054976e+09
####  HELP node_memory_Mlocked Memory information field Mlocked.
####  TYPE node_memory_Mlocked gauge
node_memory_Mlocked 0
####  HELP node_memory_NFS_Unstable Memory information field NFS_Unstable.
####  TYPE node_memory_NFS_Unstable gauge
node_memory_NFS_Unstable 0
####  HELP node_memory_PageTables Memory information field PageTables.
####  TYPE node_memory_PageTables gauge
node_memory_PageTables 1.826816e+06
####  HELP node_memory_SReclaimable Memory information field SReclaimable.
####  TYPE node_memory_SReclaimable gauge
node_memory_SReclaimable 3.7978112e+07
####  HELP node_memory_SUnreclaim Memory information field SUnreclaim.
####  TYPE node_memory_SUnreclaim gauge
node_memory_SUnreclaim 2.02752e+07
####  HELP node_memory_Shmem Memory information field Shmem.
####  TYPE node_memory_Shmem gauge
node_memory_Shmem 2.19611136e+08
####  HELP node_memory_Slab Memory information field Slab.
####  TYPE node_memory_Slab gauge
node_memory_Slab 5.8253312e+07
####  HELP node_memory_SwapCached Memory information field SwapCached.
####  TYPE node_memory_SwapCached gauge
node_memory_SwapCached 0
####  HELP node_memory_SwapFree Memory information field SwapFree.
####  TYPE node_memory_SwapFree gauge
node_memory_SwapFree 2.6843136e+08
####  HELP node_memory_SwapTotal Memory information field SwapTotal.
####  TYPE node_memory_SwapTotal gauge
node_memory_SwapTotal 2.6843136e+08
####  HELP node_memory_Unevictable Memory information field Unevictable.
####  TYPE node_memory_Unevictable gauge
node_memory_Unevictable 0
####  HELP node_memory_VmallocChunk Memory information field VmallocChunk.
####  TYPE node_memory_VmallocChunk gauge
node_memory_VmallocChunk 0
####  HELP node_memory_VmallocTotal Memory information field VmallocTotal.
####  TYPE node_memory_VmallocTotal gauge
node_memory_VmallocTotal 3.5184372087808e+13
####  HELP node_memory_VmallocUsed Memory information field VmallocUsed.
####  TYPE node_memory_VmallocUsed gauge
node_memory_VmallocUsed 0
####  HELP node_memory_Writeback Memory information field Writeback.
####  TYPE node_memory_Writeback gauge
node_memory_Writeback 0
####  HELP node_memory_WritebackTmp Memory information field WritebackTmp.
####  TYPE node_memory_WritebackTmp gauge
node_memory_WritebackTmp 0
####  HELP node_netstat_IcmpMsg_InType11 Protocol IcmpMsg statistic InType11.
####  TYPE node_netstat_IcmpMsg_InType11 untyped
node_netstat_IcmpMsg_InType11 245113
####  HELP node_netstat_IcmpMsg_InType13 Protocol IcmpMsg statistic InType13.
####  TYPE node_netstat_IcmpMsg_InType13 untyped
node_netstat_IcmpMsg_InType13 26
####  HELP node_netstat_IcmpMsg_InType3 Protocol IcmpMsg statistic InType3.
####  TYPE node_netstat_IcmpMsg_InType3 untyped
node_netstat_IcmpMsg_InType3 73143
####  HELP node_netstat_IcmpMsg_InType5 Protocol IcmpMsg statistic InType5.
####  TYPE node_netstat_IcmpMsg_InType5 untyped
node_netstat_IcmpMsg_InType5 1
####  HELP node_netstat_IcmpMsg_InType8 Protocol IcmpMsg statistic InType8.
####  TYPE node_netstat_IcmpMsg_InType8 untyped
node_netstat_IcmpMsg_InType8 80091
####  HELP node_netstat_IcmpMsg_OutType0 Protocol IcmpMsg statistic OutType0.
####  TYPE node_netstat_IcmpMsg_OutType0 untyped
node_netstat_IcmpMsg_OutType0 80091
####  HELP node_netstat_IcmpMsg_OutType11 Protocol IcmpMsg statistic OutType11.
####  TYPE node_netstat_IcmpMsg_OutType11 untyped
node_netstat_IcmpMsg_OutType11 1
####  HELP node_netstat_IcmpMsg_OutType14 Protocol IcmpMsg statistic OutType14.
####  TYPE node_netstat_IcmpMsg_OutType14 untyped
node_netstat_IcmpMsg_OutType14 26
####  HELP node_netstat_IcmpMsg_OutType3 Protocol IcmpMsg statistic OutType3.
####  TYPE node_netstat_IcmpMsg_OutType3 untyped
node_netstat_IcmpMsg_OutType3 111791
####  HELP node_netstat_Icmp_InAddrMaskReps Protocol Icmp statistic InAddrMaskReps.
####  TYPE node_netstat_Icmp_InAddrMaskReps untyped
node_netstat_Icmp_InAddrMaskReps 0
####  HELP node_netstat_Icmp_InAddrMasks Protocol Icmp statistic InAddrMasks.
####  TYPE node_netstat_Icmp_InAddrMasks untyped
node_netstat_Icmp_InAddrMasks 0
####  HELP node_netstat_Icmp_InCsumErrors Protocol Icmp statistic InCsumErrors.
####  TYPE node_netstat_Icmp_InCsumErrors untyped
node_netstat_Icmp_InCsumErrors 2
####  HELP node_netstat_Icmp_InDestUnreachs Protocol Icmp statistic InDestUnreachs.
####  TYPE node_netstat_Icmp_InDestUnreachs untyped
node_netstat_Icmp_InDestUnreachs 73143
####  HELP node_netstat_Icmp_InEchoReps Protocol Icmp statistic InEchoReps.
####  TYPE node_netstat_Icmp_InEchoReps untyped
node_netstat_Icmp_InEchoReps 0
####  HELP node_netstat_Icmp_InEchos Protocol Icmp statistic InEchos.
####  TYPE node_netstat_Icmp_InEchos untyped
node_netstat_Icmp_InEchos 80091
####  HELP node_netstat_Icmp_InErrors Protocol Icmp statistic InErrors.
####  TYPE node_netstat_Icmp_InErrors untyped
node_netstat_Icmp_InErrors 64264
####  HELP node_netstat_Icmp_InMsgs Protocol Icmp statistic InMsgs.
####  TYPE node_netstat_Icmp_InMsgs untyped
node_netstat_Icmp_InMsgs 398376
####  HELP node_netstat_Icmp_InParmProbs Protocol Icmp statistic InParmProbs.
####  TYPE node_netstat_Icmp_InParmProbs untyped
node_netstat_Icmp_InParmProbs 0
####  HELP node_netstat_Icmp_InRedirects Protocol Icmp statistic InRedirects.
####  TYPE node_netstat_Icmp_InRedirects untyped
node_netstat_Icmp_InRedirects 1
####  HELP node_netstat_Icmp_InSrcQuenchs Protocol Icmp statistic InSrcQuenchs.
####  TYPE node_netstat_Icmp_InSrcQuenchs untyped
node_netstat_Icmp_InSrcQuenchs 0
####  HELP node_netstat_Icmp_InTimeExcds Protocol Icmp statistic InTimeExcds.
####  TYPE node_netstat_Icmp_InTimeExcds untyped
node_netstat_Icmp_InTimeExcds 245113
####  HELP node_netstat_Icmp_InTimestampReps Protocol Icmp statistic InTimestampReps.
####  TYPE node_netstat_Icmp_InTimestampReps untyped
node_netstat_Icmp_InTimestampReps 0
####  HELP node_netstat_Icmp_InTimestamps Protocol Icmp statistic InTimestamps.
####  TYPE node_netstat_Icmp_InTimestamps untyped
node_netstat_Icmp_InTimestamps 26
####  HELP node_netstat_Icmp_OutAddrMaskReps Protocol Icmp statistic OutAddrMaskReps.
####  TYPE node_netstat_Icmp_OutAddrMaskReps untyped
node_netstat_Icmp_OutAddrMaskReps 0
####  HELP node_netstat_Icmp_OutAddrMasks Protocol Icmp statistic OutAddrMasks.
####  TYPE node_netstat_Icmp_OutAddrMasks untyped
node_netstat_Icmp_OutAddrMasks 0
####  HELP node_netstat_Icmp_OutDestUnreachs Protocol Icmp statistic OutDestUnreachs.
####  TYPE node_netstat_Icmp_OutDestUnreachs untyped
node_netstat_Icmp_OutDestUnreachs 111791
####  HELP node_netstat_Icmp_OutEchoReps Protocol Icmp statistic OutEchoReps.
####  TYPE node_netstat_Icmp_OutEchoReps untyped
node_netstat_Icmp_OutEchoReps 80091
####  HELP node_netstat_Icmp_OutEchos Protocol Icmp statistic OutEchos.
####  TYPE node_netstat_Icmp_OutEchos untyped
node_netstat_Icmp_OutEchos 0
####  HELP node_netstat_Icmp_OutErrors Protocol Icmp statistic OutErrors.
####  TYPE node_netstat_Icmp_OutErrors untyped
node_netstat_Icmp_OutErrors 0
####  HELP node_netstat_Icmp_OutMsgs Protocol Icmp statistic OutMsgs.
####  TYPE node_netstat_Icmp_OutMsgs untyped
node_netstat_Icmp_OutMsgs 191909
####  HELP node_netstat_Icmp_OutParmProbs Protocol Icmp statistic OutParmProbs.
####  TYPE node_netstat_Icmp_OutParmProbs untyped
node_netstat_Icmp_OutParmProbs 0
####  HELP node_netstat_Icmp_OutRedirects Protocol Icmp statistic OutRedirects.
####  TYPE node_netstat_Icmp_OutRedirects untyped
node_netstat_Icmp_OutRedirects 0
####  HELP node_netstat_Icmp_OutSrcQuenchs Protocol Icmp statistic OutSrcQuenchs.
####  TYPE node_netstat_Icmp_OutSrcQuenchs untyped
node_netstat_Icmp_OutSrcQuenchs 0
####  HELP node_netstat_Icmp_OutTimeExcds Protocol Icmp statistic OutTimeExcds.
####  TYPE node_netstat_Icmp_OutTimeExcds untyped
node_netstat_Icmp_OutTimeExcds 1
####  HELP node_netstat_Icmp_OutTimestampReps Protocol Icmp statistic OutTimestampReps.
####  TYPE node_netstat_Icmp_OutTimestampReps untyped
node_netstat_Icmp_OutTimestampReps 26
####  HELP node_netstat_Icmp_OutTimestamps Protocol Icmp statistic OutTimestamps.
####  TYPE node_netstat_Icmp_OutTimestamps untyped
node_netstat_Icmp_OutTimestamps 0
####  HELP node_netstat_IpExt_InBcastOctets Protocol IpExt statistic InBcastOctets.
####  TYPE node_netstat_IpExt_InBcastOctets untyped
node_netstat_IpExt_InBcastOctets 1.226903e+07
####  HELP node_netstat_IpExt_InBcastPkts Protocol IpExt statistic InBcastPkts.
####  TYPE node_netstat_IpExt_InBcastPkts untyped
node_netstat_IpExt_InBcastPkts 150549
####  HELP node_netstat_IpExt_InCEPkts Protocol IpExt statistic InCEPkts.
####  TYPE node_netstat_IpExt_InCEPkts untyped
node_netstat_IpExt_InCEPkts 1109
####  HELP node_netstat_IpExt_InCsumErrors Protocol IpExt statistic InCsumErrors.
####  TYPE node_netstat_IpExt_InCsumErrors untyped
node_netstat_IpExt_InCsumErrors 0
####  HELP node_netstat_IpExt_InECT0Pkts Protocol IpExt statistic InECT0Pkts.
####  TYPE node_netstat_IpExt_InECT0Pkts untyped
node_netstat_IpExt_InECT0Pkts 3.152578e+06
####  HELP node_netstat_IpExt_InECT1Pkts Protocol IpExt statistic InECT1Pkts.
####  TYPE node_netstat_IpExt_InECT1Pkts untyped
node_netstat_IpExt_InECT1Pkts 53
####  HELP node_netstat_IpExt_InMcastOctets Protocol IpExt statistic InMcastOctets.
####  TYPE node_netstat_IpExt_InMcastOctets untyped
node_netstat_IpExt_InMcastOctets 0
####  HELP node_netstat_IpExt_InMcastPkts Protocol IpExt statistic InMcastPkts.
####  TYPE node_netstat_IpExt_InMcastPkts untyped
node_netstat_IpExt_InMcastPkts 0
####  HELP node_netstat_IpExt_InNoECTPkts Protocol IpExt statistic InNoECTPkts.
####  TYPE node_netstat_IpExt_InNoECTPkts untyped
node_netstat_IpExt_InNoECTPkts 9.6520701e+07
####  HELP node_netstat_IpExt_InNoRoutes Protocol IpExt statistic InNoRoutes.
####  TYPE node_netstat_IpExt_InNoRoutes untyped
node_netstat_IpExt_InNoRoutes 1
####  HELP node_netstat_IpExt_InOctets Protocol IpExt statistic InOctets.
####  TYPE node_netstat_IpExt_InOctets untyped
node_netstat_IpExt_InOctets 5.0768526731e+10
####  HELP node_netstat_IpExt_InTruncatedPkts Protocol IpExt statistic InTruncatedPkts.
####  TYPE node_netstat_IpExt_InTruncatedPkts untyped
node_netstat_IpExt_InTruncatedPkts 0
####  HELP node_netstat_IpExt_OutBcastOctets Protocol IpExt statistic OutBcastOctets.
####  TYPE node_netstat_IpExt_OutBcastOctets untyped
node_netstat_IpExt_OutBcastOctets 0
####  HELP node_netstat_IpExt_OutBcastPkts Protocol IpExt statistic OutBcastPkts.
####  TYPE node_netstat_IpExt_OutBcastPkts untyped
node_netstat_IpExt_OutBcastPkts 0
####  HELP node_netstat_IpExt_OutMcastOctets Protocol IpExt statistic OutMcastOctets.
####  TYPE node_netstat_IpExt_OutMcastOctets untyped
node_netstat_IpExt_OutMcastOctets 2.350574e+06
####  HELP node_netstat_IpExt_OutMcastPkts Protocol IpExt statistic OutMcastPkts.
####  TYPE node_netstat_IpExt_OutMcastPkts untyped
node_netstat_IpExt_OutMcastPkts 19267
####  HELP node_netstat_IpExt_OutOctets Protocol IpExt statistic OutOctets.
####  TYPE node_netstat_IpExt_OutOctets untyped
node_netstat_IpExt_OutOctets 1.46717792513e+11
####  HELP node_netstat_Ip_DefaultTTL Protocol Ip statistic DefaultTTL.
####  TYPE node_netstat_Ip_DefaultTTL untyped
node_netstat_Ip_DefaultTTL 64
####  HELP node_netstat_Ip_ForwDatagrams Protocol Ip statistic ForwDatagrams.
####  TYPE node_netstat_Ip_ForwDatagrams untyped
node_netstat_Ip_ForwDatagrams 4.5605107e+07
####  HELP node_netstat_Ip_Forwarding Protocol Ip statistic Forwarding.
####  TYPE node_netstat_Ip_Forwarding untyped
node_netstat_Ip_Forwarding 1
####  HELP node_netstat_Ip_FragCreates Protocol Ip statistic FragCreates.
####  TYPE node_netstat_Ip_FragCreates untyped
node_netstat_Ip_FragCreates 16
####  HELP node_netstat_Ip_FragFails Protocol Ip statistic FragFails.
####  TYPE node_netstat_Ip_FragFails untyped
node_netstat_Ip_FragFails 40
####  HELP node_netstat_Ip_FragOKs Protocol Ip statistic FragOKs.
####  TYPE node_netstat_Ip_FragOKs untyped
node_netstat_Ip_FragOKs 8
####  HELP node_netstat_Ip_InAddrErrors Protocol Ip statistic InAddrErrors.
####  TYPE node_netstat_Ip_InAddrErrors untyped
node_netstat_Ip_InAddrErrors 0
####  HELP node_netstat_Ip_InDelivers Protocol Ip statistic InDelivers.
####  TYPE node_netstat_Ip_InDelivers untyped
node_netstat_Ip_InDelivers 4.4035817e+07
####  HELP node_netstat_Ip_InDiscards Protocol Ip statistic InDiscards.
####  TYPE node_netstat_Ip_InDiscards untyped
node_netstat_Ip_InDiscards 0
####  HELP node_netstat_Ip_InHdrErrors Protocol Ip statistic InHdrErrors.
####  TYPE node_netstat_Ip_InHdrErrors untyped
node_netstat_Ip_InHdrErrors 1
####  HELP node_netstat_Ip_InReceives Protocol Ip statistic InReceives.
####  TYPE node_netstat_Ip_InReceives untyped
node_netstat_Ip_InReceives 8.9653925e+07
####  HELP node_netstat_Ip_InUnknownProtos Protocol Ip statistic InUnknownProtos.
####  TYPE node_netstat_Ip_InUnknownProtos untyped
node_netstat_Ip_InUnknownProtos 0
####  HELP node_netstat_Ip_OutDiscards Protocol Ip statistic OutDiscards.
####  TYPE node_netstat_Ip_OutDiscards untyped
node_netstat_Ip_OutDiscards 1
####  HELP node_netstat_Ip_OutNoRoutes Protocol Ip statistic OutNoRoutes.
####  TYPE node_netstat_Ip_OutNoRoutes untyped
node_netstat_Ip_OutNoRoutes 120
####  HELP node_netstat_Ip_OutRequests Protocol Ip statistic OutRequests.
####  TYPE node_netstat_Ip_OutRequests untyped
node_netstat_Ip_OutRequests 1.28536652e+08
####  HELP node_netstat_Ip_ReasmFails Protocol Ip statistic ReasmFails.
####  TYPE node_netstat_Ip_ReasmFails untyped
node_netstat_Ip_ReasmFails 5
####  HELP node_netstat_Ip_ReasmOKs Protocol Ip statistic ReasmOKs.
####  TYPE node_netstat_Ip_ReasmOKs untyped
node_netstat_Ip_ReasmOKs 8015
####  HELP node_netstat_Ip_ReasmReqds Protocol Ip statistic ReasmReqds.
####  TYPE node_netstat_Ip_ReasmReqds untyped
node_netstat_Ip_ReasmReqds 16035
####  HELP node_netstat_Ip_ReasmTimeout Protocol Ip statistic ReasmTimeout.
####  TYPE node_netstat_Ip_ReasmTimeout untyped
node_netstat_Ip_ReasmTimeout 5
####  HELP node_netstat_TcpExt_ArpFilter Protocol TcpExt statistic ArpFilter.
####  TYPE node_netstat_TcpExt_ArpFilter untyped
node_netstat_TcpExt_ArpFilter 0
####  HELP node_netstat_TcpExt_BusyPollRxPackets Protocol TcpExt statistic BusyPollRxPackets.
####  TYPE node_netstat_TcpExt_BusyPollRxPackets untyped
node_netstat_TcpExt_BusyPollRxPackets 0
####  HELP node_netstat_TcpExt_DelayedACKLocked Protocol TcpExt statistic DelayedACKLocked.
####  TYPE node_netstat_TcpExt_DelayedACKLocked untyped
node_netstat_TcpExt_DelayedACKLocked 3
####  HELP node_netstat_TcpExt_DelayedACKLost Protocol TcpExt statistic DelayedACKLost.
####  TYPE node_netstat_TcpExt_DelayedACKLost untyped
node_netstat_TcpExt_DelayedACKLost 20198
####  HELP node_netstat_TcpExt_DelayedACKs Protocol TcpExt statistic DelayedACKs.
####  TYPE node_netstat_TcpExt_DelayedACKs untyped
node_netstat_TcpExt_DelayedACKs 345334
####  HELP node_netstat_TcpExt_EmbryonicRsts Protocol TcpExt statistic EmbryonicRsts.
####  TYPE node_netstat_TcpExt_EmbryonicRsts untyped
node_netstat_TcpExt_EmbryonicRsts 4033
####  HELP node_netstat_TcpExt_IPReversePathFilter Protocol TcpExt statistic IPReversePathFilter.
####  TYPE node_netstat_TcpExt_IPReversePathFilter untyped
node_netstat_TcpExt_IPReversePathFilter 4939
####  HELP node_netstat_TcpExt_ListenDrops Protocol TcpExt statistic ListenDrops.
####  TYPE node_netstat_TcpExt_ListenDrops untyped
node_netstat_TcpExt_ListenDrops 9
####  HELP node_netstat_TcpExt_ListenOverflows Protocol TcpExt statistic ListenOverflows.
####  TYPE node_netstat_TcpExt_ListenOverflows untyped
node_netstat_TcpExt_ListenOverflows 0
####  HELP node_netstat_TcpExt_LockDroppedIcmps Protocol TcpExt statistic LockDroppedIcmps.
####  TYPE node_netstat_TcpExt_LockDroppedIcmps untyped
node_netstat_TcpExt_LockDroppedIcmps 0
####  HELP node_netstat_TcpExt_OfoPruned Protocol TcpExt statistic OfoPruned.
####  TYPE node_netstat_TcpExt_OfoPruned untyped
node_netstat_TcpExt_OfoPruned 0
####  HELP node_netstat_TcpExt_OutOfWindowIcmps Protocol TcpExt statistic OutOfWindowIcmps.
####  TYPE node_netstat_TcpExt_OutOfWindowIcmps untyped
node_netstat_TcpExt_OutOfWindowIcmps 0
####  HELP node_netstat_TcpExt_PAWSActive Protocol TcpExt statistic PAWSActive.
####  TYPE node_netstat_TcpExt_PAWSActive untyped
node_netstat_TcpExt_PAWSActive 0
####  HELP node_netstat_TcpExt_PAWSEstab Protocol TcpExt statistic PAWSEstab.
####  TYPE node_netstat_TcpExt_PAWSEstab untyped
node_netstat_TcpExt_PAWSEstab 653
####  HELP node_netstat_TcpExt_PFMemallocDrop Protocol TcpExt statistic PFMemallocDrop.
####  TYPE node_netstat_TcpExt_PFMemallocDrop untyped
node_netstat_TcpExt_PFMemallocDrop 0
####  HELP node_netstat_TcpExt_PruneCalled Protocol TcpExt statistic PruneCalled.
####  TYPE node_netstat_TcpExt_PruneCalled untyped
node_netstat_TcpExt_PruneCalled 0
####  HELP node_netstat_TcpExt_RcvPruned Protocol TcpExt statistic RcvPruned.
####  TYPE node_netstat_TcpExt_RcvPruned untyped
node_netstat_TcpExt_RcvPruned 0
####  HELP node_netstat_TcpExt_SyncookiesFailed Protocol TcpExt statistic SyncookiesFailed.
####  TYPE node_netstat_TcpExt_SyncookiesFailed untyped
node_netstat_TcpExt_SyncookiesFailed 0
####  HELP node_netstat_TcpExt_SyncookiesRecv Protocol TcpExt statistic SyncookiesRecv.
####  TYPE node_netstat_TcpExt_SyncookiesRecv untyped
node_netstat_TcpExt_SyncookiesRecv 0
####  HELP node_netstat_TcpExt_SyncookiesSent Protocol TcpExt statistic SyncookiesSent.
####  TYPE node_netstat_TcpExt_SyncookiesSent untyped
node_netstat_TcpExt_SyncookiesSent 0
####  HELP node_netstat_TcpExt_TCPACKSkippedChallenge Protocol TcpExt statistic TCPACKSkippedChallenge.
####  TYPE node_netstat_TcpExt_TCPACKSkippedChallenge untyped
node_netstat_TcpExt_TCPACKSkippedChallenge 1095
####  HELP node_netstat_TcpExt_TCPACKSkippedFinWait2 Protocol TcpExt statistic TCPACKSkippedFinWait2.
####  TYPE node_netstat_TcpExt_TCPACKSkippedFinWait2 untyped
node_netstat_TcpExt_TCPACKSkippedFinWait2 0
####  HELP node_netstat_TcpExt_TCPACKSkippedPAWS Protocol TcpExt statistic TCPACKSkippedPAWS.
####  TYPE node_netstat_TcpExt_TCPACKSkippedPAWS untyped
node_netstat_TcpExt_TCPACKSkippedPAWS 32
####  HELP node_netstat_TcpExt_TCPACKSkippedSeq Protocol TcpExt statistic TCPACKSkippedSeq.
####  TYPE node_netstat_TcpExt_TCPACKSkippedSeq untyped
node_netstat_TcpExt_TCPACKSkippedSeq 82
####  HELP node_netstat_TcpExt_TCPACKSkippedSynRecv Protocol TcpExt statistic TCPACKSkippedSynRecv.
####  TYPE node_netstat_TcpExt_TCPACKSkippedSynRecv untyped
node_netstat_TcpExt_TCPACKSkippedSynRecv 16
####  HELP node_netstat_TcpExt_TCPACKSkippedTimeWait Protocol TcpExt statistic TCPACKSkippedTimeWait.
####  TYPE node_netstat_TcpExt_TCPACKSkippedTimeWait untyped
node_netstat_TcpExt_TCPACKSkippedTimeWait 1
####  HELP node_netstat_TcpExt_TCPAbortFailed Protocol TcpExt statistic TCPAbortFailed.
####  TYPE node_netstat_TcpExt_TCPAbortFailed untyped
node_netstat_TcpExt_TCPAbortFailed 0
####  HELP node_netstat_TcpExt_TCPAbortOnClose Protocol TcpExt statistic TCPAbortOnClose.
####  TYPE node_netstat_TcpExt_TCPAbortOnClose untyped
node_netstat_TcpExt_TCPAbortOnClose 39
####  HELP node_netstat_TcpExt_TCPAbortOnData Protocol TcpExt statistic TCPAbortOnData.
####  TYPE node_netstat_TcpExt_TCPAbortOnData untyped
node_netstat_TcpExt_TCPAbortOnData 511
####  HELP node_netstat_TcpExt_TCPAbortOnLinger Protocol TcpExt statistic TCPAbortOnLinger.
####  TYPE node_netstat_TcpExt_TCPAbortOnLinger untyped
node_netstat_TcpExt_TCPAbortOnLinger 0
####  HELP node_netstat_TcpExt_TCPAbortOnMemory Protocol TcpExt statistic TCPAbortOnMemory.
####  TYPE node_netstat_TcpExt_TCPAbortOnMemory untyped
node_netstat_TcpExt_TCPAbortOnMemory 0
####  HELP node_netstat_TcpExt_TCPAbortOnTimeout Protocol TcpExt statistic TCPAbortOnTimeout.
####  TYPE node_netstat_TcpExt_TCPAbortOnTimeout untyped
node_netstat_TcpExt_TCPAbortOnTimeout 11926
####  HELP node_netstat_TcpExt_TCPAutoCorking Protocol TcpExt statistic TCPAutoCorking.
####  TYPE node_netstat_TcpExt_TCPAutoCorking untyped
node_netstat_TcpExt_TCPAutoCorking 0
####  HELP node_netstat_TcpExt_TCPBacklogDrop Protocol TcpExt statistic TCPBacklogDrop.
####  TYPE node_netstat_TcpExt_TCPBacklogDrop untyped
node_netstat_TcpExt_TCPBacklogDrop 0
####  HELP node_netstat_TcpExt_TCPChallengeACK Protocol TcpExt statistic TCPChallengeACK.
####  TYPE node_netstat_TcpExt_TCPChallengeACK untyped
node_netstat_TcpExt_TCPChallengeACK 41962
####  HELP node_netstat_TcpExt_TCPDSACKIgnoredNoUndo Protocol TcpExt statistic TCPDSACKIgnoredNoUndo.
####  TYPE node_netstat_TcpExt_TCPDSACKIgnoredNoUndo untyped
node_netstat_TcpExt_TCPDSACKIgnoredNoUndo 8563
####  HELP node_netstat_TcpExt_TCPDSACKIgnoredOld Protocol TcpExt statistic TCPDSACKIgnoredOld.
####  TYPE node_netstat_TcpExt_TCPDSACKIgnoredOld untyped
node_netstat_TcpExt_TCPDSACKIgnoredOld 0
####  HELP node_netstat_TcpExt_TCPDSACKOfoRecv Protocol TcpExt statistic TCPDSACKOfoRecv.
####  TYPE node_netstat_TcpExt_TCPDSACKOfoRecv untyped
node_netstat_TcpExt_TCPDSACKOfoRecv 20
####  HELP node_netstat_TcpExt_TCPDSACKOfoSent Protocol TcpExt statistic TCPDSACKOfoSent.
####  TYPE node_netstat_TcpExt_TCPDSACKOfoSent untyped
node_netstat_TcpExt_TCPDSACKOfoSent 67
####  HELP node_netstat_TcpExt_TCPDSACKOldSent Protocol TcpExt statistic TCPDSACKOldSent.
####  TYPE node_netstat_TcpExt_TCPDSACKOldSent untyped
node_netstat_TcpExt_TCPDSACKOldSent 20583
####  HELP node_netstat_TcpExt_TCPDSACKRecv Protocol TcpExt statistic TCPDSACKRecv.
####  TYPE node_netstat_TcpExt_TCPDSACKRecv untyped
node_netstat_TcpExt_TCPDSACKRecv 17371
####  HELP node_netstat_TcpExt_TCPDSACKUndo Protocol TcpExt statistic TCPDSACKUndo.
####  TYPE node_netstat_TcpExt_TCPDSACKUndo untyped
node_netstat_TcpExt_TCPDSACKUndo 251
####  HELP node_netstat_TcpExt_TCPDeferAcceptDrop Protocol TcpExt statistic TCPDeferAcceptDrop.
####  TYPE node_netstat_TcpExt_TCPDeferAcceptDrop untyped
node_netstat_TcpExt_TCPDeferAcceptDrop 0
####  HELP node_netstat_TcpExt_TCPFastOpenActive Protocol TcpExt statistic TCPFastOpenActive.
####  TYPE node_netstat_TcpExt_TCPFastOpenActive untyped
node_netstat_TcpExt_TCPFastOpenActive 0
####  HELP node_netstat_TcpExt_TCPFastOpenActiveFail Protocol TcpExt statistic TCPFastOpenActiveFail.
####  TYPE node_netstat_TcpExt_TCPFastOpenActiveFail untyped
node_netstat_TcpExt_TCPFastOpenActiveFail 0
####  HELP node_netstat_TcpExt_TCPFastOpenBlackhole Protocol TcpExt statistic TCPFastOpenBlackhole.
####  TYPE node_netstat_TcpExt_TCPFastOpenBlackhole untyped
node_netstat_TcpExt_TCPFastOpenBlackhole 0
####  HELP node_netstat_TcpExt_TCPFastOpenCookieReqd Protocol TcpExt statistic TCPFastOpenCookieReqd.
####  TYPE node_netstat_TcpExt_TCPFastOpenCookieReqd untyped
node_netstat_TcpExt_TCPFastOpenCookieReqd 30
####  HELP node_netstat_TcpExt_TCPFastOpenListenOverflow Protocol TcpExt statistic TCPFastOpenListenOverflow.
####  TYPE node_netstat_TcpExt_TCPFastOpenListenOverflow untyped
node_netstat_TcpExt_TCPFastOpenListenOverflow 0
####  HELP node_netstat_TcpExt_TCPFastOpenPassive Protocol TcpExt statistic TCPFastOpenPassive.
####  TYPE node_netstat_TcpExt_TCPFastOpenPassive untyped
node_netstat_TcpExt_TCPFastOpenPassive 0
####  HELP node_netstat_TcpExt_TCPFastOpenPassiveFail Protocol TcpExt statistic TCPFastOpenPassiveFail.
####  TYPE node_netstat_TcpExt_TCPFastOpenPassiveFail untyped
node_netstat_TcpExt_TCPFastOpenPassiveFail 0
####  HELP node_netstat_TcpExt_TCPFastRetrans Protocol TcpExt statistic TCPFastRetrans.
####  TYPE node_netstat_TcpExt_TCPFastRetrans untyped
node_netstat_TcpExt_TCPFastRetrans 297542
####  HELP node_netstat_TcpExt_TCPFromZeroWindowAdv Protocol TcpExt statistic TCPFromZeroWindowAdv.
####  TYPE node_netstat_TcpExt_TCPFromZeroWindowAdv untyped
node_netstat_TcpExt_TCPFromZeroWindowAdv 0
####  HELP node_netstat_TcpExt_TCPFullUndo Protocol TcpExt statistic TCPFullUndo.
####  TYPE node_netstat_TcpExt_TCPFullUndo untyped
node_netstat_TcpExt_TCPFullUndo 32
####  HELP node_netstat_TcpExt_TCPHPAcks Protocol TcpExt statistic TCPHPAcks.
####  TYPE node_netstat_TcpExt_TCPHPAcks untyped
node_netstat_TcpExt_TCPHPAcks 381583
####  HELP node_netstat_TcpExt_TCPHPHits Protocol TcpExt statistic TCPHPHits.
####  TYPE node_netstat_TcpExt_TCPHPHits untyped
node_netstat_TcpExt_TCPHPHits 693187
####  HELP node_netstat_TcpExt_TCPHystartDelayCwnd Protocol TcpExt statistic TCPHystartDelayCwnd.
####  TYPE node_netstat_TcpExt_TCPHystartDelayCwnd untyped
node_netstat_TcpExt_TCPHystartDelayCwnd 0
####  HELP node_netstat_TcpExt_TCPHystartDelayDetect Protocol TcpExt statistic TCPHystartDelayDetect.
####  TYPE node_netstat_TcpExt_TCPHystartDelayDetect untyped
node_netstat_TcpExt_TCPHystartDelayDetect 0
####  HELP node_netstat_TcpExt_TCPHystartTrainCwnd Protocol TcpExt statistic TCPHystartTrainCwnd.
####  TYPE node_netstat_TcpExt_TCPHystartTrainCwnd untyped
node_netstat_TcpExt_TCPHystartTrainCwnd 0
####  HELP node_netstat_TcpExt_TCPHystartTrainDetect Protocol TcpExt statistic TCPHystartTrainDetect.
####  TYPE node_netstat_TcpExt_TCPHystartTrainDetect untyped
node_netstat_TcpExt_TCPHystartTrainDetect 0
####  HELP node_netstat_TcpExt_TCPKeepAlive Protocol TcpExt statistic TCPKeepAlive.
####  TYPE node_netstat_TcpExt_TCPKeepAlive untyped
node_netstat_TcpExt_TCPKeepAlive 1
####  HELP node_netstat_TcpExt_TCPLossFailures Protocol TcpExt statistic TCPLossFailures.
####  TYPE node_netstat_TcpExt_TCPLossFailures untyped
node_netstat_TcpExt_TCPLossFailures 825
####  HELP node_netstat_TcpExt_TCPLossProbeRecovery Protocol TcpExt statistic TCPLossProbeRecovery.
####  TYPE node_netstat_TcpExt_TCPLossProbeRecovery untyped
node_netstat_TcpExt_TCPLossProbeRecovery 9146
####  HELP node_netstat_TcpExt_TCPLossProbes Protocol TcpExt statistic TCPLossProbes.
####  TYPE node_netstat_TcpExt_TCPLossProbes untyped
node_netstat_TcpExt_TCPLossProbes 156342
####  HELP node_netstat_TcpExt_TCPLossUndo Protocol TcpExt statistic TCPLossUndo.
####  TYPE node_netstat_TcpExt_TCPLossUndo untyped
node_netstat_TcpExt_TCPLossUndo 2224
####  HELP node_netstat_TcpExt_TCPLostRetransmit Protocol TcpExt statistic TCPLostRetransmit.
####  TYPE node_netstat_TcpExt_TCPLostRetransmit untyped
node_netstat_TcpExt_TCPLostRetransmit 541
####  HELP node_netstat_TcpExt_TCPMD5Failure Protocol TcpExt statistic TCPMD5Failure.
####  TYPE node_netstat_TcpExt_TCPMD5Failure untyped
node_netstat_TcpExt_TCPMD5Failure 0
####  HELP node_netstat_TcpExt_TCPMD5NotFound Protocol TcpExt statistic TCPMD5NotFound.
####  TYPE node_netstat_TcpExt_TCPMD5NotFound untyped
node_netstat_TcpExt_TCPMD5NotFound 0
####  HELP node_netstat_TcpExt_TCPMD5Unexpected Protocol TcpExt statistic TCPMD5Unexpected.
####  TYPE node_netstat_TcpExt_TCPMD5Unexpected untyped
node_netstat_TcpExt_TCPMD5Unexpected 0
####  HELP node_netstat_TcpExt_TCPMTUPFail Protocol TcpExt statistic TCPMTUPFail.
####  TYPE node_netstat_TcpExt_TCPMTUPFail untyped
node_netstat_TcpExt_TCPMTUPFail 0
####  HELP node_netstat_TcpExt_TCPMTUPSuccess Protocol TcpExt statistic TCPMTUPSuccess.
####  TYPE node_netstat_TcpExt_TCPMTUPSuccess untyped
node_netstat_TcpExt_TCPMTUPSuccess 0
####  HELP node_netstat_TcpExt_TCPMemoryPressures Protocol TcpExt statistic TCPMemoryPressures.
####  TYPE node_netstat_TcpExt_TCPMemoryPressures untyped
node_netstat_TcpExt_TCPMemoryPressures 0
####  HELP node_netstat_TcpExt_TCPMemoryPressuresChrono Protocol TcpExt statistic TCPMemoryPressuresChrono.
####  TYPE node_netstat_TcpExt_TCPMemoryPressuresChrono untyped
node_netstat_TcpExt_TCPMemoryPressuresChrono 0
####  HELP node_netstat_TcpExt_TCPMinTTLDrop Protocol TcpExt statistic TCPMinTTLDrop.
####  TYPE node_netstat_TcpExt_TCPMinTTLDrop untyped
node_netstat_TcpExt_TCPMinTTLDrop 0
####  HELP node_netstat_TcpExt_TCPOFODrop Protocol TcpExt statistic TCPOFODrop.
####  TYPE node_netstat_TcpExt_TCPOFODrop untyped
node_netstat_TcpExt_TCPOFODrop 0
####  HELP node_netstat_TcpExt_TCPOFOMerge Protocol TcpExt statistic TCPOFOMerge.
####  TYPE node_netstat_TcpExt_TCPOFOMerge untyped
node_netstat_TcpExt_TCPOFOMerge 67
####  HELP node_netstat_TcpExt_TCPOFOQueue Protocol TcpExt statistic TCPOFOQueue.
####  TYPE node_netstat_TcpExt_TCPOFOQueue untyped
node_netstat_TcpExt_TCPOFOQueue 19593
####  HELP node_netstat_TcpExt_TCPOrigDataSent Protocol TcpExt statistic TCPOrigDataSent.
####  TYPE node_netstat_TcpExt_TCPOrigDataSent untyped
node_netstat_TcpExt_TCPOrigDataSent 3.463732e+06
####  HELP node_netstat_TcpExt_TCPPartialUndo Protocol TcpExt statistic TCPPartialUndo.
####  TYPE node_netstat_TcpExt_TCPPartialUndo untyped
node_netstat_TcpExt_TCPPartialUndo 0
####  HELP node_netstat_TcpExt_TCPPureAcks Protocol TcpExt statistic TCPPureAcks.
####  TYPE node_netstat_TcpExt_TCPPureAcks untyped
node_netstat_TcpExt_TCPPureAcks 3.069336e+06
####  HELP node_netstat_TcpExt_TCPRcvCoalesce Protocol TcpExt statistic TCPRcvCoalesce.
####  TYPE node_netstat_TcpExt_TCPRcvCoalesce untyped
node_netstat_TcpExt_TCPRcvCoalesce 144851
####  HELP node_netstat_TcpExt_TCPRcvCollapsed Protocol TcpExt statistic TCPRcvCollapsed.
####  TYPE node_netstat_TcpExt_TCPRcvCollapsed untyped
node_netstat_TcpExt_TCPRcvCollapsed 0
####  HELP node_netstat_TcpExt_TCPRenoFailures Protocol TcpExt statistic TCPRenoFailures.
####  TYPE node_netstat_TcpExt_TCPRenoFailures untyped
node_netstat_TcpExt_TCPRenoFailures 0
####  HELP node_netstat_TcpExt_TCPRenoRecovery Protocol TcpExt statistic TCPRenoRecovery.
####  TYPE node_netstat_TcpExt_TCPRenoRecovery untyped
node_netstat_TcpExt_TCPRenoRecovery 0
####  HELP node_netstat_TcpExt_TCPRenoRecoveryFail Protocol TcpExt statistic TCPRenoRecoveryFail.
####  TYPE node_netstat_TcpExt_TCPRenoRecoveryFail untyped
node_netstat_TcpExt_TCPRenoRecoveryFail 0
####  HELP node_netstat_TcpExt_TCPRenoReorder Protocol TcpExt statistic TCPRenoReorder.
####  TYPE node_netstat_TcpExt_TCPRenoReorder untyped
node_netstat_TcpExt_TCPRenoReorder 0
####  HELP node_netstat_TcpExt_TCPReqQFullDoCookies Protocol TcpExt statistic TCPReqQFullDoCookies.
####  TYPE node_netstat_TcpExt_TCPReqQFullDoCookies untyped
node_netstat_TcpExt_TCPReqQFullDoCookies 0
####  HELP node_netstat_TcpExt_TCPReqQFullDrop Protocol TcpExt statistic TCPReqQFullDrop.
####  TYPE node_netstat_TcpExt_TCPReqQFullDrop untyped
node_netstat_TcpExt_TCPReqQFullDrop 0
####  HELP node_netstat_TcpExt_TCPRetransFail Protocol TcpExt statistic TCPRetransFail.
####  TYPE node_netstat_TcpExt_TCPRetransFail untyped
node_netstat_TcpExt_TCPRetransFail 0
####  HELP node_netstat_TcpExt_TCPSACKDiscard Protocol TcpExt statistic TCPSACKDiscard.
####  TYPE node_netstat_TcpExt_TCPSACKDiscard untyped
node_netstat_TcpExt_TCPSACKDiscard 0
####  HELP node_netstat_TcpExt_TCPSACKReneging Protocol TcpExt statistic TCPSACKReneging.
####  TYPE node_netstat_TcpExt_TCPSACKReneging untyped
node_netstat_TcpExt_TCPSACKReneging 0
####  HELP node_netstat_TcpExt_TCPSACKReorder Protocol TcpExt statistic TCPSACKReorder.
####  TYPE node_netstat_TcpExt_TCPSACKReorder untyped
node_netstat_TcpExt_TCPSACKReorder 1379
####  HELP node_netstat_TcpExt_TCPSYNChallenge Protocol TcpExt statistic TCPSYNChallenge.
####  TYPE node_netstat_TcpExt_TCPSYNChallenge untyped
node_netstat_TcpExt_TCPSYNChallenge 0
####  HELP node_netstat_TcpExt_TCPSackFailures Protocol TcpExt statistic TCPSackFailures.
####  TYPE node_netstat_TcpExt_TCPSackFailures untyped
node_netstat_TcpExt_TCPSackFailures 41504
####  HELP node_netstat_TcpExt_TCPSackMerged Protocol TcpExt statistic TCPSackMerged.
####  TYPE node_netstat_TcpExt_TCPSackMerged untyped
node_netstat_TcpExt_TCPSackMerged 29
####  HELP node_netstat_TcpExt_TCPSackRecovery Protocol TcpExt statistic TCPSackRecovery.
####  TYPE node_netstat_TcpExt_TCPSackRecovery untyped
node_netstat_TcpExt_TCPSackRecovery 286571
####  HELP node_netstat_TcpExt_TCPSackRecoveryFail Protocol TcpExt statistic TCPSackRecoveryFail.
####  TYPE node_netstat_TcpExt_TCPSackRecoveryFail untyped
node_netstat_TcpExt_TCPSackRecoveryFail 3503
####  HELP node_netstat_TcpExt_TCPSackShiftFallback Protocol TcpExt statistic TCPSackShiftFallback.
####  TYPE node_netstat_TcpExt_TCPSackShiftFallback untyped
node_netstat_TcpExt_TCPSackShiftFallback 333241
####  HELP node_netstat_TcpExt_TCPSackShifted Protocol TcpExt statistic TCPSackShifted.
####  TYPE node_netstat_TcpExt_TCPSackShifted untyped
node_netstat_TcpExt_TCPSackShifted 4
####  HELP node_netstat_TcpExt_TCPSlowStartRetrans Protocol TcpExt statistic TCPSlowStartRetrans.
####  TYPE node_netstat_TcpExt_TCPSlowStartRetrans untyped
node_netstat_TcpExt_TCPSlowStartRetrans 5818
####  HELP node_netstat_TcpExt_TCPSpuriousRTOs Protocol TcpExt statistic TCPSpuriousRTOs.
####  TYPE node_netstat_TcpExt_TCPSpuriousRTOs untyped
node_netstat_TcpExt_TCPSpuriousRTOs 17
####  HELP node_netstat_TcpExt_TCPSpuriousRtxHostQueues Protocol TcpExt statistic TCPSpuriousRtxHostQueues.
####  TYPE node_netstat_TcpExt_TCPSpuriousRtxHostQueues untyped
node_netstat_TcpExt_TCPSpuriousRtxHostQueues 0
####  HELP node_netstat_TcpExt_TCPSynRetrans Protocol TcpExt statistic TCPSynRetrans.
####  TYPE node_netstat_TcpExt_TCPSynRetrans untyped
node_netstat_TcpExt_TCPSynRetrans 136194
####  HELP node_netstat_TcpExt_TCPTSReorder Protocol TcpExt statistic TCPTSReorder.
####  TYPE node_netstat_TcpExt_TCPTSReorder untyped
node_netstat_TcpExt_TCPTSReorder 0
####  HELP node_netstat_TcpExt_TCPTimeWaitOverflow Protocol TcpExt statistic TCPTimeWaitOverflow.
####  TYPE node_netstat_TcpExt_TCPTimeWaitOverflow untyped
node_netstat_TcpExt_TCPTimeWaitOverflow 0
####  HELP node_netstat_TcpExt_TCPTimeouts Protocol TcpExt statistic TCPTimeouts.
####  TYPE node_netstat_TcpExt_TCPTimeouts untyped
node_netstat_TcpExt_TCPTimeouts 134708
####  HELP node_netstat_TcpExt_TCPToZeroWindowAdv Protocol TcpExt statistic TCPToZeroWindowAdv.
####  TYPE node_netstat_TcpExt_TCPToZeroWindowAdv untyped
node_netstat_TcpExt_TCPToZeroWindowAdv 0
####  HELP node_netstat_TcpExt_TCPWantZeroWindowAdv Protocol TcpExt statistic TCPWantZeroWindowAdv.
####  TYPE node_netstat_TcpExt_TCPWantZeroWindowAdv untyped
node_netstat_TcpExt_TCPWantZeroWindowAdv 0
####  HELP node_netstat_TcpExt_TCPWinProbe Protocol TcpExt statistic TCPWinProbe.
####  TYPE node_netstat_TcpExt_TCPWinProbe untyped
node_netstat_TcpExt_TCPWinProbe 0
####  HELP node_netstat_TcpExt_TW Protocol TcpExt statistic TW.
####  TYPE node_netstat_TcpExt_TW untyped
node_netstat_TcpExt_TW 364098
####  HELP node_netstat_TcpExt_TWKilled Protocol TcpExt statistic TWKilled.
####  TYPE node_netstat_TcpExt_TWKilled untyped
node_netstat_TcpExt_TWKilled 0
####  HELP node_netstat_TcpExt_TWRecycled Protocol TcpExt statistic TWRecycled.
####  TYPE node_netstat_TcpExt_TWRecycled untyped
node_netstat_TcpExt_TWRecycled 0
####  HELP node_netstat_Tcp_ActiveOpens Protocol Tcp statistic ActiveOpens.
####  TYPE node_netstat_Tcp_ActiveOpens untyped
node_netstat_Tcp_ActiveOpens 2184
####  HELP node_netstat_Tcp_AttemptFails Protocol Tcp statistic AttemptFails.
####  TYPE node_netstat_Tcp_AttemptFails untyped
node_netstat_Tcp_AttemptFails 4037
####  HELP node_netstat_Tcp_CurrEstab Protocol Tcp statistic CurrEstab.
####  TYPE node_netstat_Tcp_CurrEstab untyped
node_netstat_Tcp_CurrEstab 1
####  HELP node_netstat_Tcp_EstabResets Protocol Tcp statistic EstabResets.
####  TYPE node_netstat_Tcp_EstabResets untyped
node_netstat_Tcp_EstabResets 1748
####  HELP node_netstat_Tcp_InCsumErrors Protocol Tcp statistic InCsumErrors.
####  TYPE node_netstat_Tcp_InCsumErrors untyped
node_netstat_Tcp_InCsumErrors 691
####  HELP node_netstat_Tcp_InErrs Protocol Tcp statistic InErrs.
####  TYPE node_netstat_Tcp_InErrs untyped
node_netstat_Tcp_InErrs 691
####  HELP node_netstat_Tcp_InSegs Protocol Tcp statistic InSegs.
####  TYPE node_netstat_Tcp_InSegs untyped
node_netstat_Tcp_InSegs 6.774305e+06
####  HELP node_netstat_Tcp_MaxConn Protocol Tcp statistic MaxConn.
####  TYPE node_netstat_Tcp_MaxConn untyped
node_netstat_Tcp_MaxConn -1
####  HELP node_netstat_Tcp_OutRsts Protocol Tcp statistic OutRsts.
####  TYPE node_netstat_Tcp_OutRsts untyped
node_netstat_Tcp_OutRsts 321493
####  HELP node_netstat_Tcp_OutSegs Protocol Tcp statistic OutSegs.
####  TYPE node_netstat_Tcp_OutSegs untyped
node_netstat_Tcp_OutSegs 6.453715e+06
####  HELP node_netstat_Tcp_PassiveOpens Protocol Tcp statistic PassiveOpens.
####  TYPE node_netstat_Tcp_PassiveOpens untyped
node_netstat_Tcp_PassiveOpens 532633
####  HELP node_netstat_Tcp_RetransSegs Protocol Tcp statistic RetransSegs.
####  TYPE node_netstat_Tcp_RetransSegs untyped
node_netstat_Tcp_RetransSegs 725992
####  HELP node_netstat_Tcp_RtoAlgorithm Protocol Tcp statistic RtoAlgorithm.
####  TYPE node_netstat_Tcp_RtoAlgorithm untyped
node_netstat_Tcp_RtoAlgorithm 1
####  HELP node_netstat_Tcp_RtoMax Protocol Tcp statistic RtoMax.
####  TYPE node_netstat_Tcp_RtoMax untyped
node_netstat_Tcp_RtoMax 120000
####  HELP node_netstat_Tcp_RtoMin Protocol Tcp statistic RtoMin.
####  TYPE node_netstat_Tcp_RtoMin untyped
node_netstat_Tcp_RtoMin 200
####  HELP node_netstat_UdpLite_IgnoredMulti Protocol UdpLite statistic IgnoredMulti.
####  TYPE node_netstat_UdpLite_IgnoredMulti untyped
node_netstat_UdpLite_IgnoredMulti 0
####  HELP node_netstat_UdpLite_InCsumErrors Protocol UdpLite statistic InCsumErrors.
####  TYPE node_netstat_UdpLite_InCsumErrors untyped
node_netstat_UdpLite_InCsumErrors 0
####  HELP node_netstat_UdpLite_InDatagrams Protocol UdpLite statistic InDatagrams.
####  TYPE node_netstat_UdpLite_InDatagrams untyped
node_netstat_UdpLite_InDatagrams 0
####  HELP node_netstat_UdpLite_InErrors Protocol UdpLite statistic InErrors.
####  TYPE node_netstat_UdpLite_InErrors untyped
node_netstat_UdpLite_InErrors 0
####  HELP node_netstat_UdpLite_NoPorts Protocol UdpLite statistic NoPorts.
####  TYPE node_netstat_UdpLite_NoPorts untyped
node_netstat_UdpLite_NoPorts 0
####  HELP node_netstat_UdpLite_OutDatagrams Protocol UdpLite statistic OutDatagrams.
####  TYPE node_netstat_UdpLite_OutDatagrams untyped
node_netstat_UdpLite_OutDatagrams 0
####  HELP node_netstat_UdpLite_RcvbufErrors Protocol UdpLite statistic RcvbufErrors.
####  TYPE node_netstat_UdpLite_RcvbufErrors untyped
node_netstat_UdpLite_RcvbufErrors 0
####  HELP node_netstat_UdpLite_SndbufErrors Protocol UdpLite statistic SndbufErrors.
####  TYPE node_netstat_UdpLite_SndbufErrors untyped
node_netstat_UdpLite_SndbufErrors 0
####  HELP node_netstat_Udp_IgnoredMulti Protocol Udp statistic IgnoredMulti.
####  TYPE node_netstat_Udp_IgnoredMulti untyped
node_netstat_Udp_IgnoredMulti 150549
####  HELP node_netstat_Udp_InCsumErrors Protocol Udp statistic InCsumErrors.
####  TYPE node_netstat_Udp_InCsumErrors untyped
node_netstat_Udp_InCsumErrors 66
####  HELP node_netstat_Udp_InDatagrams Protocol Udp statistic InDatagrams.
####  TYPE node_netstat_Udp_InDatagrams untyped
node_netstat_Udp_InDatagrams 3.6730784e+07
####  HELP node_netstat_Udp_InErrors Protocol Udp statistic InErrors.
####  TYPE node_netstat_Udp_InErrors untyped
node_netstat_Udp_InErrors 7041
####  HELP node_netstat_Udp_NoPorts Protocol Udp statistic NoPorts.
####  TYPE node_netstat_Udp_NoPorts untyped
node_netstat_Udp_NoPorts 47156
####  HELP node_netstat_Udp_OutDatagrams Protocol Udp statistic OutDatagrams.
####  TYPE node_netstat_Udp_OutDatagrams untyped
node_netstat_Udp_OutDatagrams 7.6493385e+07
####  HELP node_netstat_Udp_RcvbufErrors Protocol Udp statistic RcvbufErrors.
####  TYPE node_netstat_Udp_RcvbufErrors untyped
node_netstat_Udp_RcvbufErrors 6975
####  HELP node_netstat_Udp_SndbufErrors Protocol Udp statistic SndbufErrors.
####  TYPE node_netstat_Udp_SndbufErrors untyped
node_netstat_Udp_SndbufErrors 0
####  HELP node_network_receive_bytes Network device statistic receive_bytes.
####  TYPE node_network_receive_bytes gauge
node_network_receive_bytes{device="dummy0"} 0
node_network_receive_bytes{device="erspan0"} 0
node_network_receive_bytes{device="eth0"} 5.1364491855e+10
node_network_receive_bytes{device="gre0"} 0
node_network_receive_bytes{device="gretap0"} 0
node_network_receive_bytes{device="ip6_vti0"} 0
node_network_receive_bytes{device="ip6gre0"} 0
node_network_receive_bytes{device="ip6tnl0"} 0
node_network_receive_bytes{device="ip_vti0"} 0
node_network_receive_bytes{device="lo"} 46112
node_network_receive_bytes{device="sit0"} 0
node_network_receive_bytes{device="teql0"} 0
node_network_receive_bytes{device="tunl0"} 0
node_network_receive_bytes{device="zt0"} 2.630108603e+09
####  HELP node_network_receive_compressed Network device statistic receive_compressed.
####  TYPE node_network_receive_compressed gauge
node_network_receive_compressed{device="dummy0"} 0
node_network_receive_compressed{device="erspan0"} 0
node_network_receive_compressed{device="eth0"} 0
node_network_receive_compressed{device="gre0"} 0
node_network_receive_compressed{device="gretap0"} 0
node_network_receive_compressed{device="ip6_vti0"} 0
node_network_receive_compressed{device="ip6gre0"} 0
node_network_receive_compressed{device="ip6tnl0"} 0
node_network_receive_compressed{device="ip_vti0"} 0
node_network_receive_compressed{device="lo"} 0
node_network_receive_compressed{device="sit0"} 0
node_network_receive_compressed{device="teql0"} 0
node_network_receive_compressed{device="tunl0"} 0
node_network_receive_compressed{device="zt0"} 0
####  HELP node_network_receive_drop Network device statistic receive_drop.
####  TYPE node_network_receive_drop gauge
node_network_receive_drop{device="dummy0"} 0
node_network_receive_drop{device="erspan0"} 0
node_network_receive_drop{device="eth0"} 0
node_network_receive_drop{device="gre0"} 0
node_network_receive_drop{device="gretap0"} 0
node_network_receive_drop{device="ip6_vti0"} 0
node_network_receive_drop{device="ip6gre0"} 0
node_network_receive_drop{device="ip6tnl0"} 0
node_network_receive_drop{device="ip_vti0"} 0
node_network_receive_drop{device="lo"} 0
node_network_receive_drop{device="sit0"} 0
node_network_receive_drop{device="teql0"} 0
node_network_receive_drop{device="tunl0"} 0
node_network_receive_drop{device="zt0"} 0
####  HELP node_network_receive_errs Network device statistic receive_errs.
####  TYPE node_network_receive_errs gauge
node_network_receive_errs{device="dummy0"} 0
node_network_receive_errs{device="erspan0"} 0
node_network_receive_errs{device="eth0"} 0
node_network_receive_errs{device="gre0"} 0
node_network_receive_errs{device="gretap0"} 0
node_network_receive_errs{device="ip6_vti0"} 0
node_network_receive_errs{device="ip6gre0"} 0
node_network_receive_errs{device="ip6tnl0"} 0
node_network_receive_errs{device="ip_vti0"} 0
node_network_receive_errs{device="lo"} 0
node_network_receive_errs{device="sit0"} 0
node_network_receive_errs{device="teql0"} 0
node_network_receive_errs{device="tunl0"} 0
node_network_receive_errs{device="zt0"} 0
####  HELP node_network_receive_fifo Network device statistic receive_fifo.
####  TYPE node_network_receive_fifo gauge
node_network_receive_fifo{device="dummy0"} 0
node_network_receive_fifo{device="erspan0"} 0
node_network_receive_fifo{device="eth0"} 0
node_network_receive_fifo{device="gre0"} 0
node_network_receive_fifo{device="gretap0"} 0
node_network_receive_fifo{device="ip6_vti0"} 0
node_network_receive_fifo{device="ip6gre0"} 0
node_network_receive_fifo{device="ip6tnl0"} 0
node_network_receive_fifo{device="ip_vti0"} 0
node_network_receive_fifo{device="lo"} 0
node_network_receive_fifo{device="sit0"} 0
node_network_receive_fifo{device="teql0"} 0
node_network_receive_fifo{device="tunl0"} 0
node_network_receive_fifo{device="zt0"} 0
####  HELP node_network_receive_frame Network device statistic receive_frame.
####  TYPE node_network_receive_frame gauge
node_network_receive_frame{device="dummy0"} 0
node_network_receive_frame{device="erspan0"} 0
node_network_receive_frame{device="eth0"} 0
node_network_receive_frame{device="gre0"} 0
node_network_receive_frame{device="gretap0"} 0
node_network_receive_frame{device="ip6_vti0"} 0
node_network_receive_frame{device="ip6gre0"} 0
node_network_receive_frame{device="ip6tnl0"} 0
node_network_receive_frame{device="ip_vti0"} 0
node_network_receive_frame{device="lo"} 0
node_network_receive_frame{device="sit0"} 0
node_network_receive_frame{device="teql0"} 0
node_network_receive_frame{device="tunl0"} 0
node_network_receive_frame{device="zt0"} 0
####  HELP node_network_receive_multicast Network device statistic receive_multicast.
####  TYPE node_network_receive_multicast gauge
node_network_receive_multicast{device="dummy0"} 0
node_network_receive_multicast{device="erspan0"} 0
node_network_receive_multicast{device="eth0"} 0
node_network_receive_multicast{device="gre0"} 0
node_network_receive_multicast{device="gretap0"} 0
node_network_receive_multicast{device="ip6_vti0"} 0
node_network_receive_multicast{device="ip6gre0"} 0
node_network_receive_multicast{device="ip6tnl0"} 0
node_network_receive_multicast{device="ip_vti0"} 0
node_network_receive_multicast{device="lo"} 0
node_network_receive_multicast{device="sit0"} 0
node_network_receive_multicast{device="teql0"} 0
node_network_receive_multicast{device="tunl0"} 0
node_network_receive_multicast{device="zt0"} 0
####  HELP node_network_receive_packets Network device statistic receive_packets.
####  TYPE node_network_receive_packets gauge
node_network_receive_packets{device="dummy0"} 0
node_network_receive_packets{device="erspan0"} 0
node_network_receive_packets{device="eth0"} 8.0749291e+07
node_network_receive_packets{device="gre0"} 0
node_network_receive_packets{device="gretap0"} 0
node_network_receive_packets{device="ip6_vti0"} 0
node_network_receive_packets{device="ip6gre0"} 0
node_network_receive_packets{device="ip6tnl0"} 0
node_network_receive_packets{device="ip_vti0"} 0
node_network_receive_packets{device="lo"} 127
node_network_receive_packets{device="sit0"} 0
node_network_receive_packets{device="teql0"} 0
node_network_receive_packets{device="tunl0"} 0
node_network_receive_packets{device="zt0"} 2.6003584e+07
####  HELP node_network_transmit_bytes Network device statistic transmit_bytes.
####  TYPE node_network_transmit_bytes gauge
node_network_transmit_bytes{device="dummy0"} 0
node_network_transmit_bytes{device="erspan0"} 0
node_network_transmit_bytes{device="eth0"} 5.8941990389e+10
node_network_transmit_bytes{device="gre0"} 0
node_network_transmit_bytes{device="gretap0"} 0
node_network_transmit_bytes{device="ip6_vti0"} 0
node_network_transmit_bytes{device="ip6gre0"} 0
node_network_transmit_bytes{device="ip6tnl0"} 0
node_network_transmit_bytes{device="ip_vti0"} 0
node_network_transmit_bytes{device="lo"} 46112
node_network_transmit_bytes{device="sit0"} 0
node_network_transmit_bytes{device="teql0"} 0
node_network_transmit_bytes{device="tunl0"} 0
node_network_transmit_bytes{device="zt0"} 4.7786816413e+10
####  HELP node_network_transmit_compressed Network device statistic transmit_compressed.
####  TYPE node_network_transmit_compressed gauge
node_network_transmit_compressed{device="dummy0"} 0
node_network_transmit_compressed{device="erspan0"} 0
node_network_transmit_compressed{device="eth0"} 0
node_network_transmit_compressed{device="gre0"} 0
node_network_transmit_compressed{device="gretap0"} 0
node_network_transmit_compressed{device="ip6_vti0"} 0
node_network_transmit_compressed{device="ip6gre0"} 0
node_network_transmit_compressed{device="ip6tnl0"} 0
node_network_transmit_compressed{device="ip_vti0"} 0
node_network_transmit_compressed{device="lo"} 0
node_network_transmit_compressed{device="sit0"} 0
node_network_transmit_compressed{device="teql0"} 0
node_network_transmit_compressed{device="tunl0"} 0
node_network_transmit_compressed{device="zt0"} 0
####  HELP node_network_transmit_drop Network device statistic transmit_drop.
####  TYPE node_network_transmit_drop gauge
node_network_transmit_drop{device="dummy0"} 0
node_network_transmit_drop{device="erspan0"} 0
node_network_transmit_drop{device="eth0"} 0
node_network_transmit_drop{device="gre0"} 0
node_network_transmit_drop{device="gretap0"} 0
node_network_transmit_drop{device="ip6_vti0"} 0
node_network_transmit_drop{device="ip6gre0"} 0
node_network_transmit_drop{device="ip6tnl0"} 0
node_network_transmit_drop{device="ip_vti0"} 0
node_network_transmit_drop{device="lo"} 0
node_network_transmit_drop{device="sit0"} 0
node_network_transmit_drop{device="teql0"} 0
node_network_transmit_drop{device="tunl0"} 0
node_network_transmit_drop{device="zt0"} 0
####  HELP node_network_transmit_errs Network device statistic transmit_errs.
####  TYPE node_network_transmit_errs gauge
node_network_transmit_errs{device="dummy0"} 0
node_network_transmit_errs{device="erspan0"} 0
node_network_transmit_errs{device="eth0"} 0
node_network_transmit_errs{device="gre0"} 0
node_network_transmit_errs{device="gretap0"} 0
node_network_transmit_errs{device="ip6_vti0"} 0
node_network_transmit_errs{device="ip6gre0"} 0
node_network_transmit_errs{device="ip6tnl0"} 0
node_network_transmit_errs{device="ip_vti0"} 0
node_network_transmit_errs{device="lo"} 0
node_network_transmit_errs{device="sit0"} 0
node_network_transmit_errs{device="teql0"} 0
node_network_transmit_errs{device="tunl0"} 0
node_network_transmit_errs{device="zt0"} 0
####  HELP node_network_transmit_fifo Network device statistic transmit_fifo.
####  TYPE node_network_transmit_fifo gauge
node_network_transmit_fifo{device="dummy0"} 0
node_network_transmit_fifo{device="erspan0"} 0
node_network_transmit_fifo{device="eth0"} 0
node_network_transmit_fifo{device="gre0"} 0
node_network_transmit_fifo{device="gretap0"} 0
node_network_transmit_fifo{device="ip6_vti0"} 0
node_network_transmit_fifo{device="ip6gre0"} 0
node_network_transmit_fifo{device="ip6tnl0"} 0
node_network_transmit_fifo{device="ip_vti0"} 0
node_network_transmit_fifo{device="lo"} 0
node_network_transmit_fifo{device="sit0"} 0
node_network_transmit_fifo{device="teql0"} 0
node_network_transmit_fifo{device="tunl0"} 0
node_network_transmit_fifo{device="zt0"} 0
####  HELP node_network_transmit_frame Network device statistic transmit_frame.
####  TYPE node_network_transmit_frame gauge
node_network_transmit_frame{device="dummy0"} 0
node_network_transmit_frame{device="erspan0"} 0
node_network_transmit_frame{device="eth0"} 0
node_network_transmit_frame{device="gre0"} 0
node_network_transmit_frame{device="gretap0"} 0
node_network_transmit_frame{device="ip6_vti0"} 0
node_network_transmit_frame{device="ip6gre0"} 0
node_network_transmit_frame{device="ip6tnl0"} 0
node_network_transmit_frame{device="ip_vti0"} 0
node_network_transmit_frame{device="lo"} 0
node_network_transmit_frame{device="sit0"} 0
node_network_transmit_frame{device="teql0"} 0
node_network_transmit_frame{device="tunl0"} 0
node_network_transmit_frame{device="zt0"} 0
####  HELP node_network_transmit_multicast Network device statistic transmit_multicast.
####  TYPE node_network_transmit_multicast gauge
node_network_transmit_multicast{device="dummy0"} 0
node_network_transmit_multicast{device="erspan0"} 0
node_network_transmit_multicast{device="eth0"} 0
node_network_transmit_multicast{device="gre0"} 0
node_network_transmit_multicast{device="gretap0"} 0
node_network_transmit_multicast{device="ip6_vti0"} 0
node_network_transmit_multicast{device="ip6gre0"} 0
node_network_transmit_multicast{device="ip6tnl0"} 0
node_network_transmit_multicast{device="ip_vti0"} 0
node_network_transmit_multicast{device="lo"} 0
node_network_transmit_multicast{device="sit0"} 0
node_network_transmit_multicast{device="teql0"} 0
node_network_transmit_multicast{device="tunl0"} 0
node_network_transmit_multicast{device="zt0"} 0
####  HELP node_network_transmit_packets Network device statistic transmit_packets.
####  TYPE node_network_transmit_packets gauge
node_network_transmit_packets{device="dummy0"} 0
node_network_transmit_packets{device="erspan0"} 0
node_network_transmit_packets{device="eth0"} 1.06602383e+08
node_network_transmit_packets{device="gre0"} 0
node_network_transmit_packets{device="gretap0"} 0
node_network_transmit_packets{device="ip6_vti0"} 0
node_network_transmit_packets{device="ip6gre0"} 0
node_network_transmit_packets{device="ip6tnl0"} 0
node_network_transmit_packets{device="ip_vti0"} 0
node_network_transmit_packets{device="lo"} 127
node_network_transmit_packets{device="sit0"} 0
node_network_transmit_packets{device="teql0"} 0
node_network_transmit_packets{device="tunl0"} 0
node_network_transmit_packets{device="zt0"} 3.8529746e+07
####  HELP node_nf_conntrack_entries Number of currently allocated flow entries for connection tracking.
####  TYPE node_nf_conntrack_entries gauge
node_nf_conntrack_entries 66
####  HELP node_nf_conntrack_entries_limit Maximum size of connection tracking table.
####  TYPE node_nf_conntrack_entries_limit gauge
node_nf_conntrack_entries_limit 65536
####  HELP node_procs_blocked Number of processes blocked waiting for I/O to complete.
####  TYPE node_procs_blocked gauge
node_procs_blocked 0
####  HELP node_procs_running Number of processes in runnable state.
####  TYPE node_procs_running gauge
node_procs_running 3
####  HELP node_scrape_collector_duration_seconds node_exporter: Duration of a collector scrape.
####  TYPE node_scrape_collector_duration_seconds gauge
node_scrape_collector_duration_seconds{collector="conntrack"} 6.710100000000001e-05
node_scrape_collector_duration_seconds{collector="diskstats"} 0.0006620580000000001
node_scrape_collector_duration_seconds{collector="edac"} 3.8727000000000004e-05
node_scrape_collector_duration_seconds{collector="entropy"} 2.0152000000000003e-05
node_scrape_collector_duration_seconds{collector="filefd"} 4.6801e-05
node_scrape_collector_duration_seconds{collector="filesystem"} 0.0005411270000000001
node_scrape_collector_duration_seconds{collector="hwmon"} 2.8931e-05
node_scrape_collector_duration_seconds{collector="infiniband"} 6.148400000000001e-05
node_scrape_collector_duration_seconds{collector="loadavg"} 5.394e-05
node_scrape_collector_duration_seconds{collector="mdadm"} 4.5039e-05
node_scrape_collector_duration_seconds{collector="meminfo"} 0.00036728300000000004
node_scrape_collector_duration_seconds{collector="netdev"} 0.00048281800000000004
node_scrape_collector_duration_seconds{collector="netstat"} 0.000940225
node_scrape_collector_duration_seconds{collector="sockstat"} 0.000119078
node_scrape_collector_duration_seconds{collector="stat"} 0.000136076
node_scrape_collector_duration_seconds{collector="textfile"} 3.7900000000000005e-07
node_scrape_collector_duration_seconds{collector="time"} 9.971e-06
node_scrape_collector_duration_seconds{collector="uname"} 2.5235e-05
node_scrape_collector_duration_seconds{collector="vmstat"} 0.000370269
node_scrape_collector_duration_seconds{collector="wifi"} 0.001591037
node_scrape_collector_duration_seconds{collector="zfs"} 3.7682e-05
####  HELP node_scrape_collector_success node_exporter: Whether a collector succeeded.
####  TYPE node_scrape_collector_success gauge
node_scrape_collector_success{collector="conntrack"} 1
node_scrape_collector_success{collector="diskstats"} 1
node_scrape_collector_success{collector="edac"} 1
node_scrape_collector_success{collector="entropy"} 1
node_scrape_collector_success{collector="filefd"} 1
node_scrape_collector_success{collector="filesystem"} 1
node_scrape_collector_success{collector="hwmon"} 1
node_scrape_collector_success{collector="infiniband"} 1
node_scrape_collector_success{collector="loadavg"} 1
node_scrape_collector_success{collector="mdadm"} 1
node_scrape_collector_success{collector="meminfo"} 1
node_scrape_collector_success{collector="netdev"} 1
node_scrape_collector_success{collector="netstat"} 1
node_scrape_collector_success{collector="sockstat"} 1
node_scrape_collector_success{collector="stat"} 1
node_scrape_collector_success{collector="textfile"} 1
node_scrape_collector_success{collector="time"} 1
node_scrape_collector_success{collector="uname"} 1
node_scrape_collector_success{collector="vmstat"} 1
node_scrape_collector_success{collector="wifi"} 1
node_scrape_collector_success{collector="zfs"} 1
####  HELP node_sockstat_FRAG_inuse Number of FRAG sockets in state inuse.
####  TYPE node_sockstat_FRAG_inuse gauge
node_sockstat_FRAG_inuse 0
####  HELP node_sockstat_FRAG_memory Number of FRAG sockets in state memory.
####  TYPE node_sockstat_FRAG_memory gauge
node_sockstat_FRAG_memory 0
####  HELP node_sockstat_RAW_inuse Number of RAW sockets in state inuse.
####  TYPE node_sockstat_RAW_inuse gauge
node_sockstat_RAW_inuse 0
####  HELP node_sockstat_TCP_alloc Number of TCP sockets in state alloc.
####  TYPE node_sockstat_TCP_alloc gauge
node_sockstat_TCP_alloc 12
####  HELP node_sockstat_TCP_inuse Number of TCP sockets in state inuse.
####  TYPE node_sockstat_TCP_inuse gauge
node_sockstat_TCP_inuse 6
####  HELP node_sockstat_TCP_mem Number of TCP sockets in state mem.
####  TYPE node_sockstat_TCP_mem gauge
node_sockstat_TCP_mem 1
####  HELP node_sockstat_TCP_mem_bytes Number of TCP sockets in state mem_bytes.
####  TYPE node_sockstat_TCP_mem_bytes gauge
node_sockstat_TCP_mem_bytes 4096
####  HELP node_sockstat_TCP_orphan Number of TCP sockets in state orphan.
####  TYPE node_sockstat_TCP_orphan gauge
node_sockstat_TCP_orphan 0
####  HELP node_sockstat_TCP_tw Number of TCP sockets in state tw.
####  TYPE node_sockstat_TCP_tw gauge
node_sockstat_TCP_tw 4
####  HELP node_sockstat_UDPLITE_inuse Number of UDPLITE sockets in state inuse.
####  TYPE node_sockstat_UDPLITE_inuse gauge
node_sockstat_UDPLITE_inuse 0
####  HELP node_sockstat_UDP_inuse Number of UDP sockets in state inuse.
####  TYPE node_sockstat_UDP_inuse gauge
node_sockstat_UDP_inuse 6
####  HELP node_sockstat_UDP_mem Number of UDP sockets in state mem.
####  TYPE node_sockstat_UDP_mem gauge
node_sockstat_UDP_mem 94
####  HELP node_sockstat_UDP_mem_bytes Number of UDP sockets in state mem_bytes.
####  TYPE node_sockstat_UDP_mem_bytes gauge
node_sockstat_UDP_mem_bytes 385024
####  HELP node_sockstat_sockets_used Number of sockets sockets in state used.
####  TYPE node_sockstat_sockets_used gauge
node_sockstat_sockets_used 108
####  HELP node_time System time in seconds since epoch (1970).
####  TYPE node_time gauge
node_time 1.530875596e+09
####  HELP node_uname_info Labeled system information as provided by the uname system call.
####  TYPE node_uname_info gauge
node_uname_info{domainname="(none)",machine="x86_64",nodename="localhost",release="4.15.12-x86_64-linode105",sysname="Linux",version="#### 1 SMP Thu Mar 22 02:13:40 UTC 2018"} 1
####  HELP node_vmstat_allocstall_dma /proc/vmstat information field allocstall_dma.
####  TYPE node_vmstat_allocstall_dma untyped
node_vmstat_allocstall_dma 0
####  HELP node_vmstat_allocstall_dma32 /proc/vmstat information field allocstall_dma32.
####  TYPE node_vmstat_allocstall_dma32 untyped
node_vmstat_allocstall_dma32 0
####  HELP node_vmstat_allocstall_movable /proc/vmstat information field allocstall_movable.
####  TYPE node_vmstat_allocstall_movable untyped
node_vmstat_allocstall_movable 0
####  HELP node_vmstat_allocstall_normal /proc/vmstat information field allocstall_normal.
####  TYPE node_vmstat_allocstall_normal untyped
node_vmstat_allocstall_normal 0
####  HELP node_vmstat_balloon_deflate /proc/vmstat information field balloon_deflate.
####  TYPE node_vmstat_balloon_deflate untyped
node_vmstat_balloon_deflate 0
####  HELP node_vmstat_balloon_inflate /proc/vmstat information field balloon_inflate.
####  TYPE node_vmstat_balloon_inflate untyped
node_vmstat_balloon_inflate 0
####  HELP node_vmstat_balloon_migrate /proc/vmstat information field balloon_migrate.
####  TYPE node_vmstat_balloon_migrate untyped
node_vmstat_balloon_migrate 0
####  HELP node_vmstat_compact_daemon_free_scanned /proc/vmstat information field compact_daemon_free_scanned.
####  TYPE node_vmstat_compact_daemon_free_scanned untyped
node_vmstat_compact_daemon_free_scanned 0
####  HELP node_vmstat_compact_daemon_migrate_scanned /proc/vmstat information field compact_daemon_migrate_scanned.
####  TYPE node_vmstat_compact_daemon_migrate_scanned untyped
node_vmstat_compact_daemon_migrate_scanned 0
####  HELP node_vmstat_compact_daemon_wake /proc/vmstat information field compact_daemon_wake.
####  TYPE node_vmstat_compact_daemon_wake untyped
node_vmstat_compact_daemon_wake 0
####  HELP node_vmstat_compact_fail /proc/vmstat information field compact_fail.
####  TYPE node_vmstat_compact_fail untyped
node_vmstat_compact_fail 0
####  HELP node_vmstat_compact_free_scanned /proc/vmstat information field compact_free_scanned.
####  TYPE node_vmstat_compact_free_scanned untyped
node_vmstat_compact_free_scanned 0
####  HELP node_vmstat_compact_isolated /proc/vmstat information field compact_isolated.
####  TYPE node_vmstat_compact_isolated untyped
node_vmstat_compact_isolated 0
####  HELP node_vmstat_compact_migrate_scanned /proc/vmstat information field compact_migrate_scanned.
####  TYPE node_vmstat_compact_migrate_scanned untyped
node_vmstat_compact_migrate_scanned 0
####  HELP node_vmstat_compact_stall /proc/vmstat information field compact_stall.
####  TYPE node_vmstat_compact_stall untyped
node_vmstat_compact_stall 0
####  HELP node_vmstat_compact_success /proc/vmstat information field compact_success.
####  TYPE node_vmstat_compact_success untyped
node_vmstat_compact_success 0
####  HELP node_vmstat_drop_pagecache /proc/vmstat information field drop_pagecache.
####  TYPE node_vmstat_drop_pagecache untyped
node_vmstat_drop_pagecache 0
####  HELP node_vmstat_drop_slab /proc/vmstat information field drop_slab.
####  TYPE node_vmstat_drop_slab untyped
node_vmstat_drop_slab 0
####  HELP node_vmstat_kswapd_high_wmark_hit_quickly /proc/vmstat information field kswapd_high_wmark_hit_quickly.
####  TYPE node_vmstat_kswapd_high_wmark_hit_quickly untyped
node_vmstat_kswapd_high_wmark_hit_quickly 0
####  HELP node_vmstat_kswapd_inodesteal /proc/vmstat information field kswapd_inodesteal.
####  TYPE node_vmstat_kswapd_inodesteal untyped
node_vmstat_kswapd_inodesteal 0
####  HELP node_vmstat_kswapd_low_wmark_hit_quickly /proc/vmstat information field kswapd_low_wmark_hit_quickly.
####  TYPE node_vmstat_kswapd_low_wmark_hit_quickly untyped
node_vmstat_kswapd_low_wmark_hit_quickly 0
####  HELP node_vmstat_nr_active_anon /proc/vmstat information field nr_active_anon.
####  TYPE node_vmstat_nr_active_anon untyped
node_vmstat_nr_active_anon 36893
####  HELP node_vmstat_nr_active_file /proc/vmstat information field nr_active_file.
####  TYPE node_vmstat_nr_active_file untyped
node_vmstat_nr_active_file 26927
####  HELP node_vmstat_nr_anon_pages /proc/vmstat information field nr_anon_pages.
####  TYPE node_vmstat_nr_anon_pages untyped
node_vmstat_nr_anon_pages 16639
####  HELP node_vmstat_nr_anon_transparent_hugepages /proc/vmstat information field nr_anon_transparent_hugepages.
####  TYPE node_vmstat_nr_anon_transparent_hugepages untyped
node_vmstat_nr_anon_transparent_hugepages 0
####  HELP node_vmstat_nr_bounce /proc/vmstat information field nr_bounce.
####  TYPE node_vmstat_nr_bounce untyped
node_vmstat_nr_bounce 0
####  HELP node_vmstat_nr_dirtied /proc/vmstat information field nr_dirtied.
####  TYPE node_vmstat_nr_dirtied untyped
node_vmstat_nr_dirtied 1.972078e+06
####  HELP node_vmstat_nr_dirty /proc/vmstat information field nr_dirty.
####  TYPE node_vmstat_nr_dirty untyped
node_vmstat_nr_dirty 7
####  HELP node_vmstat_nr_dirty_background_threshold /proc/vmstat information field nr_dirty_background_threshold.
####  TYPE node_vmstat_nr_dirty_background_threshold untyped
node_vmstat_nr_dirty_background_threshold 89676
####  HELP node_vmstat_nr_dirty_threshold /proc/vmstat information field nr_dirty_threshold.
####  TYPE node_vmstat_nr_dirty_threshold untyped
node_vmstat_nr_dirty_threshold 179572
####  HELP node_vmstat_nr_file_pages /proc/vmstat information field nr_file_pages.
####  TYPE node_vmstat_nr_file_pages untyped
node_vmstat_nr_file_pages 198300
####  HELP node_vmstat_nr_free_cma /proc/vmstat information field nr_free_cma.
####  TYPE node_vmstat_nr_free_cma untyped
node_vmstat_nr_free_cma 0
####  HELP node_vmstat_nr_free_pages /proc/vmstat information field nr_free_pages.
####  TYPE node_vmstat_nr_free_pages untyped
node_vmstat_nr_free_pages 763310
####  HELP node_vmstat_nr_inactive_anon /proc/vmstat information field nr_inactive_anon.
####  TYPE node_vmstat_nr_inactive_anon untyped
node_vmstat_nr_inactive_anon 33362
####  HELP node_vmstat_nr_inactive_file /proc/vmstat information field nr_inactive_file.
####  TYPE node_vmstat_nr_inactive_file untyped
node_vmstat_nr_inactive_file 117758
####  HELP node_vmstat_nr_isolated_anon /proc/vmstat information field nr_isolated_anon.
####  TYPE node_vmstat_nr_isolated_anon untyped
node_vmstat_nr_isolated_anon 0
####  HELP node_vmstat_nr_isolated_file /proc/vmstat information field nr_isolated_file.
####  TYPE node_vmstat_nr_isolated_file untyped
node_vmstat_nr_isolated_file 0
####  HELP node_vmstat_nr_kernel_stack /proc/vmstat information field nr_kernel_stack.
####  TYPE node_vmstat_nr_kernel_stack untyped
node_vmstat_nr_kernel_stack 1584
####  HELP node_vmstat_nr_mapped /proc/vmstat information field nr_mapped.
####  TYPE node_vmstat_nr_mapped untyped
node_vmstat_nr_mapped 9961
####  HELP node_vmstat_nr_mlock /proc/vmstat information field nr_mlock.
####  TYPE node_vmstat_nr_mlock untyped
node_vmstat_nr_mlock 0
####  HELP node_vmstat_nr_page_table_pages /proc/vmstat information field nr_page_table_pages.
####  TYPE node_vmstat_nr_page_table_pages untyped
node_vmstat_nr_page_table_pages 446
####  HELP node_vmstat_nr_shmem /proc/vmstat information field nr_shmem.
####  TYPE node_vmstat_nr_shmem untyped
node_vmstat_nr_shmem 53616
####  HELP node_vmstat_nr_shmem_hugepages /proc/vmstat information field nr_shmem_hugepages.
####  TYPE node_vmstat_nr_shmem_hugepages untyped
node_vmstat_nr_shmem_hugepages 0
####  HELP node_vmstat_nr_shmem_pmdmapped /proc/vmstat information field nr_shmem_pmdmapped.
####  TYPE node_vmstat_nr_shmem_pmdmapped untyped
node_vmstat_nr_shmem_pmdmapped 0
####  HELP node_vmstat_nr_slab_reclaimable /proc/vmstat information field nr_slab_reclaimable.
####  TYPE node_vmstat_nr_slab_reclaimable untyped
node_vmstat_nr_slab_reclaimable 9272
####  HELP node_vmstat_nr_slab_unreclaimable /proc/vmstat information field nr_slab_unreclaimable.
####  TYPE node_vmstat_nr_slab_unreclaimable untyped
node_vmstat_nr_slab_unreclaimable 4950
####  HELP node_vmstat_nr_unevictable /proc/vmstat information field nr_unevictable.
####  TYPE node_vmstat_nr_unevictable untyped
node_vmstat_nr_unevictable 0
####  HELP node_vmstat_nr_unstable /proc/vmstat information field nr_unstable.
####  TYPE node_vmstat_nr_unstable untyped
node_vmstat_nr_unstable 0
####  HELP node_vmstat_nr_vmscan_immediate_reclaim /proc/vmstat information field nr_vmscan_immediate_reclaim.
####  TYPE node_vmstat_nr_vmscan_immediate_reclaim untyped
node_vmstat_nr_vmscan_immediate_reclaim 0
####  HELP node_vmstat_nr_vmscan_write /proc/vmstat information field nr_vmscan_write.
####  TYPE node_vmstat_nr_vmscan_write untyped
node_vmstat_nr_vmscan_write 0
####  HELP node_vmstat_nr_writeback /proc/vmstat information field nr_writeback.
####  TYPE node_vmstat_nr_writeback untyped
node_vmstat_nr_writeback 0
####  HELP node_vmstat_nr_writeback_temp /proc/vmstat information field nr_writeback_temp.
####  TYPE node_vmstat_nr_writeback_temp untyped
node_vmstat_nr_writeback_temp 0
####  HELP node_vmstat_nr_written /proc/vmstat information field nr_written.
####  TYPE node_vmstat_nr_written untyped
node_vmstat_nr_written 1.958949e+06
####  HELP node_vmstat_nr_zone_active_anon /proc/vmstat information field nr_zone_active_anon.
####  TYPE node_vmstat_nr_zone_active_anon untyped
node_vmstat_nr_zone_active_anon 36893
####  HELP node_vmstat_nr_zone_active_file /proc/vmstat information field nr_zone_active_file.
####  TYPE node_vmstat_nr_zone_active_file untyped
node_vmstat_nr_zone_active_file 26927
####  HELP node_vmstat_nr_zone_inactive_anon /proc/vmstat information field nr_zone_inactive_anon.
####  TYPE node_vmstat_nr_zone_inactive_anon untyped
node_vmstat_nr_zone_inactive_anon 33362
####  HELP node_vmstat_nr_zone_inactive_file /proc/vmstat information field nr_zone_inactive_file.
####  TYPE node_vmstat_nr_zone_inactive_file untyped
node_vmstat_nr_zone_inactive_file 117758
####  HELP node_vmstat_nr_zone_unevictable /proc/vmstat information field nr_zone_unevictable.
####  TYPE node_vmstat_nr_zone_unevictable untyped
node_vmstat_nr_zone_unevictable 0
####  HELP node_vmstat_nr_zone_write_pending /proc/vmstat information field nr_zone_write_pending.
####  TYPE node_vmstat_nr_zone_write_pending untyped
node_vmstat_nr_zone_write_pending 7
####  HELP node_vmstat_numa_foreign /proc/vmstat information field numa_foreign.
####  TYPE node_vmstat_numa_foreign untyped
node_vmstat_numa_foreign 0
####  HELP node_vmstat_numa_hit /proc/vmstat information field numa_hit.
####  TYPE node_vmstat_numa_hit untyped
node_vmstat_numa_hit 2.32088122e+08
####  HELP node_vmstat_numa_interleave /proc/vmstat information field numa_interleave.
####  TYPE node_vmstat_numa_interleave untyped
node_vmstat_numa_interleave 15374
####  HELP node_vmstat_numa_local /proc/vmstat information field numa_local.
####  TYPE node_vmstat_numa_local untyped
node_vmstat_numa_local 2.32088122e+08
####  HELP node_vmstat_numa_miss /proc/vmstat information field numa_miss.
####  TYPE node_vmstat_numa_miss untyped
node_vmstat_numa_miss 0
####  HELP node_vmstat_numa_other /proc/vmstat information field numa_other.
####  TYPE node_vmstat_numa_other untyped
node_vmstat_numa_other 0
####  HELP node_vmstat_oom_kill /proc/vmstat information field oom_kill.
####  TYPE node_vmstat_oom_kill untyped
node_vmstat_oom_kill 0
####  HELP node_vmstat_pageoutrun /proc/vmstat information field pageoutrun.
####  TYPE node_vmstat_pageoutrun untyped
node_vmstat_pageoutrun 0
####  HELP node_vmstat_pgactivate /proc/vmstat information field pgactivate.
####  TYPE node_vmstat_pgactivate untyped
node_vmstat_pgactivate 206279
####  HELP node_vmstat_pgalloc_dma /proc/vmstat information field pgalloc_dma.
####  TYPE node_vmstat_pgalloc_dma untyped
node_vmstat_pgalloc_dma 0
####  HELP node_vmstat_pgalloc_dma32 /proc/vmstat information field pgalloc_dma32.
####  TYPE node_vmstat_pgalloc_dma32 untyped
node_vmstat_pgalloc_dma32 0
####  HELP node_vmstat_pgalloc_movable /proc/vmstat information field pgalloc_movable.
####  TYPE node_vmstat_pgalloc_movable untyped
node_vmstat_pgalloc_movable 0
####  HELP node_vmstat_pgalloc_normal /proc/vmstat information field pgalloc_normal.
####  TYPE node_vmstat_pgalloc_normal untyped
node_vmstat_pgalloc_normal 4.75217133e+08
####  HELP node_vmstat_pgdeactivate /proc/vmstat information field pgdeactivate.
####  TYPE node_vmstat_pgdeactivate untyped
node_vmstat_pgdeactivate 0
####  HELP node_vmstat_pgfault /proc/vmstat information field pgfault.
####  TYPE node_vmstat_pgfault untyped
node_vmstat_pgfault 1.80243946e+08
####  HELP node_vmstat_pgfree /proc/vmstat information field pgfree.
####  TYPE node_vmstat_pgfree untyped
node_vmstat_pgfree 4.75980856e+08
####  HELP node_vmstat_pginodesteal /proc/vmstat information field pginodesteal.
####  TYPE node_vmstat_pginodesteal untyped
node_vmstat_pginodesteal 0
####  HELP node_vmstat_pglazyfree /proc/vmstat information field pglazyfree.
####  TYPE node_vmstat_pglazyfree untyped
node_vmstat_pglazyfree 0
####  HELP node_vmstat_pglazyfreed /proc/vmstat information field pglazyfreed.
####  TYPE node_vmstat_pglazyfreed untyped
node_vmstat_pglazyfreed 0
####  HELP node_vmstat_pgmajfault /proc/vmstat information field pgmajfault.
####  TYPE node_vmstat_pgmajfault untyped
node_vmstat_pgmajfault 576
####  HELP node_vmstat_pgmigrate_fail /proc/vmstat information field pgmigrate_fail.
####  TYPE node_vmstat_pgmigrate_fail untyped
node_vmstat_pgmigrate_fail 0
####  HELP node_vmstat_pgmigrate_success /proc/vmstat information field pgmigrate_success.
####  TYPE node_vmstat_pgmigrate_success untyped
node_vmstat_pgmigrate_success 0
####  HELP node_vmstat_pgpgin /proc/vmstat information field pgpgin.
####  TYPE node_vmstat_pgpgin untyped
node_vmstat_pgpgin 160098
####  HELP node_vmstat_pgpgout /proc/vmstat information field pgpgout.
####  TYPE node_vmstat_pgpgout untyped
node_vmstat_pgpgout 2.2696648e+07
####  HELP node_vmstat_pgrefill /proc/vmstat information field pgrefill.
####  TYPE node_vmstat_pgrefill untyped
node_vmstat_pgrefill 0
####  HELP node_vmstat_pgrotated /proc/vmstat information field pgrotated.
####  TYPE node_vmstat_pgrotated untyped
node_vmstat_pgrotated 0
####  HELP node_vmstat_pgscan_direct /proc/vmstat information field pgscan_direct.
####  TYPE node_vmstat_pgscan_direct untyped
node_vmstat_pgscan_direct 0
####  HELP node_vmstat_pgscan_direct_throttle /proc/vmstat information field pgscan_direct_throttle.
####  TYPE node_vmstat_pgscan_direct_throttle untyped
node_vmstat_pgscan_direct_throttle 0
####  HELP node_vmstat_pgscan_kswapd /proc/vmstat information field pgscan_kswapd.
####  TYPE node_vmstat_pgscan_kswapd untyped
node_vmstat_pgscan_kswapd 0
####  HELP node_vmstat_pgskip_dma /proc/vmstat information field pgskip_dma.
####  TYPE node_vmstat_pgskip_dma untyped
node_vmstat_pgskip_dma 0
####  HELP node_vmstat_pgskip_dma32 /proc/vmstat information field pgskip_dma32.
####  TYPE node_vmstat_pgskip_dma32 untyped
node_vmstat_pgskip_dma32 0
####  HELP node_vmstat_pgskip_movable /proc/vmstat information field pgskip_movable.
####  TYPE node_vmstat_pgskip_movable untyped
node_vmstat_pgskip_movable 0
####  HELP node_vmstat_pgskip_normal /proc/vmstat information field pgskip_normal.
####  TYPE node_vmstat_pgskip_normal untyped
node_vmstat_pgskip_normal 0
####  HELP node_vmstat_pgsteal_direct /proc/vmstat information field pgsteal_direct.
####  TYPE node_vmstat_pgsteal_direct untyped
node_vmstat_pgsteal_direct 0
####  HELP node_vmstat_pgsteal_kswapd /proc/vmstat information field pgsteal_kswapd.
####  TYPE node_vmstat_pgsteal_kswapd untyped
node_vmstat_pgsteal_kswapd 0
####  HELP node_vmstat_pswpin /proc/vmstat information field pswpin.
####  TYPE node_vmstat_pswpin untyped
node_vmstat_pswpin 0
####  HELP node_vmstat_pswpout /proc/vmstat information field pswpout.
####  TYPE node_vmstat_pswpout untyped
node_vmstat_pswpout 0
####  HELP node_vmstat_slabs_scanned /proc/vmstat information field slabs_scanned.
####  TYPE node_vmstat_slabs_scanned untyped
node_vmstat_slabs_scanned 0
####  HELP node_vmstat_swap_ra /proc/vmstat information field swap_ra.
####  TYPE node_vmstat_swap_ra untyped
node_vmstat_swap_ra 0
####  HELP node_vmstat_swap_ra_hit /proc/vmstat information field swap_ra_hit.
####  TYPE node_vmstat_swap_ra_hit untyped
node_vmstat_swap_ra_hit 0
####  HELP node_vmstat_unevictable_pgs_cleared /proc/vmstat information field unevictable_pgs_cleared.
####  TYPE node_vmstat_unevictable_pgs_cleared untyped
node_vmstat_unevictable_pgs_cleared 0
####  HELP node_vmstat_unevictable_pgs_culled /proc/vmstat information field unevictable_pgs_culled.
####  TYPE node_vmstat_unevictable_pgs_culled untyped
node_vmstat_unevictable_pgs_culled 0
####  HELP node_vmstat_unevictable_pgs_mlocked /proc/vmstat information field unevictable_pgs_mlocked.
####  TYPE node_vmstat_unevictable_pgs_mlocked untyped
node_vmstat_unevictable_pgs_mlocked 0
####  HELP node_vmstat_unevictable_pgs_munlocked /proc/vmstat information field unevictable_pgs_munlocked.
####  TYPE node_vmstat_unevictable_pgs_munlocked untyped
node_vmstat_unevictable_pgs_munlocked 0
####  HELP node_vmstat_unevictable_pgs_rescued /proc/vmstat information field unevictable_pgs_rescued.
####  TYPE node_vmstat_unevictable_pgs_rescued untyped
node_vmstat_unevictable_pgs_rescued 0
####  HELP node_vmstat_unevictable_pgs_scanned /proc/vmstat information field unevictable_pgs_scanned.
####  TYPE node_vmstat_unevictable_pgs_scanned untyped
node_vmstat_unevictable_pgs_scanned 0
####  HELP node_vmstat_unevictable_pgs_stranded /proc/vmstat information field unevictable_pgs_stranded.
####  TYPE node_vmstat_unevictable_pgs_stranded untyped
node_vmstat_unevictable_pgs_stranded 0
####  HELP node_vmstat_workingset_activate /proc/vmstat information field workingset_activate.
####  TYPE node_vmstat_workingset_activate untyped
node_vmstat_workingset_activate 0
####  HELP node_vmstat_workingset_nodereclaim /proc/vmstat information field workingset_nodereclaim.
####  TYPE node_vmstat_workingset_nodereclaim untyped
node_vmstat_workingset_nodereclaim 0
####  HELP node_vmstat_workingset_refault /proc/vmstat information field workingset_refault.
####  TYPE node_vmstat_workingset_refault untyped
node_vmstat_workingset_refault 0
####  HELP node_vmstat_zone_reclaim_failed /proc/vmstat information field zone_reclaim_failed.
####  TYPE node_vmstat_zone_reclaim_failed untyped
node_vmstat_zone_reclaim_failed 0
####  HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
####  TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 6089.04
####  HELP process_max_fds Maximum number of open file descriptors.
####  TYPE process_max_fds gauge
process_max_fds 1024
####  HELP process_open_fds Number of open file descriptors.
####  TYPE process_open_fds gauge
process_open_fds 8
####  HELP process_resident_memory_bytes Resident memory size in bytes.
####  TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 1.7321984e+07
####  HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
####  TYPE process_start_time_seconds gauge
process_start_time_seconds 1.52484971386e+09
####  HELP process_virtual_memory_bytes Virtual memory size in bytes.
####  TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 2.20807168e+08
```
