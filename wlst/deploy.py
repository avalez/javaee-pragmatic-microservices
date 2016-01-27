connect('weblogic', 'welcome1', 't3://localhost:7001')

deploy(appName='cargo-tracker', path='cargo-tracker/target/cargo-tracker.war', resourceGroup='ResourceGroup-0', partition='Partition-0')
deploy(appName='path-finder', path='path-finder/target/path-finder.war', resourceGroup='ResourceGroup-0', partition='Partition-1')
