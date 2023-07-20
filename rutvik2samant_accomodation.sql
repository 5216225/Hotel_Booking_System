-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: rutvik2samant
-- ------------------------------------------------------
-- Server version	8.0.29-0ubuntu0.20.04.2

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
-- Table structure for table `accomodation`
--

DROP TABLE IF EXISTS `accomodation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accomodation` (
  `idAccomodation` int NOT NULL AUTO_INCREMENT,
  `accFare` double NOT NULL DEFAULT '100',
  `smoking` char(1) NOT NULL,
  `accFeatures` varchar(80) NOT NULL,
  `accCity` varchar(45) NOT NULL,
  `address` varchar(70) NOT NULL,
  `roomtype` varchar(16) DEFAULT NULL,
  PRIMARY KEY (`idAccomodation`),
  UNIQUE KEY `idAccomodation_UNIQUE` (`idAccomodation`)
) ENGINE=InnoDB AUTO_INCREMENT=1047 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accomodation`
--

LOCK TABLES `accomodation` WRITE;
/*!40000 ALTER TABLE `accomodation` DISABLE KEYS */;
INSERT INTO `accomodation` VALUES (1,84,'N','Satellite TV, Wifi, Safe, Iron/board, Breakfast, Kitchen','Edinburgh','20 Victoria Street, Soonsquare, MN23 2AL, Edinburgh','Double Room'),(2,70,'N','TV, Wifi','Bristol','18 Near Street, Hyte Gardens, B56 8HG, Bristol','Single Room'),(3,70,'N','Satellite TV, Wifi, Safe, Kitchen','Edinburgh','20 Victoria Street, Soonsquare, MN23 2AL, Edinburgh','Single Room'),(4,90,'N','Satellite TV, Wifi, Safe, Iron/board, Breakfast, Gym, Swimming, Kitchen','Cardiff','1 Jones square, Hutton Gardens, C23 2AX, Cardiff','Family Room'),(5,105,'N','Satellite TV, Wifi, Safe, Iron/board, Breakfast, Gym, Swimming, Kitchen','Edinburgh','20 Victoria Street, Soonsquare, MN23 2AL, Edinburgh','Family Room'),(6,72,'N','Satellite TV, Wifi, Safe, Iron/board, Breakfast, Kitchen','Cardiff','1 Jones square, Hutton Gardens, C23 2AX, Cardiff','Double Room'),(7,60,'N','TV, Wifi','Cardiff','1 Jones square, Hutton Gardens, C23 2AX, Cardiff','Single Room'),(8,105,'N','Satellite TV, Wifi, Safe, Iron/board, Breakfast, Kitchen','Birmingham','27 Victoria Street, Clifton, B27 7HJ, Birmingham','Family Room'),(9,84,'N','Satellite TV, Wifi, Safe, Iron/board, Kitchen','Birmingham','27 Victoria Street, Clifton, B27 7HJ, Birmingham','Double Room'),(10,90,'N','Satellite TV, Wifi, Safe, Iron/board, Breakfast, Kitchen','Belfast','87 Field View Drive, Saxons, B12 J7G, Belfast','Family Room'),(11,70,'N','TV, Wifi','Birmingham','27 Victoria Street, Clifton, B27 7HJ, Birmingham','Single Room'),(12,84,'N','Satellite TV, Wifi, Safe, Iron/board, Kitchen','Bristol','18 Near Street, Hyte Gardens, B56 8HG, Bristol','Double Room'),(13,105,'N','Satellite TV, Wifi, Safe, Iron/board, Breakfast, Kitchen','Bristol','18 Near Street, Hyte Gardens, B56 8HG, Bristol','Family Room'),(14,72,'N','Satellite TV, Wifi, Safe, Iron/board, Kitchen','Belfast','87 Field View Drive, Saxons, B12 J7G, Belfast','Double Room'),(15,72,'Y','Satellite TV, Wifi, Safe, Iron/board, Kitchen','Aberdeen','15 Abotts Road, Abbswood, A12 6JX, Aberdeen','Double Room'),(16,60,'Y','TV, Wifi','Aberdeen','15 Abotts Road, Abbswood, A12 6JX, Aberdeen','Single Room'),(17,3,'N','Satellite TV, Wifi, Safe, Iron/board, Breakfast, Kitchen','Abeerden','15 Abotts Road, Abbswood, A12 6JX, Aberdeen','Family Room'),(18,60,'N','TV, Wifi','Belfast','87 Field View Drive, Saxons, B12 J7G, Belfast','Single Room'),(19,70,'Y','TV, Wifi','Glasglow','48 Hyden Gardens, Moons, G45 7JK, Glasglow','Single Room'),(20,84,'Y','Satellite TV, Wifi, Safe, Iron/board, Breakfast, Kitchen','Glasglow','48 Hyden Gardens, Moons, G45 7JK, Glasglow','Double Room'),(21,105,'Y','Satellite TV, Wifi, Safe, Iron/board, Breakfast, Gym, Swimming, Kitchen','Glasglow','48 Hyden Gardens, Moons, G45 7JK, Glasglow','Family Room'),(22,80,'N','TV, Wifi','London','10A Prinknash Road, Edgewood, L23 7HG, London','Single Room'),(23,96,'N','Satellite TV, Wifi, Safe, Iron/board, Breakfast, Kitchen','London','10A Prinknash Road, Edgewood, L23 7HG, London','Double Room'),(24,120,'N','Satellite TV, Wifi, Safe, Iron/board, Breakfast, Gym, Swimming, Kitchen','London','10A Prinknash Road, Edgewood, L23 7HG, London','Family Room'),(25,80,'Y','TV, Wifi','Manchester','45 Elders Road, Edlens, M12 9KJ, Manchester','Single Room'),(26,96,'Y','Satellite TV, Wifi, Safe, Iron/board, Breakfast, Kitchen','Manchester','45 Elders Road, Eldens, M12 9KJ, Manchester','Double Room'),(27,120,'Y','Satellite TV, Wifi, Safe, Iron/board, Breakfast, Gym, Swimming, Kitchen','Manchester','45 Elders Road, Eldens, M12 9KJ, Manchester','Family Room'),(28,60,'N','TV, Wifi','New Castle','68 Causeway Road, Jasons, N13 6JK, New Castle','Single Room'),(29,72,'N','Satellite TV, Wifi, Safe, Iron/board, Breakfast, Kitchen','New Castle','68 Causeway Road, Jasons, N13 6JK, New Castle','Double Room'),(30,90,'N','Satellite TV, Wifi, Safe, Iron/board, Breakfast, Gym, Swimming, Kitchen','New Castle','68 Causeway Road, Jasons, N13 6JK, New Castle','Family Room'),(31,60,'Y','TV, Wifi','Norwich','95 Edgeway Road, Rasens, N89 9IK, Norwich','Single Room'),(32,72,'Y','Satellite TV, Wifi, Safe, Iron/board, Breakfast, Kitchen','Norwich','95 Edgeway Road, Rasens, N89 9IK, Norwich','Double Room'),(33,90,'Y','Satellite TV, Wifi, Safe, Iron/board, Breakfast, Gym, Swimming, Kitchen','Norwich','95 Edgeway Road, Rasens, N89 9IK, Norwich','Family Room'),(34,70,'N','TV, Wifi','Nottingham','56 Greenwich Avenue, Greenwich, N98 7HJ, Nottingham','Single Room'),(35,84,'N','Satellite TV, Wifi, Safe, Iron/board, Breakfast, Kitchen','Nottingham','56 Greenwich Avenue, Greenwich, N98 7HJ, Nottingham','Double Room'),(36,105,'N','Satellite TV, Wifi, Safe, Iron/board, Breakfast, Gym, Swimming, Kitchen','Nottingham','56 Greenwich Avenue, Greenwich, N98 7HJ, Nottingham','Family Room'),(37,70,'N','TV, Wifi','Oxford','86 Painswick Road, Barnwood, OX12 8KL, Oxford','Single Room'),(38,84,'N','Satellite TV, Wifi, Safe, Iron/board, Breakfast, Kitchen','Oxford','86 Painswick Road, Barnwood, OX12 8KL, Oxford','Double Room'),(39,105,'N','Satellite TV, Wifi, Safe, Iron/board, Breakfast, Gym, Swimming, Kitchen','Oxford','86 Painswick Road, Barnwood, OX12 8KL, Oxford','Family Room'),(40,50,'N','TV, Wifi','Plymouth','21 Matson Avenue, Matson, P23 6YT, Plymouth','Single Room'),(41,60,'N','Satellite TV, Wifi, Safe, Iron/board, Breakfast, Kitchen','Plymouth','21 Matson Avenue, Matson, P23 6YT, Plymouth','Double Room'),(42,75,'N','Satellite TV, Wifi, Safe, Iron/board, Breakfast, Gym, Swimming, Kitchen','Plymouth','21 Matson Avenue, Matson, P23 6YT, Plymouth','Family Room'),(43,50,'N','TV, Wifi','Swansea','65 Evanwicks Road, Robinswood, S34 8IO, Swansea','Single Room'),(44,60,'N','Satellite TV, Wifi, Safe, Iron/board, Breakfast, Kitchen','Swansea','65 Evanwicks Road, Robinswood, S34 8IO, Swansea','Double Room'),(45,75,'N','Satellite TV, Wifi, Safe, Iron/board, Breakfast, Gym, Swimming, Kitchen','Swansea','65 Evanwicks Road, Robinswood, S34 8IO, Swansea','Family Room');
/*!40000 ALTER TABLE `accomodation` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-04 12:52:27
