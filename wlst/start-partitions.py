connect("weblogic", "welcome1", "t3://localhost:7001")

domainRuntime()
cd('/')
taskMbean1 = cmo.lookupDomainPartitionRuntime('Partition-0').getPartitionLifeCycleRuntime().start()
taskMbean2 = cmo.lookupDomainPartitionRuntime('Partition-1').getPartitionLifeCycleRuntime().start()
while (taskMbean1.getStatus() != 'TASK COMPLETED' and taskMbean2.getStatus() != 'TASK COMPLETED'):import time;time.sleep(1)
