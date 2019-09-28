-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 28. Sep 2019 um 11:38
-- Server-Version: 10.4.6-MariaDB
-- PHP-Version: 7.1.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `planeten`
--
CREATE DATABASE IF NOT EXISTS `planeten` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin;
USE `planeten`;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `benutzer`
--

DROP TABLE IF EXISTS `benutzer`;
CREATE TABLE `benutzer` (
  `Id` int(32) NOT NULL,
  `name` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '-'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- TRUNCATE Tabelle vor dem Einfügen `benutzer`
--

TRUNCATE TABLE `benutzer`;
-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `monde`
--

DROP TABLE IF EXISTS `monde`;
CREATE TABLE `monde` (
  `Id` int(32) NOT NULL,
  `name` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '-',
  `planet_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- TRUNCATE Tabelle vor dem Einfügen `monde`
--

TRUNCATE TABLE `monde`;
--
-- Daten für Tabelle `monde`
--

INSERT INTO `monde` (`Id`, `name`, `planet_id`) VALUES
(1, 'mond 1', 1);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `planet`
--

DROP TABLE IF EXISTS `planet`;
CREATE TABLE `planet` (
  `Id` int(11) NOT NULL,
  `name` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '-',
  `gewicht` int(32) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- TRUNCATE Tabelle vor dem Einfügen `planet`
--

TRUNCATE TABLE `planet`;
--
-- Daten für Tabelle `planet`
--

INSERT INTO `planet` (`Id`, `name`, `gewicht`) VALUES
(1, 'Jupiter', 100);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `sichtungen`
--

DROP TABLE IF EXISTS `sichtungen`;
CREATE TABLE `sichtungen` (
  `Id_nutzer` int(32) UNSIGNED NOT NULL,
  `Id_planet` int(32) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- TRUNCATE Tabelle vor dem Einfügen `sichtungen`
--

TRUNCATE TABLE `sichtungen`;
--
-- Daten für Tabelle `sichtungen`
--

INSERT INTO `sichtungen` (`Id_nutzer`, `Id_planet`) VALUES
(3, 1),
(3, 1);

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `monde`
--
ALTER TABLE `monde`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `fk_mond_planet` (`planet_id`);

--
-- Indizes für die Tabelle `planet`
--
ALTER TABLE `planet`
  ADD PRIMARY KEY (`Id`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `monde`
--
ALTER TABLE `monde`
  MODIFY `Id` int(32) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT für Tabelle `planet`
--
ALTER TABLE `planet`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints der exportierten Tabellen
--

--
-- Constraints der Tabelle `monde`
--
ALTER TABLE `monde`
  ADD CONSTRAINT `fk_mond_planet` FOREIGN KEY (`planet_id`) REFERENCES `planet` (`Id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
