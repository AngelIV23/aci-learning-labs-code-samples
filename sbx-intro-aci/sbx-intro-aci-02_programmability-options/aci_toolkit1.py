from credentials import *
from acitoolkit import acitoolkit

# connect to the apic
session = acitoolkit.Session(URL, LOGIN, PASSWORD)
session.login()
# <Response [200]> --> If you do not see this response the login did not work

# Create a Variable for your Tenant Name
# Use your initials in the name
# Example: tenant_name = "js_Toolkit_Tenant"
tenant_name = "INITIALS_Toolkit_Tenant_AIV"

# create a new tenant
new_tenant = acitoolkit.Tenant(tenant_name)

# commit the new configuration
session.push_to_apic(new_tenant.get_url(), new_tenant.get_json())
# <Response [200]> --> If you do not see this response the tenant create did no