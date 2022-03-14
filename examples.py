#Finalement on va laisser les annotations REST, grpc ou auxtres. On va signaler dans les calculs les
# Trucs qui correspondent aux services et ceux qui correspondent aux bases de DONNÉES
# Faire la différence entre ce qui est schema et ce qui est base de données unique, meme si un schema protege les bases de donnees to talk to each other, cela reste un couplage de base de DONNÉES
# Lorsque les services sont reliés à la base de données on a TABLE qui signifie que le service est relié à une table, SCHEMA qui signifie que le service est relie a un schema dans la BD et FULL_DATABASE lorsque le servicea acces a toutes les données sans restrictions
# DATABASE


#On va calculer en fonction des relations le type de connexion avec la base de données



##### ARCHITECTURE DES PROJETS
#SERVICE, FACADE, DATABASE, MESSAGE_BROKER,
#Doit-on ajouter les MESSAGE_BROKER ? Oui bien voir les interactions avec les MESSAGE_BROKER
#RabbitMQ = Message MESSAGE_BROKER
#Kafka stream processing

projet1 = { "name" : "Teastore",
"services" : [
[0, 'FACADE', 'WEB UI'],
[1, 'SERVICE', 'Registry'],
[2, 'SERVICE', 'Authentication'],
[3, 'SERVICE', 'ImageProvider'],
[4, 'SERVICE', 'Persistence'],
[5, 'SERVICE', 'Recommender'],
[6, 'DATABASE', 'MYSQL']],

"relations" : [
[0, 1, {"link": ["POST /{name}/{location} ", " DELETE /{name}/{location}"]}],
[0, 2, {"link": ["POST /cart/add/{id} ", " POST /cart/remove/{id} ", " PUT /cart/{id} ", " POST /useractions/login ", " POST /useractions/logout ", " POST /useractions/placeorder ", " POST /useractions/isLoggedIn"] }],
[0, 3, {"link": ["POST /getProductImages ", " POST /getWebImages"]}],
[0, 4, {"link": ["GET /products ", " GET /categories ", " GET /users ", " GET /orders"] }],
[0, 5, {"link": ["POST /recommend/{uid}"]}],
[5, 4, {"link": ["GET /orders ", " GET /ordersitems"]}],
[2, 4, {"link": ["POST /products ", " POST /orders ", " POST /ordersitems"]}],
[3, 4, {"link": ["GET /generatedb ", " /GET products ", " GET/categories"]}],
[4, 6, {"link": ["FULL_DATABASE MYSQL"]}],
] }


projet2 = { "name" :  "Sitewhere",
"services" : [
[0, 'SERVICE', 'Device Mgmt'],
[1, 'SERVICE', 'outbounds-connectors'],
[2, 'SERVICE', 'event-sources'],
[3, 'SERVICE', 'inbound-processing'],
[4, 'SERVICE', 'batch-operations'],
[5, 'SERVICE', 'event-mgmt'],
[6, 'SERVICE', 'tenant-mgmt'],
[7, 'SERVICE', 'instance-mgmt'],
[8, 'SERVICE', 'user-mgmt'],
[9, 'SERVICE', 'asset-mgmt'],
[10, 'SERVICE', 'command-delivery'],
[11, 'SERVICE', 'label-generation'],
[12, 'SERVICE', 'schedule-mgmt'],
[13, 'SERVICE', 'device-registration'],
[14, 'SERVICE', 'device-state'],
[15, 'MESSAGE_BROKER', 'RabbitMQ'],
[16, 'SERVICE', 'streaming-media'],
[17, 'SERVICE', 'service-event-search'],
[18, 'EVENT_BUS', 'KAFKA'],
[19, 'DATABASE', 'MySQL']],


"relations" : [
[0, 19, {"link": ["SCHEMA devicemanagement"]}],
[4, 19, {"link": ["SCHEMA batchoperations"]}],
[14, 19, {"link": ["SCHEMA devicestate"]}],
[12, 19, {"link": ["SCHEMA schedule-management"]}],
[9, 19, {"link": ["TABLE assets", "TABLE assets_metadata", "TABLE asset_type", "TABLE asset_type_metadata"]}],
[0, 9, {"link": ["gRPC getAssetByToken()"]}],
[1, 0, {"link": ["gRPC getArea()", "gRPC getDevice()", "gRPC getDeviceType()", "gRPC getDeviceAssignment()" ]}],
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
[0, 18, {"link": ["Message Producer"]}],
[1, 18, {"link": ["Message Consumer"]}],
[1, 15, {"link": ["Message Producer"]}],
[2, 18, {"link": ["Message Producer"]}],
[3, 18, {"link": ["Stream Consumer"]}],
[4, 18, {"link": ["Message Producer", "Message Consumer"]}],
[5, 18, {"link": ["Message Producer"]}],
[7, 18, {"link": ["Stream Consumer"]}],
[10, 18, {"link": ["Message Producer", "Message Consumer"]}],
[12, 18, {"link": ["Message Consumer"]}],
[14, 18, {"link": ["Stream Consumer"]}],
[13, 18, {"link": ["Stream Consumer"]}],
[16, 18, {"link": ["EVENT_SOURCING"]}],
[17, 18, {"link": ["EVENT_SOURCING"]}],
[11, 18, {"link": ["EVENT_SOURCING"]}],

]}



