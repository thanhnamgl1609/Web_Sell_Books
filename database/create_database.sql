IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'BOOK_STORE')
BEGIN
create database Book_Store;
END
GO

use Book_Store;
go

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'AccCat' and xtype = 'U')
BEGIN
create table AccCat(
	ID char(1) not null primary key,
	Type nvarchar(15) not null
);
END
GO


IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Account' and xtype = 'U')
BEGIN
create table Account(
	--- INFO
	Username varchar(20) not null primary key,
	Password varchar(32) not null,
	TypeID char(1) not null,
	--- CONSTRAINT
	foreign key (TypeID) references AccCat(ID)
);
END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Person' and xtype = 'U')
BEGIN
create table Person(
	-- INFO
	ID int not null IDENTITY(1,1),
	Username varchar(20),
	FirstName nvarchar(10),
	MiddleName nvarchar(10),
	LastName nvarchar(10),
	DoB date,
	Email nvarchar(30),
	Gender char(1),
	-- CONSTRAINT
	primary key (ID),
	foreign key (Username) REFERENCES Account(Username),
	constraint UQ_CUSTOMER_AccountID UNIQUE (Username),
	constraint CK_CUSTOMER_NAME CHECK ((FirstName IS NOT NULL) OR (LASTNAME IS NOT NULL) OR (MIDDLENAME IS NOT NULL)),
	constraint CK_CUSTOMER_Gender CHECK (Gender in ('M','F')),
);
END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Address' and xtype = 'U')
BEGIN
create table Address(
	-- INFO
	ID int not null primary key IDENTITY(1,1),
	PersonID int not null,
	Num int not null,
	Street nvarchar(15) not null,
	Ward nvarchar(15),
	District nvarchar(15),
	City nvarchar(15) not null,
	Province nvarchar(15),
	PhoneNumber varchar(15) NOT NULL,
	-- CONSTRAINT
	constraint CK_Address_District_Province CHECK ((District IS NOT NULL) OR (PROVINCE IS NOT NULL)),
	foreign key (PersonID) REFERENCES Person(ID),
);
END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Category' and xtype = 'U')
BEGIN
create table Category(
	ID int not null primary key IDENTITY(1,1),
	Name nvarchar(50) not null,
	parentID int,
	FOREIGN KEY (parentID) references Category(ID)
);
END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Book' and xtype = 'U')
BEGIN
create table Book(
	ID int not null primary key IDENTITY(1,1),
	Name nvarchar(100) not null,
	Author nvarchar(50),
	Publisher nvarchar(50),
	Year int,
	Stock smallint default(0),
	Price money default(0),
	Image varchar(50)
	CatID int,
	CONSTRAINT CK_BOOK_YEAR CHECK (YEAR <= YEAR(GETDATE())),
	FOREIGN KEY (CatID) references Category(ID),
);
END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Stock' and xtype = 'U')
BEGIN
create table Stock(
	ID int not null primary key IDENTITY(1,1),
	DateIn datetime,
	CONSTRAINT CK_STOCK_DATEIN CHECK (DateIn <= GETDATE())
);
END
GO


IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'StockDetail' and xtype = 'U')
BEGIN
create table StockDetail(
	StockID int not null,
	BookID int not null,
	Amount smallint default(0),
	primary key (StockID, BookID),
	foreign key (BookID) references Book(ID),
	foreign key (StockID) references Stock(ID),
	CONSTRAINT CK_STOCK_AMOUNT CHECK (amount > 0)
);
End
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'DeliveryInfo' and xtype = 'U')
BEGIN
create table DeliveryInfo(
	ID int not null primary key IDENTITY(1,1),
	Status nvarchar(20) not null
);
END
GO


IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Payment' and xtype = 'U')
BEGIN
create table Payment(
	ID int not null primary key IDENTITY(1,1),
	Method nvarchar(20) not null,
);
END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Orders' and xtype = 'U')
BEGIN
create table Orders(
	ID int not null primary key IDENTITY(1,1),
	DateOrder datetime default(GETDATE()),
	PaymentMethod int not null,
	Paid bit not null,
	TotalPrice money default(0),
	foreign key (PaymentMethod) references Payment(ID),
	CONSTRAINT CK_ORDER_DATEORDER CHECK (DateOrder <= GETDATE())
);
END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'OrderDetail' and xtype = 'U')
BEGIN
create table OrderDetail(
	OrderID int not null,
	BookID int not null,
	Amount smallint not null,
	UnitPrice money default(0),
	primary key (OrderID, BookID),
	foreign key (OrderID) references Orders(ID),
	foreign key (BookID) references Book(ID),
	CONSTRAINT CK_ORDERDETAIL_AMOUNT CHECK (AMOUNT >= 0),
	CONSTRAINT CK_ORDERDETAIL_UNITPRICE CHECK (UnitPrice >= 0)
);
END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'OrderDelivery' and xtype = 'U')
BEGIN
create table OrderDelivery(
	OrderID int not null,
	InfoID int not null,
	Time datetime,
	primary key (OrderID, InfoID),
	foreign key (OrderID) references Orders(ID),
	foreign key (InfoID) references DeliveryInfo(ID),
	CONSTRAINT CK_ORDERDELIVERY_TIME CHECK (Time <= GetDate())
);
END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'VoucherCategory' and xtype = 'U')
BEGIN
create table VoucherCategory(
	ID tinyint not null primary key,
	Name nvarchar(20) not null,
);
END
GO


IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Voucher' and xtype = 'U')
BEGIN
create table Voucher(
	ID tinyint not null primary key,
	CatID tinyint not null,
	Amount int default(0),
	foreign key (CatID) references VoucherCategory(ID),
	CONSTRAINT CK_VOUCHER_AMOUNT CHECK (Amount >= 0)
);
END
GO
