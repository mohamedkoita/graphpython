
##### ARCHITECTURE DES PROJETS
projet1 = { "name" : "Teastore",
"services" : [[0, 'REST', 'WEB UI'], [1, 'REST', 'Registry'], [2, 'REST', 'Authentication'], [3, 'REST', 'ImageProvider'], [4, 'REST', 'Persistence'], [5, 'REST', 'Recommender']],
"relations" : [
[0, 1, {"link": ["POST /{name}/{location} ", " DELETE /{name}/{location}"]}],
[0, 2, {"link": ["POST /cart/add/{id} ", " POST /cart/remove/{id} ", " PUT /cart/{id} ", " POST /useractions/login ", " POST /useractions/logout ", " POST /useractions/placeorder ", " POST /useractions/isLoggedIn"] }],
[0, 3, {"link": ["POST /getProductImages ", " POST /getWebImages"]}],
[0, 4, {"link": ["GET /products ", " GET /categories ", " GET /users ", " GET /orders"] }],
[0, 5, {"link": ["POST /recommend/{uid}"]}],
[5, 4, {"link": ["GET /orders ", " GET /ordersitems"]}],
[2, 4, {"link": ["POST /products ", " POST /orders ", " POST /ordersitems"]}],
[3, 4, {"link": ["GET /generatedb ", " /GET products ", " GET/categories"]}]
] }

