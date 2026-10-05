-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: localhost    Database: newmanikantajewellery
-- ------------------------------------------------------
-- Server version	8.0.46

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `account_details`
--

DROP TABLE IF EXISTS `account_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `account_details` (
  `account_id` int NOT NULL AUTO_INCREMENT,
  `account_name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `print_name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `account_group` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `op_bal` decimal(15,2) DEFAULT NULL,
  `metal_balance` decimal(15,2) DEFAULT NULL,
  `dr_cr` enum('Dr','Cr') COLLATE utf8mb4_general_ci DEFAULT NULL,
  `address1` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `address2` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `city` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `pincode` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `state` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `state_code` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `phone` varchar(15) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `mobile` varchar(15) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `contact_person` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `email` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `anniversary` date DEFAULT NULL,
  `bank_account_no` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `bank_name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `ifsc_code` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `branch` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `gst_in` varchar(15) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `aadhar_card` varchar(12) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `pan_card` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `religion` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `images` varchar(450) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `password` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `joining_date` date DEFAULT NULL,
  `kyc_status` enum('pending','verified','rejected') COLLATE utf8mb4_general_ci DEFAULT 'pending',
  `aadhaar_document` varchar(450) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `pan_document` varchar(450) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `verified_by` int DEFAULT NULL,
  `rejection_reason` text COLLATE utf8mb4_general_ci,
  `referred_person_name` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `referred_person_id` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `referred_person_referral_code` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `customer_referral_code` varchar(30) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `nominee_name` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `nominee_email` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `nominee_phone_number` varchar(15) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `relationship` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `nominee_aadhaar_number` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `nominee_pan_number` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `remarks` text COLLATE utf8mb4_general_ci,
  PRIMARY KEY (`account_id`),
  UNIQUE KEY `customer_referral_code` (`customer_referral_code`),
  KEY `idx_kyc_status` (`kyc_status`),
  KEY `idx_joining_date` (`joining_date`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_details`
--

LOCK TABLES `account_details` WRITE;
/*!40000 ALTER TABLE `account_details` DISABLE KEYS */;
INSERT INTO `account_details` VALUES (52,'SAIKRUSHNA CHARY KADARLA','SAIKRUSHNA CHARY KADARLA','CUSTOMERS',NULL,NULL,NULL,'SH11, Sircilla, Sircilla mandal, Rajanna Sircilla, Telangana, 505301, India','Sircilla','Sircilla','505301',NULL,NULL,'0938185028','0938185028',NULL,'kadarlasaikrushna99@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2026-04-07 10:28:29',NULL,NULL,'1234',NULL,'pending',NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,''),(53,'PAVANI','PAVANI','SUPPLIERS',NULL,NULL,NULL,'SH11, Sircilla, Sircilla mandal, Rajanna Sircilla, Telangana, 505301, India','Sircilla','Sircilla','505301','','','0938185028','0938185025',NULL,'kadarlasaikrushna99@gmail.com',NULL,NULL,'','','','','','','','2026-04-07 10:29:33',NULL,NULL,NULL,NULL,'pending',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(54,'saikrushna Chary kadarla','saikrushna Chary kadarla','CUSTOMERS',NULL,NULL,NULL,'','','Rajanna Sircilla','505301','Telangana','','9381850288','9381850288',NULL,'kadarlasaikrushna9901@gmail.com','2026-04-29',NULL,'','','','','','','','2026-04-28 07:54:25','',NULL,NULL,NULL,'pending',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(55,'saikrushna Chary kadarla','saikrushna Chary kadarla','CUSTOMERS',NULL,NULL,NULL,'','','Rajanna Sircilla','505301','Andhra Pradesh','','7381850288','7381850288',NULL,'admin123@gmail.com',NULL,'2026-04-15','','','','','','','','2026-04-30 09:58:01','',NULL,NULL,NULL,'pending',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `account_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accountgroup`
--

DROP TABLE IF EXISTS `accountgroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accountgroup` (
  `accountgroup_id` int NOT NULL AUTO_INCREMENT,
  `AccountsGroupName` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`accountgroup_id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accountgroup`
--

LOCK TABLES `accountgroup` WRITE;
/*!40000 ALTER TABLE `accountgroup` DISABLE KEYS */;
/*!40000 ALTER TABLE `accountgroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `assigned_repairdetails`
--

DROP TABLE IF EXISTS `assigned_repairdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `assigned_repairdetails` (
  `id` int NOT NULL AUTO_INCREMENT,
  `repair_id` int DEFAULT NULL,
  `item_name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `purity` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `qty` int DEFAULT NULL,
  `weight` decimal(10,3) DEFAULT NULL,
  `rate_type` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `rate` decimal(10,2) DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `assigned_repairdetails`
--

LOCK TABLES `assigned_repairdetails` WRITE;
/*!40000 ALTER TABLE `assigned_repairdetails` DISABLE KEYS */;
INSERT INTO `assigned_repairdetails` VALUES (32,52,'Gold','22K',1,5.000,'Rate for Weight',500.00,2500.00,'2026-01-17 11:27:25'),(33,53,'gold','22K',1,1.000,'Rate per Qty',5400.00,5400.00,'2026-04-07 06:59:49'),(34,54,'gold','22 KT',1,1.000,'Rate per Qty',5400.00,5400.00,'2026-04-07 07:11:36');
/*!40000 ALTER TABLE `assigned_repairdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add scheme',7,'add_scheme'),(26,'Can change scheme',7,'change_scheme'),(27,'Can delete scheme',7,'delete_scheme'),(28,'Can view scheme',7,'view_scheme'),(29,'Can add customer scheme enrollment',8,'add_customerschemeenrollment'),(30,'Can change customer scheme enrollment',8,'change_customerschemeenrollment'),(31,'Can delete customer scheme enrollment',8,'delete_customerschemeenrollment'),(32,'Can view customer scheme enrollment',8,'view_customerschemeenrollment'),(33,'Can add scheme installment',9,'add_schemeinstallment'),(34,'Can change scheme installment',9,'change_schemeinstallment'),(35,'Can delete scheme installment',9,'delete_schemeinstallment'),(36,'Can view scheme installment',9,'view_schemeinstallment'),(37,'Can add scheme receipt',10,'add_schemereceipt'),(38,'Can change scheme receipt',10,'change_schemereceipt'),(39,'Can delete scheme receipt',10,'delete_schemereceipt'),(40,'Can view scheme receipt',10,'view_schemereceipt'),(41,'Can add account details',11,'add_accountdetails'),(42,'Can change account details',11,'change_accountdetails'),(43,'Can delete account details',11,'delete_accountdetails'),(44,'Can view account details',11,'view_accountdetails'),(45,'Can add users',12,'add_users'),(46,'Can change users',12,'change_users'),(47,'Can delete users',12,'delete_users'),(48,'Can view users',12,'view_users');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$1000000$YDG0fxcl2ul4dJWGRysdfI$M6uASrfmu+sbDj2K+rlDOr25FmHi349RwXCwaKy6114=','2026-07-17 12:53:59.411968',1,'admin','','','',1,1,'2026-07-17 12:53:50.788066');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_details`
--

DROP TABLE IF EXISTS `company_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company_details` (
  `id` int NOT NULL AUTO_INCREMENT,
  `company_name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `address` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `address2` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `city` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `pincode` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `state` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `state_code` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `country` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `mobile` varchar(15) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `phone` varchar(15) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `website` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `gst_no` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `pan_no` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `bank_name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `bank_account_no` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `ifsc_code` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `branch` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `bank_url` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `email` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_details`
--

LOCK TABLES `company_details` WRITE;
/*!40000 ALTER TABLE `company_details` DISABLE KEYS */;
INSERT INTO `company_details` VALUES (7,'MANIKANTA JEWELLERS','Keshavakrupa complex, near chennakeshava swamy temple','','kote, belur','573115','Karnataka','29','India','','','','29EXQPP3451K1ZN','','','','','','','');
/*!40000 ALTER TABLE `company_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `current_rates`
--

DROP TABLE IF EXISTS `current_rates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `current_rates` (
  `current_rates_id` int NOT NULL AUTO_INCREMENT,
  `rate_date` date NOT NULL,
  `rate_time` time NOT NULL,
  `rate_9crt` decimal(10,2) DEFAULT NULL,
  `rate_16crt` decimal(10,2) DEFAULT NULL,
  `rate_18crt` decimal(10,2) DEFAULT NULL,
  `rate_22crt` decimal(10,2) DEFAULT NULL,
  `rate_24crt` decimal(10,2) DEFAULT NULL,
  `silver_rate` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`current_rates_id`),
  UNIQUE KEY `rate_date` (`rate_date`,`rate_time`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `current_rates`
--

LOCK TABLES `current_rates` WRITE;
/*!40000 ALTER TABLE `current_rates` DISABLE KEYS */;
INSERT INTO `current_rates` VALUES (1,'2026-05-12','16:40:25',4909.00,7855.00,9949.00,12000.00,13091.00,120.00);
/*!40000 ALTER TABLE `current_rates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `designmaster`
--

DROP TABLE IF EXISTS `designmaster`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `designmaster` (
  `design_id` int NOT NULL AUTO_INCREMENT,
  `metal` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `short_id` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `item_type` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `design_item` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `design_name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `wastage_percentage` decimal(5,2) DEFAULT NULL,
  `making_charge` decimal(10,2) DEFAULT NULL,
  `design_short_code` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `brand_category` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `mc_type` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`design_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `designmaster`
--

LOCK TABLES `designmaster` WRITE;
/*!40000 ALTER TABLE `designmaster` DISABLE KEYS */;
INSERT INTO `designmaster` VALUES (15,'GOLD','G253','Ring','','Wedding Ring',NULL,NULL,'','','','2025-12-12 13:12:12','2025-12-12 13:12:12'),(16,'GOLD','G253','Ring','','Elegant Gold Ring',NULL,NULL,'','','','2025-12-12 13:12:31','2025-12-12 13:12:31'),(17,'SILVER','','Anklets','','Bridal ',NULL,NULL,'','','','2025-12-12 13:12:53','2025-12-12 13:12:53');
/*!40000 ALTER TABLE `designmaster` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2026-07-17 16:38:48.089942','52','AccountDetails object (52)',2,'[{\"changed\": {\"fields\": [\"Password\"]}}]',11,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(11,'erp','accountdetails'),(12,'erp','users'),(8,'schemes','customerschemeenrollment'),(7,'schemes','scheme'),(9,'schemes','schemeinstallment'),(10,'schemes','schemereceipt'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2026-07-17 12:48:05.523637'),(2,'auth','0001_initial','2026-07-17 12:48:06.232038'),(3,'admin','0001_initial','2026-07-17 12:48:06.401320'),(4,'admin','0002_logentry_remove_auto_add','2026-07-17 12:48:06.426845'),(5,'admin','0003_logentry_add_action_flag_choices','2026-07-17 12:48:06.433661'),(6,'contenttypes','0002_remove_content_type_name','2026-07-17 12:48:06.548563'),(7,'auth','0002_alter_permission_name_max_length','2026-07-17 12:48:06.642802'),(8,'auth','0003_alter_user_email_max_length','2026-07-17 12:48:06.672236'),(9,'auth','0004_alter_user_username_opts','2026-07-17 12:48:06.678157'),(10,'auth','0005_alter_user_last_login_null','2026-07-17 12:48:06.738919'),(11,'auth','0006_require_contenttypes_0002','2026-07-17 12:48:06.741605'),(12,'auth','0007_alter_validators_add_error_messages','2026-07-17 12:48:06.747012'),(13,'auth','0008_alter_user_username_max_length','2026-07-17 12:48:06.828614'),(14,'auth','0009_alter_user_last_name_max_length','2026-07-17 12:48:06.906836'),(15,'auth','0010_alter_group_name_max_length','2026-07-17 12:48:06.921398'),(16,'auth','0011_update_proxy_permissions','2026-07-17 12:48:06.931954'),(17,'auth','0012_alter_user_first_name_max_length','2026-07-17 12:48:07.002822'),(18,'erp','0001_initial','2026-07-17 12:48:07.009296'),(19,'schemes','0001_initial','2026-07-17 12:48:07.680285'),(20,'sessions','0001_initial','2026-07-17 12:48:07.716592');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('5rc2uhmgm2ah9z1myybxyj18vrbulaeb','.eJxVjMsOwiAUBf-FtSG8WsCle7-B3AdI1dCktCvjv2uTLnR7Zua8RIJtrWnreUkTi7PQ4vS7IdAjtx3wHdptljS3dZlQ7oo8aJfXmfPzcrh_BxV6_dZRWcNkiUMcc3BWY-aBDLHCotAD2GJ1dGEwprDHkdhDBHbeQCDiLN4f94Q47Q:1wki4l:-XZufsxtGThBWpmBrSGG_kK8nbDbKmmyuKUThlj5W3c','2026-07-31 12:53:59.416540');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estimate`
--

DROP TABLE IF EXISTS `estimate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estimate` (
  `estimate_id` int NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `pcode` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `estimate_number` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `opentag_id` int DEFAULT NULL,
  `code` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `product_id` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `product_name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `metal_type` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `design_name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `purity` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `category` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `sub_category` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `gross_weight` decimal(10,3) DEFAULT NULL,
  `stone_weight` decimal(10,3) DEFAULT NULL,
  `stone_price` decimal(10,2) DEFAULT NULL,
  `weight_bw` decimal(10,3) DEFAULT NULL,
  `va_on` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `va_percent` decimal(10,2) DEFAULT NULL,
  `wastage_weight` decimal(10,3) DEFAULT NULL,
  `total_weight_av` decimal(10,3) DEFAULT NULL,
  `mc_on` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `mc_per_gram` decimal(10,2) DEFAULT NULL,
  `making_charges` decimal(10,2) DEFAULT NULL,
  `rate` decimal(10,2) DEFAULT NULL,
  `rate_amt` int DEFAULT NULL,
  `tax_percent` decimal(5,2) DEFAULT NULL,
  `tax_amt` decimal(10,2) DEFAULT NULL,
  `total_price` decimal(10,2) DEFAULT NULL,
  `pricing` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `pieace_cost` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `disscount_percentage` decimal(10,2) DEFAULT NULL,
  `disscount` decimal(10,2) DEFAULT NULL,
  `hm_charges` decimal(10,2) DEFAULT NULL,
  `total_amount` decimal(10,2) DEFAULT NULL,
  `taxable_amount` decimal(10,2) DEFAULT NULL,
  `tax_amount` decimal(10,2) DEFAULT NULL,
  `net_amount` decimal(10,2) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `original_total_price` decimal(10,2) DEFAULT NULL,
  `qty` int DEFAULT NULL,
  PRIMARY KEY (`estimate_id`)
) ENGINE=InnoDB AUTO_INCREMENT=90 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estimate`
--

LOCK TABLES `estimate` WRITE;
/*!40000 ALTER TABLE `estimate` DISABLE KEYS */;
/*!40000 ALTER TABLE `estimate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member_schemes`
--

DROP TABLE IF EXISTS `member_schemes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member_schemes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `invoice_id` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `scheme` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `member_name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `member_number` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `scheme_name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `installments_paid` int DEFAULT '0',
  `duration_months` int DEFAULT '0',
  `paid_months` int DEFAULT '0',
  `pending_months` int DEFAULT '0',
  `pending_amount` decimal(10,2) DEFAULT '0.00',
  `paid_amount` decimal(10,2) DEFAULT '0.00',
  `schemes_total_amount` decimal(10,2) DEFAULT '0.00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member_schemes`
--

LOCK TABLES `member_schemes` WRITE;
/*!40000 ALTER TABLE `member_schemes` DISABLE KEYS */;
/*!40000 ALTER TABLE `member_schemes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `metaltype`
--

DROP TABLE IF EXISTS `metaltype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `metaltype` (
  `metal_type_id` int NOT NULL AUTO_INCREMENT,
  `metal_name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `hsn_code` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `description` text COLLATE utf8mb4_unicode_ci,
  `default_purity` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `default_purity_for_rate_entry` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `default_purity_for_old_metal` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `default_issue_purity` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`metal_type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `metaltype`
--

LOCK TABLES `metaltype` WRITE;
/*!40000 ALTER TABLE `metaltype` DISABLE KEYS */;
INSERT INTO `metaltype` VALUES (2,'GOLD','','','99.9','99.9','99.5','99.5','2025-09-26 09:09:47','2025-10-31 09:35:10'),(3,'SILVER','','','99.90','99.90','99.90','99.90','2025-10-08 10:28:37','2025-10-08 10:28:37'),(4,'DIAMOND','','','99.50','95.00','99.50','99.50','2025-10-09 04:24:04','2025-10-09 04:24:04');
/*!40000 ALTER TABLE `metaltype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `offerstable`
--

DROP TABLE IF EXISTS `offerstable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `offerstable` (
  `offer_id` int NOT NULL,
  `offer_name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `discount_on` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `discount_on_rate` decimal(10,2) DEFAULT NULL,
  `discount_percentage` int DEFAULT NULL,
  `discount_percent_fixed` int DEFAULT NULL,
  `valid_from` datetime DEFAULT NULL,
  `valid_to` datetime DEFAULT NULL,
  `offer_status` varchar(50) COLLATE utf8mb4_general_ci DEFAULT 'Applied',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`offer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `offerstable`
--

LOCK TABLES `offerstable` WRITE;
/*!40000 ALTER TABLE `offerstable` DISABLE KEYS */;
INSERT INTO `offerstable` VALUES (1,'Special Offer','',250.00,25,25,'2026-04-18 00:00:00','2026-05-18 00:00:00','Unapplied','2026-04-18 08:54:38','2026-05-01 08:59:08');
/*!40000 ALTER TABLE `offerstable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `old_items`
--

DROP TABLE IF EXISTS `old_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `old_items` (
  `id` int NOT NULL AUTO_INCREMENT,
  `invoice_id` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `product` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `metal` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `purity` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `hsn_code` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `gross` decimal(10,3) DEFAULT '0.000',
  `dust` decimal(10,3) DEFAULT '0.000',
  `ml_percent` decimal(10,2) DEFAULT '0.00',
  `net_wt` decimal(10,3) DEFAULT '0.000',
  `remarks` text COLLATE utf8mb4_unicode_ci,
  `rate` decimal(10,2) DEFAULT '0.00',
  `total_amount` decimal(10,2) DEFAULT '0.00',
  `total_old_amount` decimal(10,2) DEFAULT '0.00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `old_items`
--

LOCK TABLES `old_items` WRITE;
/*!40000 ALTER TABLE `old_items` DISABLE KEYS */;
/*!40000 ALTER TABLE `old_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `opening_tags_entry`
--

DROP TABLE IF EXISTS `opening_tags_entry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `opening_tags_entry` (
  `opentag_id` int NOT NULL AUTO_INCREMENT,
  `product_id` int DEFAULT NULL,
  `subcategory_id` int DEFAULT NULL,
  `sub_category` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Pricing` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Prefix` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `category` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Purity` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `metal_type` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `PCode_BarCode` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Gross_Weight` decimal(10,3) DEFAULT '0.000',
  `Stones_Weight` decimal(10,3) DEFAULT '0.000',
  `Stones_Price` decimal(10,2) DEFAULT '0.00',
  `Weight_BW` decimal(10,3) DEFAULT '0.000',
  `HUID_No` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Wastage_On` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Wastage_Percentage` decimal(10,2) DEFAULT NULL,
  `WastageWeight` decimal(10,3) DEFAULT '0.000',
  `MC_Per_Gram` decimal(10,2) DEFAULT NULL,
  `Making_Charges_On` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `TotalWeight_AW` decimal(10,3) DEFAULT NULL,
  `Making_Charges` decimal(10,2) DEFAULT NULL,
  `rate` decimal(10,2) DEFAULT NULL,
  `tax` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `tax_amt` decimal(10,2) DEFAULT NULL,
  `total_price` decimal(12,2) DEFAULT NULL,
  `Status` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Source` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Stock_Point` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `making_on` varchar(250) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `dropdown` varchar(250) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `selling_price` int DEFAULT NULL,
  `pcs` int DEFAULT NULL,
  `pieace_cost` decimal(10,2) DEFAULT NULL,
  `design_master` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `product_Name` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `qr_status` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `cut` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `color` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `clarity` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `stone_price_per_carat` decimal(10,2) DEFAULT NULL,
  `deduct_st_Wt` varchar(5) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `MC_Per_Gram_Label` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `pur_Gross_Weight` decimal(10,3) DEFAULT '0.000',
  `pur_Stones_Weight` decimal(10,3) DEFAULT '0.000',
  `pur_deduct_st_Wt` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `pur_stone_price_per_carat` decimal(10,2) DEFAULT NULL,
  `pur_Stones_Price` decimal(10,2) DEFAULT '0.00',
  `pur_Weight_BW` decimal(10,3) DEFAULT NULL,
  `pur_Making_Charges_On` varchar(30) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `pur_MC_Per_Gram` decimal(10,2) DEFAULT NULL,
  `pur_Making_Charges` decimal(10,2) DEFAULT NULL,
  `pur_Wastage_On` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `pur_Wastage_Percentage` decimal(5,2) DEFAULT NULL,
  `pur_WastageWeight` decimal(10,3) DEFAULT NULL,
  `pur_TotalWeight_AW` decimal(10,3) DEFAULT NULL,
  `tag_id` int DEFAULT NULL,
  `tag_weight` decimal(10,3) DEFAULT NULL,
  `size` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `account_name` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `invoice` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `image` longtext COLLATE utf8mb4_general_ci,
  `item_prefix` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `suffix` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `pur_MC_Per_Gram_Label` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `tax_percent` varchar(30) COLLATE utf8mb4_general_ci DEFAULT '0.00',
  `mrp_price` decimal(10,2) DEFAULT '0.00',
  `total_pcs_cost` decimal(10,2) DEFAULT '0.00',
  `pur_rate_cut` decimal(10,2) DEFAULT NULL,
  `pur_Purity` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `pur_purityPercentage` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `printing_purity` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`opentag_id`)
) ENGINE=InnoDB AUTO_INCREMENT=105 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `opening_tags_entry`
--

LOCK TABLES `opening_tags_entry` WRITE;
/*!40000 ALTER TABLE `opening_tags_entry` DISABLE KEYS */;
INSERT INTO `opening_tags_entry` VALUES (94,145,157,'GOLD BRACELETS','By Weight','GBR','GOLD JEWELLERY','95','GOLD','GBR001',10.000,0.000,0.00,10.000,'','Gross Weight',10.00,1.000,10.00,'MC %',11.000,13680.09,12436.45,'03% GST',4514.43,154995.47,'Sold','Purchase','Display Floor1','','',0,1,0.00,'Bridal ','','No','2026-04-17 21:33:52','','','',0.00,'Yes',NULL,10.000,0.000,'Yes',0.00,0.00,10.000,'MC %',0.00,0.00,'Gross Weight',0.00,0.000,10.000,5,0.000,'0','PAVANI','INV001',NULL,NULL,NULL,NULL,'0',0.00,0.00,12000.00,'95','0','95'),(95,146,158,'SILVER PATTI','By Weight','ST','SILVER JEWELLERY','92','SILVER','ST001',10.000,0.000,0.00,10.000,'','Gross Weight',10.00,1.000,10.00,'MC / Gram',11.000,110.00,110.40,'03% GST',39.73,1364.13,'Available','Purchase','Display Floor1','','',0,1,0.00,'Bridal ','','No','2026-04-17 21:36:23','','','',0.00,'Yes',NULL,10.000,0.000,'Yes',0.00,0.00,10.000,'MC / Gram',0.00,0.00,'Gross Weight',0.00,0.000,10.000,6,0.000,'0','SAIKRUSHNA CHARY KADARLA','INV003',NULL,NULL,NULL,NULL,'0',0.00,0.00,120.00,'95','0','92'),(96,146,158,'SILVER PATTI','By Weight','ST','SILVER JEWELLERY','92','SILVER','ST002',10.000,0.000,0.00,10.000,'','Gross Weight',10.00,1.000,10.00,'MC / Gram',11.000,110.00,110.40,'03% GST',39.73,1364.13,'Sold','Purchase','Display Floor1','','',0,1,0.00,'Bridal ','','No','2026-04-18 10:51:25','','','',0.00,'Yes',NULL,10.000,0.000,'Yes',0.00,0.00,10.000,'MC / Gram',0.00,0.00,'Gross Weight',0.00,0.000,10.000,6,0.000,'0','SAIKRUSHNA CHARY KADARLA','INV003',NULL,NULL,NULL,NULL,'0',0.00,0.00,120.00,'95','0','92'),(97,146,158,'SILVER PATTI','By Weight','ST','SILVER JEWELLERY','92','SILVER','ST003',10.000,1.000,0.00,9.000,'','Gross Weight',10.00,1.000,10.00,'MC / Gram',10.000,100.00,110.40,'03% GST',36.12,1240.12,'Sold','Purchase','Display Floor1','','',0,1,0.00,'Bridal ','','No','2026-04-18 10:56:07','','','',0.00,'Yes',NULL,10.000,0.000,'Yes',0.00,0.00,10.000,'MC / Gram',0.00,0.00,'Gross Weight',0.00,0.000,10.000,6,0.000,'0','SAIKRUSHNA CHARY KADARLA','INV003',NULL,NULL,NULL,NULL,'0',0.00,0.00,120.00,'95','0','92'),(98,146,158,'SILVER PATTI','By Weight','ST','SILVER JEWELLERY','92','SILVER','ST004',10.000,1.000,1000.00,9.000,'','Gross Weight',10.00,1.000,50.00,'MC / Gram',10.000,500.00,110.40,'03% GST',78.12,2682.12,'Sold','Purchase','Display Floor1','','',0,1,0.00,'Bridal ','','No','2026-04-18 10:59:01','','','',0.00,'Yes',NULL,10.000,0.000,'Yes',0.00,0.00,10.000,'MC / Gram',0.00,0.00,'Gross Weight',0.00,0.000,10.000,6,0.000,'0','SAIKRUSHNA CHARY KADARLA','INV003',NULL,NULL,NULL,NULL,'0',0.00,0.00,120.00,'95','0','92'),(99,146,158,'SILVER PATTI','By Weight','ST','SILVER JEWELLERY','92','SILVER','ST005',10.000,1.000,0.00,9.000,'','Gross Weight',10.00,1.000,40.00,'MC / Gram',10.000,400.00,110.40,'03% GST',45.12,1549.12,'Sold','Purchase','Display Floor1','','',0,1,0.00,'Bridal ','','No','2026-04-18 11:01:15','','','',0.00,'Yes',NULL,10.000,0.000,'Yes',0.00,0.00,10.000,'MC / Gram',0.00,0.00,'Gross Weight',0.00,0.000,10.000,6,0.000,'0','SAIKRUSHNA CHARY KADARLA','INV003',NULL,NULL,NULL,NULL,'0',0.00,0.00,120.00,'95','0','92'),(100,145,157,'GOLD BRACELETS','By Weight','GBR','GOLD JEWELLERY','95','GOLD','GBR002',10.000,0.000,0.00,10.000,'','Gross Weight',10.00,1.000,0.00,'MC %',11.000,0.00,12436.45,'03% GST',4104.03,140904.98,'Available','Purchase','Display Floor1','','',0,1,0.00,'Bridal ','','No','2026-04-18 13:55:40','','','',0.00,'Yes',NULL,10.000,0.000,'Yes',0.00,0.00,10.000,'MC %',0.00,0.00,'Gross Weight',0.00,0.000,10.000,5,0.000,'0','PAVANI','INV001',NULL,NULL,NULL,NULL,'0',0.00,0.00,12000.00,'95','0','95'),(101,145,157,'GOLD BRACELETS','By Weight','GBR','GOLD JEWELLERY','95','GOLD','GBR003',10.000,1.000,0.00,9.000,'','Gross Weight',10.00,1.000,10.00,'MC %',10.000,12436.45,12436.45,'03% GST',4104.03,140904.98,'Sold','Purchase','Display Floor1','','',0,1,0.00,'Bridal ','','No','2026-04-18 14:38:40','','','',0.00,'Yes',NULL,10.000,0.000,'Yes',0.00,0.00,10.000,'MC %',0.00,0.00,'Gross Weight',0.00,0.000,10.000,5,0.000,'0','PAVANI','INV001',NULL,NULL,NULL,NULL,'0',0.00,0.00,12000.00,'95','0','95'),(102,146,158,'SILVER PATTI','By Weight','ST','SILVER JEWELLERY','92','SILVER','ST006',10.000,0.000,0.00,10.000,'','Gross Weight',10.00,1.000,10.00,'MC / Gram',11.000,110.00,110.40,'03% GST',39.73,1364.13,'Sold','Purchase','Display Floor1','','',0,1,0.00,'Bridal ','','No','2026-04-20 10:39:36','','','',0.00,'Yes',NULL,10.000,0.000,'Yes',0.00,0.00,10.000,'MC / Gram',0.00,0.00,'Gross Weight',0.00,0.000,10.000,6,0.000,'0','SAIKRUSHNA CHARY KADARLA','INV003',NULL,NULL,NULL,NULL,'0',0.00,0.00,120.00,'95','0','92'),(103,146,158,'SILVER PATTI','By Weight','ST','SILVER JEWELLERY','92','SILVER','ST007',10.000,0.000,0.00,10.000,'','Gross Weight',10.00,1.000,10.00,'MC / Gram',11.000,110.00,110.40,'03% GST',39.73,1364.13,'Sold','Purchase','Display Floor1','','',0,1,0.00,'Bridal ','','No','2026-04-20 10:45:40','','','',0.00,'Yes',NULL,10.000,0.000,'Yes',0.00,0.00,10.000,'MC / Gram',0.00,0.00,'Gross Weight',0.00,0.000,10.000,6,0.000,'0','SAIKRUSHNA CHARY KADARLA','INV003',NULL,NULL,NULL,NULL,'0',0.00,0.00,120.00,'95','0','92'),(104,146,158,'SILVER PATTI','By Weight','ST','SILVER JEWELLERY','92','SILVER','ST008',10.000,0.000,0.00,10.000,'','Gross Weight',10.00,1.000,10.00,'MC / Gram',11.000,110.00,110.40,'03% GST',39.73,1364.13,'Available','Purchase','Display Floor1','','',0,1,0.00,'Bridal ','','No','2026-04-20 10:49:14','','','',0.00,'Yes',NULL,10.000,0.000,'Yes',0.00,0.00,10.000,'MC / Gram',0.00,0.00,'Gross Weight',0.00,0.000,10.000,6,0.000,'0','SAIKRUSHNA CHARY KADARLA','INV003',NULL,NULL,NULL,NULL,'0',0.00,0.00,120.00,'95','0','92');
/*!40000 ALTER TABLE `opening_tags_entry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `transaction_type` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `date` date NOT NULL,
  `mode` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `cheque_number` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `receipt_no` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `account_name` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `invoice_number` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `total_amt` decimal(10,2) DEFAULT NULL,
  `discount_amt` decimal(10,2) DEFAULT '0.00',
  `cash_amt` decimal(10,2) DEFAULT '0.00',
  `remarks` text COLLATE utf8mb4_general_ci,
  `total_wt` decimal(10,3) DEFAULT '0.000',
  `paid_wt` decimal(10,3) DEFAULT '0.000',
  `bal_wt` decimal(10,3) DEFAULT '0.000',
  `rate` decimal(10,2) DEFAULT NULL,
  `category` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `mobile` varchar(15) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `source` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `invoice_splitted` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `split_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `product_id` int NOT NULL AUTO_INCREMENT,
  `product_name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `rbarcode` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `metal_type_id` int DEFAULT NULL,
  `Category` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `design_id` int DEFAULT NULL,
  `design_master` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `purity_id` int DEFAULT NULL,
  `purity` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `item_prefix` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `short_name` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `sale_account_head` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `purchase_account_head` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `status` enum('ACTIVE','INACTIVE') COLLATE utf8mb4_general_ci DEFAULT 'ACTIVE',
  `tax_slab` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `tax_slab_id` int DEFAULT NULL,
  `hsn_code` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `maintain_tags` tinyint(1) DEFAULT '0',
  `op_qty` decimal(10,2) DEFAULT NULL,
  `op_value` decimal(10,2) DEFAULT NULL,
  `op_weight` decimal(10,2) DEFAULT NULL,
  `huid_no` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `pur_qty` int DEFAULT NULL,
  `pur_weight` decimal(10,3) DEFAULT NULL,
  `avl_qty` int DEFAULT NULL,
  `avl_weight` decimal(10,3) DEFAULT NULL,
  `sale_qty` int DEFAULT NULL,
  `sale_weight` decimal(10,3) DEFAULT NULL,
  `bal_qty` int DEFAULT NULL,
  `bal_weight` decimal(10,3) DEFAULT NULL,
  `salereturn_qty` int DEFAULT NULL,
  `salereturn_weight` decimal(10,3) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=149 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (145,'GOLD JEWELLERY','RB001',2,'GOLD',NULL,'',NULL,'24K','','','Sales','Purchase','ACTIVE','03% GST',NULL,'HSN001',0,0.00,0.00,0.00,'',310,3100.000,NULL,NULL,44,720.000,266,2380.000,1,10.000),(146,'SILVER JEWELLERY','RB002',3,'SILVER',NULL,'',NULL,'24K','','','Sales','Purchase','ACTIVE','03% GST',NULL,'HSN002',0,0.00,0.00,0.00,'',20,200.000,NULL,NULL,13,185.000,7,15.000,NULL,NULL),(147,'SILVER ARTICLES','RB003',3,'SILVER',NULL,'',NULL,'24K','','','Sales','Purchase','ACTIVE','03% GST',NULL,'HSN003',0,0.00,0.00,0.00,'',NULL,NULL,NULL,NULL,1,10.000,NULL,NULL,NULL,NULL),(148,'DIAMOND JEWELLERY','RB004',4,'DIAMOND',NULL,'',NULL,'24K','','','Sales','Purchase','ACTIVE','03% GST',NULL,'HSN004',0,0.00,0.00,0.00,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productstockentry_stone_details`
--

DROP TABLE IF EXISTS `productstockentry_stone_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productstockentry_stone_details` (
  `id` int NOT NULL AUTO_INCREMENT,
  `subproductname` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `weight` decimal(10,2) NOT NULL,
  `ratepergram` decimal(10,2) NOT NULL,
  `amount` int NOT NULL,
  `totalweight` decimal(10,2) NOT NULL,
  `totalprice` decimal(10,2) NOT NULL,
  `c_weight` decimal(10,3) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productstockentry_stone_details`
--

LOCK TABLES `productstockentry_stone_details` WRITE;
/*!40000 ALTER TABLE `productstockentry_stone_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `productstockentry_stone_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchasepayments`
--

DROP TABLE IF EXISTS `purchasepayments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchasepayments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `mode` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `cheque_number` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `payment_no` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `account_name` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `invoice` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `category` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `rate_cut` decimal(10,2) DEFAULT NULL,
  `total_wt` decimal(10,3) DEFAULT NULL,
  `paid_wt` decimal(10,3) DEFAULT NULL,
  `bal_wt` decimal(10,3) DEFAULT NULL,
  `total_amt` decimal(12,2) DEFAULT NULL,
  `paid_amt` decimal(12,2) DEFAULT NULL,
  `bal_amt` decimal(12,2) DEFAULT NULL,
  `paid_by` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `remarks` text COLLATE utf8mb4_general_ci,
  `rate_cut_id` int DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchasepayments`
--

LOCK TABLES `purchasepayments` WRITE;
/*!40000 ALTER TABLE `purchasepayments` DISABLE KEYS */;
/*!40000 ALTER TABLE `purchasepayments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchases`
--

DROP TABLE IF EXISTS `purchases`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchases` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int DEFAULT NULL,
  `mobile` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `account_name` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `gst_in` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `terms` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `invoice` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `bill_no` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `date` date DEFAULT NULL,
  `bill_date` date DEFAULT NULL,
  `due_date` date DEFAULT NULL,
  `Pricing` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `product_id` int DEFAULT NULL,
  `category` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `metal_type` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `rbarcode` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `hsn_code` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `pcs` int DEFAULT NULL,
  `gross_weight` decimal(10,3) DEFAULT '0.000',
  `stone_weight` decimal(10,3) DEFAULT '0.000',
  `deduct_st_Wt` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `net_weight` decimal(10,3) DEFAULT '0.000',
  `purity` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `purityPercentage` varchar(25) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `pure_weight` decimal(10,3) DEFAULT NULL,
  `wastage_on` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `wastage` decimal(10,2) DEFAULT NULL,
  `wastage_wt` decimal(10,3) DEFAULT '0.000',
  `Making_Charges_On` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Making_Charges_Value` decimal(10,2) DEFAULT NULL,
  `total_mc` decimal(10,2) DEFAULT '0.00',
  `total_pure_wt` decimal(10,3) DEFAULT '0.000',
  `paid_pure_weight` decimal(10,3) DEFAULT NULL,
  `balance_pure_weight` decimal(10,3) DEFAULT NULL,
  `rate` decimal(10,2) DEFAULT NULL,
  `total_amount` decimal(10,2) DEFAULT NULL,
  `tax_slab` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tax_amt` decimal(10,2) DEFAULT NULL,
  `net_amt` decimal(10,2) DEFAULT NULL,
  `rate_cut` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `rate_cut_wt` decimal(10,3) DEFAULT NULL,
  `rate_cut_amt` decimal(10,2) DEFAULT NULL,
  `paid_amount` decimal(10,2) DEFAULT NULL,
  `balance_amount` decimal(10,2) DEFAULT NULL,
  `hm_charges` decimal(10,2) DEFAULT NULL,
  `charges` decimal(10,2) DEFAULT NULL,
  `remarks` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `cut` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `color` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `clarity` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `carat_wt` decimal(10,3) DEFAULT NULL,
  `stone_price` decimal(10,2) DEFAULT NULL,
  `final_stone_amount` decimal(10,2) DEFAULT NULL,
  `paid_amt` decimal(10,2) DEFAULT NULL,
  `balance_after_receipt` decimal(10,2) DEFAULT NULL,
  `paid_wt` decimal(10,3) DEFAULT NULL,
  `balWt_after_payment` decimal(10,3) DEFAULT NULL,
  `paid_by` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `bal_wt_amt` decimal(10,3) DEFAULT NULL,
  `other_charges` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `overall_total_wt` decimal(10,3) DEFAULT '0.000',
  `overall_paid_wt` decimal(10,3) DEFAULT '0.000',
  `overall_bal_wt` decimal(10,3) DEFAULT '0.000',
  `overall_taxableAmt` decimal(10,2) NOT NULL DEFAULT '0.00',
  `overall_taxAmt` decimal(10,2) NOT NULL DEFAULT '0.00',
  `overall_netAmt` decimal(10,2) NOT NULL DEFAULT '0.00',
  `overall_hmCharges` decimal(10,2) NOT NULL DEFAULT '0.00',
  `bal_tag_pcs` int DEFAULT NULL,
  `bal_tag_grossWeight` decimal(10,3) DEFAULT NULL,
  `tag_id` int DEFAULT NULL,
  `discount_amt` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `final_amt` decimal(10,2) DEFAULT NULL,
  `claim_remark` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=113 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchases`
--

LOCK TABLES `purchases` WRITE;
/*!40000 ALTER TABLE `purchases` DISABLE KEYS */;
INSERT INTO `purchases` VALUES (111,53,'0938185025','PAVANI',NULL,'Cash','INV001',NULL,'2026-04-07','2026-04-07',NULL,'By Weight',145,'GOLD JEWELLERY','GOLD','RB001','HSN001',100,1000.000,0.000,'No',1000.000,'Manual','100',1000.000,'Pure Wt',10.00,100.000,'MC %',10.00,1320000.00,1100.000,0.000,1100.000,12000.00,13200000.00,'03% GST',435600.00,14955600.00,'12000.00',0.000,0.00,0.00,0.00,0.00,0.00,'0','0','0','0',0.000,0.00,0.00,NULL,0.00,NULL,0.000,'By Weight',1100.000,'0',0.000,0.000,0.000,14520000.00,435600.00,14955600.00,0.00,NULL,NULL,5,'0',14955600.00,NULL),(112,52,'0938185028','SAIKRUSHNA CHARY KADARLA',NULL,'Cash','INV003',NULL,'2026-04-17','2026-04-17',NULL,'By Weight',146,'SILVER JEWELLERY','SILVER','RB002','HSN002',20,200.000,0.000,'No',200.000,'Manual','100',200.000,'Pure Wt',10.00,20.000,'MC / Gram',10.00,2200.00,220.000,100.000,120.000,120.00,26400.00,'03% GST',858.00,29458.00,'0',0.000,0.00,0.00,0.00,0.00,0.00,'0','0','0','0',0.000,0.00,0.00,NULL,0.00,NULL,0.000,'By Weight',120.000,'0',0.000,0.000,0.000,28600.00,858.00,29458.00,0.00,NULL,NULL,6,'0',29458.00,NULL);
/*!40000 ALTER TABLE `purchases` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purity`
--

DROP TABLE IF EXISTS `purity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purity` (
  `purity_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `metal` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `purity_percentage` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `purity` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `urd_purity` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `old_purity_desc` text COLLATE utf8mb4_unicode_ci,
  `cut_issue` text COLLATE utf8mb4_unicode_ci,
  `skin_print` text COLLATE utf8mb4_unicode_ci,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`purity_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purity`
--

LOCK TABLES `purity` WRITE;
/*!40000 ALTER TABLE `purity` DISABLE KEYS */;
INSERT INTO `purity` VALUES (3,'22 KT','GOLD','91.6 %','91.6HM',NULL,NULL,NULL,NULL,'2025-10-09 04:26:52','2025-10-09 04:29:32'),(4,'24 KT','GOLD','99.9 %','99.9 %',NULL,NULL,NULL,NULL,'2025-10-09 04:27:23','2025-10-09 04:29:48'),(5,'18 KT','GOLD','76 %','76 %',NULL,NULL,NULL,NULL,'2025-10-09 04:27:52','2025-10-09 04:29:56'),(6,'14 KT','GOLD','60 %','60 %',NULL,NULL,NULL,NULL,'2025-10-09 04:28:20','2025-10-09 04:30:03'),(7,'22 KT','SILVER',NULL,'91.6HM',NULL,NULL,NULL,NULL,'2025-10-09 04:30:23','2025-10-09 04:30:23'),(8,'80 HM','SILVER',NULL,'80HM',NULL,NULL,NULL,NULL,'2025-10-09 04:30:49','2025-10-09 04:30:49');
/*!40000 ALTER TABLE `purity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ratecuts`
--

DROP TABLE IF EXISTS `ratecuts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ratecuts` (
  `rate_cut_id` int NOT NULL AUTO_INCREMENT,
  `purchase_id` int DEFAULT NULL,
  `invoice` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `category` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `total_pure_wt` decimal(10,3) DEFAULT NULL,
  `rate_cut_wt` decimal(10,3) DEFAULT NULL,
  `rate_cut` decimal(10,2) DEFAULT NULL,
  `rate_cut_amt` decimal(10,2) DEFAULT NULL,
  `paid_amount` decimal(10,2) DEFAULT NULL,
  `balance_amount` decimal(10,2) DEFAULT NULL,
  `paid_wt` decimal(10,3) DEFAULT NULL,
  `bal_wt` decimal(10,3) DEFAULT NULL,
  `paid_by` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`rate_cut_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ratecuts`
--

LOCK TABLES `ratecuts` WRITE;
/*!40000 ALTER TABLE `ratecuts` DISABLE KEYS */;
INSERT INTO `ratecuts` VALUES (1,110,'INV003','GOLD JEWELLERY',1000.000,100.000,12000.00,1200000.00,700000.00,500000.00,58.334,41.666,NULL,'2026-04-07 06:57:50');
/*!40000 ALTER TABLE `ratecuts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rates`
--

DROP TABLE IF EXISTS `rates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rates` (
  `rates_id` int NOT NULL AUTO_INCREMENT,
  `rate_date` date NOT NULL,
  `rate_time` time NOT NULL,
  `rate_9crt` int DEFAULT NULL,
  `rate_16crt` decimal(10,2) DEFAULT NULL,
  `rate_18crt` decimal(10,2) DEFAULT NULL,
  `rate_22crt` decimal(10,2) DEFAULT NULL,
  `rate_24crt` decimal(10,2) DEFAULT NULL,
  `silver_rate` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`rates_id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rates`
--

LOCK TABLES `rates` WRITE;
/*!40000 ALTER TABLE `rates` DISABLE KEYS */;
INSERT INTO `rates` VALUES (44,'2025-12-12','18:39:01',NULL,7855.00,9949.00,12000.00,13091.00,120.00),(45,'2026-05-12','16:12:42',NULL,7855.00,9949.00,12000.00,13091.00,120.00),(46,'2026-05-12','16:20:56',NULL,7855.00,9949.00,12000.00,13091.00,120.00),(47,'2026-05-12','16:20:59',NULL,7855.00,9949.00,12000.00,13091.00,120.00),(48,'2026-05-12','16:23:01',NULL,7855.00,9949.00,12000.00,13091.00,120.00),(49,'2026-05-12','16:23:15',NULL,7855.00,9949.00,12000.00,13091.00,120.00),(50,'2026-05-12','16:26:32',NULL,7855.00,9949.00,12000.00,13091.00,120.00),(51,'2026-05-12','16:28:08',NULL,7855.00,9949.00,12000.00,13091.00,120.00),(52,'2026-05-12','16:29:43',NULL,7855.00,9949.00,12000.00,13091.00,120.00),(53,'2026-05-12','16:30:09',NULL,7855.00,9949.00,12000.00,13091.00,120.00),(54,'2026-05-12','16:40:25',4909,7855.00,9949.00,12000.00,13091.00,120.00);
/*!40000 ALTER TABLE `rates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `receipts`
--

DROP TABLE IF EXISTS `receipts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `receipts` (
  `receipt_id` int NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `mode` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `cheque_number` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `receipt_no` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `account_name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `total_amt` decimal(10,2) NOT NULL,
  `discount_amt` decimal(10,2) DEFAULT NULL,
  `cash_amt` decimal(10,2) DEFAULT NULL,
  `remarks` text COLLATE utf8mb4_general_ci,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`receipt_id`),
  UNIQUE KEY `receipt_no` (`receipt_no`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `receipts`
--

LOCK TABLES `receipts` WRITE;
/*!40000 ALTER TABLE `receipts` DISABLE KEYS */;
/*!40000 ALTER TABLE `receipts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `repair_details`
--

DROP TABLE IF EXISTS `repair_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `repair_details` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int DEFAULT NULL,
  `mobile` varchar(15) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `account_name` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `email` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `address1` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `address2` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `city` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `pincode` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `state` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `state_code` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `aadhar_card` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `gst_in` varchar(30) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `pan_card` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `terms` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `date` date DEFAULT NULL,
  `invoice_number` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `code` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `product_id` int DEFAULT NULL,
  `opentag_id` int DEFAULT NULL,
  `metal` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `product_name` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `metal_type` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `design_name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `purity` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `selling_purity` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `printing_purity` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `custom_purity` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `pricing` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `category` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `sub_category` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `gross_weight` decimal(10,3) DEFAULT NULL,
  `stone_weight` decimal(10,3) DEFAULT NULL,
  `weight_bw` decimal(10,3) DEFAULT NULL,
  `stone_price` decimal(10,2) DEFAULT NULL,
  `va_on` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `va_percent` decimal(10,2) DEFAULT NULL,
  `wastage_weight` decimal(10,3) DEFAULT NULL,
  `total_weight_av` decimal(10,3) DEFAULT NULL,
  `mc_on` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `mc_per_gram` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `making_charges` decimal(10,2) DEFAULT NULL,
  `disscount_percentage` decimal(10,2) DEFAULT NULL,
  `disscount` decimal(10,2) DEFAULT NULL,
  `rate` decimal(10,2) DEFAULT NULL,
  `rate_24k` decimal(10,2) DEFAULT NULL,
  `rate_amt` decimal(10,2) DEFAULT NULL,
  `tax_percent` decimal(5,2) DEFAULT NULL,
  `tax_amt` decimal(10,2) DEFAULT NULL,
  `total_price` decimal(10,2) DEFAULT NULL,
  `cash_amount` decimal(10,2) DEFAULT NULL,
  `card_amount` decimal(10,2) DEFAULT NULL,
  `card_amt` decimal(10,2) DEFAULT NULL,
  `chq` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `chq_amt` decimal(10,2) DEFAULT NULL,
  `online` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `online_amt` decimal(10,2) DEFAULT NULL,
  `transaction_status` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `qty` int DEFAULT NULL,
  `taxable_amount` decimal(10,2) DEFAULT NULL,
  `tax_amount` decimal(10,2) DEFAULT NULL,
  `net_amount` decimal(10,2) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `product_image` longtext COLLATE utf8mb4_general_ci,
  `imagePreview` longtext COLLATE utf8mb4_general_ci,
  `assigning` varchar(50) COLLATE utf8mb4_general_ci DEFAULT 'pending',
  `worker_name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `account_id` int DEFAULT NULL,
  `status` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `net_bill_amount` decimal(10,2) DEFAULT NULL,
  `paid_amt` decimal(10,2) DEFAULT NULL,
  `old_exchange_amt` decimal(10,2) DEFAULT NULL,
  `scheme_amt` decimal(10,2) DEFAULT NULL,
  `sale_return_amt` decimal(10,2) DEFAULT NULL,
  `advance_receipt_amt` decimal(15,2) DEFAULT NULL,
  `receipts_amt` decimal(10,2) DEFAULT NULL,
  `bal_after_receipts` decimal(10,2) DEFAULT NULL,
  `bal_amt` decimal(10,2) DEFAULT NULL,
  `order_status` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `order_number` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `invoice` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `delivery_date` date DEFAULT NULL,
  `original_total_price` decimal(10,2) DEFAULT NULL,
  `pieace_cost` decimal(10,2) DEFAULT NULL,
  `mrp_price` decimal(10,2) DEFAULT NULL,
  `hm_charges` decimal(10,2) DEFAULT NULL,
  `remarks` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `sale_status` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `original_piece_taxable_amt` decimal(10,2) DEFAULT NULL,
  `piece_taxable_amt` decimal(10,2) DEFAULT NULL,
  `festival_discount` decimal(10,2) DEFAULT NULL,
  `time` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `advance_amt` decimal(10,2) DEFAULT NULL,
  `customerImage` varchar(450) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `size` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2570 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `repair_details`
--

LOCK TABLES `repair_details` WRITE;
/*!40000 ALTER TABLE `repair_details` DISABLE KEYS */;
INSERT INTO `repair_details` VALUES (2546,52,'0938185028','SAIKRUSHNA CHARY KADARLA','kadarlasaikrushna99@gmail.com','SH11, Sircilla, Sircilla mandal, Rajanna Sircilla, Telangana, 505301, India','Sircilla','Sircilla','505301',NULL,NULL,NULL,NULL,NULL,'Cash','2026-04-30','INV001','RB001',145,NULL,NULL,'GOLD BRACELETS','GOLD','Bridal ','95','95','95',NULL,'By Weight','GOLD JEWELLERY',NULL,20.000,2.000,18.000,2000.00,'Gross Weight',10.00,2.000,20.000,'MC %','10',24872.90,NULL,NULL,12436.45,13091.00,248729.00,3.00,8068.31,268943.67,277012.00,NULL,NULL,NULL,NULL,NULL,NULL,'Sales',1,268943.67,8068.31,277011.98,'2026-04-30 07:26:43',NULL,NULL,'pending',NULL,NULL,NULL,277012.00,277012.00,0.00,0.00,0.00,0.00,NULL,NULL,0.00,NULL,NULL,NULL,NULL,60.00,NULL,NULL,60.00,NULL,'Delivered',0.00,0.00,6718.23,'12:56 PM',NULL,NULL,NULL),(2547,52,'0938185028','SAIKRUSHNA CHARY KADARLA','kadarlasaikrushna99@gmail.com','SH11, Sircilla, Sircilla mandal, Rajanna Sircilla, Telangana, 505301, India','Sircilla','Sircilla','505301',NULL,NULL,NULL,NULL,NULL,'Cash','2026-04-30','INV002','RB001',145,NULL,NULL,'GOLD BRACELETS','GOLD','Bridal ','95','95','95',NULL,'By Weight','GOLD JEWELLERY',NULL,20.000,2.000,18.000,2000.00,'Gross Weight',10.00,2.000,20.000,'MC %','10',24872.90,NULL,NULL,12436.45,13091.00,248729.00,3.00,8068.31,268943.67,277012.00,NULL,NULL,NULL,NULL,NULL,NULL,'Sales',1,268943.67,8068.31,277011.98,'2026-04-30 07:40:27',NULL,NULL,'pending',NULL,NULL,NULL,277012.00,277012.00,0.00,0.00,0.00,0.00,NULL,NULL,0.00,NULL,NULL,NULL,NULL,60.00,NULL,NULL,60.00,NULL,'Delivered',0.00,0.00,6718.23,'01:10 PM',NULL,NULL,NULL),(2548,52,'0938185028','SAIKRUSHNA CHARY KADARLA','kadarlasaikrushna99@gmail.com','SH11, Sircilla, Sircilla mandal, Rajanna Sircilla, Telangana, 505301, India','Sircilla','Sircilla','505301',NULL,NULL,NULL,NULL,NULL,'Cash','2026-04-30','INV003','RB001',145,NULL,NULL,'GOLD BRACELETS','GOLD','Bridal ','95','95','95',NULL,'By Weight','GOLD JEWELLERY',NULL,20.000,2.000,18.000,2000.00,'Gross Weight',10.00,2.000,20.000,'MC %','10',24872.90,NULL,NULL,12436.45,13091.00,248729.00,3.00,8068.31,268943.67,277012.00,NULL,NULL,NULL,NULL,NULL,NULL,'Sales',1,268943.67,8068.31,277011.98,'2026-04-30 07:54:33',NULL,NULL,'pending',NULL,NULL,NULL,277012.00,277012.00,0.00,0.00,0.00,0.00,NULL,NULL,0.00,NULL,NULL,NULL,NULL,60.00,NULL,NULL,60.00,NULL,'Delivered',0.00,0.00,6718.23,'01:24 PM',NULL,NULL,NULL),(2549,52,'0938185028','SAIKRUSHNA CHARY KADARLA','kadarlasaikrushna99@gmail.com','SH11, Sircilla, Sircilla mandal, Rajanna Sircilla, Telangana, 505301, India','Sircilla','Sircilla','505301',NULL,NULL,NULL,NULL,NULL,'Cash','2026-04-30','INV004','RB001',145,NULL,NULL,'GOLD CHAIN','GOLD','Bridal ','95','95','96',NULL,'By Weight','GOLD JEWELLERY',NULL,10.000,1.000,9.000,1000.00,'Gross Weight',10.00,1.000,10.000,'MC %','10',12436.45,16.08,2000.00,12436.45,13091.00,124364.50,3.00,3975.06,136476.90,136477.00,NULL,NULL,NULL,NULL,NULL,NULL,'Sales',1,132501.84,3975.06,136476.90,'2026-04-30 08:03:21',NULL,NULL,'pending',NULL,NULL,NULL,136477.00,136477.00,0.00,0.00,0.00,0.00,NULL,NULL,0.00,NULL,NULL,NULL,NULL,60.00,NULL,NULL,60.00,NULL,'Delivered',0.00,0.00,3359.11,'01:33 PM',NULL,NULL,NULL),(2550,52,'0938185028','SAIKRUSHNA CHARY KADARLA','kadarlasaikrushna99@gmail.com','SH11, Sircilla, Sircilla mandal, Rajanna Sircilla, Telangana, 505301, India','Sircilla','Sircilla','505301',NULL,NULL,NULL,NULL,NULL,'Cash','2026-04-30','INV005','RB001',145,NULL,NULL,'GOLD CHAIN','GOLD','Bridal ','95','95','96',NULL,'By Weight','GOLD JEWELLERY',NULL,20.000,2.000,18.000,2000.00,'Gross Weight',10.00,2.000,20.000,'MC %','10',24872.90,NULL,NULL,12436.45,13091.00,248729.00,3.00,8068.31,268943.67,77012.00,NULL,NULL,NULL,NULL,NULL,NULL,'Sales',1,268943.67,8068.31,277011.98,'2026-04-30 08:08:33',NULL,NULL,'pending',NULL,NULL,NULL,277012.00,77012.00,0.00,0.00,0.00,0.00,NULL,NULL,200000.00,NULL,NULL,NULL,NULL,60.00,NULL,NULL,60.00,NULL,'Delivered',0.00,0.00,6718.23,'01:38 PM',NULL,NULL,NULL),(2551,52,'0938185028','SAIKRUSHNA CHARY KADARLA','kadarlasaikrushna99@gmail.com','SH11, Sircilla, Sircilla mandal, Rajanna Sircilla, Telangana, 505301, India','Sircilla','Sircilla','505301',NULL,NULL,NULL,NULL,NULL,'Cash','2026-04-30','INV006','RB001',145,NULL,NULL,'GOLD BRACELETS','GOLD','Bridal ','95','95','95',NULL,'By Weight','GOLD JEWELLERY',NULL,20.000,1.000,19.000,2000.00,'Gross Weight',10.00,2.000,21.000,'MC %','10',26116.54,NULL,NULL,12436.45,13091.00,261165.45,3.00,8469.39,282312.86,290782.00,NULL,NULL,NULL,NULL,NULL,NULL,'Sales',1,282312.85,8469.39,290782.24,'2026-04-30 08:15:07',NULL,NULL,'pending',NULL,NULL,NULL,290782.00,290782.00,0.00,0.00,0.00,0.00,NULL,NULL,0.00,NULL,NULL,NULL,NULL,60.00,NULL,NULL,60.00,NULL,'Delivered',0.00,0.00,7029.14,'01:45 PM',NULL,NULL,NULL),(2552,52,'0938185028','SAIKRUSHNA CHARY KADARLA','kadarlasaikrushna99@gmail.com','SH11, Sircilla, Sircilla mandal, Rajanna Sircilla, Telangana, 505301, India','Sircilla','Sircilla','505301',NULL,NULL,NULL,NULL,NULL,'Cash','2026-04-30','INV007','RB001',145,NULL,NULL,'GOLD BRACELETS','GOLD','Bridal ','95','95','95',NULL,'By Weight','GOLD JEWELLERY',NULL,10.000,1.000,9.000,1000.00,'Gross Weight',10.00,1.000,10.000,'MC %','10',12436.45,NULL,NULL,12436.45,13091.00,124364.50,3.00,4035.06,134501.84,138537.00,NULL,NULL,NULL,NULL,NULL,NULL,'Sales',1,134501.84,4035.06,138536.90,'2026-04-30 08:15:59',NULL,NULL,'pending',NULL,NULL,NULL,138537.00,138537.00,0.00,0.00,0.00,0.00,NULL,NULL,0.00,NULL,NULL,NULL,NULL,60.00,NULL,NULL,60.00,NULL,'Delivered',0.00,0.00,3359.11,'01:45 PM',NULL,NULL,NULL),(2553,52,'0938185028','SAIKRUSHNA CHARY KADARLA','kadarlasaikrushna99@gmail.com','SH11, Sircilla, Sircilla mandal, Rajanna Sircilla, Telangana, 505301, India','Sircilla','Sircilla','505301',NULL,NULL,NULL,NULL,NULL,'Cash','2026-04-30','INV008','RB001',145,NULL,NULL,'GOLD BRACELETS','GOLD','Bridal ','95','95','95',NULL,'By Weight','GOLD JEWELLERY',NULL,20.000,2.000,18.000,2000.00,'Gross Weight',10.00,2.000,20.000,'MC %','10',24872.90,NULL,NULL,12436.45,13091.00,248729.00,3.00,8068.31,268943.67,277012.00,NULL,NULL,NULL,NULL,NULL,NULL,'Sales',1,268943.67,8068.31,277011.98,'2026-04-30 08:22:41',NULL,NULL,'pending',NULL,NULL,NULL,277012.00,277012.00,0.00,0.00,0.00,0.00,NULL,NULL,0.00,NULL,NULL,NULL,NULL,60.00,NULL,NULL,60.00,NULL,'Delivered',0.00,0.00,6718.23,'01:52 PM',NULL,NULL,NULL),(2554,52,'0938185028','SAIKRUSHNA CHARY KADARLA','kadarlasaikrushna99@gmail.com','SH11, Sircilla, Sircilla mandal, Rajanna Sircilla, Telangana, 505301, India','Sircilla','Sircilla','505301',NULL,NULL,NULL,NULL,NULL,'Cash','2026-04-30','INV009','RB001',145,NULL,NULL,'GOLD CHAIN','GOLD','Bridal ','95','95','96',NULL,'By Weight','GOLD JEWELLERY',NULL,20.000,2.000,18.000,2000.00,'Gross Weight',10.00,2.000,20.000,'MC %','10',24872.90,NULL,NULL,12436.45,13091.00,248729.00,3.00,8068.31,268943.67,277012.00,NULL,NULL,NULL,NULL,NULL,NULL,'Sales',1,268943.67,8068.31,277011.98,'2026-04-30 08:24:28',NULL,NULL,'pending',NULL,NULL,NULL,277012.00,277012.00,0.00,0.00,0.00,0.00,NULL,NULL,0.00,NULL,NULL,NULL,NULL,60.00,NULL,NULL,60.00,NULL,'Delivered',0.00,0.00,6718.23,'01:54 PM',NULL,NULL,NULL),(2555,52,'0938185028','SAIKRUSHNA CHARY KADARLA','kadarlasaikrushna99@gmail.com','SH11, Sircilla, Sircilla mandal, Rajanna Sircilla, Telangana, 505301, India','Sircilla','Sircilla','505301',NULL,NULL,NULL,NULL,NULL,'Cash','2026-04-30','INV010','RB001',145,NULL,NULL,'GOLD BRACELETS','GOLD','Bridal ','95','95','95',NULL,'By Weight','GOLD JEWELLERY',NULL,20.000,2.000,18.000,2000.00,'Gross Weight',10.00,2.000,20.000,'MC %','10',24872.90,NULL,NULL,12436.45,13091.00,248729.00,3.00,8068.31,268943.67,277012.00,NULL,NULL,NULL,NULL,NULL,NULL,'Sales',1,268943.67,8068.31,277011.98,'2026-04-30 08:28:35',NULL,NULL,'pending',NULL,NULL,NULL,277012.00,277012.00,0.00,0.00,0.00,0.00,NULL,NULL,0.00,NULL,NULL,NULL,NULL,60.00,NULL,NULL,60.00,NULL,'Delivered',0.00,0.00,6718.23,'01:58 PM',NULL,NULL,NULL),(2556,52,'0938185028','SAIKRUSHNA CHARY KADARLA','kadarlasaikrushna99@gmail.com','SH11, Sircilla, Sircilla mandal, Rajanna Sircilla, Telangana, 505301, India','Sircilla','Sircilla','505301',NULL,NULL,NULL,NULL,NULL,'Cash','2026-05-04','INV011','RB001',145,NULL,NULL,'GOLD BRACELETS','GOLD','Bridal ','95','95','95',NULL,'By Weight','GOLD JEWELLERY',NULL,20.000,2.000,18.000,2000.00,'Gross Weight',10.00,2.000,20.000,'MC %','10',24872.90,NULL,NULL,12436.45,13091.00,248729.00,3.00,8269.86,275661.90,283932.00,NULL,NULL,NULL,NULL,NULL,NULL,'Sales',1,275661.90,8269.86,283931.76,'2026-05-04 06:01:56',NULL,NULL,'pending',NULL,NULL,NULL,283932.00,283932.00,0.00,0.00,0.00,0.00,NULL,NULL,0.00,NULL,NULL,NULL,NULL,NULL,NULL,NULL,60.00,NULL,'Delivered',0.00,0.00,NULL,'11:31 AM',NULL,NULL,NULL),(2557,52,'0938185028','SAIKRUSHNA CHARY KADARLA','kadarlasaikrushna99@gmail.com','SH11, Sircilla, Sircilla mandal, Rajanna Sircilla, Telangana, 505301, India','Sircilla','Sircilla','505301',NULL,NULL,NULL,NULL,NULL,'Cash','2026-05-04','INV012','RB001',145,NULL,NULL,'GOLD BRACELETS','GOLD','Wedding Ring','95','95','95',NULL,'By Weight','GOLD JEWELLERY',NULL,10.000,1.000,9.000,1000.00,'Gross Weight',10.00,1.000,10.000,'MC %','10',12436.45,NULL,NULL,12436.45,13091.00,124364.50,3.00,4135.83,137860.95,141997.00,NULL,NULL,NULL,NULL,NULL,NULL,'Sales',1,137860.95,4135.83,141996.78,'2026-05-04 06:05:33',NULL,NULL,'pending',NULL,NULL,NULL,141997.00,141997.00,0.00,0.00,0.00,0.00,NULL,NULL,0.00,NULL,NULL,NULL,NULL,NULL,NULL,NULL,60.00,NULL,'Delivered',0.00,0.00,NULL,'11:35 AM',NULL,NULL,NULL),(2558,52,'0938185028','SAIKRUSHNA CHARY KADARLA','kadarlasaikrushna99@gmail.com','SH11, Sircilla, Sircilla mandal, Rajanna Sircilla, Telangana, 505301, India','Sircilla','Sircilla','505301',NULL,NULL,NULL,NULL,NULL,'Cash','2026-05-12','INV013','RB002',146,NULL,NULL,'SILVER PATTI','SILVER','Bridal ','95','92','92',NULL,'By Weight','SILVER JEWELLERY',NULL,10.000,1.000,9.000,1000.00,'Gross Weight',10.00,1.000,10.000,'MC %','10',110.40,NULL,NULL,110.40,120.00,1104.00,3.00,68.23,2274.40,2343.00,NULL,NULL,NULL,NULL,NULL,NULL,'Sales',1,2274.40,68.23,2342.63,'2026-05-12 09:21:31',NULL,NULL,'pending',NULL,NULL,NULL,2343.00,2343.00,0.00,0.00,0.00,0.00,NULL,NULL,0.00,NULL,NULL,NULL,NULL,NULL,NULL,NULL,60.00,NULL,'Delivered',0.00,0.00,NULL,'02:51 PM',NULL,NULL,NULL),(2559,52,'0938185028','SAIKRUSHNA CHARY KADARLA','kadarlasaikrushna99@gmail.com','SH11, Sircilla, Sircilla mandal, Rajanna Sircilla, Telangana, 505301, India','Sircilla','Sircilla','505301',NULL,NULL,NULL,NULL,NULL,'Cash','2026-05-12','INV014','RB002',146,NULL,NULL,'SILVER PATTI','SILVER','Elegant Gold Ring','95','92','92',NULL,'By Weight','SILVER JEWELLERY',NULL,20.000,2.000,18.000,2000.00,'Gross Weight',10.00,2.000,20.000,'MC %','10',220.80,NULL,NULL,110.40,120.00,2208.00,3.00,134.66,4488.80,4623.00,NULL,NULL,NULL,NULL,NULL,NULL,'Sales',1,4488.80,134.66,4623.46,'2026-05-12 09:30:16',NULL,NULL,'pending',NULL,NULL,NULL,4623.00,4623.00,0.00,0.00,0.00,0.00,NULL,NULL,0.00,NULL,NULL,NULL,NULL,NULL,NULL,NULL,60.00,NULL,'Delivered',0.00,0.00,NULL,'03:00 PM',NULL,NULL,NULL),(2560,52,'0938185028','SAIKRUSHNA CHARY KADARLA','kadarlasaikrushna99@gmail.com','SH11, Sircilla, Sircilla mandal, Rajanna Sircilla, Telangana, 505301, India','Sircilla','Sircilla','505301',NULL,NULL,NULL,NULL,NULL,'Cash','2026-05-12','INV015','RB001',145,NULL,NULL,'GOLD BRACELETS','GOLD','Bridal ','95','95','95',NULL,'By Weight','GOLD JEWELLERY',NULL,20.000,2.000,18.000,2000.00,'Gross Weight',10.00,2.000,20.000,'MC %','10',24872.90,NULL,NULL,12436.45,13091.00,248729.00,3.00,8269.86,275661.90,283932.00,NULL,NULL,NULL,NULL,NULL,NULL,'Sales',1,275661.90,8269.86,283931.76,'2026-05-12 09:30:55',NULL,NULL,'pending',NULL,NULL,NULL,283932.00,283932.00,0.00,0.00,0.00,0.00,NULL,NULL,0.00,NULL,NULL,NULL,NULL,NULL,NULL,NULL,60.00,NULL,'Delivered',0.00,0.00,NULL,'03:00 PM',NULL,NULL,NULL),(2561,52,'0938185028','SAIKRUSHNA CHARY KADARLA','kadarlasaikrushna99@gmail.com','SH11, Sircilla, Sircilla mandal, Rajanna Sircilla, Telangana, 505301, India','Sircilla','Sircilla','505301',NULL,NULL,NULL,NULL,NULL,'Cash','2026-05-12','INV016','RB002',146,NULL,NULL,'SILVER PATTI','SILVER','Bridal ','95','92','92',NULL,'By Weight','SILVER JEWELLERY',NULL,20.000,2.000,18.000,2000.00,'Gross Weight',10.00,2.000,20.000,'MC / Gram','10',200.00,NULL,NULL,110.40,120.00,2208.00,3.00,134.04,4468.00,6934.00,NULL,NULL,NULL,NULL,NULL,NULL,'Sales',1,6732.00,201.96,6933.96,'2026-05-12 10:21:47',NULL,NULL,'pending',NULL,NULL,NULL,6934.00,6934.00,0.00,0.00,0.00,0.00,NULL,NULL,0.00,NULL,NULL,NULL,NULL,NULL,NULL,NULL,60.00,NULL,'Delivered',0.00,0.00,NULL,'03:51 PM',NULL,NULL,NULL),(2562,52,'0938185028','SAIKRUSHNA CHARY KADARLA','kadarlasaikrushna99@gmail.com','SH11, Sircilla, Sircilla mandal, Rajanna Sircilla, Telangana, 505301, India','Sircilla','Sircilla','505301',NULL,NULL,NULL,NULL,NULL,'Cash','2026-05-12','INV016','RB003',147,NULL,NULL,'SILVER DEEPA','SILVER','Bridal ','92','92','92',NULL,'By Weight','SILVER ARTICLES',NULL,10.000,1.000,9.000,1000.00,'Gross Weight',10.00,1.000,10.000,'MC / Gram','10',100.00,NULL,NULL,110.40,120.00,1104.00,3.00,67.92,2264.00,6934.00,NULL,NULL,NULL,NULL,NULL,NULL,'Sales',1,6732.00,201.96,6933.96,'2026-05-12 10:21:47',NULL,NULL,'pending',NULL,NULL,NULL,6934.00,6934.00,0.00,0.00,0.00,0.00,NULL,NULL,0.00,NULL,NULL,NULL,NULL,NULL,NULL,NULL,60.00,NULL,'Delivered',0.00,0.00,NULL,'03:51 PM',NULL,NULL,NULL),(2563,52,'0938185028','SAIKRUSHNA CHARY KADARLA','kadarlasaikrushna99@gmail.com','SH11, Sircilla, Sircilla mandal, Rajanna Sircilla, Telangana, 505301, India','Sircilla','Sircilla','505301',NULL,NULL,NULL,NULL,NULL,'Cash','2026-05-13','INV017','RB001',145,NULL,NULL,'GOLD CHAIN','GOLD','Bridal ','95','95','96',NULL,'By Weight','GOLD JEWELLERY',NULL,20.000,2.000,18.000,2000.00,'Gross Weight',NULL,0.000,18.000,'MC %','10',22385.61,NULL,NULL,12436.45,13091.00,223856.10,3.00,7449.05,248301.71,255751.00,NULL,NULL,NULL,NULL,NULL,NULL,'Sales',1,248301.71,7449.05,255750.76,'2026-05-13 07:06:57',NULL,NULL,'pending',NULL,NULL,NULL,255751.00,255751.00,0.00,0.00,0.00,0.00,NULL,NULL,0.00,NULL,NULL,NULL,NULL,NULL,NULL,NULL,60.00,NULL,'Delivered',0.00,0.00,NULL,'12:36 PM',NULL,NULL,NULL),(2564,52,'0938185028','SAIKRUSHNA CHARY KADARLA','kadarlasaikrushna99@gmail.com','SH11, Sircilla, Sircilla mandal, Rajanna Sircilla, Telangana, 505301, India','Sircilla','Sircilla','505301',NULL,NULL,NULL,NULL,NULL,'Cash','2026-05-13','INV018','RB001',145,NULL,NULL,'GOLD CHAIN','GOLD','Bridal ','95','95','96',NULL,'By Weight','GOLD JEWELLERY',NULL,20.000,2.000,18.000,2000.00,'Gross Weight',NULL,0.000,18.000,'MC %','10',22385.61,NULL,NULL,12436.45,13091.00,223856.10,3.00,7449.05,248301.71,255751.00,NULL,NULL,NULL,NULL,NULL,NULL,'Sales',1,248301.71,7449.05,255750.76,'2026-05-13 07:18:40',NULL,NULL,'pending',NULL,NULL,NULL,255751.00,255751.00,0.00,0.00,0.00,0.00,NULL,NULL,0.00,NULL,NULL,NULL,NULL,NULL,NULL,NULL,60.00,NULL,'Delivered',0.00,0.00,NULL,'12:48 PM',NULL,NULL,NULL),(2565,52,'0938185028','SAIKRUSHNA CHARY KADARLA','kadarlasaikrushna99@gmail.com','SH11, Sircilla, Sircilla mandal, Rajanna Sircilla, Telangana, 505301, India','Sircilla','Sircilla','505301',NULL,NULL,NULL,NULL,NULL,'Cash','2026-05-13','INV019','RB001',145,NULL,NULL,'GOLD CHAIN','GOLD','Bridal ','95','95','96',NULL,'By Weight','GOLD JEWELLERY',NULL,15.000,2.000,13.000,5000.00,'Gross Weight',5.00,0.750,13.750,'MC %','10',17100.12,NULL,NULL,12436.45,13091.00,171001.19,3.00,5794.84,193161.31,198956.00,NULL,NULL,NULL,NULL,NULL,NULL,'Sales',1,193161.31,5794.84,198956.15,'2026-05-13 07:19:09',NULL,NULL,'pending',NULL,NULL,NULL,198956.00,198956.00,0.00,0.00,0.00,0.00,NULL,NULL,0.00,NULL,NULL,NULL,NULL,NULL,NULL,NULL,60.00,NULL,'Delivered',0.00,0.00,NULL,'12:49 PM',NULL,NULL,NULL),(2566,52,'0938185028','SAIKRUSHNA CHARY KADARLA','kadarlasaikrushna99@gmail.com','SH11, Sircilla, Sircilla mandal, Rajanna Sircilla, Telangana, 505301, India','Sircilla','Sircilla','505301',NULL,NULL,NULL,NULL,NULL,'Cash','2026-05-13','INV020','RB002',146,NULL,NULL,'SILVER PATTI','SILVER','Bridal ','95','92','92',NULL,'By Weight','SILVER JEWELLERY',NULL,10.000,1.000,9.000,100.00,'Gross Weight',NULL,0.000,9.000,'MC / Gram','10',90.00,NULL,NULL,110.40,120.00,993.60,3.00,37.31,1243.60,1281.00,NULL,NULL,NULL,NULL,NULL,NULL,'Sales',1,1243.60,37.31,1280.91,'2026-05-13 10:22:46',NULL,NULL,'pending',NULL,NULL,NULL,1281.00,1281.00,0.00,0.00,0.00,0.00,NULL,NULL,0.00,NULL,NULL,NULL,NULL,NULL,NULL,NULL,60.00,NULL,'Delivered',0.00,0.00,NULL,'03:52 PM',NULL,NULL,NULL),(2567,52,'0938185028','SAIKRUSHNA CHARY KADARLA','kadarlasaikrushna99@gmail.com','SH11, Sircilla, Sircilla mandal, Rajanna Sircilla, Telangana, 505301, India','Sircilla','Sircilla','505301',NULL,NULL,NULL,NULL,NULL,'Cash','2026-05-13','INV021','RB002',146,NULL,NULL,'SILVER PATTI','SILVER','Bridal ','95','92','92',NULL,'By Weight','SILVER JEWELLERY',NULL,20.000,2.000,18.000,200.00,'Gross Weight',NULL,0.000,18.000,'MC / Gram','50',900.00,NULL,NULL,110.40,120.00,1987.20,3.00,94.42,3147.20,3242.00,NULL,NULL,NULL,NULL,NULL,NULL,'Sales',1,3147.20,94.42,3241.62,'2026-05-13 10:23:39',NULL,NULL,'pending',NULL,NULL,NULL,3242.00,3242.00,0.00,0.00,0.00,0.00,NULL,NULL,0.00,NULL,NULL,NULL,NULL,NULL,NULL,NULL,60.00,NULL,'Delivered',0.00,0.00,NULL,'03:53 PM',NULL,NULL,NULL),(2568,52,'0938185028','SAIKRUSHNA CHARY KADARLA','kadarlasaikrushna99@gmail.com','SH11, Sircilla, Sircilla mandal, Rajanna Sircilla, Telangana, 505301, India','Sircilla','Sircilla','505301',NULL,NULL,NULL,NULL,NULL,'Cash','2026-05-13','INV022','RB002',146,NULL,NULL,'SILVER PATTI','SILVER','Bridal ','95','92','92',NULL,'By Weight','SILVER JEWELLERY',NULL,25.000,2.000,23.000,200.00,'Gross Weight',NULL,0.000,23.000,'MC / Gram','50',1150.00,NULL,NULL,110.40,120.00,2539.20,3.00,118.48,3949.20,4068.00,NULL,NULL,NULL,NULL,NULL,NULL,'Sales',1,3949.20,118.48,4067.68,'2026-05-13 10:33:24',NULL,NULL,'pending',NULL,NULL,NULL,4068.00,4068.00,0.00,0.00,0.00,0.00,NULL,NULL,0.00,NULL,NULL,NULL,NULL,NULL,NULL,NULL,60.00,NULL,'Delivered',0.00,0.00,NULL,'04:03 PM',NULL,NULL,NULL),(2569,52,'0938185028','SAIKRUSHNA CHARY KADARLA','kadarlasaikrushna99@gmail.com','SH11, Sircilla, Sircilla mandal, Rajanna Sircilla, Telangana, 505301, India','Sircilla','Sircilla','505301',NULL,NULL,NULL,NULL,NULL,'Cash','2026-05-13','INV023','RB001',145,NULL,NULL,'GOLD BRACELETS','GOLD','Bridal ','95','95','95',NULL,'By Weight','GOLD JEWELLERY',NULL,10.000,1.000,9.000,1000.00,'Gross Weight',10.00,1.000,10.000,'MC %','10',12436.45,NULL,NULL,12436.45,13091.00,124364.50,3.00,4135.83,137860.95,141997.00,NULL,NULL,NULL,NULL,NULL,NULL,'Sales',1,137860.95,4135.83,141996.78,'2026-05-13 10:34:36',NULL,NULL,'pending',NULL,NULL,NULL,141997.00,141997.00,0.00,0.00,0.00,0.00,NULL,NULL,0.00,NULL,NULL,NULL,NULL,NULL,NULL,NULL,60.00,NULL,'Delivered',0.00,0.00,NULL,'04:04 PM',NULL,NULL,NULL);
/*!40000 ALTER TABLE `repair_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `repairdetails`
--

DROP TABLE IF EXISTS `repairdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `repairdetails` (
  `repairdetails_id` int NOT NULL AUTO_INCREMENT,
  `repair_id` int DEFAULT NULL,
  `metal_type` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `description` text COLLATE utf8mb4_general_ci,
  `weight` float DEFAULT NULL,
  `qty` int DEFAULT NULL,
  `rate_type` enum('Per Qty','Per Weight') COLLATE utf8mb4_general_ci DEFAULT NULL,
  `rate` float DEFAULT NULL,
  `overall_weight` float DEFAULT NULL,
  `overall_qty` int DEFAULT NULL,
  `overall_total` float DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`repairdetails_id`),
  KEY `repair_id` (`repair_id`),
  CONSTRAINT `repairdetails_ibfk_1` FOREIGN KEY (`repair_id`) REFERENCES `repairs` (`repair_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `repairdetails`
--

LOCK TABLES `repairdetails` WRITE;
/*!40000 ALTER TABLE `repairdetails` DISABLE KEYS */;
/*!40000 ALTER TABLE `repairdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `repairs`
--

DROP TABLE IF EXISTS `repairs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `repairs` (
  `repair_id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int DEFAULT NULL,
  `account_name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `mobile` varchar(15) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `email` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `address1` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `address2` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `address3` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `staff` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `delivery_date` date DEFAULT NULL,
  `place` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `metal` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `counter` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `entry_type` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `date` date DEFAULT NULL,
  `metal_type` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `item` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `tag_no` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `description` text COLLATE utf8mb4_general_ci,
  `purity` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `category` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `sub_category` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `gross_weight` decimal(10,3) DEFAULT NULL,
  `pcs` int DEFAULT NULL,
  `estimated_dust` decimal(10,3) DEFAULT NULL,
  `estimated_amt` decimal(10,2) DEFAULT NULL,
  `extra_weight` decimal(10,3) DEFAULT NULL,
  `stone_value` decimal(10,2) DEFAULT NULL,
  `making_charge` decimal(10,2) DEFAULT NULL,
  `handling_charge` decimal(10,2) DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL,
  `city` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `repair_no` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `status` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `image` longtext COLLATE utf8mb4_general_ci,
  `gross_wt_after_repair` decimal(10,2) DEFAULT NULL,
  `total_amt` decimal(10,2) DEFAULT NULL,
  `invoice` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `invoice_number` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`repair_id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `repairs`
--

LOCK TABLES `repairs` WRITE;
/*!40000 ALTER TABLE `repairs` DISABLE KEYS */;
/*!40000 ALTER TABLE `repairs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schemes_customerschemeenrollment`
--

DROP TABLE IF EXISTS `schemes_customerschemeenrollment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `schemes_customerschemeenrollment` (
  `enrollment_id` int NOT NULL AUTO_INCREMENT,
  `enrollment_number` varchar(50) NOT NULL,
  `enrollment_date` date NOT NULL,
  `maturity_date` date NOT NULL,
  `installment_amount` decimal(12,2) NOT NULL,
  `total_installments` int unsigned NOT NULL,
  `paid_installments` int unsigned NOT NULL,
  `pending_installments` int unsigned NOT NULL,
  `total_paid_amount` decimal(15,2) NOT NULL,
  `remarks` longtext,
  `status` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int DEFAULT NULL,
  `customer_id` int NOT NULL,
  `scheme_id` int NOT NULL,
  PRIMARY KEY (`enrollment_id`),
  UNIQUE KEY `enrollment_number` (`enrollment_number`),
  KEY `schemes_customerschem_created_by_id_35e46ae0_fk_users_id` (`created_by_id`),
  KEY `schemes_customersche_customer_id_57c963c1_fk_account_d` (`customer_id`),
  KEY `schemes_customersche_scheme_id_a6d27c20_fk_schemes_s` (`scheme_id`),
  CONSTRAINT `schemes_customersche_customer_id_57c963c1_fk_account_d` FOREIGN KEY (`customer_id`) REFERENCES `account_details` (`account_id`),
  CONSTRAINT `schemes_customersche_scheme_id_a6d27c20_fk_schemes_s` FOREIGN KEY (`scheme_id`) REFERENCES `schemes_scheme` (`scheme_id`),
  CONSTRAINT `schemes_customerschem_created_by_id_35e46ae0_fk_users_id` FOREIGN KEY (`created_by_id`) REFERENCES `users` (`id`),
  CONSTRAINT `schemes_customerschemeenrollment_chk_1` CHECK ((`total_installments` >= 0)),
  CONSTRAINT `schemes_customerschemeenrollment_chk_2` CHECK ((`paid_installments` >= 0)),
  CONSTRAINT `schemes_customerschemeenrollment_chk_3` CHECK ((`pending_installments` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schemes_customerschemeenrollment`
--

LOCK TABLES `schemes_customerschemeenrollment` WRITE;
/*!40000 ALTER TABLE `schemes_customerschemeenrollment` DISABLE KEYS */;
/*!40000 ALTER TABLE `schemes_customerschemeenrollment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schemes_scheme`
--

DROP TABLE IF EXISTS `schemes_scheme`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `schemes_scheme` (
  `scheme_id` int NOT NULL AUTO_INCREMENT,
  `scheme_name` varchar(200) NOT NULL,
  `scheme_maturity_period` int DEFAULT NULL,
  `scheme_benefit` varchar(50) NOT NULL,
  `scheme_installment_amount` int DEFAULT NULL,
  `x_value` int unsigned DEFAULT NULL,
  `y_value` int unsigned DEFAULT NULL,
  `payable_installments` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int DEFAULT NULL,
  `updated_by_id` int DEFAULT NULL,
  PRIMARY KEY (`scheme_id`),
  UNIQUE KEY `scheme_name` (`scheme_name`),
  KEY `schemes_scheme_created_by_id_356a91ef_fk_users_id` (`created_by_id`),
  KEY `schemes_scheme_updated_by_id_e4e16a60_fk_users_id` (`updated_by_id`),
  CONSTRAINT `schemes_scheme_created_by_id_356a91ef_fk_users_id` FOREIGN KEY (`created_by_id`) REFERENCES `users` (`id`),
  CONSTRAINT `schemes_scheme_updated_by_id_e4e16a60_fk_users_id` FOREIGN KEY (`updated_by_id`) REFERENCES `users` (`id`),
  CONSTRAINT `schemes_scheme_chk_1` CHECK ((`x_value` >= 0)),
  CONSTRAINT `schemes_scheme_chk_2` CHECK ((`y_value` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schemes_scheme`
--

LOCK TABLES `schemes_scheme` WRITE;
/*!40000 ALTER TABLE `schemes_scheme` DISABLE KEYS */;
INSERT INTO `schemes_scheme` VALUES (1,'Gold Saver 10+1',11,'x_plus_y',1000,10,1,10,'2026-07-17 16:51:33.911631','2026-07-17 16:51:33.911631',NULL,NULL);
/*!40000 ALTER TABLE `schemes_scheme` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schemes_schemeinstallment`
--

DROP TABLE IF EXISTS `schemes_schemeinstallment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `schemes_schemeinstallment` (
  `installment_id` int NOT NULL AUTO_INCREMENT,
  `installment_no` int unsigned NOT NULL,
  `due_date` date NOT NULL,
  `amount` decimal(12,2) NOT NULL,
  `paid_amount` decimal(12,2) NOT NULL,
  `paid_date` date DEFAULT NULL,
  `receipt_number` varchar(50) DEFAULT NULL,
  `payment_mode` varchar(20) DEFAULT NULL,
  `transaction_reference` varchar(100) DEFAULT NULL,
  `remarks` longtext,
  `status` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `enrollment_id` int NOT NULL,
  PRIMARY KEY (`installment_id`),
  UNIQUE KEY `schemes_schemeinstallmen_enrollment_id_installmen_b4466444_uniq` (`enrollment_id`,`installment_no`),
  CONSTRAINT `schemes_schemeinstal_enrollment_id_0ac41f20_fk_schemes_c` FOREIGN KEY (`enrollment_id`) REFERENCES `schemes_customerschemeenrollment` (`enrollment_id`),
  CONSTRAINT `schemes_schemeinstallment_chk_1` CHECK ((`installment_no` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schemes_schemeinstallment`
--

LOCK TABLES `schemes_schemeinstallment` WRITE;
/*!40000 ALTER TABLE `schemes_schemeinstallment` DISABLE KEYS */;
/*!40000 ALTER TABLE `schemes_schemeinstallment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schemes_schemereceipt`
--

DROP TABLE IF EXISTS `schemes_schemereceipt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `schemes_schemereceipt` (
  `receipt_id` int NOT NULL AUTO_INCREMENT,
  `receipt_number` varchar(50) NOT NULL,
  `receipt_date` date NOT NULL,
  `amount` decimal(12,2) NOT NULL,
  `payment_mode` varchar(20) NOT NULL,
  `transaction_reference` varchar(100) DEFAULT NULL,
  `remarks` longtext,
  `created_at` datetime(6) NOT NULL,
  `installment_id` int NOT NULL,
  PRIMARY KEY (`receipt_id`),
  UNIQUE KEY `receipt_number` (`receipt_number`),
  KEY `schemes_schemereceip_installment_id_ddef6961_fk_schemes_s` (`installment_id`),
  CONSTRAINT `schemes_schemereceip_installment_id_ddef6961_fk_schemes_s` FOREIGN KEY (`installment_id`) REFERENCES `schemes_schemeinstallment` (`installment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schemes_schemereceipt`
--

LOCK TABLES `schemes_schemereceipt` WRITE;
/*!40000 ALTER TABLE `schemes_schemereceipt` DISABLE KEYS */;
/*!40000 ALTER TABLE `schemes_schemereceipt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `states`
--

DROP TABLE IF EXISTS `states`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `states` (
  `state_id` int NOT NULL AUTO_INCREMENT,
  `state_name` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `state_code` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`state_id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `states`
--

LOCK TABLES `states` WRITE;
/*!40000 ALTER TABLE `states` DISABLE KEYS */;
INSERT INTO `states` VALUES (1,'Telangana','36'),(2,'Jammu and Kashmir','01'),(3,'Himachal Pradesh','02'),(4,'Punjab','03'),(5,'Chandigarh','04'),(6,'Uttarakhand','05'),(7,'Haryana','06'),(8,'Rajasthan','08'),(9,'Uttar Pradesh','09'),(10,'Bihar','10'),(11,'Sikkim','11'),(12,'Arunachal Pradesh','12'),(13,'Nagaland','13'),(14,'Manipur','14'),(15,'Mizoram','15'),(16,'Tripura','16'),(17,'Meghalaya','17'),(18,'Assam','18'),(19,'West Bengal','19'),(20,'Jharkhand','20'),(21,'Odisha','21'),(22,'Chattisgarh','22'),(23,'Madhya Pradesh','23'),(24,'Gujarat','24'),(25,'Maharashtra','27'),(26,'Karnataka','29'),(27,'Goa','30'),(28,'Kerala','32'),(29,'Tamil Nadu','33'),(30,'Andhra Pradesh','37'),(31,'Delhi (NCT)','07'),(32,'Chandigarh','04'),(33,'Dadra & Nagar Haveli and Daman & Diu','26'),(34,'Lakshadweep','31'),(35,'Puducherry','34'),(36,'Andaman & Nicobar Islands','35'),(37,'Ladakh','38'),(38,'Other Territory','97'),(39,'Center Jurisdiction','99');
/*!40000 ALTER TABLE `states` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stone_details`
--

DROP TABLE IF EXISTS `stone_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stone_details` (
  `id` int NOT NULL AUTO_INCREMENT,
  `stoneName` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `cut` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `color` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `clarity` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `stoneWt` decimal(10,3) DEFAULT NULL,
  `caratWt` decimal(10,3) DEFAULT NULL,
  `stonePrice` decimal(10,2) DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `purchase_id` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stone_details`
--

LOCK TABLES `stone_details` WRITE;
/*!40000 ALTER TABLE `stone_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `stone_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subcategory`
--

DROP TABLE IF EXISTS `subcategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subcategory` (
  `subcategory_id` int NOT NULL AUTO_INCREMENT,
  `category_id` int DEFAULT NULL,
  `metal_type_id` int DEFAULT NULL,
  `metal_type` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `sub_category_name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `category` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `prefix` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `purity` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `selling_purity` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `printing_purity` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `pricing` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`subcategory_id`)
) ENGINE=InnoDB AUTO_INCREMENT=161 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subcategory`
--

LOCK TABLES `subcategory` WRITE;
/*!40000 ALTER TABLE `subcategory` DISABLE KEYS */;
INSERT INTO `subcategory` VALUES (157,145,2,'GOLD','GOLD BRACELETS','GOLD JEWELLERY','GBR','95','95','95','By Weight'),(158,146,NULL,'SILVER','SILVER PATTI','SILVER JEWELLERY','ST','95','92','92',NULL),(159,145,2,'GOLD','GOLD CHAIN','GOLD JEWELLERY','CH','95','95','96','By Weight'),(160,147,3,'SILVER','SILVER DEEPA','SILVER ARTICLES','SD','92','92','92','By Weight');
/*!40000 ALTER TABLE `subcategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `taxslabs`
--

DROP TABLE IF EXISTS `taxslabs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `taxslabs` (
  `tax_id` int NOT NULL AUTO_INCREMENT,
  `TaxSlabID` int NOT NULL,
  `TaxSlabName` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `TaxationType` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `SGSTPercentage` float DEFAULT NULL,
  `CGSTPercentage` float DEFAULT NULL,
  `IGSTPercentage` float DEFAULT NULL,
  `TaxCategory` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`tax_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `taxslabs`
--

LOCK TABLES `taxslabs` WRITE;
/*!40000 ALTER TABLE `taxslabs` DISABLE KEYS */;
INSERT INTO `taxslabs` VALUES (1,9,'03% GST','Taxable',1.5,1.5,3,'Goods'),(2,8,'18% GST','Taxable',9,9,18,'Goods'),(4,4,'12% GST','Taxable',6,6,12,'Goods'),(5,3,'05% GST','Taxable',2.5,2.5,5,'Goods'),(6,1,'Tax Free','Taxable',0,0,0,'Goods'),(7,2,'28%','Taxable',14,14,28,'Goods');
/*!40000 ALTER TABLE `taxslabs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `updated_values_table`
--

DROP TABLE IF EXISTS `updated_values_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `updated_values_table` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `pcs` int DEFAULT NULL,
  `gross_weight` decimal(10,3) DEFAULT NULL,
  `bal_pcs` int DEFAULT NULL,
  `bal_gross_weight` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `added_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `tag_id` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `updated_values_table`
--

LOCK TABLES `updated_values_table` WRITE;
/*!40000 ALTER TABLE `updated_values_table` DISABLE KEYS */;
INSERT INTO `updated_values_table` VALUES (1,'145',10,100.000,10,'100','2025-12-15 11:10:18',1),(2,'145',100,1000.000,100,'1000','2026-04-07 11:58:51',2),(3,'145',100,1000.000,100,'1000','2026-04-07 12:15:04',3),(4,'145',100,1000.000,100,'1000','2026-04-07 12:26:18',4),(5,'145',100,1000.000,97,'970','2026-04-07 16:00:05',5),(6,'146',20,200.000,12,'120','2026-04-17 21:35:16',6);
/*!40000 ALTER TABLE `updated_values_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `urd_purchase_details`
--

DROP TABLE IF EXISTS `urd_purchase_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `urd_purchase_details` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int DEFAULT NULL,
  `account_name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `mobile` varchar(15) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `email` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `address1` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `address2` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `city` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `state` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `state_code` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `aadhar_card` varchar(12) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `gst_in` varchar(15) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `pan_card` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `date` date DEFAULT NULL,
  `urdpurchase_number` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `product_id` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `product_name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `metal` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `purity` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `hsn_code` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `gross` decimal(10,3) DEFAULT NULL,
  `dust` decimal(10,3) DEFAULT NULL,
  `touch_percent` decimal(5,2) DEFAULT NULL,
  `ml_percent` decimal(5,2) DEFAULT NULL,
  `eqt_wt` decimal(10,3) DEFAULT NULL,
  `remarks` text COLLATE utf8mb4_general_ci,
  `rate` decimal(10,2) DEFAULT NULL,
  `total_amount` decimal(10,2) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `urd_purchase_details`
--

LOCK TABLES `urd_purchase_details` WRITE;
/*!40000 ALTER TABLE `urd_purchase_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `urd_purchase_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_permissions`
--

DROP TABLE IF EXISTS `user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_type_id` int NOT NULL,
  `user_type` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `menu_name` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `can_add` tinyint(1) DEFAULT '0',
  `can_modify` tinyint(1) DEFAULT '0',
  `can_delete` tinyint(1) DEFAULT '0',
  `can_view` tinyint(1) DEFAULT '0',
  `can_print` tinyint(1) DEFAULT '0',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_permissions`
--

LOCK TABLES `user_permissions` WRITE;
/*!40000 ALTER TABLE `user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `phone_number` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `email` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `password` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `retype_password` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `role` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `user_type_id` int DEFAULT NULL,
  `full_name` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'ADMIN','1234567896','admin@gmail.com','admin@123','admin@123','admin',1,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usertype`
--

DROP TABLE IF EXISTS `usertype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usertype` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_type` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usertype`
--

LOCK TABLES `usertype` WRITE;
/*!40000 ALTER TABLE `usertype` DISABLE KEYS */;
/*!40000 ALTER TABLE `usertype` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-07-20 11:40:09
