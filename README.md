## AtScale Qlik Script generator

This notebooks helps to create a qlik script an uploads it into the qlik app on your qlik saas tenant.

Get a Token on your qlik saas tenant: https://qlik.dev/authenticate/api-key/generate-your-first-api-key/

create your .env file:
```sh
atscale-user="your.user.name"
atscale-password="password"
atscale-server="https://your.atscale-environment.com"

qlik-saas-tenant = "https://your-tenant.eu.qlikcloud.com"
qlik-saas-token = "qlik-saas-token-string"
```