projet2 = { "name" :  "Sitewhere",
"services" : [[0, 'gRPC', 'Device Mgmt'], [1, 'gRPC', 'outbounds-connectors'], [2, 'gRPC', 'event-sources'], [3, 'gRPC', 'inbound-processing'], [4, 'gRPC', 'batch-operations'], [5, 'gRPC', 'event-mgmt'], [6, 'gRPC', 'tenant-mgmt'], [7, 'gRPC', 'instance-mgmt'], [8, 'gRPC', 'user-mgmt'], [9, 'gRPC', 'asset-mgmt'], [10, 'gRPC', 'command-delivery'], [11, 'gRPC', 'label-generation'], [12, 'gRPC', 'schedule-mgmt'], [13, 'gRPC', 'device-registration'], [14, 'gRPC', 'device-state'] ],
"relations" : [
[0, 9, {"link": ["gRPC getAssetByToken()"]}],
[1, 0, {"link": [ "gRPC getArea()", "gRPC getDevice()", "gRPC getDeviceType()", "gRPC getDeviceAssignment()" ]}],
[2, 0, {"link": ["gRPC getDeviceByToken()", "gRPC getDeviceType()"]}],
[2, 5, {"link": ["gRPC getDeviceEventByAlternateId()"]}],
[3, 0, {"link": ["gRPC getDeviceByToken()", "gRPC getDeviceType()"]}],
[4, 0, {"link": ["getDevice()", "gRPC getDeviceByToken()", "gRPC getDeviceCommandByToken()", "gRPC getDeviceType()", "gRPC getActiveDeviceByAssignments()"]}],
[5, 0, {"link": ["gRPC getDeviceCommandByToken()", "gRPC getDeviceAssignment()"]}],
[10, 0, {"link": ["gRPC getDevice()", "gRPC getDeviceCommand()", "gRPC getDeviceByToken()"]}],
[11, 0, {"link": ["gRPC getArea()", "gRPC getDevice()"]}],
[13, 0, {"link": ["gRPC createDeviceAssignment()", "gRPC getDeviceByToken()", "gRPC createDevice()", "gRPC updateDevice()", "gRPC getDeviceTypeByToken()", "gRPC getCustomerByToken()"]}],
[14, 0, {"link": ["gRPC getDeviceByToken()", "gRPC getDeviceTypeByToken()", "gRPC getDeviceAssignementByToken()", "gRPC getCustomerByToken()", "gRPC getAreaByToken()"]}],
[7, 0, {"link": ["gRPC createArea()" , "gRPC updateArea()" , "gRPC listAreas()" , "gRPC deleteArea()", "gRPC getAreasTree()" , "gRPC getAreaByToken()", "gRPC createAreaType()", "gRPC updateAreaType()", "gRPC listAreaTypes()", "gRPC deleteAreaType()" , "gRPC listDeviceAssignments()"]}],
[7, 4, {"link": ["gRPC getBatchOperationByToken()", "gRPC listBatchOperations()", "gRPC listBatchElements()" , "gRPC createBatchCommandInvocation()" ]}],
[7, 8, {"link": ["gRPC getUserByUsername()", "gRPC createUser()", "gRPC updateUser()", "gRPC deleteUser()", "gRPC listUsers()", "gRPC getAccessToken()", "gRPC createGrantedAuthority()", "gRPC getGrantedAuthorityByName()", "gRPC listGrantedAuthorities()", "gRPC getRoleByName()", "gRPC listRoles()", "gRPC deleteRole()", "gRPC createRole()", "gRPC UpdateRole()", "gRPC getRoles()", "gRPC addRoles()", "gRPC removeRoles()"]}],
[7, 9, {"link": ["gRPC createAsset()", "gRPC updateAsset()", "gRPC listAssets()", "gRPC deleteAsset()", "gRPC getAssetByToken()", "gRPC createAssetType()", "gRPC updateAssetType()", "gRPC listAssetTypes()", "gRPC deleteAssetType()", "gRPC getAssetTypeByToken()"]}],
[7, 11, {"link": ["gRPC getAreaLabel()" , "gRPC getAreaTypeLabel()" , "gRPC getAssetLabel()", "gRPC getAssetTypeLabel()" , "gRPC getDeviceAssignmentLabel()" , "gRPC getCustomerLabel()", "gRPC getCustomerTypeLabel()" , "gRPC getDeviceGroupLabel()" , "gRPC getDeviceLabel()", "gRPC getDeviceTypeLabel()"]}],
[7, 12, {"link": ["gRPC createScheduledJob()", "gRPC getScheduledJobByToken()", "gRPC updateScheduledJob()", "gRPC deleteScheduledJob()", "gRPC listScheduledJobs()", "gRPC createSchedule()", "gRPC getScheduleByToken()", "gRPC updateSchedule()", "gRPC listSchedules()", "gRPC deleteSchedule()", "gRPC getSchedule()"]}],
[11, 9, {"link": ["gRPC getAsset()"]}],
[13, 0, {"link": ["gRPC createDeviceAssignment()" , "gRPC getDeviceByToken()" , "gRPC createDevice()" , "gRPC updateDevice()" , "gRPC getDeviceTypeByToken()", "gRPC getCustomerByToken()"]}],
[13, 9, {"link": ["gRPC getAssetByToken()"]}],
[14, 0, {"link": ["gRPC getDeviceByToken()", "gRPC getDeviceTypeByToken()", "gRPC getDeviceAssignementByToken()", "gRPC getCustomerByToken()", "gRPC getAreaByToken()"]}],
[14, 9, {"link": ["gRPC getAssetByToken()"]}],
] }

projet3 = { "name" :  "Petclinic",
"services" : [[0, 'REST', 'API GATEWAY'], [1, 'REST', 'Customer-service'], [2, 'REST', 'Vet-service'], [3, 'REST', 'Visit-service']],
"relations" : [
[0, 1, {"link": ["GET /owners/{ownerId} "]}],
[0, 2, {"link": ["GET /vet/vets "] }],
[0, 3, {"link": ["GET /pets/visits "]}]
]}

projet4 = { "name" :  "eShop",
"services" : [[0, 'gRPC/Event', 'API GATEWAY'], [1, 'gRPC/Event', 'Ordering'], [2, 'gRPC/Event', 'Basket'], [3, 'gRPC', 'Catalog'], [4, 'Event', 'Payment']],
"relations" : [
[0, 1, {"link": ["gRPC CreateOrderDraftFromBasket() "]}],
[0, 2, {"link": ["gRPC GetBasketById() ", "gRPC UpdateBasket() "] }],
[0, 3, {"link": ["gRPC getItemById() ", "gRPC getItemsById() "]}],
[1, 2, {"link": ["EVENT OrderStartedIntegrationEvent "]}],
[2, 1, {"link": ["EVENT UserCheckoutAcceptedIntegrationEvent "]}],
[1, 4, {"link": ["EVENT OrderStatusChangedToStockConfirmedIntegrationEvent "]}],
[4, 1, {"link": ["EVENT orderPaymentIntegrationEvent "]}],
[3, 1, {"link": ["EVENT ProductPriceChangedIntegrationEvent "]}]
]}

