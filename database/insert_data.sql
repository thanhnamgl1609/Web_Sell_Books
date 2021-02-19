use book_store;

insert into Category(name) values (N'Sách Tiếng Việt'), (N'Văn phòng phẩm'), (N'Quà lưu niệm'), (N'English Books');
GO

insert into Category(name,parentid) values (N'Sách thiếu nhi',4), (N'Sách văn học',4), (N'Sách kỹ năng sống',4), (N'Sách tham khảo',4)
GO

insert into Category(name, parentid) values
	(N'Dụng cụ văn phòng',5),
	(N'Bút - Viết các loại',5),
	(N'Dụng cụ học sinh',5),
	(N'Sổ tay các loại',5),
	(N'Móc khoá - Phụ kiện trang trí', 6),
	(N'Thiệp - Bưu ảnh', 6),
	(N'Quà tặng trang trí khác', 6),
	(N'Phụ kiện - Vật liệu trang trí', 6),
	(N'Children''s Books', 7),
	(N'Education - Teaching', 7),
	(N'Fiction - Literature', 7),
	(N'Business & Economics', 7)
