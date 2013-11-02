CREATE TABLE `access_points` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hotspot` int(11) DEFAULT NULL,
  `mask` varchar(100) DEFAULT NULL,
  `created` datetime DEFAULT CURRENT_TIMESTAMP,
  `lastupdated` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mask_UNIQUE` (`mask`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `accounts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` int(11) DEFAULT NULL,
  `provider` varchar(255) DEFAULT NULL,
  `uid` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `data` text,
  `created` datetime DEFAULT NULL,
  `lastlogin` datetime DEFAULT NULL,
  `lastupdated` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `authorizations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hotspot` int(11) DEFAULT NULL,
  `access_point` int(11) DEFAULT NULL,
  `user` int(11) DEFAULT NULL,
  `account` int(11) DEFAULT NULL,
  `device` int(11) DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `lastupdated` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `devices` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `user` int(11) DEFAULT NULL,
  `mask` varchar(255) DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `lastupdated` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `hotspots` (
  `id` int(11) NOT NULL,
  `ssid` varchar(150) NOT NULL,
  `name` varchar(255) NOT NULL,
  `logo` varchar(255) NOT NULL,
  `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `lastupdated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ssid_UNIQUE` (`ssid`),
  KEY `BySSID` (`ssid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `packages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hotspot` int(11) DEFAULT NULL,
  `uid` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `quote_data` int(11) DEFAULT NULL,
  `quote_speed` int(11) DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `lastupdated` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `sessions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hotspot` int(11) DEFAULT NULL,
  `access_point` int(11) DEFAULT NULL,
  `user` int(11) DEFAULT NULL,
  `token` varchar(255) DEFAULT NULL,
  `ip_addr` varchar(100) DEFAULT NULL,
  `mask` varchar(100) DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `ended` datetime DEFAULT NULL,
  `lastupdated` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `traffic` (
  `hotspot` int(11) NOT NULL,
  `ap` varchar(45) NOT NULL,
  `user` int(11) NOT NULL,
  `in` int(11) DEFAULT '0',
  `out` int(11) DEFAULT '0',
  `created` datetime NOT NULL,
  PRIMARY KEY (`hotspot`,`ap`,`created`,`user`),
  KEY `SearchByHotspot` (`hotspot`),
  KEY `SearchByHotspotDateTimeRange` (`hotspot`,`created`),
  KEY `SearchByUser` (`user`),
  KEY `SearchByUserRange` (`user`,`created`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `lastlogin` datetime DEFAULT NULL,
  `lastupdated` varchar(255) NOT NULL DEFAULT 'now()',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `vouchers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hotspot` int(11) DEFAULT NULL,
  `package` int(11) DEFAULT NULL,
  `code` varchar(255) DEFAULT NULL,
  `valid_till` datetime DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `lastupdated` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