projet5 = { "name" :  "GoogleCloudPlatform",
"services" : [[0, 'gRPC/REST', 'FRONTEND'], [1, 'gRPC/REST', 'Cart'], [2, 'gRPC/REST', 'Currency'], [3, 'gRPC', 'Shipping'], [4, 'gRPC', 'Payment'], [5, 'gRPC/REST', 'Checkout'], [6, 'gRPC', 'Recommandation'], [7, 'gRPC', 'Email'], [8, 'gRPC/REST', 'Product Catalog'], [9, 'gRPC', 'Ad']],
"relations" : [
[0, 1, {"link": ["POST /cart ", "POST /cart/empty ", "GET /cart ", "gRPC addItem() ", "gRPC getCart() ", "gRPC emptyCart() "]}],
[0, 2, {"link": ["POST /setCurrency ", "gRPC getSupportedCurrencies() ", "gRPC convert()"] }],
[0, 3, {"link": ["gRPC getQuote() "]}],
[0, 5, {"link": ["POST /cart/checkout ", "gRPC placeOrder() "]}],
[0, 6, {"link": ["gRPC ListRecommandations() "]}],
[0, 8, {"link": ["GET /product/{id} ", "gRPC GetProduct", "gRPC ListProducts "]}],
[0, 9, {"link": ["gRPC getAds "]}],
[5, 1, {"link": ["gRpc getCart ", "gRPC emptyCart"]}],
[5, 2, {"link": ["gRPC convert "]}],
[5, 3, {"link": ["gRPC shipOrder ", "gRPC getQuote "]}],
[5, 4, {"link": ["gRPC Pcharge "]}],
[5, 7, {"link": ["gRPC sendOrderConfirmation "]}],
[5, 8, {"link": ["gRPC getProduct "]}],
[6, 8, {"link": ["gRPC ListProducts "]}],
]}

projet6 = { "name" :  "Mspnp",
"services" : [[0, 'REST', 'Workflow service'], [1, 'REST', 'Package Service'], [2, 'REST', 'Drone Scheduler'], [3, 'REST', 'Delivery service'], [4, 'Event', 'Ingestion service']],
"relations" : [
[0, 1, {"link": ["PUT /api/package/{packageId} "]}],
[0, 2, {"link": ["PUT /api/dronedeliveries/{id} "] }],
[0, 3, {"link": ["PUT /api/deliveries/{id} "]}],
[4, 0, {"link": ["EVENT OperationEvent "]}]
]}

projet7 = { "name" :  "Piggymetrics",
"services" : [[0, 'REST', 'API GATEWAY'], [1, 'REST', 'Authentication'], [2, 'REST', 'Notification'], [3, 'REST', 'Account'], [4, 'REST', 'Statistics']],
"relations" : [
[0, 1, {"link": ["GET /uaa"]}],
[0, 2, {"link": ["GET /notifications "] }],
[0, 3, {"link": ["GET /accounts "]}],
[0, 4, {"link": ["GET /statistics "]}],
[2, 3, {"link": ["GET /accounts/{accountname} "]}],
[3, 1, {"link": ["POST /uaa/users "]}],
[3, 4, {"link": ["PUT /statistics/{accountname} "]}]
]}

