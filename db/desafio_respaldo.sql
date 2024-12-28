-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: desafio_ip
-- ------------------------------------------------------
-- Server version	8.0.40

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
-- Table structure for table `analisis_ip`
--

DROP TABLE IF EXISTS `analisis_ip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `analisis_ip` (
  `id` int NOT NULL AUTO_INCREMENT,
  `direccion_ip` varchar(15) DEFAULT NULL,
  `pais` varchar(50) DEFAULT NULL,
  `ciudad` varchar(50) DEFAULT NULL,
  `indice_reputacion` varchar(50) DEFAULT NULL,
  `estado` varchar(50) DEFAULT NULL,
  `latitud` float DEFAULT NULL,
  `longitud` float DEFAULT NULL,
  `total_reportes` int DEFAULT NULL,
  `ultimo_reporte` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `analisis_ip`
--

LOCK TABLES `analisis_ip` WRITE;
/*!40000 ALTER TABLE `analisis_ip` DISABLE KEYS */;
INSERT INTO `analisis_ip` VALUES (25,'195.47.238.82','Sweden','Stockholm','100','Maliciosa',59.3321,18.0575,359,'2024-12-27T19:13:03+00:00'),(26,'185.220.101.2','Germany','Hamburg','100','Maliciosa',53.5685,10.0589,199,'2024-12-27T16:47:41+00:00'),(27,'192.42.116.216','Netherlands','Nieuwegein','100','Maliciosa',52.0475,5.07549,1157,'2024-12-28T02:07:02+00:00'),(29,'87.248.1.199','Norway','Gjøvik','100','Maliciosa',60.7142,10.8577,1036,'2024-12-28T02:32:01+00:00'),(30,'102.165.1.137','South Africa','Johannesburg','7','Confiable',-26.1992,28.0564,17,'2024-11-07T04:40:09+00:00'),(33,'104.28.48.166','United States','Long Beach','0','Confiable',33.7808,-118.159,0,'2024-09-16T15:59:37+00:00'),(35,'184.75.210.50','Canada','Toronto','33','Sospechosa',43.7032,-79.5122,11,'2024-12-26T12:39:47+00:00'),(36,'176.67.86.248','Poland','Warsaw','84','Maliciosa',52.2317,21.0183,64,'2024-12-26T12:39:47+00:00'),(38,'176.67.86.248','Poland','Warsaw','82','Maliciosa',52.2317,21.0183,54,'2024-12-27T21:59:34+00:00');
/*!40000 ALTER TABLE `analisis_ip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'xavier_test','xavier_test');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-28 18:42:18
