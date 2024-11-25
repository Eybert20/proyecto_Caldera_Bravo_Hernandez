/*
 Navicat Premium Dump SQL

 Source Server         : Eybert
 Source Server Type    : MySQL
 Source Server Version : 80030 (8.0.30)
 Source Host           : localhost:3306
 Source Schema         : gestion_construccion

 Target Server Type    : MySQL
 Target Server Version : 80030 (8.0.30)
 File Encoding         : 65001

 Date: 20/11/2024 18:11:53
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for calculos
-- ----------------------------
DROP TABLE IF EXISTS `calculos`;
CREATE TABLE `calculos`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `proyecto_id` int UNSIGNED NULL DEFAULT NULL,
  `formula_id` int UNSIGNED NOT NULL,
  `resultado` decimal(10, 2) NULL DEFAULT NULL,
  `parametros` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `fecha_creacion` date NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `proyecto_id`(`proyecto_id` ASC) USING BTREE,
  INDEX `formula_id`(`formula_id` ASC) USING BTREE,
  CONSTRAINT `calculos_ibfk_1` FOREIGN KEY (`proyecto_id`) REFERENCES `proyectos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `calculos_ibfk_2` FOREIGN KEY (`formula_id`) REFERENCES `formulas` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of calculos
-- ----------------------------
INSERT INTO `calculos` VALUES (11, 13, 19, 21.00, '1,8,6,3', NULL);
INSERT INTO `calculos` VALUES (12, 13, 17, 10.00, '5,2,1', NULL);

-- ----------------------------
-- Table structure for categorias
-- ----------------------------
DROP TABLE IF EXISTS `categorias`;
CREATE TABLE `categorias`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `descripcion` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `fecha_creacion` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of categorias
-- ----------------------------
INSERT INTO `categorias` VALUES (3, 'Ciclopeo', 'Este es un Muro Ciclopeo de Concreto sin acero', NULL);
INSERT INTO `categorias` VALUES (4, 'Tipo T', 'Este es un Muro en Tipo  de Concreto Armado con Acero', NULL);
INSERT INTO `categorias` VALUES (5, 'Tipo L', 'Este es un Muro en Tipo  de Concreto Armado con Acero', NULL);

-- ----------------------------
-- Table structure for formulas
-- ----------------------------
DROP TABLE IF EXISTS `formulas`;
CREATE TABLE `formulas`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `descripcion` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `expresion` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `fecha_creacion` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 27 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of formulas
-- ----------------------------
INSERT INTO `formulas` VALUES (13, 'Excavacion', 'Esta fórmula se utiliza para la Excavación de área su Formula original es Vexc= L*(B * hexc)/2', 'a*(b *c )/2', NULL);
INSERT INTO `formulas` VALUES (14, 'Compactación ', 'Esta fórmula se utiliza para la compactación de área su Formula original es VRELL= L * Arell * Hrell ', 'a*b *c ', NULL);
INSERT INTO `formulas` VALUES (15, 'Concreto Zapata', 'Esta fórmula se utiliza para la Calcular el Concreto de la Pantalla Su Formula Original es L*B*H', 'a*b *c ', NULL);
INSERT INTO `formulas` VALUES (16, 'Cantidad Cemento Zapata', 'Esta fórmula se utiliza para la Calcular la cantidad de Cemento Su Formula Original es = Volumen Zapata * N° Sacos de cemento m3', 'a*b ', NULL);
INSERT INTO `formulas` VALUES (17, 'Cantidad Arena Lavada Zapata', 'Esta fórmula se utiliza para la Calcular la cantidad de Arena Lavada Su Formula Original es = volumen * m3 arena / m3 Concreto', 'a*b/c', NULL);
INSERT INTO `formulas` VALUES (18, 'Cantidad Piedra Picada Zapata', 'Esta fórmula se utiliza para la Calcular la cantidad de Piedra Picada Su Formula Original es = volumen * m3 Piedra Picada / m3 Concreto', 'a*b/c', NULL);
INSERT INTO `formulas` VALUES (19, 'Concreto Pantalla', 'Esta fórmula se utiliza para la Calcular el Concreto en la Pantalla Su Formula Original es L*((Fuste+Corona)/2)*H', 'a*((b+c)/2)*d', NULL);
INSERT INTO `formulas` VALUES (20, 'Volumen Total', 'Esta fórmula se utiliza para la Calcular el Concreto en la Pantalla Su Formula Original es Volumen Zapata + Volumen Pantalla', 'a+b', NULL);
INSERT INTO `formulas` VALUES (21, 'Cantidad Total de Cemento', 'Esta fórmula se utiliza para la Calcular el Concreto en la Pantalla Su Formula Original es CCementoZ + CCemnetoP', 'a+b', NULL);
INSERT INTO `formulas` VALUES (22, 'Cantidad Total de Arena lavada', 'Esta fórmula se utiliza para la Calcular el Concreto en la Pantalla Su Formula Original es CArenalZ + CArenaLP', 'a+b', NULL);
INSERT INTO `formulas` VALUES (23, 'Cantidad Total de Piedra Picada', 'Esta fórmula se utiliza para la Calcular el Cantidad de Pierda.P Su Formula Original es CP.PZ + CP.P.P', 'a+b', NULL);
INSERT INTO `formulas` VALUES (24, 'Para Cabillas Tipo A', 'Esta fórmula se utiliza para la Calcular La cabilla su formula original es Lpza Aint*N°pza Aint', 'a*b', NULL);
INSERT INTO `formulas` VALUES (25, 'Para Cabillas Tipo b', 'Esta fórmula se utiliza para la Calcular La cabilla su formula original es Lpza Bint*N°pza Bint', 'a*b', NULL);
INSERT INTO `formulas` VALUES (26, 'Para Cabillas Tipo C', 'Esta fórmula se utiliza para la Calcular La cabilla su formula original es Lpza Cint*N°pza Cint', 'a*b', NULL);

-- ----------------------------
-- Table structure for proyectos
-- ----------------------------
DROP TABLE IF EXISTS `proyectos`;
CREATE TABLE `proyectos`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `categoria_id` int UNSIGNED NULL DEFAULT NULL,
  `usuario_id` int UNSIGNED NULL DEFAULT NULL,
  `titulo` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `descripcion` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `fecha_inicio` date NULL DEFAULT NULL,
  `fecha_fin` date NULL DEFAULT NULL,
  `fecha_creacion` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `usuario_id`(`usuario_id` ASC) USING BTREE,
  INDEX `categoria_id`(`categoria_id` ASC) USING BTREE,
  CONSTRAINT `proyectos_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `proyectos_ibfk_2` FOREIGN KEY (`categoria_id`) REFERENCES `categorias` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of proyectos
-- ----------------------------
INSERT INTO `proyectos` VALUES (13, 3, 1, 'Muro en Betijoque', 'saef', '2024-11-19', '2024-10-18', NULL);

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `correo` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `contraseña` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `rol` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `fecha_creacion` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES (1, 'Eybert', 'eybertcaldera15@gmail.com', 'scrypt:32768:8:1$LmdMsNjoBQGyXPAV$b1b1ff46fb9264b298a068fe5ca2c33371089566c868d80686249cb0375423e63ef055839e8de35870546cbaf4ca0b16a5bd08ecc5fcd7daa68fb980300dfac8', 'ing', '2024-10-31 23:00:25');

SET FOREIGN_KEY_CHECKS = 1;