projet8 = { "name" :  "PitStop",
"services" : [[0, 'REST', 'WebApp'], [1, 'REST', 'Vehicule Mgmt'], [2, 'REST', 'Customer Mgmt'], [3, 'REST', 'Workshop API'], [4, 'REST', 'Invoicing'], [5, 'REST', 'Notifications'], [6, 'REST', 'Workshop Event'], [7, 'REST', 'Auditlog'], [8, 'REST', 'Time']],
"relations" : [
[0, 1, {"link": ["GET /vehicles ", "POST /vehicles ", "GET /vehicles/{id} "]}],
[0, 2, {"link": ["GET /customers ", "POST /customers ", "GET /customers/{id} "] }],
[0, 3, {"link": ["GET /workshopplanning/{planningDate} ", "POST /workshopplanning/{planningDate} ", "POST /workshopplanning/{planningDate}/jobs ", "GET /workshopplanning/{planningDate}/jobs/{jobId} ", "PUT /workshopplanning/{planningDate}/jobs/{jobId}/finish ", "GET /refdata/customers ", "GET /refdata/customers/{id} ", "GET /refdata/vehicles ", "GET /refdata/vehicles/{id} "]}],
[1, 6, {"link": ["EVENT VehicleRegistered "] }],
[1, 7, {"link": ["EVENT VehicleRegistered "] }],
[2, 4, {"link": ["EVENT CustomerRegistered "] }],
[2, 5, {"link": ["EVENT CustomerRegistered "] }],
[2, 6, {"link": ["EVENT CustomerRegistered "] }],
[2, 7, {"link": ["EVENT CustomerRegistered "] }],
[3, 4, {"link": ["EVENT MaintenanceJobFinished, MaintenanceJobPlanned "] }],
[3, 5, {"link": ["EVENT MaintenanceJobFinished, MaintenanceJobPlanned "] }],
[3, 6, {"link": ["EVENT MaintenanceJobFinished, MaintenanceJobPlanned "] }],
[3, 7, {"link": ["EVENT MaintenanceJobFinished, MaintenanceJobPlanned, WorkshopPlanningCreated "] }],
[8, 4, {"link": ["EVENT DayHasPassed "] }],
[8, 5, {"link": ["EVENT DayHasPassed "] }],
[8, 7, {"link": ["EVENT DayHasPassed "] }]
]}

projet9 = { "name" :  "RobotShop",
"services" : [[0, 'REST', 'Catalogue'], [1, 'REST', 'Ratings'], [2, 'REST', 'Cart'], [3, 'EVENT', 'Dispatch'], [4, 'REST', 'Shipping'], [5, 'REST', 'Users'], [6, 'REST', 'Payments']],
"relations" : [
[1, 0, {"link": ["GET /product/{sku} "]}],
[2, 0, {"link": ["GET /product "] }],
[4, 2, {"link": ["POST /shipping/{id} "]}],
[6, 2, {"link": ["DELETE /cart/{id} "]}],
[6, 3, {"link": ["EVENT Dispatch "]}],
[6, 5, {"link": ["GET /check/{id} ", "POST /check/{id} "]}]
]}

projet10 = { "name" : "Digota" ,
"services" : [[0, 'gRPC', 'Payment'], [1, 'gRPC', 'Order'], [2, 'gRPC', 'Product'], [3, 'gRPC/REST', 'Sku']],
"relations" : [
[1, 0, {"link": ["gRPC NewCharge ", "gRPC RefundCharge "]}],
[1, 3, {"link": ["gRPC Get ", "gRPC GetWithInventoryLock "] }],
[2, 3, {"link": ["gRPC ProductData "]}],
[3, 2, {"link": ["gRPC Get "]}]
]}

projet11 = { "name" : "PartsUnlimited" ,
"services" : [[0, 'REST', 'WEB UI'], [1, 'REST', 'Quote'], [2, 'REST', 'Catalogue'], [3, 'REST', 'Order'], [4, 'REST', 'Dealer'], [5, 'REST', 'Shipment']],
"relations" : [
[0, 1, {"link": ["GET /quote ", "POST /quote ", "GET /quote/{quoteId} ", "DELETE /quote/{quoteId} ", "PUT /quote/{quoteId} ", "GET /quote/bydealer/{dealername} "]}],
[0, 2, {"link": ["GET /catalogue", "POST /catalogue ", "GET /catalogue/{skuNumber} ", "DELETE /catalogue/{skuNumber} ", "PUT /catalogue/{skuNumber} "] }],
[0, 3, {"link": ["GET /orders ", "POST /orders ", "GET /orders/{orderId} ", "PUT /orders/{orderId} ", "DELETE /orders/{orderId} ", "PUT /orders/{orderId}/status ", "POST /orders/{orderId}/events "]}],
[0, 4, {"link": ["GET /dealer ", "POST /dealer ", "GET /dealer/{dealerName} ", "DELETE /dealer/{dealerName} ", "PUT /dealer/{dealerName} "]}],
[0, 5, {"link": ["GET /shipments ", "POST /shipments ", "GET /shipments/{id} ", "DELETE /shipments/{id} ", "PUT /shipments/{id} ", "GET /shipments/{id}/events "]}]
]}

