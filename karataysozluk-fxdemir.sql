-- phpMyAdmin SQL Dump
-- version 5.0.0-rc1
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1:3306
-- Üretim Zamanı: 26 Ara 2019, 13:03:20
-- Sunucu sürümü: 8.0.18
-- PHP Sürümü: 7.2.24-0ubuntu0.18.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `fxdemir`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `anonim`
--

CREATE TABLE `anonim` (
  `itiraf_id` int(11) NOT NULL,
  `itiraf` text CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `rumuz` varchar(50) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `cinsiyet` varchar(10) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `tarih` text CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `from_uye` int(11) NOT NULL,
  `onay` int(11) DEFAULT NULL,
  `rapor` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `anonim`
--

INSERT INTO `anonim` (`itiraf_id`, `itiraf`, `rumuz`, `cinsiyet`, `tarih`, `from_uye`, `onay`, `rapor`) VALUES
(24, 'vbvxbxb', 'bxbxxb', 'erkek', '20-07-19 ', 22, 0, NULL),
(25, 'Test İtiraf', 'Test Rumuz', 'erkek', '20-07-19 ', 22, 1, NULL);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `anonim_mod`
--

CREATE TABLE `anonim_mod` (
  `mod_id` int(11) NOT NULL,
  `mod_uye` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `anonim_mod`
--

INSERT INTO `anonim_mod` (`mod_id`, `mod_uye`) VALUES
(1, 22);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `baslik`
--

CREATE TABLE `baslik` (
  `baslik_id` int(11) NOT NULL,
  `baslik_baslik` varchar(70) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `baslik_puan` int(11) DEFAULT NULL,
  `baslik_acan` int(11) NOT NULL,
  `sayfa` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `baslik`
--

INSERT INTO `baslik` (`baslik_id`, `baslik_baslik`, `baslik_puan`, `baslik_acan`, `sayfa`) VALUES
(1, 'Test Deneme Başlık', NULL, 22, 2),
(3, 'Deneme 3', NULL, 22, 1),
(4, 'hjklgf', NULL, 25, 1);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `begeni`
--

CREATE TABLE `begeni` (
  `like_to_entry` int(11) NOT NULL,
  `like_from_uye` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `entry`
--

CREATE TABLE `entry` (
  `entry_id` int(11) NOT NULL,
  `entry_from_baslik` int(11) NOT NULL,
  `entry_from_uye` int(11) NOT NULL,
  `entry_entry` text CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `entry_date` varchar(255) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `entry`
--

INSERT INTO `entry` (`entry_id`, `entry_from_baslik`, `entry_from_uye`, `entry_entry`, `entry_date`) VALUES
(1, 1, 22, 'Deneme Entry', '16:10 20-07-19 '),
(2, 1, 22, 'tetete', '16:22 20-07-19 '),
(3, 1, 22, 'trrrrrrrrrrrrrrr', '16:22 20-07-19 '),
(4, 1, 22, 'ssdsdsdgsg', '16:22 20-07-19 '),
(5, 1, 22, 'bvbv', '16:22 20-07-19 '),
(6, 1, 22, 'htrhtrhtr', '16:22 20-07-19 '),
(7, 1, 22, 'qweqweqwe', '16:22 20-07-19 '),
(8, 1, 22, 'fads', '16:23 20-07-19 '),
(9, 1, 22, 'vzcvzc', '16:23 20-07-19 '),
(10, 1, 22, 'gs', '16:23 20-07-19 '),
(11, 1, 22, 'ttetete', '16:23 20-07-19 '),
(12, 1, 22, 'dfhdf', '16:23 20-07-19 '),
(13, 1, 22, 'hdhddhdhg', '16:23 20-07-19 '),
(14, 3, 22, 'test', '16:26 20-07-19 '),
(15, 3, 25, 'test olarak kurulmuş başlık.', '17:39 20-07-19 '),
(16, 4, 25, 'Furkan Demir\'in bıkmadan usanmadan kullandığı random random.', '17:40 20-07-19 '),
(17, 1, 22, 'DhdhdhdhshshdhDhdhdhdhshshdhDhdhdhdhshshdh', '14:08 23-07-19 ');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `haber`
--

CREATE TABLE `haber` (
  `haber_id` int(11) NOT NULL,
  `haber_baslik` varchar(255) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `haber_aciklama` text CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `haber_tarih` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `haber`
--

INSERT INTO `haber` (`haber_id`, `haber_baslik`, `haber_aciklama`, `haber_tarih`) VALUES
(1, 'Test haber', 'Deneme haber deneme test haber deneme diqqska akdjdja shdjsj', '2019-08-14'),
(2, 'Test haber', 'Deneme haber deneme test haber deneme diqqska akdjdja shdjsj', '2019-08-14'),
(3, 'Test haber', 'Deneme haber deneme test haber deneme diqqska akdjdja shdjsj', '2019-08-14');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `mesajlar`
--

CREATE TABLE `mesajlar` (
  `msj_id` int(11) NOT NULL,
  `msj_from` int(11) NOT NULL,
  `msj_to` int(11) NOT NULL,
  `msj_text` text CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `msj_okunma` int(11) NOT NULL,
  `msj_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `mesajlar`
--

INSERT INTO `mesajlar` (`msj_id`, `msj_from`, `msj_to`, `msj_text`, `msj_okunma`, `msj_date`) VALUES
(1, 1, 13, 'test', 0, '0000-00-00'),
(2, 1, 13, 'test', 0, '0000-00-00');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `topluluk`
--

CREATE TABLE `topluluk` (
  `tp_id` int(11) NOT NULL,
  `tp_ad` varchar(255) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `tp_kisaltma` varchar(255) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `tp_aciklama` text CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `tp_foto` text CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `tp_face` varchar(50) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `tp_insta` varchar(50) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `tp_twitter` varchar(50) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `topluluk`
--

INSERT INTO `topluluk` (`tp_id`, `tp_ad`, `tp_kisaltma`, `tp_aciklama`, `tp_foto`, `tp_face`, `tp_insta`, `tp_twitter`) VALUES
(1, 'Yazılımda Gelişim Topluluğu', 'YAGET', ' Yazılımda Gelişim Topluluğu olarak amacımız Yazılım dünyasına giriş yapmak. Yazılım dünyasında projeler geliştirerek geniş kitlere ulaşmak böylece yazılım algoritması’ nın temel yapısını, mantığını ve uygulamalı olarak göstermek ve öğretmektir.\r\n    Tüm dünyada gerek üretim gerek sanayi olarak büyük değişimin içindeyiz. Üretimden elde edeceğimiz ürünlerin, gelişen teknolojiler sayesinde gün geçtikçe daha da artıyor. Bu büyük değişimin adı Endüstri 4.0’dır. Biz Yaget topluluğu Endüstri 4.0’nın önemli kısım olan digital dünya’ya hazırlanmak ve konferans gibi etkinlikler yaparak kendimizi Endüstri 4.0’a hazırlamaktır.', '', '', '', '');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `tp_haber`
--

CREATE TABLE `tp_haber` (
  `tphaber_id` int(11) NOT NULL,
  `tp_from` int(11) NOT NULL,
  `tphaber_baslik` varchar(255) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `tphaber_aciklama` text CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `tphaber_date` varchar(100) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `nick` varchar(50) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `bolum` varchar(255) CHARACTER SET utf8 COLLATE utf8_turkish_ci DEFAULT NULL,
  `bio` varchar(255) CHARACTER SET utf8 COLLATE utf8_turkish_ci DEFAULT NULL,
  `uyetarih` date DEFAULT NULL,
  `face` varchar(50) CHARACTER SET utf8 COLLATE utf8_turkish_ci DEFAULT NULL,
  `twitter` varchar(50) CHARACTER SET utf8 COLLATE utf8_turkish_ci DEFAULT NULL,
  `insta` varchar(50) CHARACTER SET utf8 COLLATE utf8_turkish_ci DEFAULT NULL,
  `pp` varchar(535) CHARACTER SET utf8 COLLATE utf8_turkish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `password`, `nick`, `bolum`, `bio`, `uyetarih`, `face`, `twitter`, `insta`, `pp`) VALUES
(22, 'Furkan Demir', 'furkantekhesap@gmail.com', '123123', 'FxDemir', 'Elektrik - Elektronik Müh.', 'Road to AI.', NULL, '', 'Fxdemir', 'Fxdemir', 'rk195t.jpg'),
(23, 'Test Üye', 'test@fjdjd.xom', '123123', 'Testuye', NULL, NULL, NULL, NULL, NULL, NULL, 'noprofile.jpg'),
(24, 'Ben', 'dede@dede.com', '123123', 'Ben', NULL, NULL, NULL, NULL, NULL, NULL, 'noprofile.jpg'),
-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `yetkiler`
--

CREATE TABLE `yetkiler` (
  `yetkiler_id` int(10) NOT NULL,
  `yetki_from_uye` int(11) NOT NULL,
  `yetki_from_tp` int(11) NOT NULL,
  `yetki_from_rank` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `anonim`
--
ALTER TABLE `anonim`
  ADD PRIMARY KEY (`itiraf_id`);

--
-- Tablo için indeksler `anonim_mod`
--
ALTER TABLE `anonim_mod`
  ADD PRIMARY KEY (`mod_id`);

--
-- Tablo için indeksler `baslik`
--
ALTER TABLE `baslik`
  ADD PRIMARY KEY (`baslik_id`);

--
-- Tablo için indeksler `entry`
--
ALTER TABLE `entry`
  ADD PRIMARY KEY (`entry_id`),
  ADD KEY `entry_from_uye` (`entry_from_uye`);

--
-- Tablo için indeksler `haber`
--
ALTER TABLE `haber`
  ADD PRIMARY KEY (`haber_id`);

--
-- Tablo için indeksler `mesajlar`
--
ALTER TABLE `mesajlar`
  ADD PRIMARY KEY (`msj_id`);

--
-- Tablo için indeksler `topluluk`
--
ALTER TABLE `topluluk`
  ADD PRIMARY KEY (`tp_id`);

--
-- Tablo için indeksler `tp_haber`
--
ALTER TABLE `tp_haber`
  ADD PRIMARY KEY (`tphaber_id`);

--
-- Tablo için indeksler `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `yetkiler`
--
ALTER TABLE `yetkiler`
  ADD PRIMARY KEY (`yetkiler_id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `anonim`
--
ALTER TABLE `anonim`
  MODIFY `itiraf_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- Tablo için AUTO_INCREMENT değeri `anonim_mod`
--
ALTER TABLE `anonim_mod`
  MODIFY `mod_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Tablo için AUTO_INCREMENT değeri `baslik`
--
ALTER TABLE `baslik`
  MODIFY `baslik_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Tablo için AUTO_INCREMENT değeri `entry`
--
ALTER TABLE `entry`
  MODIFY `entry_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- Tablo için AUTO_INCREMENT değeri `haber`
--
ALTER TABLE `haber`
  MODIFY `haber_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Tablo için AUTO_INCREMENT değeri `mesajlar`
--
ALTER TABLE `mesajlar`
  MODIFY `msj_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Tablo için AUTO_INCREMENT değeri `topluluk`
--
ALTER TABLE `topluluk`
  MODIFY `tp_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Tablo için AUTO_INCREMENT değeri `tp_haber`
--
ALTER TABLE `tp_haber`
  MODIFY `tphaber_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Tablo için AUTO_INCREMENT değeri `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- Tablo için AUTO_INCREMENT değeri `yetkiler`
--
ALTER TABLE `yetkiler`
  MODIFY `yetkiler_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

