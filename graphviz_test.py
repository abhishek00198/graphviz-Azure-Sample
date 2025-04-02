from diagrams import Diagram, Cluster, Edge
from diagrams.azure.analytics import (
    AnalysisServices, DataFactories, Databricks, EventHubs, SynapseAnalytics, StreamAnalyticsJobs, LogAnalyticsWorkspaces
)
from diagrams.azure.compute import (
    AppServices, AutomanagedVM, BatchAccounts, ContainerInstances, ContainerRegistries, FunctionApps, KubernetesServices, VMScaleSet
)
from diagrams.azure.database import (
    CacheForRedis, CosmosDb, SQLDatabases, SQLServers, DataLake, BlobStorage
)
from diagrams.azure.devops import ApplicationInsights, Devops, Repos, Pipelines
from diagrams.azure.general import Resourcegroups, Subscriptions, Managementgroups, Usericon
from diagrams.azure.identity import ActiveDirectory, ManagedIdentities, Users
from diagrams.azure.integration import LogicApps, ServiceBus, EventGridTopics, APIManagement
from diagrams.azure.iot import IotHub, DigitalTwins
from diagrams.azure.ml import CognitiveServices, AzureOpenAI
from diagrams.azure.monitor import Monitor, Logs
from diagrams.azure.network import (
    ApplicationGateway, DNSZones, FrontDoors, LoadBalancers, VirtualNetworks, NetworkSecurityGroupsClassic, PrivateEndpoint
)
from diagrams.azure.security import KeyVaults, SecurityCenter, Sentinel
from diagrams.azure.storage import StorageAccounts, DataLakeStorage, QueuesStorage, TableStorage
from diagrams.azure.web import AppServicePlans, Signalr

