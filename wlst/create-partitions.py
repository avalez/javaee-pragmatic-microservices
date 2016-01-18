connect('admin', 'admin123', 't3://localhost:7001')

edit()
startEdit()

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