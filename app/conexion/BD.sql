

CREATE TABLE `chat`.`users` (
  `idUser` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `primer_nombre` VARCHAR(45) NULL,
  `email_cliente` VARCHAR(45) NULL,
  `password_cliente` MEDIUMTEXT NULL,
  `estado` TINYINT(1) NULL,
  PRIMARY KEY (`idUser`));