projet12 = { "name" : "Blueprint" ,
"services" : [[0, 'REST', 'API GATEWAY'], [1, 'REST', 'Inventory'], [2, 'REST', 'Account'], [3, 'REST', 'Product'], [4, 'REST', 'Shopping-Cart'], [5, 'REST', 'Order'], [6, 'REST', 'Payment'], [7, 'REST', 'Store']],
"relations" : [
[0, 1, {"link": ["GET /api/inventory/{productId} "]}],
[0, 2, {"link": ["GET /uaa ", "POST /logout "] }],
[0, 3, {"link": ["GET /api/product/{productId} "]}],
[0, 4, {"link": ["GET /api/cart/cart ", "POST /api/cart/events ", "POST /api/cart/checkout "]}],
[0, 5, {"link": ["GET /api/order/orders/{orderId} ", "GET /api/order/user/{userId}/orders "]}],
[4, 1, {"link": ["GET /inventory/{productId} "]}],
[4, 5, {"link": ["EVENT SHOPPING_TO_ORDER "]}],
[4, 6, {"link": ["EVENT SHOPPING_TO_PAYMENT "]}],
[5, 1, {"link": ["PUT /inventory/{productId}/decrease?n={amount} "]}],
]}

projet13 = { "name" : "MicroservicesDemo" ,
"services" : [[0, 'REST', 'Front End'], [1, 'REST', 'Payment'], [2, 'REST', 'Catalogue'], [3, 'REST', 'Orders'], [4, 'REST', 'Users'], [5, 'REST', 'Carts'], [6, 'REST', 'Shipping'], [7, 'EVENT', 'Queue-Master']],
"relations" : [
[0, 2, {"link": ["GET /catalogue ", "GET /catalogue/images ", "GET /tags "]}],
[0, 3, {"link": ["GET /orders/* ", "POST /orders "] }],
[0, 4, {"link": ["GET /customers ", "GET /customers/{id} ", "GET /cards ", "GET /card ", "GET /address ", "POST /cards ", "GET /cards/{id} ", "POST /register ", "GET /login "]}],
[0, 5, {"link": ["GET /cart ", "DELETE /cart ", "POST /cart ", "POST /cart/update ", "DELETE /cart/{id} "]}],
[3, 1, {"link": ["POST /paymentAuth "]}],
[3, 6, {"link": ["POST /shipping "]}],
[6, 7, {"link": ["EVENT shipping-task "]}]
]}


##### PERSISTENCE DES DONNÉES
persistence1 = { "name" : "Teastore",
"services" : [[0, 'DATABASE', 'MYSQL'], [1, 'REST', 'Authentication'], [2, 'REST', 'ImageProvider'], [3, 'REST', 'Persistence'], [4, 'REST', 'Recommender']],
"relations" : [
[3, 0, {"link": [""]}],
[1, 3, {"link": [""] }],
[2, 3, {"link": [""]}],
[4, 3, {"link": [""] }]]
 }

