connect('weblogic', 'welcome1', 't3://localhost:7001')

edit()
startEdit()

# Create Domain Partiton for Cargo Tracker
cd('/')
cmo.createPartition('Partition-0')
cd('/Partitions/Partition-0')
set('AvailableTargets',jarray.array([ObjectName('com.bea:Name=VirtualTarget-0,Type=VirtualTarget')], ObjectName))
set('DefaultTargets',jarray.array([ObjectName('com.bea:Name=VirtualTarget-0,Type=VirtualTarget')], ObjectName))
cmo.createResourceGroup('ResourceGroup-0')
cd('/Partitions/Partition-0/ResourceGroups/ResourceGroup-0')
cmo.setUseDefaultTarget(true)
cmo.setTargets(None)
cmo.findEffectiveTargets()

# Create Domain Partiton for Path Finder
cd('/')
cmo.createPartition('Partition-1')
cd('/Partitions/Partition-1')
set('AvailableTargets',jarray.array([ObjectName('com.bea:Name=VirtualTarget-1,Type=VirtualTarget')], ObjectName))
set('DefaultTargets',jarray.array([ObjectName('com.bea:Name=VirtualTarget-1,Type=VirtualTarget')], ObjectName))
cmo.createResourceGroup('ResourceGroup-0')
cd('/Partitions/Partition-1/ResourceGroups/ResourceGroup-0')
cmo.setUseDefaultTarget(true)
cmo.setTargets(None)
cmo.findEffectiveTargets()

save()
activate()

# Start both partitions
domainRuntime()
cd('/')
taskMbean1 = cmo.lookupDomainPartitionRuntime('Partition-0').getPartitionLifeCycleRuntime().start()
taskMbean2 = cmo.lookupDomainPartitionRuntime('Partition-1').getPartitionLifeCycleRuntime().start()
while (taskMbean1.getStatus() != 'TASK COMPLETED' and taskMbean2.getStatus() != 'TASK COMPLETED'):import time;time.sleep(1)

