-- MySQL dump 10.13  Distrib 8.0.41, for Linux (x86_64)
--
-- Host: blockly-pg-rds.cmadu8gaa330.ap-northeast-1.rds.amazonaws.com    Database: blockly_pg
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '';

--
-- Table structure for table `AdminApp_fileupload`
--

DROP TABLE IF EXISTS `AdminApp_fileupload`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AdminApp_fileupload` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `file` varchar(100) NOT NULL,
  `upload_date` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AdminApp_fileupload`
--

LOCK TABLES `AdminApp_fileupload` WRITE;
/*!40000 ALTER TABLE `AdminApp_fileupload` DISABLE KEYS */;
/*!40000 ALTER TABLE `AdminApp_fileupload` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AdminApp_image`
--

DROP TABLE IF EXISTS `AdminApp_image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AdminApp_image` (
  `img_name` varchar(40) NOT NULL,
  `base64_image` varchar(1000) NOT NULL,
  PRIMARY KEY (`img_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AdminApp_image`
--

LOCK TABLES `AdminApp_image` WRITE;
/*!40000 ALTER TABLE `AdminApp_image` DISABLE KEYS */;
/*!40000 ALTER TABLE `AdminApp_image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `UserApp_test`
--

DROP TABLE IF EXISTS `UserApp_test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `UserApp_test` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `kadai_id` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `UserApp_test_kadai_id_f74ce06a_fk_kadai_table_number` (`kadai_id`),
  CONSTRAINT `UserApp_test_kadai_id_f74ce06a_fk_kadai_table_number` FOREIGN KEY (`kadai_id`) REFERENCES `kadai_table` (`number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UserApp_test`
--

LOCK TABLES `UserApp_test` WRITE;
/*!40000 ALTER TABLE `UserApp_test` DISABLE KEYS */;
/*!40000 ALTER TABLE `UserApp_test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `answer_table`
--

DROP TABLE IF EXISTS `answer_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `answer_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `a_text` longtext NOT NULL,
  `kadai_id` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `answer_table_kadai_id_a8b8e46e_fk_kadai_table_number` (`kadai_id`),
  CONSTRAINT `answer_table_kadai_id_a8b8e46e_fk_kadai_table_number` FOREIGN KEY (`kadai_id`) REFERENCES `kadai_table` (`number`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answer_table`
--

LOCK TABLES `answer_table` WRITE;
/*!40000 ALTER TABLE `answer_table` DISABLE KEYS */;
INSERT INTO `answer_table` VALUES (1,'import sys\r\nimport subprocess\r\n\r\n# ユーザーコードを実行\r\ndef test_user_code(user_code_path):\r\n    result = subprocess.run(\r\n        [\"python3\", user_code_path],\r\n        capture_output=True, text=True\r\n    )\r\n  # 期待される出力（標準出力には改行が含まれる）\r\n    expected_output = \"Hello\\n\"\r\n\r\n  # ユーザーコードの実行結果に応じて判定\r\n    if result.stdout == expected_output:\r\n        return 0  # 成功（期待通りの結果）\r\n    else:\r\n        return 1  # 失敗（期待される出力と一致しない）\r\n\r\n# 実行\r\nif __name__ == \"__main__\":\r\n    user_code_path = sys.argv[1]  # ユーザーコードのパスを受け取る\r\n    exit_code = test_user_code(user_code_path)\r\n    sys.exit(exit_code)','t1'),(5,'import sys\r\nimport subprocess\r\n\r\n# ユーザーコードを実行\r\ndef test_user_code(user_code_path):\r\n    result = subprocess.run(\r\n        [\"python3\", user_code_path], \r\n        capture_output=True, text=True\r\n    )\r\n    # 期待される出力\r\n    expected_output = \"\"\"Hello World!\r\nHello World!\r\nHello World!\r\n\"\"\"\r\n \r\n    if result.stdout == expected_output:\r\n        # 出力が期待通りなら成功\r\n        return 0\r\n    else:\r\n        # 出力が期待通りでないなら失敗\r\n        print(\"実際の出力:\\n\", result.stdout)\r\n        return 1\r\n\r\n# 実行\r\nif __name__ == \"__main__\":\r\n    user_code_path = sys.argv[1]  # ユーザーコードのパスを受け取る\r\n    exit_code = test_user_code(user_code_path)\r\n    sys.exit(exit_code)','b2'),(10,'# テストコード：ユーザーコードを実行し、出力が期待通りか確認する\r\nimport sys\r\nimport subprocess\r\n\r\n# ユーザーコードを実行\r\ndef test_user_code(user_code_path):\r\n    result = subprocess.run(\r\n        [\"python3\", user_code_path], \r\n        capture_output=True, text=True\r\n    )\r\n    # 期待される出力\r\n    expected_output = \"\"\"100 以下の双子素数のペア:\r\n(3, 5)\r\n(5, 7)\r\n(11, 13)\r\n(17, 19)\r\n(29, 31)\r\n(41, 43)\r\n(59, 61)\r\n(71, 73)\r\n\"\"\"\r\n \r\n    if result.stdout == expected_output:\r\n        # 出力が期待通りなら成功\r\n        return 0\r\n    else:\r\n        # 出力が期待通りでないなら失敗\r\n        print(\"実際の出力:\\n\", result.stdout)\r\n        return 1\r\n\r\n# 実行\r\nif __name__ == \"__main__\":\r\n    user_code_path = sys.argv[1]  # ユーザーコードのパスを受け取る\r\n    exit_code = test_user_code(user_code_path)\r\n    sys.exit(exit_code)','a1'),(12,'import sys\r\nimport subprocess\r\n\r\n# ユーザーコードを実行\r\ndef test_user_code(user_code_path):\r\n    result = subprocess.run(\r\n        [\"python3\", user_code_path], \r\n        capture_output=True, text=True\r\n    )\r\n    # 期待される出力（長さの確認）\r\n    expected_output = \"8\\n\"\r\n \r\n    if result.stdout == expected_output:\r\n        # 出力が期待通りなら成功\r\n        return 0\r\n    else:\r\n        # 出力が期待通りでないなら失敗\r\n        print(\"実際の出力:\\n\", result.stdout)\r\n        return 1\r\n\r\n# 実行\r\nif __name__ == \"__main__\":\r\n    user_code_path = sys.argv[1]  # ユーザーコードのパスを受け取る\r\n    exit_code = test_user_code(user_code_path)\r\n    sys.exit(exit_code)','b3'),(14,'# テストコード：ユーザーコードを実行し、出力が期待通りか確認する\r\nimport sys\r\nimport subprocess\r\n\r\n# ユーザーコードを実行\r\ndef test_user_code(user_code_path):\r\n    result = subprocess.run(\r\n        [\"python3\", user_code_path], \r\n        capture_output=True, text=True\r\n    )\r\n    # 期待される出力\r\n    expected_output = \"\"\"[12586269025, 7778742049, 4807526976, 2971215073, 1836311903, 1134903170, 701408733, 433494437, 267914296, 165580141, 102334155, 63245986, 39088169, 24157817, 14930352, 9227465, 5702887, 3524578, 2178309, 1346269, 832040, 514229, 317811, 196418, 121393, 75025, 46368, 28657, 17711, 10946, 6765, 4181, 2584, 1597, 987, 610, 377, 233, 144, 89, 55, 34, 21, 13, 8, 5, 3, 2, 1, 1]\r\n\"\"\"\r\n \r\n    if result.stdout == expected_output:\r\n        # 出力が期待通りなら成功\r\n        return 0\r\n    else:\r\n        # 出力が期待通りでないなら失敗\r\n        return 1\r\n\r\n# 実行\r\nif __name__ == \"__main__\":\r\n    user_code_path = sys.argv[1]  # ユーザーコードのパスを受け取る\r\n    exit_code = test_user_code(user_code_path)\r\n    sys.exit(exit_code)','a2'),(15,'import sys\r\nimport subprocess\r\n\r\n# ユーザーコードを実行\r\ndef test_user_code(user_code_path):\r\n    result = subprocess.run(\r\n        [\"python3\", user_code_path], \r\n        capture_output=True, text=True\r\n    )\r\n    # 期待される出力\r\n    expected_output = \"40\\n\"\r\n    \r\n    if result.stdout == expected_output:\r\n        # 出力が期待通りなら成功\r\n        return 0\r\n    else:\r\n        # 出力が期待通りでないなら失敗\r\n        print(\"実際の出力:\\n\", result.stdout)\r\n        return 1\r\n\r\n# 実行\r\nif __name__ == \"__main__\":\r\n    user_code_path = sys.argv[1]  # ユーザーコードのパスを受け取る\r\n    exit_code = test_user_code(user_code_path)\r\n    sys.exit(exit_code)','b4'),(16,'import sys\r\nimport subprocess\r\n\r\n# ユーザーコードを実行\r\ndef test_user_code(user_code_path):\r\n    result = subprocess.run(\r\n        [\"python3\", user_code_path], \r\n        capture_output=True, text=True\r\n    )\r\n    # 期待される出力\r\n    expected_output = \"\"\"[\'apple\', \'cherry\', \'grape\']\r\n\"\"\"\r\n \r\n    if result.stdout == expected_output:\r\n        # 出力が期待通りなら成功\r\n        return 0\r\n    else:\r\n        # 出力が期待通りでないなら失敗\r\n        print(\"実際の出力:\\n\", result.stdout)\r\n        return 1\r\n\r\n# 実行\r\nif __name__ == \"__main__\":\r\n    user_code_path = sys.argv[1]  # ユーザーコードのパスを受け取る\r\n    exit_code = test_user_code(user_code_path)\r\n    sys.exit(exit_code)','b5'),(20,'# テストコード：ユーザーコードを実行し、出力が期待通りか確認する\r\nimport sys\r\nimport subprocess\r\n\r\n# ユーザーコードを実行\r\ndef test_user_code(user_code_path):\r\n    result = subprocess.run(\r\n        [\"python3\", user_code_path], \r\n        capture_output=True, text=True\r\n    )\r\n    # 期待される出力（迷路の経路）\r\n    expected_output = \"\"\"経路:\r\n(0, 0)\r\n(1, 0)\r\n(2, 0)\r\n(2, 1)\r\n(2, 2)\r\n(2, 3)\r\n(2, 4)\r\n\"\"\"\r\n \r\n    if result.stdout == expected_output:\r\n        # 出力が期待通りなら成功\r\n        return 0\r\n    else:\r\n        # 出力が期待通りでないなら失敗\r\n        print(\"実際の出力:\\n\", result.stdout)\r\n        return 1\r\n\r\n# 実行\r\nif __name__ == \"__main__\":\r\n    user_code_path = sys.argv[1]  # ユーザーコードのパスを受け取る\r\n    exit_code = test_user_code(user_code_path)\r\n    sys.exit(exit_code)','a3'),(22,'import sys\r\nimport subprocess\r\n\r\n# ユーザーコードを実行\r\ndef test_user_code(user_code_path):\r\n    result = subprocess.run(\r\n        [\"python\", user_code_path],\r\n        capture_output=True, text=True\r\n    )\r\n\r\n    # 期待される出力\r\n    expected_output = \"15\\n5\\n50\\n2.0\\n\"  # 10 + 5, 10 - 5, 10 * 5 の結果をそれぞれ表示\r\n\r\n    # ユーザーコードの実行結果に応じて判定\r\n    if result.stdout == expected_output:\r\n        return 0  # 成功（期待通りの結果）\r\n    else:\r\n        return 1  # 失敗（期待される出力と一致しない）\r\n\r\n# 実行\r\nif __name__ == \"__main__\":\r\n    user_code_path = sys.argv[1]  # ユーザーコードのパスを受け取る\r\n    exit_code = test_user_code(user_code_path)\r\n    sys.exit(exit_code)','t2'),(23,'import sys\r\nimport subprocess\r\n\r\n# ユーザーコードを実行\r\ndef test_user_code(user_code_path):\r\n    result = subprocess.run(\r\n        [\"python3\", user_code_path],\r\n        capture_output=True, text=True\r\n    )\r\n\r\n    # 期待される出力（改行付き）\r\n    expected_output = \"4\\n\"\r\n\r\n    # ユーザーコードの実行結果に応じて判定\r\n    if result.stdout == expected_output:\r\n        return 0  # 成功（期待通りの結果）\r\n    else:\r\n        return 1  # 失敗（期待される出力と一致しない）\r\n\r\n# 実行\r\nif __name__ == \"__main__\":\r\n    user_code_path = sys.argv[1]  # ユーザーコードのパスを受け取る\r\n    exit_code = test_user_code(user_code_path)\r\n    sys.exit(exit_code)','t3'),(24,'import sys\r\nimport subprocess\r\n\r\n# ユーザーコードを実行\r\ndef test_user_code(user_code_path):\r\n    result = subprocess.run(\r\n        [\"python3\", user_code_path],\r\n        capture_output=True, text=True\r\n    )\r\n\r\n    # 期待される出力（改行付き）\r\n    expected_output = \"True\\nFalse\\nFalse\\nTrue\\nTrue\\nFalse\\n\"\r\n\r\n    # ユーザーコードの実行結果に応じて判定\r\n    if result.stdout == expected_output:\r\n        return 0  # 成功（期待通りの結果）\r\n    else:\r\n        return 1  # 失敗（期待される出力と一致しない）\r\n\r\n# 実行\r\nif __name__ == \"__main__\":\r\n    user_code_path = sys.argv[1]  # ユーザーコードのパスを受け取る\r\n    exit_code = test_user_code(user_code_path)\r\n    sys.exit(exit_code)','t4'),(26,'import sys\r\nimport subprocess\r\n\r\n# ユーザーコードを実行\r\ndef test_user_code(user_code_path):\r\n    result = subprocess.run(\r\n        [\"python3\", user_code_path],\r\n        capture_output=True, text=True\r\n    )\r\n\r\n    # 期待される出力（改行付き）\r\n    expected_output = \"hello\\n\"\r\n\r\n    # ユーザーコードの実行結果に応じて判定\r\n    if result.stdout == expected_output:\r\n        return 0  # 成功（期待通りの結果）\r\n    else:\r\n        return 1  # 失敗（期待される出力と一致しない）\r\n\r\n# 実行\r\nif __name__ == \"__main__\":\r\n    user_code_path = sys.argv[1]  # ユーザーコードのパスを受け取る\r\n    exit_code = test_user_code(user_code_path)\r\n    sys.exit(exit_code)','t5'),(27,'import sys\r\nimport subprocess\r\n\r\n# ユーザーコードを実行\r\ndef test_user_code(user_code_path):\r\n    result = subprocess.run(\r\n        [\"python3\", user_code_path],\r\n        capture_output=True, text=True\r\n    )\r\n\r\n    # 期待される出力（改行付き）\r\n    expected_output = \"こんにちは\\nこんにちは\\nこんにちは\\n\"\r\n\r\n    # ユーザーコードの実行結果に応じて判定\r\n    if result.stdout == expected_output:\r\n        return 0  # 成功（期待通りの結果）\r\n    else:\r\n        return 1  # 失敗（期待される出力と一致しない）\r\n\r\n# 実行\r\nif __name__ == \"__main__\":\r\n    user_code_path = sys.argv[1]  # ユーザーコードのパスを受け取る\r\n    exit_code = test_user_code(user_code_path)\r\n    sys.exit(exit_code)','b1'),(28,'import sys\r\nimport subprocess\r\n\r\n# ユーザーコードを実行\r\ndef test_user_code(user_code_path):\r\n    result = subprocess.run(\r\n        [\"python3\", user_code_path],\r\n        capture_output=True, text=True\r\n    )\r\n\r\n    # ユーザーコードの実行結果に応じて判定\r\n    output = result.stdout.strip()\r\n\r\n    # 期待される出力の候補\r\n    valid_outputs = {\"200\", \"20\", \"0\", \"20.0\"}\r\n\r\n    # 結果が期待される出力のいずれかと一致すれば成功\r\n    if output in valid_outputs:\r\n        return 0  # 成功\r\n    else:\r\n        return 1  # 失敗\r\n\r\n# 実行\r\nif __name__ == \"__main__\":\r\n    user_code_path = sys.argv[1]  # ユーザーコードのパスを受け取る\r\n    exit_code = test_user_code(user_code_path)\r\n    sys.exit(exit_code)','b6'),(29,'import sys\r\nimport subprocess\r\n\r\n# ユーザーコードを実行\r\ndef test_user_code(user_code_path):\r\n    result = subprocess.run(\r\n        [\"python3\", user_code_path],\r\n        capture_output=True, text=True\r\n    )\r\n\r\n    # 期待される出力\r\n    expected_output = \"\\n\".join(str(i) for i in range(10)) + \"\\n\"  # 0から9までを1行ずつ出力\r\n\r\n    # ユーザーコードの実行結果に応じて判定\r\n    if result.stdout == expected_output:\r\n        return 0  # 成功（期待通りの結果）\r\n    else:\r\n        return 1  # 失敗（期待される出力と一致しない）\r\n\r\n# 実行\r\nif __name__ == \"__main__\":\r\n    user_code_path = sys.argv[1]  # ユーザーコードのパスを受け取る\r\n    exit_code = test_user_code(user_code_path)\r\n    sys.exit(exit_code)','t6');
/*!40000 ALTER TABLE `answer_table` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (2,'admin'),(1,'user');
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
) ENGINE=InnoDB AUTO_INCREMENT=137 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,1,6),(7,1,7),(8,1,8),(9,1,9),(10,1,10),(11,1,11),(12,1,12),(13,1,13),(14,1,14),(15,1,15),(16,1,16),(17,1,17),(18,1,18),(19,1,19),(20,1,20),(21,1,21),(22,1,22),(23,1,23),(24,1,24),(25,1,25),(26,1,26),(27,1,27),(28,1,28),(29,1,29),(30,1,30),(31,1,31),(32,1,32),(33,1,33),(34,1,34),(35,1,35),(36,1,36),(37,1,37),(38,1,38),(39,1,39),(40,1,40),(41,1,41),(42,1,42),(43,1,43),(44,1,44),(45,1,45),(46,1,46),(47,1,47),(48,1,48),(49,1,49),(50,1,50),(51,1,51),(52,1,52),(53,1,53),(54,1,54),(55,1,55),(56,1,56),(57,1,57),(58,1,58),(59,1,59),(60,1,60),(61,1,61),(62,1,62),(63,1,63),(64,1,64),(65,1,65),(66,1,66),(67,1,67),(68,1,68),(69,2,1),(70,2,2),(71,2,3),(72,2,4),(73,2,5),(74,2,6),(75,2,7),(76,2,8),(77,2,9),(78,2,10),(79,2,11),(80,2,12),(81,2,13),(82,2,14),(83,2,15),(84,2,16),(85,2,17),(86,2,18),(87,2,19),(88,2,20),(89,2,21),(90,2,22),(91,2,23),(92,2,24),(93,2,25),(94,2,26),(95,2,27),(96,2,28),(97,2,29),(98,2,30),(99,2,31),(100,2,32),(101,2,33),(102,2,34),(103,2,35),(104,2,36),(105,2,37),(106,2,38),(107,2,39),(108,2,40),(109,2,41),(110,2,42),(111,2,43),(112,2,44),(113,2,45),(114,2,46),(115,2,47),(116,2,48),(117,2,49),(118,2,50),(119,2,51),(120,2,52),(121,2,53),(122,2,54),(123,2,55),(124,2,56),(125,2,57),(126,2,58),(127,2,59),(128,2,60),(129,2,61),(130,2,62),(131,2,63),(132,2,64),(133,2,65),(134,2,66),(135,2,67),(136,2,68);
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
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add association',7,'add_association'),(26,'Can change association',7,'change_association'),(27,'Can delete association',7,'delete_association'),(28,'Can view association',7,'view_association'),(29,'Can add code',8,'add_code'),(30,'Can change code',8,'change_code'),(31,'Can delete code',8,'delete_code'),(32,'Can view code',8,'view_code'),(33,'Can add nonce',9,'add_nonce'),(34,'Can change nonce',9,'change_nonce'),(35,'Can delete nonce',9,'delete_nonce'),(36,'Can view nonce',9,'view_nonce'),(37,'Can add user social auth',10,'add_usersocialauth'),(38,'Can change user social auth',10,'change_usersocialauth'),(39,'Can delete user social auth',10,'delete_usersocialauth'),(40,'Can view user social auth',10,'view_usersocialauth'),(41,'Can add partial',11,'add_partial'),(42,'Can change partial',11,'change_partial'),(43,'Can delete partial',11,'delete_partial'),(44,'Can view partial',11,'view_partial'),(45,'Can add test',12,'add_test'),(46,'Can change test',12,'change_test'),(47,'Can delete test',12,'delete_test'),(48,'Can view test',12,'view_test'),(49,'Can add file upload',13,'add_fileupload'),(50,'Can change file upload',13,'change_fileupload'),(51,'Can delete file upload',13,'delete_fileupload'),(52,'Can view file upload',13,'view_fileupload'),(53,'Can add kadai',14,'add_kadai'),(54,'Can change kadai',14,'change_kadai'),(55,'Can delete kadai',14,'delete_kadai'),(56,'Can view kadai',14,'view_kadai'),(57,'Can add material',15,'add_material'),(58,'Can change material',15,'change_material'),(59,'Can delete material',15,'delete_material'),(60,'Can view material',15,'view_material'),(61,'Can add answer',16,'add_answer'),(62,'Can change answer',16,'change_answer'),(63,'Can delete answer',16,'delete_answer'),(64,'Can view answer',16,'view_answer'),(65,'Can add 課題進捗',17,'add_kadaiprogress'),(66,'Can change 課題進捗',17,'change_kadaiprogress'),(67,'Can delete 課題進捗',17,'delete_kadaiprogress'),(68,'Can view 課題進捗',17,'view_kadaiprogress'),(69,'Can add image',18,'add_image'),(70,'Can change image',18,'change_image'),(71,'Can delete image',18,'delete_image'),(72,'Can view image',18,'view_image');
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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$09pKiHl0dScK6JhebVRiZ3$chIy6Lm6pYfsr97Ne86MghJRKtLi29/WXWXJH/lt3cg=','2024-12-18 07:29:50.171324',1,'000000','','','tejc210240@gmail.com',1,1,'2024-12-18 07:24:12.230816'),(2,'pbkdf2_sha256$870000$vchU7aDkMUBs8NFdxVOWM4$v9xGvWrDCSo8ySgFFQj8Qv9zTYcMdOBjjx1ySkLKMAk=','2025-02-15 04:55:48.994797',0,'test_user','','','',0,1,'2024-12-18 07:26:41.000000'),(4,'pbkdf2_sha256$870000$BY2wo0jXrvs8VstExnCIV4$j3fwb+g4KE0s6HFemrt+4BfMJhDSONVjm4l+nOYDac8=','2025-02-15 04:35:47.181736',0,'test_admin','','','',0,1,'2024-12-18 07:30:33.000000'),(6,'pbkdf2_sha256$870000$YMcEy3KRstoPu3mR0gVISV$5ZTWJbbvU/9GBI3wHzASRYJ6J2djGgl2EL/18GGqdoU=','2025-02-15 05:28:49.059152',0,'210011','','','',0,1,'2025-02-13 03:56:34.314109'),(7,'pbkdf2_sha256$870000$3n5TKxynwAJsISU76tB5rq$KzHikKnmTvoCB0xJp4Ejakb6AuJgSZJAIjJdxV6dppE=','2025-02-13 07:12:31.119524',0,'210275','','','',0,1,'2025-02-13 04:02:25.172524'),(8,'pbkdf2_sha256$870000$Y5UguVdc5PzMGLvmmJUf30$pdaCXGyy7mNvdgDdgK7jdNSsX6vrikc0XE43sdRMovc=','2025-02-14 06:20:44.536126',0,'user210011','','','',0,1,'2025-02-13 04:17:55.566278'),(9,'pbkdf2_sha256$870000$U8mRYr6u3Duq85KOXbNtB7$Cc2re6O65SDKOdaczJ9lkmKlBlsGp1bNNIwD754nku8=','2025-02-13 06:01:02.074159',0,'loop0919','','','',0,1,'2025-02-13 06:00:56.196021'),(10,'pbkdf2_sha256$870000$2vEKgw8lNR3ztCxkEGTNNl$31sD33YU2Mn4XkHu4vQsTkBs52fIeSUMjajZpTn/RGg=','2025-02-15 02:56:01.933942',0,'loginuser01','','','',0,1,'2025-02-14 00:20:23.022446'),(11,'pbkdf2_sha256$870000$d15ZJZdupHDp40UFZ9y23P$IPPHy8dhLhHjAjoikF7eu6uXGZerR6TbsxMwEOpsutY=','2025-02-15 05:36:29.980075',0,'loginuser02','','','',0,1,'2025-02-14 00:21:12.542310'),(12,'pbkdf2_sha256$870000$htynyvex3Sb7vaZgWdup2u$heXuyItl/lkcpMf7KB7eSntfUTWAsstKxbm3XgfSn5k=','2025-02-15 05:36:20.976647',0,'loginuser03','','','',0,1,'2025-02-14 00:22:24.669172'),(13,'pbkdf2_sha256$870000$Y11wW0R0b1ULnnwmyJteI8$tQx9AuS0sGPDWufserwnUMK90Vztha9YgWns5Mbdrmk=','2025-02-15 05:38:13.611711',0,'loginuser04','','','',0,1,'2025-02-14 00:26:10.594445'),(14,'pbkdf2_sha256$870000$OIo5fzFb8UJbySAAmzXwLH$be0RQ5UGTQh9Ipmpw39GZnA5NZDGZDNb4LRdL98ZN5M=','2025-02-14 00:51:18.080588',0,'210889','','','',0,1,'2025-02-14 00:50:57.342923'),(15,'pbkdf2_sha256$870000$Hv1RohHVxRcFhxMzu2zMjf$kh9HB4vIE/SJu7WTfXiwjSvtp0o/jTN/cXjbgDJ1dlw=','2025-02-14 03:47:46.158161',0,'stu2005','','','',0,1,'2025-02-14 03:47:25.372286'),(16,'pbkdf2_sha256$870000$IRMyh9peSoV8qfX1P6JCPw$k4GomVgbomDIxyLLbxtveHZCKXcofdH7rUQdxp/howA=','2025-02-14 05:00:33.006455',0,'shinohiroyuki123','','','',0,1,'2025-02-14 04:15:06.771343'),(17,'pbkdf2_sha256$870000$MgLE91fBkh2XTTMMf8yTaT$ymQpjz5eJGbjqbMx0+HRUsrfKrzPN1mGYmccqmXfRO4=','2025-02-14 04:31:22.808800',0,'hoshino','','','',0,1,'2025-02-14 04:30:55.132556'),(18,'pbkdf2_sha256$870000$WQdfl8SN8eH4VvGsv8FZgA$yWkQk5W3aNoT2RWUNmAr/18zlLrhNmZFLEB3vS9cKlM=','2025-02-14 05:14:05.980257',0,'ichi','','','',0,1,'2025-02-14 05:13:50.528816'),(19,'pbkdf2_sha256$870000$1leI9mRuqUXE3BYTujQOBW$lccppcG16OKxsSRdB4IQukxjteCCwCAhqaAWXG3a2xc=','2025-02-15 04:31:07.807821',0,'123qqq','','','',0,1,'2025-02-15 03:17:25.293764'),(20,'pbkdf2_sha256$870000$DDROmATv5C4rfwtpqC4frO$efy7sV0OqdCI9b7tpzCtzRNyqRiRfR61oV+u3DTdsgE=','2025-02-15 04:30:08.453767',0,'123456','','','',0,1,'2025-02-15 04:30:07.737080');
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
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (1,2,1),(3,4,2),(6,6,2),(8,7,2),(9,8,1),(12,9,1),(13,10,1),(14,11,1),(15,12,1),(16,13,1),(17,14,1),(18,15,1),(19,16,1),(20,17,1),(21,18,1),(22,19,1),(23,20,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-12-18 07:25:52.017607','1','user',1,'[{\"added\": {}}]',3,1),(2,'2024-12-18 07:25:59.383959','2','admin',1,'[{\"added\": {}}]',3,1),(3,'2024-12-18 07:26:41.701960','2','test_user',1,'[{\"added\": {}}]',4,1),(4,'2024-12-18 07:26:59.506819','2','test_user',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(5,'2024-12-18 07:27:57.963882','3','test_admin',1,'[{\"added\": {}}]',4,1),(6,'2024-12-18 07:28:04.812545','3','test_admin',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(7,'2024-12-18 07:30:06.915009','3','test_admin',3,'',4,1),(8,'2024-12-18 07:30:34.074807','4','test_admin',1,'[{\"added\": {}}]',4,1),(9,'2024-12-18 07:30:41.587394','4','test_admin',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(16,'AdminApp','answer'),(13,'AdminApp','fileupload'),(18,'AdminApp','image'),(14,'AdminApp','kadai'),(17,'AdminApp','kadaiprogress'),(15,'AdminApp','material'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'social_django','association'),(8,'social_django','code'),(9,'social_django','nonce'),(11,'social_django','partial'),(10,'social_django','usersocialauth'),(12,'UserApp','test');
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
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-12-18 07:17:34.318016'),(2,'auth','0001_initial','2024-12-18 07:17:35.189909'),(3,'AdminApp','0001_initial','2024-12-18 07:17:35.401627'),(4,'AdminApp','0002_material_material_id_alter_kadai_category_and_more','2024-12-18 07:17:35.686537'),(5,'AdminApp','0003_remove_material_id_alter_material_material_id','2024-12-18 07:17:35.914495'),(6,'UserApp','0001_initial','2024-12-18 07:17:36.056190'),(7,'admin','0001_initial','2024-12-18 07:17:36.274375'),(8,'admin','0002_logentry_remove_auto_add','2024-12-18 07:17:36.286649'),(9,'admin','0003_logentry_add_action_flag_choices','2024-12-18 07:17:36.299609'),(10,'contenttypes','0002_remove_content_type_name','2024-12-18 07:17:36.397646'),(11,'auth','0002_alter_permission_name_max_length','2024-12-18 07:17:36.490061'),(12,'auth','0003_alter_user_email_max_length','2024-12-18 07:17:36.523837'),(13,'auth','0004_alter_user_username_opts','2024-12-18 07:17:36.535951'),(14,'auth','0005_alter_user_last_login_null','2024-12-18 07:17:36.607958'),(15,'auth','0006_require_contenttypes_0002','2024-12-18 07:17:36.614693'),(16,'auth','0007_alter_validators_add_error_messages','2024-12-18 07:17:36.627612'),(17,'auth','0008_alter_user_username_max_length','2024-12-18 07:17:36.722333'),(18,'auth','0009_alter_user_last_name_max_length','2024-12-18 07:17:36.821495'),(19,'auth','0010_alter_group_name_max_length','2024-12-18 07:17:36.854685'),(20,'auth','0011_update_proxy_permissions','2024-12-18 07:17:36.870481'),(21,'auth','0012_alter_user_first_name_max_length','2024-12-18 07:17:36.957868'),(22,'sessions','0001_initial','2024-12-18 07:17:37.036498'),(23,'default','0001_initial','2024-12-18 07:17:37.365865'),(24,'social_auth','0001_initial','2024-12-18 07:17:37.371758'),(25,'default','0002_add_related_name','2024-12-18 07:17:37.386620'),(26,'social_auth','0002_add_related_name','2024-12-18 07:17:37.392755'),(27,'default','0003_alter_email_max_length','2024-12-18 07:17:37.413028'),(28,'social_auth','0003_alter_email_max_length','2024-12-18 07:17:37.419824'),(29,'default','0004_auto_20160423_0400','2024-12-18 07:17:37.432710'),(30,'social_auth','0004_auto_20160423_0400','2024-12-18 07:17:37.439263'),(31,'social_auth','0005_auto_20160727_2333','2024-12-18 07:17:37.472215'),(32,'social_django','0006_partial','2024-12-18 07:17:37.533725'),(33,'social_django','0007_code_timestamp','2024-12-18 07:17:37.597672'),(34,'social_django','0008_partial_timestamp','2024-12-18 07:17:37.667445'),(35,'social_django','0009_auto_20191118_0520','2024-12-18 07:17:37.759243'),(36,'social_django','0010_uid_db_index','2024-12-18 07:17:37.793573'),(37,'social_django','0011_alter_id_fields','2024-12-18 07:17:38.247234'),(38,'social_django','0012_usersocialauth_extra_data_new','2024-12-18 07:17:38.493114'),(39,'social_django','0013_migrate_extra_data','2024-12-18 07:17:38.517755'),(40,'social_django','0014_remove_usersocialauth_extra_data','2024-12-18 07:17:38.576288'),(41,'social_django','0015_rename_extra_data_new_usersocialauth_extra_data','2024-12-18 07:17:38.633657'),(42,'social_django','0016_alter_usersocialauth_extra_data','2024-12-18 07:17:38.646810'),(43,'social_django','0003_alter_email_max_length','2024-12-18 07:17:38.657680'),(44,'social_django','0005_auto_20160727_2333','2024-12-18 07:17:38.665800'),(45,'social_django','0002_add_related_name','2024-12-18 07:17:38.672148'),(46,'social_django','0004_auto_20160423_0400','2024-12-18 07:17:38.678938'),(47,'social_django','0001_initial','2024-12-18 07:17:38.685158'),(48,'AdminApp','0004_image','2025-01-17 05:42:52.926316');
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
INSERT INTO `django_session` VALUES ('0coazbbg4c35d0s4wwsqcvhyygdvtxrh','.eJxVjEsOwjAMBe-SNYpip6kbluw5Q-TELi2gRupnhbg7VOoCtm9m3ssk3tYhbYvOaRRzNmhOv1vm8tBpB3Ln6VZtqdM6j9nuij3oYq9V9Hk53L-DgZfhW1MrHaBrisvK6EoPWER86AEKdQQRNYJ3KuB6paBNQwEYvYtIrc-deX8A03M2_w:1ti6RI:co4abqGR1rF64HPnpNesM3AV0dPMtb97XEu7HjMIqvc','2025-02-26 06:41:40.055977'),('2jsrmwninyiqmasbjsju0ggqjn7zypyu','.eJxVjEEOwiAQRe_C2hBaGCgu3XsGMgODVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwJ3EWVpx-N8L44LqDdMd6azK2ui4zyV2RB-3y2hI_L4f7d1Cwl2_tJrTam3GEqJEt2cyKokdg68BziuwIabA5Aw9kDIEGPynQTrHOBsX7A_U2OEE:1tiQQB:v5RYaEH6qbTWlNt4sql2KqhVT4VZpKzL95LiC2mzYB8','2025-02-27 04:01:51.065296'),('3h1wcs9pnkhn7tc8uqtiduu74zyicf8r','.eJxVjDsOwyAQBe9CHSHDYj4p0_sMiIUlOIlAMnYV5e6xJRdJ-2bmvZkP21r81mnxc2JXJtnld8MQn1QPkB6h3huPra7LjPxQ-Ek7n1qi1-10_w5K6GWvIUogjaNygoaE2QhLTkAEhKyytqAhmIRW4YDoUKPMlsSYEfbCOsM-X-aMN-A:1tXsrG:KMuqGtCgsDbhhCOH6I0C6ExeY-s43dLxQuLUI1QNDtw','2025-01-29 02:10:14.321025'),('3lxn1nkagtsqrgy44s2qglkavbj0n0hn','.eJxVjMsOwiAQRf-FtSEwPAou3fsNZIBBqgaS0q6M_65NutDtPefcFwu4rTVsg5YwZ3Zmmp1-t4jpQW0H-Y7t1nnqbV3myHeFH3Twa8_0vBzu30HFUb-1IBctTik5R0KQjsZEtFJJ4SMYT1mCTlYiFEClVSGvPQg0kyoJFEr2_gDh1TeJ:1ti54n:TcrIH8k8gCFjWGvGVq44737ii5vLdbgB427vyp4kGJA','2025-02-26 05:14:21.834256'),('43b0o5jwkcq1q3pm665rtjdcqixkjaqm','.eJxVjMsOwiAQRf-FtSEwPAou3fsNZIBBqgaS0q6M_65NutDtPefcFwu4rTVsg5YwZ3Zmmp1-t4jpQW0H-Y7t1nnqbV3myHeFH3Twa8_0vBzu30HFUb-1IBctTik5R0KQjsZEtFJJ4SMYT1mCTlYiFEClVSGvPQg0kyoJFEr2_gDh1TeJ:1ti6I2:95q7Gav2McVPU92T6IyoJFWCRcpXR082TPVZEXVJoxQ','2025-02-26 06:32:06.294197'),('4sxg4afksotoqsdqjvzqz7dl211x8nsv','.eJxVjMsOwiAQRf-FtSEwPAou3fsNZIBBqgaS0q6M_65NutDtPefcFwu4rTVsg5YwZ3Zmmp1-t4jpQW0H-Y7t1nnqbV3myHeFH3Twa8_0vBzu30HFUb-1IBctTik5R0KQjsZEtFJJ4SMYT1mCTlYiFEClVSGvPQg0kyoJFEr2_gDh1TeJ:1ti4yv:Wel0zi2bwCWodQfyLIc-TEd3FL415nyJWyvIiMfxCpk','2025-02-26 05:08:17.459427'),('5yljpcp0jedmfbo2pojkuow5rgejc9ye','.eJxVjDsOwyAQBe9CHSHDYj4p0_sMiIUlOIlAMnYV5e6xJRdJ-2bmvZkP21r81mnxc2JXJtnld8MQn1QPkB6h3huPra7LjPxQ-Ek7n1qi1-10_w5K6GWvIUogjaNygoaE2QhLTkAEhKyytqAhmIRW4YDoUKPMlsSYEfbCOsM-X-aMN-A:1tYgDs:ioUs06X2cyNbrfSiuX5OR-MVaor2fb0q8XtppVyIc-k','2025-01-31 06:52:52.968836'),('5zcqf82o3ibg9s8ped2e61874dbdb8bn','.eJxVjDsOwyAQRO9CHaE1sBhSpvcZrIWF4CQCyZ8qyt1jSy6Scua9mbcYaVvLuC1pHicWV2HE5bcLFJ-pHoAfVO9NxlbXeQryUORJFzk0Tq_b6f4dFFrKvtbgXPZOMfQQATEFxdmisQygHfZ7RlJRdeAADevOAzFSJh8tJjLi8wW9Czcz:1tW4nN:6T_ZzBBoBohUt0hShNWjjyGuz7VqFn1cm-F1AEpRM6U','2025-01-24 02:30:45.250269'),('8vcmwflnr27jkgh6j3a1yp9no7mrw6un','.eJxVjEsOwjAMBe-SNYpip6kbluw5Q-TELi2gRupnhbg7VOoCtm9m3ssk3tYhbYvOaRRzNmhOv1vm8tBpB3Ln6VZtqdM6j9nuij3oYq9V9Hk53L-DgZfhW1MrHaBrisvK6EoPWER86AEKdQQRNYJ3KuB6paBNQwEYvYtIrc-deX8A03M2_w:1ti80L:WkDyQLJdaRvl6cn7VIkyEZNLRCbM_K2GE5lnaCUch0Q','2025-02-26 08:21:57.871426'),('97mwo1c6z6w0n8ncpe8j4mie1c1yy9k4','.eJxVjDsOwyAQBe9CHSHDYj4p0_sMiIUlOIlAMnYV5e6xJRdJ-2bmvZkP21r81mnxc2JXJtnld8MQn1QPkB6h3huPra7LjPxQ-Ek7n1qi1-10_w5K6GWvIUogjaNygoaE2QhLTkAEhKyytqAhmIRW4YDoUKPMlsSYEfbCOsM-X-aMN-A:1tXuM5:o-l05FLOlotFJG2FMEk7qFkuUHfW_fWwYNtsC27RYHg','2025-01-29 03:46:09.569915'),('etpc218xslm2lmiqauqz8n055ehqr55x','.eJxVjEsOwjAMBe-SNYpip6kbluw5Q-TELi2gRupnhbg7VOoCtm9m3ssk3tYhbYvOaRRzNmhOv1vm8tBpB3Ln6VZtqdM6j9nuij3oYq9V9Hk53L-DgZfhW1MrHaBrisvK6EoPWER86AEKdQQRNYJ3KuB6paBNQwEYvYtIrc-deX8A03M2_w:1ti7Zt:1iKL1dMOqX1WhccNBIX52XyDL7BOw3UJqaP3UvUKu18','2025-02-26 07:54:37.424866'),('ez8gx1iu2w4fbj8dj45rj0qgpiexkc7q','.eJxVjMsOwiAQRf-FtSEwPAou3fsNZIBBqgaS0q6M_65NutDtPefcFwu4rTVsg5YwZ3Zmmp1-t4jpQW0H-Y7t1nnqbV3myHeFH3Twa8_0vBzu30HFUb-1IBctTik5R0KQjsZEtFJJ4SMYT1mCTlYiFEClVSGvPQg0kyoJFEr2_gDh1TeJ:1ti77h:elF6oKND5zCt_xkSAz_NPf6TrjIaEq8zdyxJQT03du8','2025-02-26 07:25:29.126282'),('f6bt852fdxd7up9psharlfjh345pssm6','.eJxVjDsOwyAQRO9CHaE1sBhSpvcZrIWF4CQCyZ8qyt1jSy6Scua9mbcYaVvLuC1pHicWV2HE5bcLFJ-pHoAfVO9NxlbXeQryUORJFzk0Tq_b6f4dFFrKvtbgXPZOMfQQATEFxdmisQygHfZ7RlJRdeAADevOAzFSJh8tJjLi8wW9Czcz:1tW7s0:OCDLjFbEZHdO6pdU0Yg6uVpdJHCRom7q0kU-fylBiMU','2025-01-24 05:47:44.591715'),('fb4twu2n8ralopas7847pffnwkehru6r','.eJxVjDsOwyAQRO9CHaE1sBhSpvcZrIWF4CQCyZ8qyt1jSy6Scua9mbcYaVvLuC1pHicWV2HE5bcLFJ-pHoAfVO9NxlbXeQryUORJFzk0Tq_b6f4dFFrKvtbgXPZOMfQQATEFxdmisQygHfZ7RlJRdeAADevOAzFSJh8tJjLi8wW9Czcz:1tNoXs:XP1rw_GKf-1kes4c5LEyKXBl6mvYbSHf_ot9CKliBks','2025-01-01 07:32:36.933092'),('g9ufcka2wue79og75adkcqqwvicns3yr','.eJxVjMsOwiAQRf-FtSEwPAou3fsNZIBBqgaS0q6M_65NutDtPefcFwu4rTVsg5YwZ3Zmmp1-t4jpQW0H-Y7t1nnqbV3myHeFH3Twa8_0vBzu30HFUb-1IBctTik5R0KQjsZEtFJJ4SMYT1mCTlYiFEClVSGvPQg0kyoJFEr2_gDh1TeJ:1tiQQS:pe1lhcQhWnZKxEWz_kDSJInBMTUz8TlMhCI6bDRYCtY','2025-02-27 04:02:08.113930'),('gc6qxi32522ss22buh9rlfvpzhm3lz78','.eJxVjDsOwyAQBe9CHSHDYj4p0_sMiIUlOIlAMnYV5e6xJRdJ-2bmvZkP21r81mnxc2JXJtnld8MQn1QPkB6h3huPra7LjPxQ-Ek7n1qi1-10_w5K6GWvIUogjaNygoaE2QhLTkAEhKyytqAhmIRW4YDoUKPMlsSYEfbCOsM-X-aMN-A:1tYfAM:A6FUeYOLFu25dYeNs8bIgqK-AO1M6xnkKrSI-74yRTU','2025-01-31 05:45:10.467662'),('gm95lzqxbxp6kj3dxj781n872dz90e9h','.eJxVjDsOwyAQRO9CHaE1sBhSpvcZrIWF4CQCyZ8qyt1jSy6Scua9mbcYaVvLuC1pHicWV2HE5bcLFJ-pHoAfVO9NxlbXeQryUORJFzk0Tq_b6f4dFFrKvtbgXPZOMfQQATEFxdmisQygHfZ7RlJRdeAADevOAzFSJh8tJjLi8wW9Czcz:1tYbuZ:BLMdC6aWzPO9KuCMqrBLAz3uO-pZPO3I30e211k4IFQ','2025-01-31 02:16:39.733953'),('iu6aby5gso9mcicrbcqxcfj42rgun4xl','.eJxVjEsOwjAMBe-SNYpip6kbluw5Q-TELi2gRupnhbg7VOoCtm9m3ssk3tYhbYvOaRRzNmhOv1vm8tBpB3Ln6VZtqdM6j9nuij3oYq9V9Hk53L-DgZfhW1MrHaBrisvK6EoPWER86AEKdQQRNYJ3KuB6paBNQwEYvYtIrc-deX8A03M2_w:1tbCa7:fj1nTuCamYPcc37KaXAnz7DedwLCXkt_hj0GCdYpabo','2025-02-07 05:50:15.427072'),('iy2rtps65205ju2ekzvds1lzpvau8gqd','.eJxVjDsOwyAQBe9CHSHDYj4p0_sMiIUlOIlAMnYV5e6xJRdJ-2bmvZkP21r81mnxc2JXJtnld8MQn1QPkB6h3huPra7LjPxQ-Ek7n1qi1-10_w5K6GWvIUogjaNygoaE2QhLTkAEhKyytqAhmIRW4YDoUKPMlsSYEfbCOsM-X-aMN-A:1tYc4X:WdEIeSe6sCzscRK8FzVGWfbQ-fgOdk0U0HPbV3WLbjg','2025-01-31 02:26:57.746432'),('izj76nsiz5wcnsxrflwgtl7aqz1j1shg','.eJxVjEsOwjAMBe-SNYpip6kbluw5Q-TELi2gRupnhbg7VOoCtm9m3ssk3tYhbYvOaRRzNmhOv1vm8tBpB3Ln6VZtqdM6j9nuij3oYq9V9Hk53L-DgZfhW1MrHaBrisvK6EoPWER86AEKdQQRNYJ3KuB6paBNQwEYvYtIrc-deX8A03M2_w:1thNEP:voitz-Al5mAKTgZK3Q8w8u328twL8G8T0NNagiCHasQ','2025-02-24 06:25:21.000816'),('k317x75iegw5staq0e46o5oyfk7t6iu0','.eJxVjMsOwiAQRf-FtSEwPAou3fsNZIBBqgaS0q6M_65NutDtPefcFwu4rTVsg5YwZ3Zmmp1-t4jpQW0H-Y7t1nnqbV3myHeFH3Twa8_0vBzu30HFUb-1IBctTik5R0KQjsZEtFJJ4SMYT1mCTlYiFEClVSGvPQg0kyoJFEr2_gDh1TeJ:1teoE4:bpocYe7O-_rfgCau2fecm3ITbufZdaTnO0a2ZnNEgAg','2025-02-17 04:38:24.419299'),('lw4q0v9dtlr9bq3ss68hp9owpmookplh','.eJxVjMsOwiAQRf-FtSGCw8ul-35DMwyDVA0kpV0Z_92QdKHbe865bzHjvpV577zOSxJXoUCcfseI9OQ6SHpgvTdJrW7rEuVQ5EG7nFri1-1w_w4K9jJqG4MmkwnQe62YCX3g5LwG5VQGtJjgzAEM2ai9JXPRGdGRc0AusPh8AR2JOHw:1tijvK:ht29ORsAnfHu26MacUYt7dMPwIEnPuITur3WsvjEcW8','2025-02-28 00:51:18.086775'),('lzdlawapl3atlpo509z7j9ylz3xplryw','.eJxVjDsOwyAQRO9CHaE1sBhSpvcZrIWF4CQCyZ8qyt1jSy6Scua9mbcYaVvLuC1pHicWV2HE5bcLFJ-pHoAfVO9NxlbXeQryUORJFzk0Tq_b6f4dFFrKvtbgXPZOMfQQATEFxdmisQygHfZ7RlJRdeAADevOAzFSJh8tJjLi8wW9Czcz:1tVOus:2vk4tPWm29XRy5GkheCdiLhzCGS7QOQA5jVGkPcXj_I','2025-01-22 05:47:42.750036'),('mjjmn3kt9aeouo3lpqqikbt3e45l0s0t','.eJxVjDsOwyAQBe9CHSHDYj4p0_sMiIUlOIlAMnYV5e6xJRdJ-2bmvZkP21r81mnxc2JXJtnld8MQn1QPkB6h3huPra7LjPxQ-Ek7n1qi1-10_w5K6GWvIUogjaNygoaE2QhLTkAEhKyytqAhmIRW4YDoUKPMlsSYEfbCOsM-X-aMN-A:1tOSHF:p-NnvdbETr1DqCFqZCbe6l_rDYF1KOwx-o0h0FKOchs','2025-01-03 01:58:05.534573'),('ns41b3e3zqut82q10ys2mxxf5oanmlb5','.eJxVjMsOwiAQRf-FtSHlPbh07zcQYAapGkhKuzL-uzbpQrf3nHNfLMRtrWEbtIQZ2Zl5dvrdUswPajvAe2y3znNv6zInviv8oINfO9Lzcrh_BzWO-q11iaJkBUkmPdlCXoADQQqdyiQLOZwQrNAGAGxS4LM2kQxCdkkq59n7A-6kN8w:1tiSHW:MBp0R37IToxKGhO-HnRq0XcF7QoB0LVb4nVj6yqQPIo','2025-02-27 06:01:02.080262'),('pzrh0e9q2szllvvp31b8htak5lj0nhel','.eJxVjDsOwyAQBe9CHSHDYj4p0_sMiIUlOIlAMnYV5e6xJRdJ-2bmvZkP21r81mnxc2JXJtnld8MQn1QPkB6h3huPra7LjPxQ-Ek7n1qi1-10_w5K6GWvIUogjaNygoaE2QhLTkAEhKyytqAhmIRW4YDoUKPMlsSYEfbCOsM-X-aMN-A:1tXxqU:Pml-XetvNqFqjSi-QMW0G378r-YIWOIJbeh5D2kk4FA','2025-01-29 07:29:46.808090'),('q4sqovrluj29bbspd93umlmrh0pyrzuw','.eJxVjMsOwiAQRf-FtSFCh0dduu83EJgZpGogKe3K-O_apAvd3nPOfYkQt7WErfMSZhIXoQZx-h1TxAfXndA91luT2Oq6zEnuijxol1Mjfl4P9--gxF6-NViNVkc9JIPKaEbwDqNTiASMloEgD1aRppFHZ4xPWSnndLaZPJydeH8ACsg4EA:1tj7ql:h7uqMNW_0_v20EDV5cGkb8Ha1PDaLQEqn4Zzb_1X_2Q','2025-03-01 02:24:11.577663'),('q7oxxo6af642f8lgu8wp6mfu354t8ass','.eJxVjDsOwyAQBe9CHSHDYj4p0_sMiIUlOIlAMnYV5e6xJRdJ-2bmvZkP21r81mnxc2JXJtnld8MQn1QPkB6h3huPra7LjPxQ-Ek7n1qi1-10_w5K6GWvIUogjaNygoaE2QhLTkAEhKyytqAhmIRW4YDoUKPMlsSYEfbCOsM-X-aMN-A:1tW82U:dZpid5bvKEGogjw9BxGgcznre95LnfZm0PgWlXy36qo','2025-01-24 05:58:34.736200'),('qozkmnaim86iy0a8pbz1ea5udx7lz5jt','.eJxVjEsOwjAMBe-SNYpip6kbluw5Q-TELi2gRupnhbg7VOoCtm9m3ssk3tYhbYvOaRRzNmhOv1vm8tBpB3Ln6VZtqdM6j9nuij3oYq9V9Hk53L-DgZfhW1MrHaBrisvK6EoPWER86AEKdQQRNYJ3KuB6paBNQwEYvYtIrc-deX8A03M2_w:1tiTOm:xAcEDKBMPAJM6FYsFZF0ds69cKGT_wGdqoHMz2d_tXM','2025-02-27 07:12:36.224964'),('rzup7aoiw2wjpez6llwj49v6ws7dq5fs','.eJxVjEsOwjAMBe-SNYpip6kbluw5Q-TELi2gRupnhbg7VOoCtm9m3ssk3tYhbYvOaRRzNmhOv1vm8tBpB3Ln6VZtqdM6j9nuij3oYq9V9Hk53L-DgZfhW1MrHaBrisvK6EoPWER86AEKdQQRNYJ3KuB6paBNQwEYvYtIrc-deX8A03M2_w:1thOSv:-IwhTbCj2FRNFrAFxFFX_O8lTMNq2aHHmht7ZjkBUeU','2025-02-24 07:44:25.762162'),('thewx2ymr2v98hav6o9g8ufrnvgjq20j','.eJxVjEsOwjAMBe-SNYpip6kbluw5Q-TELi2gRupnhbg7VOoCtm9m3ssk3tYhbYvOaRRzNmhOv1vm8tBpB3Ln6VZtqdM6j9nuij3oYq9V9Hk53L-DgZfhW1MrHaBrisvK6EoPWER86AEKdQQRNYJ3KuB6paBNQwEYvYtIrc-deX8A03M2_w:1tdhr3:cF7hQO5kJlqNYU5cpc7P5UU43UD2OQuPxZ9YhdqcTiA','2025-02-14 03:38:05.131978'),('vlsagns31yvyn28leaxut2yok5k5d15e','.eJxVjDsOwyAQRO9CHaE1sBhSpvcZrIWF4CQCyZ8qyt1jSy6Scua9mbcYaVvLuC1pHicWV2HE5bcLFJ-pHoAfVO9NxlbXeQryUORJFzk0Tq_b6f4dFFrKvtbgXPZOMfQQATEFxdmisQygHfZ7RlJRdeAADevOAzFSJh8tJjLi8wW9Czcz:1ta3gH:2XcQZQ8RyN_-Hjhs65dADmSXidNwboz-hkUUFWHJVoE','2025-02-04 02:07:53.290204'),('vmk97k2qx2u8fdcxr6vuuc5affthqqn3','.eJxVjEsOwjAMBe-SNYpip6kbluw5Q-TELi2gRupnhbg7VOoCtm9m3ssk3tYhbYvOaRRzNmhOv1vm8tBpB3Ln6VZtqdM6j9nuij3oYq9V9Hk53L-DgZfhW1MrHaBrisvK6EoPWER86AEKdQQRNYJ3KuB6paBNQwEYvYtIrc-deX8A03M2_w:1tdhy7:QBftIyWRNL69HNJAsCbgL8kghQDdJu48GcC72KN-wz0','2025-02-14 03:45:23.902789'),('wrn5nebeq850lmqtjhmm37k58sh3undo','.eJxVjDsOwyAQBe9CHSHDYj4p0_sMiIUlOIlAMnYV5e6xJRdJ-2bmvZkP21r81mnxc2JXJtnld8MQn1QPkB6h3huPra7LjPxQ-Ek7n1qi1-10_w5K6GWvIUogjaNygoaE2QhLTkAEhKyytqAhmIRW4YDoUKPMlsSYEfbCOsM-X-aMN-A:1tVOUq:yB7JxT3eQU3WsCZ_x4-jpKxY3rM0IuSBuf3hCJGQUnQ','2025-01-22 05:20:48.786996'),('xaywabwn6n3lit8nv0uybil741o9rkk3','.eJxVjEsOwjAMBe-SNYpip6kbluw5Q-TELi2gRupnhbg7VOoCtm9m3ssk3tYhbYvOaRRzNmhOv1vm8tBpB3Ln6VZtqdM6j9nuij3oYq9V9Hk53L-DgZfhW1MrHaBrisvK6EoPWER86AEKdQQRNYJ3KuB6paBNQwEYvYtIrc-deX8A03M2_w:1tdi8Q:yCug5XQDgaGugL-wlVEchldnnJZZRB-OVU169X3RyBM','2025-02-14 03:56:02.005285'),('xl4lehgr7efcm2mehwgr0l7c0rz8m2jy','.eJxVjEsOwjAMBe-SNYpip6kbluw5Q-TELi2gRupnhbg7VOoCtm9m3ssk3tYhbYvOaRRzNmhOv1vm8tBpB3Ln6VZtqdM6j9nuij3oYq9V9Hk53L-DgZfhW1MrHaBrisvK6EoPWER86AEKdQQRNYJ3KuB6paBNQwEYvYtIrc-deX8A03M2_w:1tbCXS:47ZC_bcokGI3RtphsYx8T7UJhlgf8fRvlVAnS3B0OUI','2025-02-07 05:47:30.559809'),('yf18swavc7s406yw86277iiryda4q5m7','.eJxVjEsOwjAMBe-SNYpip6kbluw5Q-TELi2gRupnhbg7VOoCtm9m3ssk3tYhbYvOaRRzNmhOv1vm8tBpB3Ln6VZtqdM6j9nuij3oYq9V9Hk53L-DgZfhW1MrHaBrisvK6EoPWER86AEKdQQRNYJ3KuB6paBNQwEYvYtIrc-deX8A03M2_w:1tdhrn:1kaakceOdevE7hLukP0Ku7-noYBxkjCF12Wb7H3iLYE','2025-02-14 03:38:51.228995'),('ywlxht5oy20vn1oeny886070d6vhs8ua','.eJxVjDsOwyAQBe9CHSHDYj4p0_sMiIUlOIlAMnYV5e6xJRdJ-2bmvZkP21r81mnxc2JXJtnld8MQn1QPkB6h3huPra7LjPxQ-Ek7n1qi1-10_w5K6GWvIUogjaNygoaE2QhLTkAEhKyytqAhmIRW4YDoUKPMlsSYEfbCOsM-X-aMN-A:1tXt3c:XfMdLMoK2oSrGIhtkyXr0eJMLJ5R8Zdrd4zlKXbLM0Q','2025-01-29 02:23:00.814782'),('yyp83a1kj2gs3tjflboz1s08uq8r7krj','.eJxVjEsOwjAMBe-SNYpip6kbluw5Q-TELi2gRupnhbg7VOoCtm9m3ssk3tYhbYvOaRRzNmhOv1vm8tBpB3Ln6VZtqdM6j9nuij3oYq9V9Hk53L-DgZfhW1MrHaBrisvK6EoPWER86AEKdQQRNYJ3KuB6paBNQwEYvYtIrc-deX8A03M2_w:1thOek:c4f6df9CiCmmL_E6LKxc5zBcT7DpXFc-LBlNmT6f3sA','2025-02-24 07:56:38.629544'),('zk5480my4dwd82d3jc6epyombwqhyq33','.eJxVjDsOwyAQBe9CHSHDYj4p0_sMiIUlOIlAMnYV5e6xJRdJ-2bmvZkP21r81mnxc2JXJtnld8MQn1QPkB6h3huPra7LjPxQ-Ek7n1qi1-10_w5K6GWvIUogjaNygoaE2QhLTkAEhKyytqAhmIRW4YDoUKPMlsSYEfbCOsM-X-aMN-A:1tXVQG:PTajMLXyCmsdd_3pun5s0zE7U3D3qdeHd8qf6yqcsoY','2025-01-28 01:08:48.660758'),('zsnk8vb192crl1j2erm2xbqpb71go8g0','.eJxVjDEKwzAMAP_iuRgby1bcsXvfYCRZadKWBOJkCv17CWRo17vjdlNoW4eyNV3KWM3VdObyy5jkpdMh6pOmx2xlntZlZHsk9rTN3ueq79vZ_g0GasOxBVCPNWdVYVR2KXt2rsMgfUBPELwjxooBkwA4EgToc0wxU4y9mM8X3bs3hA:1tiU3m:lefkdWNU9amVKUqI_5uSgrU-dD3laogU_n2pQ2KNy2s','2025-02-27 07:54:58.080618');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `images_table`
--

DROP TABLE IF EXISTS `images_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `images_table` (
  `img_name` varchar(40) NOT NULL,
  `base64_image` varchar(1000) NOT NULL,
  PRIMARY KEY (`img_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `images_table`
--

LOCK TABLES `images_table` WRITE;
/*!40000 ALTER TABLE `images_table` DISABLE KEYS */;
/*!40000 ALTER TABLE `images_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kadai_table`
--

DROP TABLE IF EXISTS `kadai_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kadai_table` (
  `category` varchar(10) NOT NULL,
  `number` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `q_text` longtext NOT NULL,
  PRIMARY KEY (`number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kadai_table`
--

LOCK TABLES `kadai_table` WRITE;
/*!40000 ALTER TABLE `kadai_table` DISABLE KEYS */;
INSERT INTO `kadai_table` VALUES ('応用区分','a1','双子素数を探せ','問題\r\n100 以下のすべての双子素数ペアを求めてください。双子素数とは、2つの素数があり、その差がちょうど 2 であるペアのことです。例えば、(3, 5) や (11, 13) は双子素数のペアです。\r\n\r\n＃調べる数の上限値を設定\r\nn = 100\r\n\r\n＃素数を格納するリスト\r\nprimes = []\r\n\r\n出力\r\n「100 以下の双子素数ペア:」というタイトルを出力した後、双子素数のペアを1行ずつ表示してください。ペアはカッコで囲み、カンマで区切って表示します。\r\n\r\n出力形式は以下の通りです。\r\n\r\n100 以下の双子素数のペア:\r\n(3, 5)\r\n(5, 7)\r\n(11, 13)\r\n(17, 19)\r\n(29, 31)\r\n(41, 43)\r\n(59, 61)\r\n(71, 73)\r\n\r\n制約\r\n\r\n出力は指定された形式に厳密に従ってください。\r\n100 以下の双子素数のペアをすべて出力すること。\r\nヒント\r\n\r\n100 以下の素数をリストに格納し、その中で差が 2 になるペアを出力すれば良いでしょう。\r\n素数判定の方法として、2 から√n までの整数で割り切れるかどうかを確認する方法があります。'),('応用区分','a2','フィボナッチ数列を逆順に表示せよ','フィボナッチ数列の最初の50番目までの数字を求め、その数列を逆順にして表示するプログラムを作成してください。フィボナッチ数列は次のように定義されます。\r\n\r\n・最初の２つの数は１。\r\n・それ以降の数は直前の２つの数の合計。\r\n\r\n例えば、最初の５つの数列は「1, 1, 2, 3, 5」です。\r\n\r\n　この数列の５０番目までの数字を求め、それを逆順にして表示してください。また、その際には以下に示す要素を使用してください。\r\n\r\n＃フィボナッチ数列を格納するリスト\r\nfib = [1, 1]\r\n\r\n\r\n　答えは以下のようにprintで表示してください。\r\n\r\n＃解答\r\n12586269025,7778742049,,,,,,,,'),('応用区分','a3','迷路の解を探せ（深さ優先探索）','与えられた迷路の中から、スタート地点（S）からゴール地点（G）への経路を深さ優先探索（DFS）を使って探し、経路を表示するプログラムを作成してください。\r\n\r\n　迷路は以下の二次元配列で表されます。\r\n\r\n# 迷路の定義\r\nmaze = [\r\n    [\'S\', \'.\', \'.\', \'#\', \'.\'],\r\n    [\'#\', \'#\', \'.\', \'#\', \'.\'],\r\n    [\'.\', \'.\', \'.\', \'.\', \'G\'],\r\n    [\'.\', \'#\', \'#\', \'#\', \'.\'],\r\n    [\'.\', \'.\', \'.\', \'.\', \'.\']\r\n]\r\n\r\n　”S”がスタート地点、”G”がゴール地点、”・”が通れる道、”＃”は障害物です。\r\n\r\n　また、回答は以下のようにprintで表示してください。\r\n\r\n「経路:\r\n(0, 0)\r\n(1, 0)\r\n・\r\n・\r\n・」\r\n\r\n　（0, 0）などは、配列内の座標を表しています。'),('基本区分','b1','こんにちは！','「こんにちは」を3回表示しよう。'),('基本区分','b2','変数とループの組み合わせ','変数「count」を使い、「Hello World!」というメッセージを3回表示する組み合わせを作ってください。\r\n\r\n※ヒント\r\ncount = None\r\ncount = 3\r\nfor count2 in range(int(count)):\r\n  print(\'Hello World!\')'),('基本区分','b3','リスト操作','次の数字のリスト [3, 1, 4, 1, 5, 9, 2, 6] の長さを求めなさい。\r\n配列名は「numbers」\r\n長さを出力する変数名は「length」とする\r\n(注：リストの番号は1番から始まります)\r\n\r\n※ヒント\r\n１，まず「3, 1, 4, 1, 5, 9, 2, 6」 の数字を入力するためのリスト作成ブロックを使用し、それぞれの数字をリストに追加します。\r\n\r\n２、作成したリストを引数として「リストの長さを取得」ブロックに渡します。\r\n\r\n３、出力ブロックを使い、リストの長さ（8）を表示します。'),('基本区分','b4','リストの要素のアクセス','次のリスト [10, 20, 30] から、1番先頭（インデックス0）と3番目（インデックス2）の要素を取得し、その合計を求めなさい。\r\n配列名は「numbers」,変数名は「sum」とする\r\n(注：リストの番号は1番から始まります)\r\n\r\n※ヒント\r\n１，数字のリスト [10, 20, 30] を作成します。\r\n\r\n２，「リストの指定した位置の要素を取得」ブロックを2回使い、それぞれインデックス1とインデックス3を指定します。\r\n\r\n３，取得した2つの要素を加算するための「加算」ブロックを使います。\r\n\r\n４，合計を表示します。'),('基本区分','b5','リスト要素の追加と削除','次のリスト [\"apple\", \"banana\", \"cherry\"] に \"grape\" を追加し、\"banana\" を削除しなさい。\r\n(注：リストの番号は1番から始まります)\r\n\r\n※ヒント\r\n１，リスト [\"apple\", \"banana\", \"cherry\"] を作成します。\r\n\r\n２，\"grape\" を追加するために「リストに要素を追加」ブロックを使います。\r\n\r\n３，\"banana\" を削除するために「リストから要素を削除」ブロックを使います。\r\n\r\n４，最終的なリスト [\"apple\", \"cherry\", \"grape\"] を表示します。'),('基本区分','b6','if文','1.変数num1=100, num2=40, num3=60を作成する。\r\n\r\n2.条件分岐するコードを作成する\r\n①80以上の場合、2倍にした値を出力\r\n②50未満の場合、1/2倍にした値を出力\r\n①②の条件に当てはまらない場合、「0」を出力する。\r\n\r\n3.変数num1, num2, num3のいずれかを使用し、実行・解答を送信する。'),('チュートリアル','t1','Blocklyを触ってみよう！','こんにちは！\r\nこのセクションではBlocklyの使い方を学習してきます！\r\n画面上部に「Hello」と表示する組み合わせを作って下さい\r\n\r\n1.テキストタブから「表示」ブロックをドラッグする\r\n\r\n2,テキストタブから一番上の\" \"タブをドラッグする\r\n\r\n3.\" \"をクリックして、「Hello」と入力する\r\n\r\n4.コードを出力ボタンをクリックし、問題文の上のコードタブに切り替えてコード表示\r\n\r\n5.実行ボタンをクリックし、実行結果を表示\r\n\r\n6.解答を送信'),('チュートリアル','t2','計算ブロック','このセクションでは、計算ブロックの使い方について学習していきます。\r\n\r\n問題：\r\n10 + 5\r\n10 - 5\r\n10 x 5\r\n10 ÷ 5\r\nを実行し、解答を送信してください。\r\n\r\n1.テキストタブから「表示」ブロックを選択\r\n\r\n2.計算タブから 「□ + □」のブロックを選択し、printブロックにくっつける\r\n\r\n3.+ブロックを選択して - , x, ÷に変更する'),('チュートリアル','t3','余りを求める','このセクションでは、計算の余りを求めるブロックのについて学習していきます。\r\n\r\n問題：12345を7で割った余りを求める組み合わせを作ってください。\r\n\r\n※ヒント\r\n・計算に使用するブロックは項目「計算」に格納されています。\r\n・結果を画面に表示するには、Blocklyの「テキスト」ブロックを活用してください。'),('チュートリアル','t4','比較演算子','このセクションでは、条件分岐の基本的な比較演算子「=, ≠, <, >, ≤, ≥」について学びます。\r\n\r\nそれぞれの記号は以下のような意味を持ちます：\r\n・=：左右の値が等しい場合に真（True）になります。\r\n・≠：左右の値が等しくない場合に真（True）になります。\r\n・<：左の値が右の値より小さい場合に真（True）になります。\r\n・>：左の値が右の値より大きい場合に真（True）になります。\r\n・≤：左の値が右の値以下の場合に真（True）になります。\r\n・≥：左の値が右の値以上の場合に真（True）になります。\r\n\r\n例題\r\n以下のようなプログラムを作成してください。それぞれの比較の結果が正しいかどうかを画面上部に表示してください。\r\n\r\nプログラム要件\r\n\r\n「1 = 1」の結果（真または偽）を表示する。\r\n「1 ≠ 1」の結果を表示する。\r\n「1 > 2」の結果を表示する。\r\n「1 < 2」の結果を表示する。\r\n「2 ≥ 2」の結果を表示する。\r\n「3 ≤ 1」の結果を表示する。\r\n\r\nヒント\r\n・「論理演算」は項目「ロジック」の「＝」のブロックをしようします。\r\n・結果を画面に表示するには、Blocklyの「テキスト」ブロックを活用してください。'),('チュートリアル','t5','条件分岐（if文）','このセクションでは、条件分岐（if文）のブロックについて学習していきます。\r\n\r\n次に手順に沿ってブロックを組んでみましょう。\r\n\r\n１.項目「コントローラ」から「もし」ブロックを選択します。\r\n２.項目「ロジック」から「1＝1」ブロックを選択します。\r\n３.「もし」ブロックの右側に「1=1」ブロックを繋げます。\r\n４.項目「テキスト」から「\"hello\"を表示」ブロックを選択します。\r\n５.「もし」ブロックの中に選択した「\"hello\"を表示」ブロックを繋げます。\r\n６.「実行」ボタンを押し、結果を確認してください。\r\n７.「解答を送信」ボタンを押して「正解」と表示されれば完了です。'),('チュートリアル','t6','カウントアップ（for文）','０～９までを表示させてください。\r\n\r\n１．ループタブから「iを□から□まで□ずつカウントする」ブロックを選択\r\n２．計算タブから数字を選択し、左から□に０・９・１を入力\r\n３.「iを□から□まで□ずつカウントする」ブロック内に順に数字ブロックを入れる。\r\n４．テキストタブから「表示」ブロックを選択\r\n５.変数タブからiを選択し、「表示」ブロックと繋げる。\r\n６.「iを□から□まで□ずつカウントする」ブロックと「表示」ブロックを繋げる。\r\n７.実行ボタンをクリックし、実行結果を表示\r\n８.解答を送信');
/*!40000 ALTER TABLE `kadai_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `materials_table`
--

DROP TABLE IF EXISTS `materials_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `materials_table` (
  `material_name` varchar(40) NOT NULL,
  `html_file_name` varchar(40) NOT NULL,
  `material_id` varchar(32) NOT NULL,
  PRIMARY KEY (`material_id`),
  UNIQUE KEY `material_name` (`material_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materials_table`
--

LOCK TABLES `materials_table` WRITE;
/*!40000 ALTER TABLE `materials_table` DISABLE KEYS */;
INSERT INTO `materials_table` VALUES ('条件分岐','bunki.html','04c8e02e41d34e0f8f299f6902ee2916'),('変数','hensu.html','355efdd3b28c4732bfbe358d8ef43457'),('繰り返し','loop.html','5e64be0c0ad54603be7d2f5d91da7a8a'),('ソートアルゴリズム','content_sort.html','9561ae780f804f2893e5438e2b1cb2bd'),('データ構造','datakouzou.html','a4599b428bf7491b9d304b5db5a2fc9d');
/*!40000 ALTER TABLE `materials_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `progress_table`
--

DROP TABLE IF EXISTS `progress_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `progress_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `progress` varchar(10) NOT NULL,
  `update_at` datetime(6) NOT NULL,
  `kadai_id` varchar(100) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `progress_table_user_id_kadai_id_0be96ac1_uniq` (`user_id`,`kadai_id`),
  KEY `progress_table_kadai_id_3a0a8b44_fk_kadai_table_number` (`kadai_id`),
  CONSTRAINT `progress_table_kadai_id_3a0a8b44_fk_kadai_table_number` FOREIGN KEY (`kadai_id`) REFERENCES `kadai_table` (`number`),
  CONSTRAINT `progress_table_user_id_050369e1_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=308 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `progress_table`
--

LOCK TABLES `progress_table` WRITE;
/*!40000 ALTER TABLE `progress_table` DISABLE KEYS */;
INSERT INTO `progress_table` VALUES (1,'未着手','2024-12-18 07:35:47.823663','t1',1),(2,'完了','2024-12-18 07:35:47.823697','t1',2),(3,'実行中','2024-12-18 07:35:47.823712','t1',4),(4,'未着手','2025-01-08 05:56:23.272921','t2',1),(5,'完了','2025-01-08 05:56:23.272954','t2',2),(6,'未着手','2025-01-08 05:56:23.272969','t2',4),(7,'未着手','2025-01-08 07:19:14.445816','b2',1),(8,'完了','2025-01-08 07:19:14.445850','b2',2),(9,'未着手','2025-01-08 07:19:14.445864','b2',4),(10,'未着手','2025-01-08 07:24:46.512950','t3',1),(11,'未着手','2025-01-08 07:24:46.512983','t3',2),(12,'未着手','2025-01-08 07:24:46.512998','t3',4),(16,'未着手','2025-01-10 06:46:47.177642','t5',1),(17,'完了','2025-01-10 06:46:47.178511','t5',2),(18,'未着手','2025-01-10 06:46:47.178532','t5',4),(19,'未着手','2025-01-14 01:03:09.701321','t4',1),(20,'実行中','2025-01-14 01:03:09.701354','t4',2),(21,'未着手','2025-01-14 01:03:09.701368','t4',4),(31,'未着手','2025-02-12 02:24:06.693938','a1',1),(32,'実行中','2025-02-12 02:24:06.693975','a1',2),(33,'未着手','2025-02-12 02:24:06.693992','a1',4),(34,'未着手','2025-02-12 02:38:28.527050','b3',1),(35,'完了','2025-02-12 02:38:28.527371','b3',2),(36,'未着手','2025-02-12 02:38:28.527394','b3',4),(37,'未着手','2025-02-12 05:24:12.372787','a2',1),(38,'完了','2025-02-12 05:24:12.372824','a2',2),(39,'未着手','2025-02-12 05:24:12.372841','a2',4),(40,'未着手','2025-02-12 05:24:15.327277','b4',1),(41,'未着手','2025-02-12 05:24:15.327315','b4',2),(42,'未着手','2025-02-12 05:24:15.327333','b4',4),(43,'未着手','2025-02-12 05:29:00.792958','b5',1),(44,'未着手','2025-02-12 05:29:00.793002','b5',2),(45,'未着手','2025-02-12 05:29:00.793021','b5',4),(55,'未着手','2025-02-12 07:04:37.942033','a3',1),(56,'未着手','2025-02-12 07:04:37.942081','a3',2),(57,'未着手','2025-02-12 07:04:37.942099','a3',4),(61,'未着手','2025-02-13 03:56:35.008793','a1',6),(62,'未着手','2025-02-13 03:56:35.009137','a2',6),(63,'未着手','2025-02-13 03:56:35.009155','a3',6),(64,'完了','2025-02-13 03:56:35.009172','b2',6),(65,'完了','2025-02-13 03:56:35.009187','b3',6),(66,'完了','2025-02-13 03:56:35.009203','b4',6),(67,'完了','2025-02-13 03:56:35.009219','b5',6),(69,'完了','2025-02-13 03:56:35.009250','t1',6),(70,'完了','2025-02-13 03:56:35.009267','t2',6),(71,'未着手','2025-02-13 03:56:35.009283','t3',6),(72,'未着手','2025-02-13 03:56:35.009298','t4',6),(73,'未着手','2025-02-13 03:56:35.009313','t5',6),(75,'未着手','2025-02-13 04:02:25.859583','a1',7),(76,'未着手','2025-02-13 04:02:25.859617','a2',7),(77,'未着手','2025-02-13 04:02:25.859635','a3',7),(78,'未着手','2025-02-13 04:02:25.859651','b2',7),(79,'未着手','2025-02-13 04:02:25.859667','b3',7),(80,'未着手','2025-02-13 04:02:25.859683','b4',7),(81,'未着手','2025-02-13 04:02:25.859698','b5',7),(83,'実行中','2025-02-13 04:02:25.859730','t1',7),(84,'完了','2025-02-13 04:02:25.859745','t2',7),(85,'完了','2025-02-13 04:02:25.859760','t3',7),(86,'完了','2025-02-13 04:02:25.859775','t4',7),(87,'実行中','2025-02-13 04:02:25.859790','t5',7),(89,'未着手','2025-02-13 04:17:56.336313','a1',8),(90,'未着手','2025-02-13 04:17:56.336345','a2',8),(91,'未着手','2025-02-13 04:17:56.336372','a3',8),(92,'未着手','2025-02-13 04:17:56.336387','b2',8),(93,'未着手','2025-02-13 04:17:56.336404','b3',8),(94,'未着手','2025-02-13 04:17:56.336419','b4',8),(95,'未着手','2025-02-13 04:17:56.336435','b5',8),(97,'未着手','2025-02-13 04:17:56.336464','t1',8),(98,'未着手','2025-02-13 04:17:56.336479','t2',8),(99,'未着手','2025-02-13 04:17:56.336495','t3',8),(100,'未着手','2025-02-13 04:17:56.336510','t4',8),(101,'未着手','2025-02-13 04:17:56.336525','t5',8),(108,'実行中','2025-02-13 06:00:56.891479','a1',9),(109,'完了','2025-02-13 06:00:56.891516','a2',9),(110,'未着手','2025-02-13 06:00:56.891534','a3',9),(111,'未着手','2025-02-13 06:00:56.891552','b2',9),(112,'未着手','2025-02-13 06:00:56.891570','b3',9),(113,'未着手','2025-02-13 06:00:56.891587','b4',9),(114,'未着手','2025-02-13 06:00:56.891604','b5',9),(117,'未着手','2025-02-13 06:00:56.891650','t1',9),(118,'未着手','2025-02-13 06:00:56.891665','t2',9),(119,'未着手','2025-02-13 06:00:56.891680','t3',9),(120,'未着手','2025-02-13 06:00:56.891707','t4',9),(121,'未着手','2025-02-13 06:00:56.891723','t5',9),(122,'未着手','2025-02-13 06:05:58.141707','b1',1),(123,'未着手','2025-02-13 06:05:58.141741','b1',2),(124,'未着手','2025-02-13 06:05:58.141759','b1',4),(125,'完了','2025-02-13 06:05:58.141775','b1',6),(126,'未着手','2025-02-13 06:05:58.141792','b1',7),(127,'未着手','2025-02-13 06:05:58.141808','b1',8),(128,'完了','2025-02-13 06:05:58.141825','b1',9),(129,'未着手','2025-02-13 06:06:14.014696','b6',1),(130,'完了','2025-02-13 06:06:14.014734','b6',2),(131,'未着手','2025-02-13 06:06:14.014754','b6',4),(132,'完了','2025-02-13 06:06:14.014773','b6',6),(133,'未着手','2025-02-13 06:06:14.014791','b6',7),(134,'完了','2025-02-13 06:06:14.014809','b6',8),(135,'完了','2025-02-13 06:06:14.014831','b6',9),(136,'未着手','2025-02-13 07:12:25.139270','t6',1),(137,'完了','2025-02-13 07:12:25.139308','t6',2),(138,'未着手','2025-02-13 07:12:25.139326','t6',4),(139,'未着手','2025-02-13 07:12:25.139342','t6',6),(140,'未着手','2025-02-13 07:12:25.139357','t6',7),(141,'未着手','2025-02-13 07:12:25.139372','t6',8),(142,'未着手','2025-02-13 07:12:25.139387','t6',9),(143,'未着手','2025-02-14 00:20:23.732788','a1',10),(144,'未着手','2025-02-14 00:20:23.732827','a2',10),(145,'未着手','2025-02-14 00:20:23.732845','a3',10),(146,'完了','2025-02-14 00:20:23.732862','b1',10),(147,'未着手','2025-02-14 00:20:23.732877','b2',10),(148,'未着手','2025-02-14 00:20:23.732892','b3',10),(149,'未着手','2025-02-14 00:20:23.732908','b4',10),(150,'未着手','2025-02-14 00:20:23.732923','b5',10),(151,'完了','2025-02-14 00:20:23.732943','b6',10),(152,'完了','2025-02-14 00:20:23.732959','t1',10),(153,'完了','2025-02-14 00:20:23.732977','t2',10),(154,'未着手','2025-02-14 00:20:23.732992','t3',10),(155,'未着手','2025-02-14 00:20:23.733007','t4',10),(156,'未着手','2025-02-14 00:20:23.733022','t5',10),(157,'未着手','2025-02-14 00:20:23.733037','t6',10),(158,'未着手','2025-02-14 00:21:13.227481','a1',11),(159,'未着手','2025-02-14 00:21:13.227515','a2',11),(160,'未着手','2025-02-14 00:21:13.227532','a3',11),(161,'完了','2025-02-14 00:21:13.227549','b1',11),(162,'未着手','2025-02-14 00:21:13.227565','b2',11),(163,'完了','2025-02-14 00:21:13.227581','b3',11),(164,'未着手','2025-02-14 00:21:13.227596','b4',11),(165,'未着手','2025-02-14 00:21:13.227611','b5',11),(166,'完了','2025-02-14 00:21:13.227630','b6',11),(167,'完了','2025-02-14 00:21:13.227645','t1',11),(168,'完了','2025-02-14 00:21:13.227661','t2',11),(169,'完了','2025-02-14 00:21:13.227676','t3',11),(170,'完了','2025-02-14 00:21:13.227691','t4',11),(171,'完了','2025-02-14 00:21:13.227706','t5',11),(172,'完了','2025-02-14 00:21:13.227731','t6',11),(173,'未着手','2025-02-14 00:22:25.366572','a1',12),(174,'完了','2025-02-14 00:22:25.366603','a2',12),(175,'未着手','2025-02-14 00:22:25.366621','a3',12),(176,'完了','2025-02-14 00:22:25.366638','b1',12),(177,'完了','2025-02-14 00:22:25.366653','b2',12),(178,'完了','2025-02-14 00:22:25.366670','b3',12),(179,'完了','2025-02-14 00:22:25.366686','b4',12),(180,'完了','2025-02-14 00:22:25.366701','b5',12),(181,'完了','2025-02-14 00:22:25.366717','b6',12),(182,'完了','2025-02-14 00:22:25.366733','t1',12),(183,'完了','2025-02-14 00:22:25.366748','t2',12),(184,'未着手','2025-02-14 00:22:25.366763','t3',12),(185,'未着手','2025-02-14 00:22:25.366778','t4',12),(186,'完了','2025-02-14 00:22:25.366793','t5',12),(187,'完了','2025-02-14 00:22:25.366808','t6',12),(188,'未着手','2025-02-14 00:26:11.283118','a1',13),(189,'実行中','2025-02-14 00:26:11.283152','a2',13),(190,'実行中','2025-02-14 00:26:11.283169','a3',13),(191,'完了','2025-02-14 00:26:11.283186','b1',13),(192,'完了','2025-02-14 00:26:11.283202','b2',13),(193,'実行中','2025-02-14 00:26:11.283218','b3',13),(194,'実行中','2025-02-14 00:26:11.283234','b4',13),(195,'実行中','2025-02-14 00:26:11.283250','b5',13),(196,'完了','2025-02-14 00:26:11.283266','b6',13),(197,'完了','2025-02-14 00:26:11.283282','t1',13),(198,'実行中','2025-02-14 00:26:11.283297','t2',13),(199,'実行中','2025-02-14 00:26:11.283313','t3',13),(200,'実行中','2025-02-14 00:26:11.283329','t4',13),(201,'実行中','2025-02-14 00:26:11.283344','t5',13),(202,'完了','2025-02-14 00:26:11.283360','t6',13),(203,'未着手','2025-02-14 00:50:58.025315','a1',14),(204,'未着手','2025-02-14 00:50:58.025350','a2',14),(205,'未着手','2025-02-14 00:50:58.025368','a3',14),(206,'未着手','2025-02-14 00:50:58.025385','b1',14),(207,'未着手','2025-02-14 00:50:58.025401','b2',14),(208,'未着手','2025-02-14 00:50:58.025418','b3',14),(209,'未着手','2025-02-14 00:50:58.025435','b4',14),(210,'未着手','2025-02-14 00:50:58.025452','b5',14),(211,'未着手','2025-02-14 00:50:58.025469','b6',14),(212,'未着手','2025-02-14 00:50:58.025486','t1',14),(213,'未着手','2025-02-14 00:50:58.025502','t2',14),(214,'未着手','2025-02-14 00:50:58.025518','t3',14),(215,'未着手','2025-02-14 00:50:58.025534','t4',14),(216,'未着手','2025-02-14 00:50:58.025550','t5',14),(217,'未着手','2025-02-14 00:50:58.025566','t6',14),(218,'未着手','2025-02-14 03:47:26.059286','a1',15),(219,'未着手','2025-02-14 03:47:26.059322','a2',15),(220,'未着手','2025-02-14 03:47:26.059340','a3',15),(221,'未着手','2025-02-14 03:47:26.059357','b1',15),(222,'未着手','2025-02-14 03:47:26.059379','b2',15),(223,'未着手','2025-02-14 03:47:26.059401','b3',15),(224,'未着手','2025-02-14 03:47:26.059422','b4',15),(225,'未着手','2025-02-14 03:47:26.059439','b5',15),(226,'未着手','2025-02-14 03:47:26.059457','b6',15),(227,'未着手','2025-02-14 03:47:26.059473','t1',15),(228,'未着手','2025-02-14 03:47:26.059498','t2',15),(229,'未着手','2025-02-14 03:47:26.059520','t3',15),(230,'未着手','2025-02-14 03:47:26.059538','t4',15),(231,'未着手','2025-02-14 03:47:26.059553','t5',15),(232,'未着手','2025-02-14 03:47:26.059568','t6',15),(233,'未着手','2025-02-14 04:15:07.664461','a1',16),(234,'未着手','2025-02-14 04:15:07.664501','a2',16),(235,'未着手','2025-02-14 04:15:07.664526','a3',16),(236,'完了','2025-02-14 04:15:07.664542','b1',16),(237,'完了','2025-02-14 04:15:07.664558','b2',16),(238,'未着手','2025-02-14 04:15:07.664575','b3',16),(239,'未着手','2025-02-14 04:15:07.664591','b4',16),(240,'未着手','2025-02-14 04:15:07.664607','b5',16),(241,'未着手','2025-02-14 04:15:07.664624','b6',16),(242,'完了','2025-02-14 04:15:07.664641','t1',16),(243,'完了','2025-02-14 04:15:07.664656','t2',16),(244,'完了','2025-02-14 04:15:07.664671','t3',16),(245,'完了','2025-02-14 04:15:07.664687','t4',16),(246,'完了','2025-02-14 04:15:07.664706','t5',16),(247,'完了','2025-02-14 04:15:07.664723','t6',16),(248,'未着手','2025-02-14 04:30:55.810743','a1',17),(249,'未着手','2025-02-14 04:30:55.810779','a2',17),(250,'未着手','2025-02-14 04:30:55.810797','a3',17),(251,'完了','2025-02-14 04:30:55.810813','b1',17),(252,'未着手','2025-02-14 04:30:55.810829','b2',17),(253,'未着手','2025-02-14 04:30:55.810845','b3',17),(254,'未着手','2025-02-14 04:30:55.810861','b4',17),(255,'未着手','2025-02-14 04:30:55.810876','b5',17),(256,'未着手','2025-02-14 04:30:55.810891','b6',17),(257,'完了','2025-02-14 04:30:55.810907','t1',17),(258,'未着手','2025-02-14 04:30:55.810922','t2',17),(259,'未着手','2025-02-14 04:30:55.810938','t3',17),(260,'未着手','2025-02-14 04:30:55.810953','t4',17),(261,'未着手','2025-02-14 04:30:55.810968','t5',17),(262,'未着手','2025-02-14 04:30:55.810984','t6',17),(263,'未着手','2025-02-14 05:13:51.213470','a1',18),(264,'未着手','2025-02-14 05:13:51.213506','a2',18),(265,'未着手','2025-02-14 05:13:51.213524','a3',18),(266,'未着手','2025-02-14 05:13:51.213541','b1',18),(267,'未着手','2025-02-14 05:13:51.213566','b2',18),(268,'未着手','2025-02-14 05:13:51.213583','b3',18),(269,'未着手','2025-02-14 05:13:51.213599','b4',18),(270,'未着手','2025-02-14 05:13:51.213615','b5',18),(271,'未着手','2025-02-14 05:13:51.213630','b6',18),(272,'完了','2025-02-14 05:13:51.213645','t1',18),(273,'完了','2025-02-14 05:13:51.213661','t2',18),(274,'未着手','2025-02-14 05:13:51.213675','t3',18),(275,'未着手','2025-02-14 05:13:51.213690','t4',18),(276,'未着手','2025-02-14 05:13:51.213707','t5',18),(277,'未着手','2025-02-14 05:13:51.213722','t6',18),(278,'未着手','2025-02-15 03:17:25.984686','a1',19),(279,'未着手','2025-02-15 03:17:25.984723','a2',19),(280,'未着手','2025-02-15 03:17:25.984741','a3',19),(281,'未着手','2025-02-15 03:17:25.984758','b1',19),(282,'未着手','2025-02-15 03:17:25.984775','b2',19),(283,'未着手','2025-02-15 03:17:25.984791','b3',19),(284,'未着手','2025-02-15 03:17:25.984807','b4',19),(285,'未着手','2025-02-15 03:17:25.984822','b5',19),(286,'未着手','2025-02-15 03:17:25.984838','b6',19),(287,'完了','2025-02-15 03:17:25.984854','t1',19),(288,'完了','2025-02-15 03:17:25.984870','t2',19),(289,'未着手','2025-02-15 03:17:25.984885','t3',19),(290,'未着手','2025-02-15 03:17:25.984901','t4',19),(291,'未着手','2025-02-15 03:17:25.984916','t5',19),(292,'未着手','2025-02-15 03:17:25.984933','t6',19),(293,'未着手','2025-02-15 04:30:08.423966','a1',20),(294,'未着手','2025-02-15 04:30:08.424000','a2',20),(295,'未着手','2025-02-15 04:30:08.424021','a3',20),(296,'未着手','2025-02-15 04:30:08.424038','b1',20),(297,'未着手','2025-02-15 04:30:08.424054','b2',20),(298,'未着手','2025-02-15 04:30:08.424070','b3',20),(299,'未着手','2025-02-15 04:30:08.424085','b4',20),(300,'未着手','2025-02-15 04:30:08.424101','b5',20),(301,'未着手','2025-02-15 04:30:08.424117','b6',20),(302,'未着手','2025-02-15 04:30:08.424137','t1',20),(303,'未着手','2025-02-15 04:30:08.424154','t2',20),(304,'未着手','2025-02-15 04:30:08.424170','t3',20),(305,'未着手','2025-02-15 04:30:08.424186','t4',20),(306,'未着手','2025-02-15 04:30:08.424202','t5',20),(307,'未着手','2025-02-15 04:30:08.424217','t6',20);
/*!40000 ALTER TABLE `progress_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_association`
--

DROP TABLE IF EXISTS `social_auth_association`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `social_auth_association` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `server_url` varchar(255) NOT NULL,
  `handle` varchar(255) NOT NULL,
  `secret` varchar(255) NOT NULL,
  `issued` int NOT NULL,
  `lifetime` int NOT NULL,
  `assoc_type` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `social_auth_association_server_url_handle_078befa2_uniq` (`server_url`,`handle`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_association`
--

LOCK TABLES `social_auth_association` WRITE;
/*!40000 ALTER TABLE `social_auth_association` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_association` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_code`
--

DROP TABLE IF EXISTS `social_auth_code`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `social_auth_code` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `code` varchar(32) NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `social_auth_code_email_code_801b2d02_uniq` (`email`,`code`),
  KEY `social_auth_code_code_a2393167` (`code`),
  KEY `social_auth_code_timestamp_176b341f` (`timestamp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_code`
--

LOCK TABLES `social_auth_code` WRITE;
/*!40000 ALTER TABLE `social_auth_code` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_code` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_nonce`
--

DROP TABLE IF EXISTS `social_auth_nonce`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `social_auth_nonce` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `server_url` varchar(255) NOT NULL,
  `timestamp` int NOT NULL,
  `salt` varchar(65) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `social_auth_nonce_server_url_timestamp_salt_f6284463_uniq` (`server_url`,`timestamp`,`salt`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_nonce`
--

LOCK TABLES `social_auth_nonce` WRITE;
/*!40000 ALTER TABLE `social_auth_nonce` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_nonce` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_partial`
--

DROP TABLE IF EXISTS `social_auth_partial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `social_auth_partial` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `token` varchar(32) NOT NULL,
  `next_step` smallint unsigned NOT NULL,
  `backend` varchar(32) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `data` json NOT NULL DEFAULT (_utf8mb3'{}'),
  PRIMARY KEY (`id`),
  KEY `social_auth_partial_token_3017fea3` (`token`),
  KEY `social_auth_partial_timestamp_50f2119f` (`timestamp`),
  CONSTRAINT `social_auth_partial_chk_1` CHECK ((`next_step` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_partial`
--

LOCK TABLES `social_auth_partial` WRITE;
/*!40000 ALTER TABLE `social_auth_partial` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_partial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_usersocialauth`
--

DROP TABLE IF EXISTS `social_auth_usersocialauth`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `social_auth_usersocialauth` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `provider` varchar(32) NOT NULL,
  `uid` varchar(255) NOT NULL,
  `user_id` int NOT NULL,
  `created` datetime(6) NOT NULL,
  `modified` datetime(6) NOT NULL,
  `extra_data` json NOT NULL DEFAULT (_utf8mb3'{}'),
  PRIMARY KEY (`id`),
  UNIQUE KEY `social_auth_usersocialauth_provider_uid_e6b5e668_uniq` (`provider`,`uid`),
  KEY `social_auth_usersocialauth_user_id_17d28448_fk_auth_user_id` (`user_id`),
  KEY `social_auth_usersocialauth_uid_796e51dc` (`uid`),
  CONSTRAINT `social_auth_usersocialauth_user_id_17d28448_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_usersocialauth`
--

LOCK TABLES `social_auth_usersocialauth` WRITE;
/*!40000 ALTER TABLE `social_auth_usersocialauth` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_usersocialauth` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-15  6:00:47