persistence2 = { "name" :  "Sitewhere",
"services" : [[0, 'gRPC', 'Device Mgmt'], [1, 'gRPC', 'outbounds-connectors'], [2, 'gRPC', 'event-sources'], [3, 'gRPC', 'inbound-processing'], [4, 'gRPC', 'batch-operations'], [5, 'gRPC', 'event-mgmt'], [6, 'gRPC', 'tenant-mgmt'], [7, 'gRPC', 'instance-mgmt'], [8, 'gRPC', 'schedule-mgmt'], [9, 'gRPC', 'user-mgmt'], [10, 'gRPC', 'asset-mgmt'], [11, 'gRPC', 'command-delivery'], [12, 'gRPC', 'label-generation'], [13, 'gRPC', 'schedule-mgmt'], [14, 'gRPC', 'device-registration'], [15, 'gRPC', 'device-state'], [16, 'SCHEMA', 'devicemanagement'], [17, 'TABLES', 'assets, assets_metadata, asset_type, asset_type_metadata'], [18, 'SCHEMA', 'batchoperations'], [19, 'SCHEMA', 'devicestate'], [20, 'SCHEMA', 'schedule-management'], [21, 'EVENT_BUS', 'KAFKA'], [22, 'gRPC', 'streaming-media'], [23, 'gRPC', 'service-event-search'] ],
"relations" : [
[0, 16, {"link": [""]}],
[10, 17, {"link": [""]}],
[4, 18, {"link": [""]}],
[15, 19, {"link": [""]}],
[13, 20, {"link": [""]}],
[16, 21, {"link": [""]}],
[17, 21, {"link": [""]}],
[18, 21, {"link": [""]}],
[19, 21, {"link": [""]}],
[20, 21, {"link": [""]}],
[15, 21, {"link": [""]}],
[1, 21, {"link": [""]}],
[2, 21, {"link": [""]}],
[3, 21, {"link": [""]}],
[5, 21, {"link": [""]}],
[7, 21, {"link": [""]}],
[11, 21, {"link": [""]}],
[12, 21, {"link": [""]}],
[14, 21, {"link": [""]}],
[22, 21, {"link": [""]}],
[23, 21, {"link": [""]}]
] }

persistence3 = { "name" :  "Petclinic",
"services" : [[0, 'TABLE', 'visits'], [1, 'REST', 'Customer-service'], [2, 'REST', 'Vet-service'], [3, 'REST', 'Visit-service'], [4, 'TABLE','specialities'], [5, 'TABLE', 'vets'], [6, 'TABLE', 'vet_specialities'], [7, 'TABLE', 'owners'], [8, 'TABLE', 'pets'], [9, 'TABLE', 'types']],
"relations" : [
[2, 4, {"link": [""]}],
[2, 5, {"link": [""] }],
[2, 6, {"link": [""]}],
[3, 0, {"link": [""]}],
[1, 7, {"link": [""] }],
[1, 8, {"link": [""]}],
[1, 9, {"link": [""]}],
[0, 8, {"link": ["INTERSERVICE FOREIGN KEY"]}],
]}

persistence4 = { "name" :  "eShop",
"services" : [[0, 'EVENT_BUS', 'EVENT BUS'], [1, 'gRPC/Event', 'Ordering'], [2, 'gRPC/Event', 'Basket'], [3, 'gRPC', 'Catalog'], [4, 'Event', 'Identity'], [5, 'DATABASE', ' OderingdDB - SQL SERVER'], [6, 'DATABASE', ' CatalogDB - SQL SERVER'],[7, 'DATABASE', ' IdentityDB - SQL SERVER']],
"relations" : [
[1, 5, {"link": [""]}],
[2, 0, {"link": [""] }],
[3, 6, {"link": [""]}],
[4, 7, {"link": [""]}],
[1, 0, {"link": [""]}],
[3, 0, {"link": [""]}],
[4, 0, {"link": [""]}]
]}

persistence5 = { "name" :  "GoogleCloudPlatform",
"services" : [[0, 'gRPC/REST', 'FRONTEND'], [1, 'gRPC/REST', 'Cart'], [2, 'gRPC/REST', 'Currency'], [3, 'gRPC', 'Shipping'], [4, 'gRPC', 'Payment'], [5, 'gRPC/REST', 'Checkout'], [6, 'gRPC', 'Recommandation'], [7, 'gRPC', 'Email'], [8, 'gRPC/REST', 'Product Catalog'], [9, 'gRPC', 'Ad'], [10, 'DATABASE', 'REDIS'], [11, 'DATABASE', 'JSON']],
"relations" : [
[0, 1, {"link": [""]}],
[0, 2, {"link": [""] }],
[0, 3, {"link": [""]}],
[0, 5, {"link": [""]}],
[0, 6, {"link": [""]}],
[0, 8, {"link": [""]}],
[0, 9, {"link": [""]}],
[5, 1, {"link": [""]}],
[5, 2, {"link": [""]}],
[5, 3, {"link": [""]}],
[5, 4, {"link": [""]}],
[5, 7, {"link": [""]}],
[5, 8, {"link": [""]}],
[6, 8, {"link": [""]}],
[1, 10, {"link": [""]}],
[8, 11, {"link": [""] }]
]}