projet3 = { "name" :  "Petclinic",
"services" : [
[0, 'FACADE', 'API GATEWAY'],
[1, 'SERVICE', 'Customer-service'],
[2, 'SERVICE', 'Vet-service'],
[3, 'SERVICE', 'Visit-service'],
[4, 'DATABASE','MySQL-DB']],

"relations" : [
[0, 1, {"link": ["GET /owners/{ownerId} "]}],
[0, 2, {"link": ["GET /vet/vets "] }],
[0, 3, {"link": ["GET /pets/visits "]}],
[2, 4, {"link": ["TABLE specialities"]}],
[2, 4, {"link": ["TABLE vets"] }],
[2, 4, {"link": ["TABLE vet_specialities"]}],
[3, 4, {"link": ["TABLE visits"]}],
[1, 4, {"link": ["TABLE owners"] }],
[1, 4, {"link": ["TABLE pets"]}],
[1, 4, {"link": ["TABLE types"]}],
]}



projet4 = { "name" :  "eShop",
"services" : [
[0, 'FACADE', 'WEB_BFF'],
[1, 'SERVICE', 'Ordering'],
[2, 'SERVICE', 'Basket'],
[3, 'SERVICE', 'Catalog'],
[4, 'SERVICE', 'Payment'],
[5, 'EVENT_BUS', 'EVENT BUS'],
[6, 'DATABASE', ' OderingdDB - SQL SERVER'],
[7, 'DATABASE', ' CatalogDB - SQL SERVER'],
[8, 'DATABASE', ' IdentityDB - SQL SERVER'],
[9, 'FACADE', 'MOBILE_BFF'],
],


"relations" : [
[0, 1, {"link": ["gRPC ASYNC CreateOrderDraftFromBasketAsync() "]}],
[0, 2, {"link": ["gRPC ASYNC GetBasketByIdAsync() ", "gRPC ASYNC UpdateBasketAsync() "] }],
[0, 3, {"link": ["gRPC ASYNC getItemByIdAsync() ", "gRPC ASYNC getItemsByIdAsync() "]}],
[9, 1, {"link": ["gRPC ASYNC CreateOrderDraftFromBasketAsync() "]}],
[9, 2, {"link": ["gRPC ASYNC GetBasketByIdAsync() ", "gRPC ASYNC UpdateBasketAsync() "] }],
[9, 3, {"link": ["gRPC ASYNC getItemByIdAsync() ", "gRPC ASYNC getItemsByIdAsync() "]}],
[1, 5, {"link": ["publishes EVENT OrderStartedIntegrationEvent ", "publishes EVENT OrderStatusChangedToStockConfirmedIntegrationEvent ", "subscribesTo EVENT UserCheckoutAcceptedIntegrationEvent","subscribesTo EVENT orderPaymentIntegrationEvent "]}],
[2, 5, {"link": ["publishes EVENT UserCheckoutAcceptedIntegrationEvent "]}],
[4, 5, {"link": ["publishes EVENT orderPaymentIntegrationEvent ", "subscribesTo EVENT OrderStatusChangedToStockConfirmedIntegrationEvent "]}],
[3, 5, {"link": ["publishes EVENT ProductPriceChangedIntegrationEvent "]}],
[1, 6, {"link": ["FULL_DATABASE OderingdDB - SQL SERVER"]}],
[3, 7, {"link": ["FULL_DATABASE CatalogDB - SQL SERVER"]}],
[4, 8, {"link": ["FULL_DATABASE IdentityDB - SQL SERVER"]}],
]}


