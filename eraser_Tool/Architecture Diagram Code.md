# 🧭 Test Architecture Diagram (Code Highlighted)

```dsl
title Test Architecture Diagram
typeface clean
colorMode pastel
styleMode shadow
direction right
title Test Architecture Diagram
// Diagram elements
Azure [icon: azure-cloud]{

Platform Landing Zones [icon: azure-cloud]{

   Azure Firewall [icon: azure-Firewall ,label: "Azure-Firewall "]
   DDOS Protection[icon: azure-ddos-protection-plans]
   Virtual Network HUB[icon: azure-virtual-networks]
   Private Endpoints[icon: azure-private-link]
   Azure Private DNS Zone [icon: azure-dns-zones]
}
Application Landing Zones [icon: azure-cloud]{
  Azure Traffic Manager [icon: azure-traffic-manager-profiles]
Active Region 1 [color: blue] {
  App Gateway WAF 1 [icon: azure-application-gateway, label: "App Gateway WAF (Region 1)"]
  Function App 1 [icon: azure-functions, label: "Function App (Region 1)"]
  Key Vault 1 [icon: azure-key-vault, label: "Key Vault"]
  Cosmos DB 1 [icon: azure-cosmos-db, label: "Cosmos DB"]
  Storage Account [icon: azure-blob-block, label: "Storage Account"]
  Public IP1 [icon: azure-public-ip-addresses, label: "Public IP"]
    Virtual Network Spoke 1[icon: azure-virtual-networks]
     ManageIdentity 1[icon: azure-managed-identities ,label: "Manage Identity"]
}

Passive Region 2 [color: green] {
  App Gateway WAF 2 [icon: azure-application-gateway, label: "App Gateway WAF (Region 2)"]
  Function App 2 [icon: azure-functions, label: "Function App (Region 2)"]
  Key Vault 2 [icon: azure-key-vault, label: "Key Vault"]
  Cosmos DB 2 [icon: azure-cosmos-db, label: "Cosmos DB"]
    Virtual Network Spoke 2 [icon: azure-virtual-networks]
  Storage Account 2 [icon: azure-blob-block, label: "Storage Account"]
    Public IP2 [icon: azure-public-ip-addresses, label: "Public IP"]
ManageIdentity 2[icon: azure-managed-identities ,label: "Manage Identity"]
}
Azure Monitor [icon: azure-monitor, label: "Alerts & Logs"]{
 Monitor [icon: azure-monitor]
 Alerts [icon: azure-Alerts]
Grafana [icon: grafana]
}
}
Clients [icon: users] {
  CLI [icon: terminal]
  Web Interface [icon: monitor]
  API [icon: cloud]
}

}
Automation [icon: azure-automation-accounts] {
  Powerhshell [icon: terminal]
  github [icon: github]
 Terraform [icon: terraform]
 Actions [icon: github-actions]
}

// Connections
Clients > Azure Traffic Manager :1
Clients --> Active Region 1  :2
Clients --> Passive Region 2 :2
Azure Traffic Manager > App Gateway WAF 1: Priority 1 
Azure Traffic Manager > App Gateway WAF 2 : Priority 2

App Gateway WAF 1 > Function App 1
App Gateway WAF 2 > Function App 2

Function App 1 > Key Vault 1

Function App 1 > Cosmos DB 1
Function App 2 > Key Vault 2
Function App 2 > Cosmos DB 2

Cosmos DB 1 --> Cosmos DB 2 : "Multi -Region Sync"

Active Region 1  --> Azure Monitor
Passive Region 2 --> Azure Monitor
Passive Region 2 --> Automation: "CI/CD Pipelines"
Active Region 1  --> Automation: "CI/CD Pipelines"