persistence6 = { "name" :  "Mspnp",
"services" : [[0, 'REST', 'Workflow service'], [1, 'REST', 'Package Service'], [2, 'REST', 'Drone Scheduler'], [3, 'REST', 'Delivery service'], [4, 'Event', 'Ingestion service'], [5, 'DATABASE', 'mongopackageDB'], [6, 'DATABASE', 'cosmosDB'], [7, 'DATABASE', 'redis'], [8, 'EVENT_BUS', 'AZURE SERVICE BUS']],
"relations" : [
[0, 8, {"link": [""]}],
[4, 8, {"link": [""] }],
[1, 5, {"link": [""]}],
[2, 6, {"link": [""]}],
[3, 7, {"link": [""]}],
]}

persistence7 = { "name" :  "Piggymetrics",
"services" : [[0, 'COLLECTION', 'datapoints COLLECTION'], [1, 'REST', 'Authentication'], [2, 'REST', 'Notification'], [3, 'REST', 'Account'], [4, 'REST', 'Statistics'], [5, 'COLLECTION', 'users COLLECTION'], [6, 'COLLECTION', 'recipients COLLECTION'], [7, 'COLLECTION', 'accounts COLLECTION']],
"relations" : [
[1, 5, {"link": [""]}],
[2, 6, {"link": [""] }],
[3, 7, {"link": [""]}],
[4, 0, {"link": [""]}],
[4, 7, {"link": [""]}],

]}

persistence8 = { "name" :  "PitStop",
"services" : [[0, 'AMQP', 'RABBIT MQ'], [1, 'REST', 'Vehicule Mgmt'], [2, 'REST', 'Customer Mgmt'], [3, 'REST', 'Workshop API'], [4, 'REST', 'Invoicing'], [5, 'REST', 'Notifications'], [6, 'REST', 'Workshop Event'], [7, 'REST', 'Auditlog'], [8, 'REST', 'Time'], [9, 'DATABASE', 'Invoicing'], [10, 'DATABASE', 'Notifications'], [11, 'DATABASE', 'CustomerManagement'], [12, 'DATABASE', 'VehicleManagement'], [13, 'DATABASE', 'WorkshopManagement'], [14, 'DATABASE', 'WorkshopManagementEventStore']],
"relations" : [
[1, 12, {"link": [""]}],
[2, 11, {"link": [""] }],
[3, 13, {"link": [""]}],
[4, 9, {"link": [""] }],
[5, 10, {"link": [""] }],
[6, 13, {"link": [""] }],
[6, 14, {"link": [""] }],
[7, 0, {"link": [""] }],
[8, 0, {"link": [""] }],
[1, 0, {"link": [""] }],
[2, 0, {"link": [""] }],
[3, 0, {"link": [""] }],
[4, 0, {"link": [""] }],
[5, 0, {"link": [""] }],
[6, 0, {"link": [""] }],
]}

persistence9 = { "name" :  "RobotShop",
"services" : [[0, 'REST', 'Catalogue'], [1, 'REST', 'Ratings'], [2, 'REST', 'Cart'], [3, 'EVENT', 'Dispatch'], [4, 'REST', 'Shipping'], [5, 'REST', 'Users'], [6, 'REST', 'Payments'], [7,'AMQP', 'RABBIT MQ'], [8,'DATABASE', 'MongoUsers'], [9,'DATABASE', 'MySqlRatings'], [10,'DATABASE', 'MongoCatalogue'], [11,'DATABASE', 'RedisCart'], [12,'DATABASE', 'MysqlShipping']],
"relations" : [
[0, 10, {"link": [""]}],
[1, 9, {"link": [""]}],
[2, 11, {"link": [""] }],
[3, 7, {"link": [""] }],
[4, 12, {"link": [""]}],
[5, 8, {"link": [""]}],
[0, 7, {"link": [""]}],
[1, 7, {"link": [""]}],
[2, 7, {"link": [""]}],
[3, 7, {"link": [""]}],
[4, 7, {"link": [""]}],
[5, 7, {"link": [""]}],
[6, 7, {"link": [""]}],
]}