projet5 = { "name" :  "GoogleCloudPlatform",
"services" : [
 [0, 'FACADE', 'FRONTEND'],
 [1, 'SERVICE', 'Cart'],
 [2, 'SERVICE', 'Currency'],
 [3, 'SERVICE', 'Shipping'],
 [4, 'SERVICE', 'Payment'],
 [5, 'SERVICE', 'Checkout'],
 [6, 'SERVICE', 'Recommandation'],
 [7, 'SERVICE', 'Email'],
 [8, 'SERVICE', 'Product Catalog'],
 [9, 'SERVICE', 'Ad'],
 [10, 'DATABASE', 'REDIS'],
 [11, 'DATABASE', 'JSON']],
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
[1, 10, {"link": ["FULL_DATABASE REDIS"]}],
[8, 11, {"link": ["FULL_DATABASE JSON"] }]
]}



projet6 = { "name" :  "Mspnp",
"services" : [
[0, 'SERVICE', 'Workflow service'],
[1, 'SERVICE', 'Package Service'],
[2, 'SERVICE', 'Drone Scheduler'],
[3, 'SERVICE', 'Delivery service'],
[4, 'SERVICE', 'Ingestion service'],
[5, 'DATABASE', 'mongopackageDB'],
[6, 'DATABASE', 'cosmosDB'],
[7, 'DATABASE', 'redis'],
[8, 'EVENT_BUS', 'AZURE SERVICE BUS']],

"relations" : [
[0, 1, {"link": ["PUT /api/package/{packageId} "]}],
[0, 2, {"link": ["PUT /api/dronedeliveries/{id} "] }],
[0, 3, {"link": ["PUT /api/deliveries/{id} "]}],
[4, 8, {"link": ["publishes EVENT OperationEvent "]}],
[8, 0, {"link": ["subscribesTo EVENT OperationEvent "]}],
[1, 5, {"link": ["FULL_DATABASE mongopackageDB"]}],
[2, 6, {"link": ["FULL_DATABASE cosmosDB"]}],
[3, 7, {"link": ["FULL_DATABASE redis"]}],
]}


projet7 = { "name" :  "Piggymetrics",
"services" : [
[0, 'FACADE', 'API GATEWAY'],
[1, 'SERVICE', 'Authentication'],
[2, 'SERVICE', 'Notification'],
[3, 'SERVICE', 'Account'],
[4, 'SERVICE', 'Statistics'],
[5, 'DATABASE', 'MongoDB']],

"relations" : [
[0, 1, {"link": ["GET /uaa"]}],
[0, 2, {"link": ["GET /notifications "] }],
[0, 3, {"link": ["GET /accounts "]}],
[0, 4, {"link": ["GET /statistics "]}],
[2, 3, {"link": ["GET /accounts/{accountname} "]}],
[3, 1, {"link": ["POST /uaa/users "]}],
[3, 4, {"link": ["PUT /statistics/{accountname} "]}],
[1, 5, {"link": ["COLLECTION users"]}],
[2, 5, {"link": ["COLLECTION recipients"] }],
[3, 5, {"link": ["COLLECTION accounts"]}],
[4, 5, {"link": ["COLLECTION datapoints"]}],
[4, 5, {"link": ["COLLECTION accounts"]}],
]}


