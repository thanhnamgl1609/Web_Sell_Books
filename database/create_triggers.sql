use Book_Store;
GO

IF (OBJECT_ID ('TG_INSERT_STOCK_AMOUNT','TR') IS NULL)
EXEC ('CREATE TRIGGER TG_INSERT_STOCK_AMOUNT
	ON STOCKDETAIL
	AFTER INSERT AS
		UPDATE Book
		SET Book.Stock = Book.Stock + Inserted.Amount
		FROM INSERTED
		WHERE INSERTED.BookID = Book.ID;
	')
GO