persistence10 = { "name" : "Digota" ,
"services" : [[0, 'gRPC', 'Payment'], [1, 'gRPC', 'Order'], [2, 'gRPC', 'Product'], [3, 'gRPC/REST', 'Sku'], [4, 'COLLECTION', 'charge - mongoDB'], [5, 'COLLECTION', 'product - mongoDB'], [6, 'COLLECTION', 'order - mongoDB'], [7, 'COLLECTION', 'sku - mongoDB']],
"relations" : [
[0, 4, {"link": [""]}],
[1, 6, {"link": [""] }],
[2, 5, {"link": [""]}],
[3, 7, {"link": [""]}]
]}

persistence11 = { "name" : "PartsUnlimited" ,
"services" : [[0, 'REST', 'Quote'], [1, 'REST', 'Catalogue'], [2, 'REST', 'Order'], [3, 'REST', 'Dealer'], [4, 'REST', 'Shipment'], [5, 'COLLECTION', 'dealer COLLECTION'], [6, 'COLLECTION', 'catalogue COLLECTION'], [7, 'COLLECTION', 'quote COLLECTION'], [8, 'COLLECTION', 'order COLLECTION'], [9, 'COLLECTION', 'shipment COLLECTION']],
"relations" : [
[0, 7, {"link": [""]}],
[1, 6, {"link": [""] }],
[2, 8, {"link": [""]}],
[3, 5, {"link": [""]}],
[4, 9, {"link": [""]}]
]}

persistence12 = { "name" : "Blueprint" ,
"services" : [[0, 'EVENT_BUS', 'EVENT BUS'], [1, 'REST', 'Inventory'], [2, 'REST', 'Account'], [3, 'REST', 'Product'], [4, 'REST', 'Shopping-Cart'], [5, 'REST', 'Order'], [6, 'REST', 'Payment'], [7, 'REST', 'Store'], [8, 'DATABASE', 'redis'], [9, 'DATABASE', 'mongo'], [10, 'TABLE', 'user_account TABLE - mysql'], [11, 'TABLE', 'product TABLE - mysql'], [12, 'TABLE', 'order TABLE - mysql'], [13, 'TABLE', 'cart_event TABLE - mysql'], [14, 'TABLE', 'payment TABLE - mysql']],
"relations" : [
[0, 6, {"link": [""]}],
[1, 8, {"link": [""]}],
[2, 10, {"link": [""] }],
[3, 11, {"link": [""]}],
[4, 13, {"link": [""]}],
[4, 0, {"link": [""]}],
[5, 12, {"link": [""]}],
[6, 14, {"link": [""]}],
[7, 9, {"link": [""]}],
]}

persistence13 = { "name" : "MicroservicesDemo" ,
"services" : [[0, 'EVENT_BUS', 'RABBIT MQ'], [1, 'REST', 'Catalogue'], [2, 'REST', 'Orders'], [3, 'REST', 'Users'], [4, 'REST', 'Carts'], [5, 'REST', 'Shipping'], [6, 'EVENT', 'Queue-Master'], [7, 'DATABASE', 'MySQL socksDB'], [8, 'DATABASE', 'mongodb - usersdb'], [9, 'DATABASE', 'mongodb - ordersdb'], [10, 'DATABASE', 'mongodb - cartsdb']],
"relations" : [
[1, 7, {"link": [""]}],
[2, 9, {"link": [""]}],
[3, 8, {"link": [""] }],
[4, 10, {"link": [""]}],
[5, 0, {"link": [""]}],
[0, 6, {"link": [""]}],
]}