projet8 = { "name" :  "PitStop",
"services" : [
[0, 'FACADE', 'WebApp'],
[1, 'SERVICE', 'Vehicule Mgmt'],
[2, 'SERVICE', 'Customer Mgmt'],
[3, 'SERVICE', 'Workshop API'],
[4, 'SERVICE', 'Invoicing'],
[5, 'SERVICE', 'Notifications'],
[6, 'SERVICE', 'Workshop Event'],
[7, 'SERVICE', 'Auditlog'],
[8, 'SERVICE', 'Time'],
[9, 'DATABASE', 'Invoicing'],
[10, 'DATABASE', 'Notifications'],
[11, 'DATABASE', 'CustomerManagement'],
[12, 'DATABASE', 'VehicleManagement'],
[13, 'DATABASE', 'WorkshopManagement'],
[14, 'DATABASE', 'WorkshopManagementEventStore'],
[15, 'MESSAGE_BROKER', 'RABBIT MQ']],

"relations" : [
[0, 1, {"link": ["GET /vehicles ", "POST /vehicles ", "GET /vehicles/{id} "]}],
[0, 2, {"link": ["GET /customers ", "POST /customers ", "GET /customers/{id} "] }],
[0, 3, {"link": ["GET /workshopplanning/{planningDate} ", "POST /workshopplanning/{planningDate} ", "POST /workshopplanning/{planningDate}/jobs ", "GET /workshopplanning/{planningDate}/jobs/{jobId} ", "PUT /workshopplanning/{planningDate}/jobs/{jobId}/finish ", "GET /refdata/customers ", "GET /refdata/customers/{id} ", "GET /refdata/vehicles ", "GET /refdata/vehicles/{id} "]}],
[1, 15, {"link": ["publishes EVENT VehicleRegistered "] }],
[2, 15, {"link": ["publishes EVENT CustomerRegistered ",] }],
[3, 15, {"link": ["publishes EVENT MaintenanceJobFinished", "publishes MaintenanceJobPlanned ", "publishes WorkshopPlanningCreated"] }],
[4, 15, {"link": ["subscribesTo EVENT CustomerRegistered", "subscribesTo EVENT MaintenanceJobFinished", "subscribesTo EVENT MaintenanceJobPlanned", "subscribesTo EVENT WorkshopPlanningCreated", "subscribesTo EVENT DayHasPassed"] }],
[5, 15, {"link": ["subscribesTo EVENT CustomerRegistered", "subscribesTo EVENT MaintenanceJobFinished", "subscribesTo EVENT MaintenanceJobPlanned", "subscribesTo EVENT DayHasPassed"] }],
[6, 15, {"link": ["subscribesTo EVENT VehicleRegistered ", "subscribesTo EVENT CustomerRegistered", "subscribesTo EVENT MaintenanceJobFinished", "subscribesTo EVENT MaintenanceJobPlanned"] }],
[7, 15, {"link": ["subscribesTo EVENT VehicleRegistered ", "subscribesTo EVENT CustomerRegistered", "subscribesTo EVENT MaintenanceJobFinished", "subscribesTo EVENT MaintenanceJobPlanned", "subscribesTo EVENT WorkshopPlanningCreated", "subscribesTo EVENT DayHasPassed"] }],
[8, 15, {"link": ["publishes EVENT DayHasPassed "] }],
[1, 12, {"link": ["FULL_DATABASE VehicleManagement"]}],
[2, 11, {"link": ["FULL_DATABASE CustomerManagement"] }],
[3, 13, {"link": ["FULL_DATABASE WorkshopManagement"]}],
[4, 9, {"link": ["FULL_DATABASE Invoicing"] }],
[5, 10, {"link": ["FULL_DATABASE Notifications"] }],
[6, 13, {"link": ["FULL_DATABASE WorkshopManagement"] }],
[6, 14, {"link": ["FULL_DATABASE WorkshopManagementEventStore"] }],
]}


