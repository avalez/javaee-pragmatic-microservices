connect("admin", "admin123", "t3://localhost:7001")

edit()
startEdit()

#c0 = cmo.createCluster('Cluster-0')

vt0=cmo.createVirtualTarget('VirtualTarget-0')
vt0.setUriPrefix('/cargo-tracker')
vt0.addTarget(cmo.getServers()[0])

#c1 = cmo.createCluster('Cluster-1')

vt1=cmo.createVirtualTarget('VirtualTarget-1')
vt1.setUriPrefix('/path-finder')
vt1.addTarget(cmo.getServers()[0])

save()
activate(block='true')

exit()