with Diagram("Complex Azure Architecture", outformat=["jpg", "png", "dot"], show=False):
    

    with Cluster("Azure Subscription (1)"):
        subscription = Subscriptions("Subscription")

        with Cluster("Management Group (2)"):
            management_group = Managementgroups("Management Group")
            subscription >> Edge(label="Part Of") >> management_group

        with Cluster("Resource Group - Data & Analytics (3)"):
            rg_data = Resourcegroups("RG Data & Analytics")
            subscription >> Edge(label="Contains") >> rg_data

            data_factory = DataFactories("Data Factory (4)")
            databricks = Databricks("Databricks (5)")
            synapse = SynapseAnalytics("Synapse (6)")
            event_hub = EventHubs("Event Hub (7)")
            stream_analytics = StreamAnalyticsJobs("Stream Analytics (8)")
            log_analytics = LogAnalyticsWorkspaces("Log Analytics (9)")
            analysis_services = AnalysisServices("Analysis Services (10)")
            datalake = DataLake("Data Lake (11)")

            event_hub >> Edge(label="1. Data Flow") >> stream_analytics >> Edge(label="2. Data Processing") >> databricks >> Edge(label="3. Data Warehouse") >> synapse >> Edge(label="4. Data Integration") >> data_factory >> Edge(label="5. Analysis") >> analysis_services
            synapse >> Edge(label="6. Log Data") >> log_analytics
            datalake >> Edge(label="7. Data Ingestion") >> data_factory

        with Cluster("Resource Group - Compute (12)"):
            rg_compute = Resourcegroups("RG Compute")
            subscription >> Edge(label="Contains") >> rg_compute

            app_service = AppServices("App Service (13)")
            vm = AutomanagedVM("VM (14)")
            batch = BatchAccounts("Batch (15)")
            container_instance = ContainerInstances("Container Instances (16)")
            container_registry = ContainerRegistries("Container Registry (17)")
            function_app = FunctionApps("Function App (18)")
            aks = KubernetesServices("AKS (19)")
            vmss = VMScaleSet("VM Scale Set (20)")

            function_app >> Edge(label="8. Microservices") >> container_instance >> Edge(label="9. Container Orchestration") >> aks >> Edge(label="10. Scaling") >> vmss
            container_registry >> Edge(label="11. Image Storage") >> aks
            batch >> Edge(label="12. Batch Processing") >> vm
            app_service >> Edge(label="13. Web Application") >> function_app

        with Cluster("Resource Group - Database (21)"):
            rg_database = Resourcegroups("RG Database")
            subscription >> Edge(label="Contains") >> rg_database

            redis = CacheForRedis("Redis (22)")
            cosmos = CosmosDb("Cosmos DB (23)")
            sql_db = SQLDatabases("SQL Database (24)")
            sql_server = SQLServers("SQL Server (25)")
            blob_storage = BlobStorage("Blob Storage (26)")

            app_service >> Edge(label="14. Data Access") >> sql_db >> Edge(label="15. Database Server") >> sql_server
            container_instance >> Edge(label="16. Cache") >> cosmos >> Edge(label="17. Caching") >> redis
            blob_storage >> Edge(label="18. Data Source") >> databricks

        with Cluster("Resource Group - DevOps & Identity (27)"):
            rg_devops = Resourcegroups("RG DevOps & Identity")
            subscription >> Edge(label="Contains") >> rg_devops

            devops = Devops("DevOps (28)")
            repos = Repos("Repos (29)")
            pipelines = Pipelines("Pipelines (30)")
            app_insights = ApplicationInsights("App Insights (31)")
            ad = ActiveDirectory("Azure AD (32)")
            managed_identities = ManagedIdentities("Managed Identities (33)")
            users = Users("Users (34)")

            devops >> Edge(label="19. Code Management") >> repos >> Edge(label="20. CI/CD") >> pipelines >> Edge(label="21. Monitoring") >> app_insights
            ad >> Edge(label="22. Authentication") >> managed_identities >> Edge(label="23. Authorization") >> users
            app_service >> Edge(label="24. Authentication") >> managed_identities
            function_app >> Edge(label="25. Authentication") >> managed_identities

        with Cluster("Resource Group - Integration & IoT (35)"):
            rg_integration = Resourcegroups("RG Integration & IoT")
            subscription >> Edge(label="Contains") >> rg_integration

            logic_app = LogicApps("Logic Apps (36)")
            service_bus = ServiceBus("Service Bus (37)")
            event_grid = EventGridTopics("Event Grid (38)")
            api_management = APIManagement("API Management (39)")
            iot_hub = IotHub("IoT Hub (40)")
            digital_twins = DigitalTwins("Digital Twins (41)")

            logic_app >> Edge(label="26. Integration") >> service_bus >> Edge(label="27. Event Routing") >> event_grid >> Edge(label="28. API Gateway") >> api_management
            iot_hub >> Edge(label="29. IoT Data") >> digital_twins >> Edge(label="30. Data Flow") >> event_hub

        with Cluster("Resource Group - AI & Monitoring (42)"):
            rg_ai_monitor = Resourcegroups("RG AI & Monitoring")
            subscription >> Edge(label="Contains") >> rg_ai_monitor

            cognitive_services = CognitiveServices("Cognitive Services (43)")
            openai = AzureOpenAI("Azure OpenAI (44)")
            monitor = Monitor("Monitor (45)")
            logs = Logs("Logs (46)")

            cognitive_services >> Edge(label="31. AI Services") >> openai
            app_service >> Edge(label="32. Monitoring") >> monitor >> Edge(label="33. Log Aggregation") >> logs
            function_app >> Edge(label="34. Monitoring") >> monitor >> Edge(label="35. Log Aggregation") >> logs

        with Cluster("Resource Group - Networking & Security (47)"):
            rg_network_security = Resourcegroups("RG Network & Security")
            subscription >> Edge(label="Contains") >> rg_network_security

            vnet = VirtualNetworks("VNet (48)")
            app_gateway = ApplicationGateway("App Gateway (49)")
            dns = DNSZones("DNS Zones (50)")
            front_door = FrontDoors("Front Door")
            load_balancer = LoadBalancers("Load Balancer")
            nsg = NetworkSecurityGroupsClassic("NSG Classic")
            private_endpoint = PrivateEndpoint("Private Endpoint")
            key_vault = KeyVaults("Key Vault")
            security_center = SecurityCenter("Security Center")
            sentinel = Sentinel("Sentinel")

            vnet >> Edge(label="36. Network") >> load_balancer >> Edge(label="37. Load Balancing") >> app_gateway >> Edge(label="38. Web Traffic") >> front_door >> Edge(label="39. DNS") >> dns >> Edge(label="40. Network Security") >> nsg >> private_endpoint
            app_service >> Edge(label="41. Secrets") >> key_vault
            monitor >> Edge(label="42. Security Monitoring") >> security_center >> Edge(label="43. Threat Detection") >> sentinel

        with Cluster("Resource Group - Storage & Web"):
            rg_storage_web = Resourcegroups("RG Storage & Web")
            subscription >> Edge(label="Contains") >> rg_storage_web

            storage_account = StorageAccounts("Storage Account")
            data_lake_storage = DataLakeStorage("Data Lake Storage")
            queue_storage = QueuesStorage("Queue Storage")
            table_storage = TableStorage("Table Storage")
            app_service_plan = AppServicePlans("App Service Plan")
            signalr = Signalr("SignalR")

            storage_account >> data_lake_storage >> queue_storage >> table_storage
            app_service >> app_service_plan >> signalr

        user >> Edge(label="44. User Access") >> app_service
        iot_hub >> Edge(label="45. Data Ingestion") >> event_hub
        app_insights >> Edge(label="46. Application Monitoring") >> monitor