#######
projet9 = { "name" :  "RobotShop",
"services" : [
[0, 'SERVICE', 'Catalogue'],
[1, 'SERVICE', 'Ratings'],
[2, 'SERVICE', 'Cart'],
[3, 'SERVICE', 'Dispatch'],
[4, 'SERVICE', 'Shipping'],
[5, 'SERVICE', 'Users'],
[6, 'SERVICE', 'Payments'],
[7,'MESSAGE_BROKER', 'RABBIT MQ'],
[8,'DATABASE', 'MongoUsers'],
[9,'DATABASE', 'MySqlRatings'],
[10,'DATABASE', 'MongoCatalogue'],
[11,'DATABASE', 'RedisCart'],
[12,'DATABASE', 'MysqlShipping']],

"relations" : [
[1, 0, {"link": ["GET /product/{sku} "]}],
[2, 0, {"link": ["GET /product "] }],
[4, 2, {"link": ["POST /shipping/{id} "]}],
[6, 2, {"link": ["DELETE /cart/{id} "]}],
[6, 7, {"link": ["publishes EVENT Dispatch "]}],
[7, 3, {"link": ["subscribesTo EVENT Dispatch "]}],
[6, 5, {"link": ["GET /check/{id} ", "POST /check/{id} "]}],
[0, 10, {"link": ["FULL_DATABASE MongoCatalogue"]}],
[1, 9, {"link": ["FULL_DATABASE MySqlRatings"]}],
[2, 11, {"link": ["FULL_DATABASE RedisCart"] }],
[4, 12, {"link": ["FULL_DATABASE MysqlShipping"]}],
[5, 8, {"link": ["FULL_DATABASE MongoUsers"]}],


]}



projet10 = { "name" : "Digota" ,
"services" : [
[0, 'SERVICE', 'Payment'],
[1, 'SERVICE', 'Order'],
[2, 'SERVICE', 'Product'],
[3, 'SERVICE', 'Sku'],
[4, 'DATABASE', 'mongoDB']],

"relations" : [
[1, 0, {"link": ["gRPC NewCharge ", "gRPC RefundCharge "]}],
[1, 3, {"link": ["gRPC Get ", "gRPC GetWithInventoryLock "] }],
[2, 3, {"link": ["gRPC ProductData "]}],
[3, 2, {"link": ["gRPC Get "]}],
[0, 4, {"link": ["COLLECTION charge"]}],
[2, 4, {"link": ["COLLECTION product"]}],
[1, 4, {"link": ["COLLECTION order"] }],
[3, 4, {"link": ["COLLECTION sku"]}]
]}



projet11 = { "name" : "PartsUnlimited" ,
"services" : [
[0, 'FACADE', 'WEB UI'],
[1, 'SERVICE', 'Quote'],
[2, 'SERVICE', 'Catalogue'],
[3, 'SERVICE', 'Order'],
[4, 'SERVICE', 'Dealer'],
[5, 'SERVICE', 'Shipment'],
[6, 'DATABASE', 'MongoDB'],

],
"relations" : [
[0, 1, {"link": ["GET /quote ", "POST /quote ", "GET /quote/{quoteId} ", "DELETE /quote/{quoteId} ", "PUT /quote/{quoteId} ", "GET /quote/bydealer/{dealername} "]}],
[0, 2, {"link": ["GET /catalogue", "POST /catalogue ", "GET /catalogue/{skuNumber} ", "DELETE /catalogue/{skuNumber} ", "PUT /catalogue/{skuNumber} "] }],
[0, 3, {"link": ["GET /orders ", "POST /orders ", "GET /orders/{orderId} ", "PUT /orders/{orderId} ", "DELETE /orders/{orderId} ", "PUT /orders/{orderId}/status ", "POST /orders/{orderId}/events "]}],
[0, 4, {"link": ["GET /dealer ", "POST /dealer ", "GET /dealer/{dealerName} ", "DELETE /dealer/{dealerName} ", "PUT /dealer/{dealerName} "]}],
[0, 5, {"link": ["GET /shipments ", "POST /shipments ", "GET /shipments/{id} ", "DELETE /shipments/{id} ", "PUT /shipments/{id} ", "GET /shipments/{id}/events "]}],
[4, 6, {"link": ["COLLECTION dealer"]}],
[2, 6, {"link": ["COLLECTION catalogue"]}],
[1, 6, {"link": ["COLLECTION quote"]}],
[3, 6, {"link": ["COLLECTION order"]}],
[5, 6, {"link": ["COLLECTION shipment"]}]
]}


projet12 = { "name" : "Blueprint" ,
"services" : [
[0, 'FACADE', 'API GATEWAY'],
[1, 'SERVICE', 'Inventory'],
[2, 'SERVICE', 'Account'],
[3, 'SERVICE', 'Product'],
[4, 'SERVICE', 'Shopping-Cart'],
[5, 'SERVICE', 'Order'],
[6, 'SERVICE', 'Payment'],
[7, 'SERVICE', 'Store'],
[8, 'EVENT_BUS', 'EVENT BUS'],
[9, 'DATABASE', 'Redis'],
[10, 'DATABASE', 'MongoDB'],
[11, 'DATABASE', 'MySQL'],
],

"relations" : [
[0, 1, {"link": ["GET /api/inventory/{productId} "]}],
[0, 2, {"link": ["GET /uaa ", "POST /logout "] }],
[0, 3, {"link": ["GET /api/product/{productId} "]}],
[0, 4, {"link": ["GET /api/cart/cart ", "POST /api/cart/events ", "POST /api/cart/checkout "]}],
[0, 5, {"link": ["GET /api/order/orders/{orderId} ", "GET /api/order/user/{userId}/orders "]}],
[4, 1, {"link": ["GET /inventory/{productId} "]}],
[5, 1, {"link": ["PUT /inventory/{productId}/decrease?n={amount} "]}],
[4, 8, {"link": ["publishes EVENT SHOPPING_TO_ORDER", "publishes EVENT SHOPPING_TO_PAYMENT "]}],
[5, 8, {"link": ["subscribesTo EVENT SHOPPING_TO_ORDER "]}],
[6, 8, {"link": ["subscribesTo EVENT SHOPPING_TO_PAYMENT "]}],
[1, 9, {"link": ["FULL_DATABASE Redis"]}],
[7, 10, {"link": ["FULL_DATABASE MongoDB"]}],
[2, 11, {"link": ["TABLE user_account"] }],
[3, 11, {"link": ["TABLE product"]}],
[4, 11, {"link": ["TABLE cart_event"]}],
[5, 11, {"link": ["TABLE order"]}],
[6, 11, {"link": ["TABLE payment"]}],
]}



projet13 = { "name" : "MicroservicesDemo" ,
"services" : [
[0, 'FACADE', 'Front End'],
[1, 'SERVICE', 'Payment'],
[2, 'SERVICE', 'Catalogue'],
[3, 'SERVICE', 'Orders'],
[4, 'SERVICE', 'Users'],
[5, 'SERVICE', 'Carts'],
[6, 'SERVICE', 'Shipping'],
[7, 'SERVICE', 'Queue-Master'],
[8, 'MESSAGE_BROKER', 'RABBIT MQ'],
[9,  'DATABASE', 'MySQL socksDB'],
[10, 'DATABASE', 'MongoDB usersdb'],
[11, 'DATABASE', 'MongoDB ordersdb'],
[12, 'DATABASE', 'MongoDB cartsdb']],
"relations" : [
[0, 2, {"link": ["GET /catalogue ", "GET /catalogue/images ", "GET /tags "]}],
[0, 3, {"link": ["GET /orders/* ", "POST /orders "] }],
[0, 4, {"link": ["GET /customers ", "GET /customers/{id} ", "GET /cards ", "GET /card ", "GET /address ", "POST /cards ", "GET /cards/{id} ", "POST /register ", "GET /login "]}],
[0, 5, {"link": ["GET /cart ", "DELETE /cart ", "POST /cart ", "POST /cart/update ", "DELETE /cart/{id} "]}],
[3, 1, {"link": ["POST /paymentAuth "]}],
[3, 6, {"link": ["POST /shipping "]}],

[6, 8, {"link": ["publishes EVENT shipping-task "]}],
[7, 8, {"link": ["subscribesTo EVENT shipping-task "]}],

[2, 9, {"link": ["FULL_DATABASE MySQL socksDB"]}],
[3, 11, {"link": ["FULL_DATABASE MongoDB ordersdb"]}],
[4, 10, {"link": ["FULL_DATABASE MongoDB usersdb"] }],
[5, 12, {"link": ["FULL_DATABASE MongoDB cartsdb"]}],
]}
